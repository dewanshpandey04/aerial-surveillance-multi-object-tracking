from src.track_record import TrackRecord


def test_track_record_serialization():
    record = TrackRecord(
        track_id=11,
        class_id=2,
        class_name="vehicle",
        confidence=0.87654,
        bbox_xyxy=(1.0, 2.0, 30.0, 40.0),
    )
    payload = record.as_dict()
    assert payload["track_id"] == 11
    assert payload["class_name"] == "vehicle"
    assert payload["confidence"] == 0.8765
