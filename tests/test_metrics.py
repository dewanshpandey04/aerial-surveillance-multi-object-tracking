from src.metrics import RuntimeMetrics


def test_metrics_snapshot():
    metrics = RuntimeMetrics(window=3)
    metrics.add_latency_ms(25)
    metrics.add_latency_ms(25)
    result = metrics.snapshot()
    assert result["samples"] == 2
    assert result["mean_latency_ms"] == 25.0
    assert result["approx_fps"] == 40.0
