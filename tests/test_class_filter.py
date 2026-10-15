from src.class_filter import filter_tracks
from src.track_record import TrackRecord


def make_track(track_id: int, name: str, confidence: float) -> TrackRecord:
    return TrackRecord(track_id, 0, name, confidence, (0.0, 0.0, 1.0, 1.0))


def test_filter_by_confidence():
    tracks = [make_track(1, "uav", 0.9), make_track(2, "vehicle", 0.4)]
    result = filter_tracks(tracks, minimum_confidence=0.5)
    assert [track.track_id for track in result] == [1]


def test_filter_by_class():
    tracks = [make_track(1, "uav", 0.9), make_track(2, "vehicle", 0.8)]
    result = filter_tracks(tracks, allowed_classes={"vehicle"})
    assert [track.track_id for track in result] == [2]
