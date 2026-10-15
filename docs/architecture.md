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
| Runtime metrics | Rolling frame-time and approximate FPS |
| Visualization | Annotated frames for development and validation |
| Benchmarking | Separate inference-latency measurement |
| Tests | Validation of utility, filtering, export, and metadata behavior |

## Processing sequence

1. A source is resolved from CLI arguments or YAML configuration.
2. Frames are passed to the selected YOLO model.
3. ByteTrack associates detections across consecutive frames.
4. Tracker outputs are normalized into reusable `TrackRecord` objects.
5. Optional filters select classes/confidence levels for metadata reporting.
6. Track summaries and frame-time/FPS metrics are generated.
7. Metadata can be written to buffered JSONL output for offline review.
8. Optional visualization displays annotated frames without exposing stream credentials.

## Design choices

**Credential safety.** Network-stream labels are sanitized before display or logging.

**Persistent identity.** Tracking is separated from detection so object identity is maintained across frames.

**Stable metadata contract.** Model-specific results are converted into simple records before summaries or export.

**Buffered metadata export.** JSONL output keeps video and metadata concerns separate while reducing per-frame file-open overhead.

**Metric separation.** Runtime frame-time/FPS metrics describe pipeline cadence, while the benchmark utility separately measures model-reported inference latency.

**Edge-friendly structure.** Inference, metadata, filtering, export, configuration, and metrics remain modular so hardware-specific optimization can be introduced independently.

## Deployment context

The professional project used NVIDIA Jetson and Raspberry Pi-class platforms. Exact production decoder settings, private camera addresses, company footage, proprietary model weights, and internal deployment configuration are excluded.
