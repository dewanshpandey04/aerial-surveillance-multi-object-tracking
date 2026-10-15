# Aerial Surveillance Architecture

The project is structured as a small, inspectable computer-vision service rather than a single monolithic script.

## Component model

| Component | Responsibility |
|---|---|
| Video input | Webcam, recorded video, or network-stream source |
| Detector | Object detection and class/confidence output |
| Tracker | Persistent identity assignment across frames |
| Track metadata | Normalized per-object IDs and state |
| Track summary | Active-track counts and class distribution |
| Runtime metrics | FPS and inference timing |
| Visualization | Annotated frames for development and validation |
| Benchmarking | Repeatable local performance measurement |
| Tests | Validation of utility and metadata behavior |

## Processing sequence

1. A source is parsed as either a webcam index, file path, or network URL.
2. Frames are passed to the selected YOLO model.
3. ByteTrack associates detections across consecutive frames.
4. Track IDs and detection metadata are extracted into reusable structures.
5. Runtime metrics and track summaries are generated independently from model inference.
6. Optional visualization displays annotated frames without exposing stream credentials.

## Design choices

**Credential safety.** Network-stream labels are sanitized before display or logging.

**Persistent identity.** Tracking is kept separate from detection so object identity can survive short-term movement between frames.

**Inspectable outputs.** Track summaries provide simple counts and class distributions that can be tested without requiring a GPU.

**Edge-friendly structure.** The public implementation keeps source handling, inference, metadata, and metrics modular so hardware-specific optimization can be introduced without rewriting the entire application.

## Deployment context

The professional project used NVIDIA Jetson and Raspberry Pi-class platforms. Exact production decoder settings, private camera addresses, company footage, proprietary model weights, and internal deployment configuration are excluded.
