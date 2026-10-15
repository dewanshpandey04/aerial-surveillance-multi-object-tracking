from __future__ import annotations

from .track_record import TrackRecord


def track_records_from_result(result) -> list[TrackRecord]:
    """Convert an Ultralytics result to stable, serializable track records."""
    boxes = getattr(result, "boxes", None)
    if boxes is None or boxes.id is None:
        return []

    ids = [int(v) for v in boxes.id.cpu().tolist()]
    xyxy = boxes.xyxy.cpu().tolist()
    conf = boxes.conf.cpu().tolist() if boxes.conf is not None else [0.0] * len(ids)
    classes = boxes.cls.cpu().tolist() if boxes.cls is not None else [-1] * len(ids)
    names = getattr(result, "names", {}) or {}

    records: list[TrackRecord] = []
    for track_id, class_id, confidence, box in zip(ids, classes, conf, xyxy):
        class_id = int(class_id)
        records.append(
            TrackRecord(
                track_id=track_id,
                class_id=class_id,
                class_name=str(names.get(class_id, class_id)),
                confidence=float(confidence),
                bbox_xyxy=tuple(float(v) for v in box),
            )
        )
    return records
