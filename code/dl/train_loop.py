from __future__ import annotations
import math, time, random, os, sys
from dataclasses import dataclass
from typing import Callable, Dict, Any, Tuple
import torch
from torch import nn
from torch.utils.data import DataLoader

@dataclass
class TrainConfig:
    epochs: int = 10
    lr: float = 3e-4
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    log_every: int = 50
    amp: bool = True

class SimpleNet(nn.Module):
    def __init__(self, in_dim: int, out_dim: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 256),
            nn.ReLU(),
            nn.Linear(256, out_dim),
        )
    def forward(self, x):
        return self.net(x)

def train(model: nn.Module, train_loader: DataLoader, val_loader: DataLoader | None, cfg: TrainConfig):
    model = model.to(cfg.device)
    opt = torch.optim.AdamW(model.parameters(), lr=cfg.lr)
    scaler = torch.cuda.amp.GradScaler(enabled=cfg.amp)
    loss_fn = nn.CrossEntropyLoss()

    step = 0
    for epoch in range(cfg.epochs):
        model.train()
        for xb, yb in train_loader:
            xb, yb = xb.to(cfg.device), yb.to(cfg.device)
            with torch.cuda.amp.autocast(enabled=cfg.amp):
                logits = model(xb)
                loss = loss_fn(logits, yb)
            scaler.scale(loss).backward()
            scaler.step(opt)
            scaler.update()
            opt.zero_grad(set_to_none=True)

            if step % cfg.log_every == 0:
                print(f"epoch={epoch} step={step} loss={loss.item():.4f}")
            step += 1
        if val_loader:
            validate(model, val_loader, cfg)

def validate(model: nn.Module, val_loader: DataLoader, cfg: TrainConfig):
    model.eval()
    correct = total = 0
    with torch.no_grad():
        for xb, yb in val_loader:
            xb, yb = xb.to(cfg.device), yb.to(cfg.device)
            logits = model(xb)
            pred = logits.argmax(dim=-1)
            correct += (pred == yb).sum().item()
            total += yb.numel()
    acc = correct / max(total, 1)
    print(f"val_acc={acc:.4f}")
