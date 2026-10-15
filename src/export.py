from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .track_record import TrackRecord


class JsonlTrackExporter:
    """Append frame-level tracking metadata to JSON Lines."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

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
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, separators=(",", ":")) + "\n")
