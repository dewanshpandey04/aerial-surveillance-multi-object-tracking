from __future__ import annotations

import argparse
import time
from typing import Any

from src.class_filter import filter_tracks, parse_class_names
from src.config import load_config
from src.export import JsonlTrackExporter
from src.metrics import RuntimeMetrics
from src.result_adapter import track_records_from_result
from src.track_summary import summarize_tracks
from src.utils import parse_source, safe_stream_label


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Real-time aerial detection and multi-object tracking."
    )
    parser.add_argument("--config", default=None, help="Optional YAML runtime configuration.")
    parser.add_argument("--model", default=None)
    parser.add_argument("--source", default=None, help="Webcam index, video path, or network stream.")
    parser.add_argument("--tracker", default=None)
    parser.add_argument("--conf", type=float, default=None)
    parser.add_argument("--imgsz", type=int, default=None)
    parser.add_argument("--device", default=None)
    parser.add_argument(
        "--report-classes",
        default=None,
        help="Optional comma-separated class names for metadata reporting.",
    )
    parser.add_argument(
        "--report-min-confidence",
        type=float,
        default=0.0,
        help="Optional confidence threshold applied to reported track metadata.",
    )
    parser.add_argument(
        "--export-jsonl",
        default=None,
        help="Optional path for frame-level JSONL tracking metadata.",
    )
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--save", action="store_true")
    return parser


def _section(config: dict[str, Any], name: str) -> dict[str, Any]:
    value = config.get(name, {})
    return value if isinstance(value, dict) else {}


def main() -> None:
    args = build_parser().parse_args()
    config = load_config(args.config) if args.config else {}

    stream = _section(config, "stream")
    detection = _section(config, "detection")
    tracking = _section(config, "tracking")

    model_path = args.model or detection.get("model", "yolo11n.pt")
    source = parse_source(args.source if args.source is not None else stream.get("source", 0))
    tracker = args.tracker or tracking.get("tracker", "bytetrack.yaml")
    conf = args.conf if args.conf is not None else float(detection.get("confidence_threshold", 0.35))
    imgsz = args.imgsz if args.imgsz is not None else int(detection.get("image_size", 640))

    from ultralytics import YOLO

    cv2 = None
    if args.show:
        import cv2 as cv2_module

        cv2 = cv2_module

    model = YOLO(model_path)
    metrics = RuntimeMetrics(window=60)
    allowed_classes = parse_class_names(args.report_classes)
    exporter = JsonlTrackExporter(args.export_jsonl) if args.export_jsonl else None

    results = model.track(
        source=source,
        tracker=tracker,
        persist=True,
        conf=conf,
        imgsz=imgsz,
        device=args.device,
        stream=True,
        save=args.save,
        verbose=False,
    )

    previous = time.perf_counter()
    display_source = safe_stream_label(str(source))

    try:
        for frame_id, result in enumerate(results, start=1):
            now = time.perf_counter()
            metrics.add_frame_time_ms((now - previous) * 1000.0)
            previous = now

            records = track_records_from_result(result)
            reported_records = filter_tracks(
                records,
                allowed_classes=allowed_classes,
                minimum_confidence=args.report_min_confidence,
            )
            summary = summarize_tracks(reported_records)

            if exporter is not None:
                exporter.write(
                    frame_id=frame_id,
                    timestamp=time.time(),
                    fps=metrics.fps,
                    tracks=reported_records,
                )

            if args.show:
                frame = result.plot()
                cv2.putText(
                    frame,
                    f"FPS {metrics.fps:.1f} | Reported tracks {summary['active_tracks']}",
                    (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 255),
                    2,
                    cv2.LINE_AA,
                )
                cv2.putText(
                    frame,
                    f"Source: {display_source}",
                    (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (255, 255, 255),
                    2,
                    cv2.LINE_AA,
                )
                cv2.imshow("Aerial Surveillance & Tracking", frame)
                if cv2.waitKey(1) & 0xFF in (27, ord("q")):
                    break
    finally:
        if exporter is not None:
            exporter.close()
        if cv2 is not None:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
