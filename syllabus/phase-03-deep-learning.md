# Phase 3 — Deep Learning (Weeks 17–24)

## Optimization & Training
- SGD, momentum, Adam/AdamW; LR schedules, warmup, cosine decay; weight decay vs L2; gradient clipping.
- Initialization, normalization (Batch/Layer/RMS), residual connections.
- Regularization: dropout, label smoothing, mixup/cutmix.
- Mixed precision; gradient checkpointing; DDP basics.

## Architectures
- MLPs; CNNs (conv, pooling, receptive fields); RNN/LSTM/GRU; attention; Transformers.

## Practicalities
- Data pipelines: WebDataset/TFRecords; caching; sharding.
- Checkpointing strategies; early stopping; reproducibility seeds.
- Profiling: PyTorch profiler; bottlenecks (GPU util, input stalls).

## Deliverables
- Module: `code/dl/train_loop.py` — minimal yet robust training loop.
- Repro: Train small CNN on CIFAR‑10 with proper logs, plots, and unit tests.
