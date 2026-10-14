from __future__ import annotations

from dataclasses import dataclass
from collections import Counter


@dataclass(frozen=True)
class VisibleTrack:
    track_id: int
    class_name: str
    confidence: float


def summarize_tracks(tracks: list[VisibleTrack]) -> dict:
    """Summarize currently visible tracks for HUD/logging use."""
    by_class = Counter(track.class_name for track in tracks)
    return {
        "active_tracks": len(tracks),
        "classes": dict(sorted(by_class.items())),
        "track_ids": [track.track_id for track in tracks],
    }
