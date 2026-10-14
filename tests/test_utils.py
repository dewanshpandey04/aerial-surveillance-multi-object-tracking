from src.utils import parse_source, safe_stream_label


def test_parse_source_webcam():
    assert parse_source("0") == 0


def test_safe_stream_label_redacts_credentials():
    label = safe_stream_label("rtsp://user:secret@10.0.0.4/stream")
    assert label == "rtsp://<redacted-stream>"
    assert "secret" not in label
