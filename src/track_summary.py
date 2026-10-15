from __future__ import annotations

from collections import Counter
from collections.abc import Iterable

from .track_record import TrackRecord


def summarize_tracks(tracks: Iterable[TrackRecord]) -> dict:
    """Summarize currently visible normalized track records."""
    records = list(tracks)
    by_class = Counter(track.class_name for track in records)
    return {
        "active_tracks": len(records),
        "classes": dict(sorted(by_class.items())),
        "track_ids": [track.track_id for track in records],
    }
