from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from statistics import mean


@dataclass
class RuntimeMetrics:
    """Rolling performance metrics for live video processing."""

    window: int = 60
    _latencies_ms: deque[float] = field(default_factory=deque)

    def add_latency_ms(self, value: float) -> None:
        self._latencies_ms.append(float(value))
        while len(self._latencies_ms) > self.window:
            self._latencies_ms.popleft()

    @property
    def mean_latency_ms(self) -> float:
        return mean(self._latencies_ms) if self._latencies_ms else 0.0

    @property
    def approx_fps(self) -> float:
        latency = self.mean_latency_ms
        return 1000.0 / latency if latency > 0 else 0.0

    def snapshot(self) -> dict:
        return {
            "samples": len(self._latencies_ms),
            "mean_latency_ms": round(self.mean_latency_ms, 3),
            "approx_fps": round(self.approx_fps, 2),
        }
