from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TrackRecord:
    """Normalized metadata for one visible tracked object."""

    track_id: int
    class_id: int
    class_name: str
    confidence: float
    bbox_xyxy: tuple[float, float, float, float]

    def as_dict(self) -> dict:
        return {
            "track_id": self.track_id,
            "class_id": self.class_id,
            "class_name": self.class_name,
            "confidence": round(float(self.confidence), 4),
            "bbox_xyxy": [float(v) for v in self.bbox_xyxy],
        }
