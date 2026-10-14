from src.track_summary import VisibleTrack, summarize_tracks


def test_track_summary():
    tracks = [
        VisibleTrack(1, "uav", 0.91),
        VisibleTrack(2, "vehicle", 0.86),
        VisibleTrack(3, "uav", 0.82),
    ]
    summary = summarize_tracks(tracks)
    assert summary["active_tracks"] == 3
    assert summary["classes"] == {"uav": 2, "vehicle": 1}
    assert summary["track_ids"] == [1, 2, 3]
