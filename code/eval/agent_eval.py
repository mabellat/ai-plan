from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Any, Callable
import statistics as stats
import time

@dataclass
class AgentRun:
    success: bool
    steps: int
    tokens: int
    latency_ms: float
    cost_usd: float

def aggregate(runs: List[AgentRun]) -> Dict[str, float]:
    return {
        "success@1": sum(r.success for r in runs) / max(len(runs), 1),
        "median_steps": stats.median(r.steps for r in runs),
        "p95_latency_ms": sorted(r.latency_ms for r in runs)[int(0.95*len(runs))-1] if runs else 0.0,
        "avg_cost_usd": stats.mean(r.cost_usd for r in runs) if runs else 0.0,
    }
