"""Regression tests for safe video-source error messages."""

import sys
from types import SimpleNamespace

import pytest

from src.stream import VideoStream


class FakeCapture:
    def __init__(self, source):
        self.source = source
        self.released = False

    def isOpened(self):
        return False

    def release(self):
        self.released = True


def test_failed_rtsp_connection_redacts_credentials(monkeypatch):
    captures = []

    def capture_factory(source):
        capture = FakeCapture(source)
        captures.append(capture)
        return capture

    monkeypatch.setitem(sys.modules, "cv2", SimpleNamespace(VideoCapture=capture_factory))
    url = "rtsp://private_user:private_password@example.test/live"

    with pytest.raises(RuntimeError) as exc:
        VideoStream(url)

    message = str(exc.value)
    assert "private_user" not in message
    assert "private_password" not in message
    assert "rtsp://<redacted-stream>" in message
    assert captures[0].released


def test_failed_local_video_reports_file_path(monkeypatch):
    monkeypatch.setitem(
        sys.modules,
        "cv2",
        SimpleNamespace(VideoCapture=lambda source: FakeCapture(source)),
    )

    with pytest.raises(RuntimeError, match="sample.mp4"):
        VideoStream("sample.mp4")
