from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, TextIO

from .track_record import TrackRecord


class JsonlTrackExporter:
    """Write frame-level tracking metadata to line-buffered JSON Lines."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._handle: TextIO | None = None

    def _open(self) -> TextIO:
        if self._handle is None:
            self._handle = self.path.open("a", encoding="utf-8", buffering=1)
        return self._handle

    def write(
        self,
        *,
        frame_id: int,
        timestamp: float,
        fps: float,
        tracks: Iterable[TrackRecord],
    ) -> None:
        payload = {
            "frame_id": int(frame_id),
            "timestamp": float(timestamp),
            "fps": round(float(fps), 2),
            "tracks": [track.as_dict() for track in tracks],
        }
        self._open().write(json.dumps(payload, separators=(",", ":")) + "\n")

    def close(self) -> None:
        if self._handle is not None:
            self._handle.close()
            self._handle = None

    def __enter__(self) -> "JsonlTrackExporter":
        self._open()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
