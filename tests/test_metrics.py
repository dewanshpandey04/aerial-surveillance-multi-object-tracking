from src.metrics import RuntimeMetrics


def test_metrics_snapshot():
    metrics = RuntimeMetrics(window=3)
    metrics.add_frame_time_ms(25)
    metrics.add_frame_time_ms(25)

    result = metrics.snapshot()

    assert result["samples"] == 2
    assert result["mean_frame_time_ms"] == 25.0
    assert result["fps"] == 40.0
