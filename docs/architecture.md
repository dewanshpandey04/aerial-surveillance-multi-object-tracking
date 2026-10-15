# Aerial Surveillance Architecture

The project is structured as a small, inspectable computer-vision service rather than a single monolithic script.

## Component model

| Component | Responsibility |
|---|---|
| Video input | Webcam, recorded video, or network stream |
| Detector | Object detection and class/confidence output |
| Tracker | Persistent identity assignment across frames |
| Result adapter | Convert tracker-specific results into stable records |
| Track metadata | IDs, class names, confidence, and boxes |
| Track summary | Active-track counts and class distribution |
| Class filter | Optional class/confidence filtering for reporting |
| JSONL export | Persist frame-level metadata for offline analysis |
| Runtime metrics | FPS and inference timing |
| Visualization | Annotated frames for development and validation |
| Benchmarking | Repeatable local performance measurement |
| Tests | Validation of utility, filtering, export, and metadata behavior |

## Processing sequence

1. A source is parsed as a webcam index, file path, or network URL.
2. Frames are passed to the selected YOLO model.
3. ByteTrack associates detections across consecutive frames.
4. Tracker outputs are normalized into reusable `TrackRecord` objects.
5. Optional filters select classes/confidence levels for reporting.
6. Track summaries and runtime metrics are generated independently from inference.
7. Metadata can be written to JSONL for offline review.
8. Optional visualization displays annotated frames without exposing stream credentials.

## Design choices

**Credential safety.** Network-stream labels are sanitized before display or logging.

**Persistent identity.** Tracking is separated from detection so object identity is maintained across frames.

**Stable metadata contract.** Model-specific results are converted into simple records before summaries or export.

**Offline inspection.** JSONL output provides a lightweight way to analyze tracking behavior without storing private video.

**Edge-friendly structure.** Source handling, inference, metadata, filtering, export, and metrics remain modular so hardware-specific optimizations can be introduced independently.

## Deployment context

The professional project used NVIDIA Jetson and Raspberry Pi-class platforms. Exact production decoder settings, private camera addresses, company footage, proprietary model weights, and internal deployment configuration are excluded.
