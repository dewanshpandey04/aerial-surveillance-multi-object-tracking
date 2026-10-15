from src.track_record import TrackRecord
from src.track_summary import summarize_tracks


def test_track_summary():
    tracks = [
        TrackRecord(1, 0, "uav", 0.91, (0.0, 0.0, 1.0, 1.0)),
        TrackRecord(2, 1, "vehicle", 0.86, (0.0, 0.0, 1.0, 1.0)),
        TrackRecord(3, 0, "uav", 0.82, (0.0, 0.0, 1.0, 1.0)),
    ]
    summary = summarize_tracks(tracks)

    assert summary["active_tracks"] == 3
    assert summary["classes"] == {"uav": 2, "vehicle": 1}
    assert summary["track_ids"] == [1, 2, 3]
