from __future__ import annotations

from collections.abc import Iterable

from .track_record import TrackRecord


def filter_tracks(
    tracks: Iterable[TrackRecord],
    allowed_classes: set[str] | None = None,
    minimum_confidence: float = 0.0,
) -> list[TrackRecord]:
    """Filter visible records for display/reporting."""
    output = []
    for track in tracks:
        if track.confidence < minimum_confidence:
            continue
        if allowed_classes is not None and track.class_name not in allowed_classes:
            continue
        output.append(track)
    return output
