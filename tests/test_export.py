import json

from src.export import JsonlTrackExporter
from src.track_record import TrackRecord


def test_jsonl_export(tmp_path):
    path = tmp_path / "tracks.jsonl"

    with JsonlTrackExporter(path) as exporter:
        exporter.write(
            frame_id=1,
            timestamp=123.0,
            fps=30.0,
            tracks=[TrackRecord(5, 1, "uav", 0.95, (1.0, 2.0, 3.0, 4.0))],
        )

    payload = json.loads(path.read_text(encoding="utf-8").strip())

    assert payload["frame_id"] == 1
    assert payload["fps"] == 30.0
    assert payload["tracks"][0]["track_id"] == 5
