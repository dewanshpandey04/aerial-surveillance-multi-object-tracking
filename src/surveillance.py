from __future__ import annotations

import argparse
import time

import cv2
from ultralytics import YOLO

from utils import parse_source, safe_stream_label


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Real-time aerial surveillance and multi-object tracking demo."
    )
    parser.add_argument("--model", default="yolo11n.pt")
    parser.add_argument("--source", required=True, help="Webcam index, video path, or network stream.")
    parser.add_argument("--tracker", default="bytetrack.yaml")
    parser.add_argument("--conf", type=float, default=0.35)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--device", default=None)
    parser.add_argument("--show", action="store_true")
    parser.add_argument("--save", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    source = parse_source(args.source)
    model = YOLO(args.model)

    results = model.track(
        source=source,
        tracker=args.tracker,
        persist=True,
        conf=args.conf,
        imgsz=args.imgsz,
        device=args.device,
        stream=True,
        save=args.save,
        verbose=False,
    )

    previous = time.perf_counter()
    display_source = safe_stream_label(str(args.source))

    for result in results:
        now = time.perf_counter()
        fps = 1.0 / max(now - previous, 1e-9)
        previous = now

        frame = result.plot()
        active_tracks = 0
        if result.boxes is not None and result.boxes.id is not None:
            active_tracks = len(result.boxes.id)

        cv2.putText(
            frame,
            f"FPS {fps:.1f} | Active tracks {active_tracks}",
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

        if args.show:
            cv2.imshow("Aerial Surveillance & Tracking", frame)
            if cv2.waitKey(1) & 0xFF in (27, ord("q")):
                break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
