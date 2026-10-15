# AI-Powered Aerial Surveillance & Multi-Object Tracking System

![CI](https://github.com/dewanshpandey04/aerial-surveillance-multi-object-tracking/actions/workflows/ci.yml/badge.svg)

Real-time **aerial object detection and multi-object tracking software** for webcam, recorded-video, and network-stream inputs, with normalized track metadata, filtering, runtime metrics, JSONL export, and edge-AI deployment support.

**Python · PyTorch · YOLO · OpenCV · ByteTrack · RTSP · CUDA · NVIDIA Jetson · Raspberry Pi · GitHub Actions**

## Engineering highlights

- YOLO-based real-time object detection
- ByteTrack persistent multi-object tracking
- Stable `TrackRecord` data model for downstream processing
- Result adapters that isolate application code from framework-specific result objects
- Class-name and confidence filtering for metadata reporting
- Active-track counts, class distributions, and persistent-ID summaries
- Credential-safe RTSP/network-stream labels
- Frame-level JSONL metadata export
- Offline metadata summarization
- Rolling latency and approximate FPS metrics
- Unit-tested reusable logic
- Automated syntax, lint, and test checks on Python 3.10, 3.11, and 3.12
- Deployment notes for NVIDIA Jetson and Raspberry Pi-class systems

## Processing pipeline

1. **Input** — webcam index, video file, or network stream
2. **Detection** — YOLO class/confidence/bounding-box inference
3. **Tracking** — ByteTrack persistent object IDs
4. **Normalization** — tracker results converted into `TrackRecord` objects
5. **Reporting filters** — optional class and confidence filtering
6. **Summaries** — track count, class distribution, and visible IDs
7. **Metrics** — rolling latency and approximate FPS
8. **Export** — optional JSONL metadata for offline analysis
9. **Visualization** — annotated OpenCV display with sanitized source label

## Measured project results

The original project work included real-time detection and tracking of **humans, UAVs, tanks, vehicles, and other ground objects** from aerial imagery.

| Metric | Result |
|---|---:|
| Custom detector | mAP50 > 0.92 |
| Optimized live UAV camera pipeline | 50+ FPS |

These results refer to the original project environment. Private training data, production model weights, customer footage, and exact deployment configuration are not included in this repository.

## Repository structure

| Path | Responsibility |
|---|---|
| `src/surveillance.py` | Main YOLO + ByteTrack pipeline |
| `src/stream.py` | Video-source abstraction |
| `src/track_record.py` | Normalized tracked-object record |
| `src/result_adapter.py` | Ultralytics result normalization |
| `src/track_summary.py` | Active-track and class summaries |
| `src/class_filter.py` | Class parsing and metadata filtering |
| `src/export.py` | JSONL tracking-metadata export |
| `src/metrics.py` | Rolling latency / FPS metrics |
| `src/config.py` | YAML configuration validation |
| `src/utils.py` | Source parsing and credential-safe labels |
| `config/` | Example runtime configuration |
| `scripts/benchmark.py` | Inference benchmark utility |
| `scripts/summarize_jsonl.py` | Offline metadata summarizer |
| `tests/` | Unit tests |
| `docs/` | Architecture, deployment, verification, and performance notes |
| `pyproject.toml` | Test and lint configuration |

## Setup

```powershell
git clone https://github.com/dewanshpandey04/aerial-surveillance-multi-object-tracking.git
cd aerial-surveillance-multi-object-tracking

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

For development and repository quality checks:

```powershell
pip install -r requirements-dev.txt
```

> NVIDIA Jetson deployments may require the JetPack-compatible PyTorch build provided for the target platform.

## Usage

Webcam:

```powershell
python -m src.surveillance --source 0 --show
```

Recorded video:

```powershell
python -m src.surveillance --source path\to\video.mp4 --show
```

Network stream:

```powershell
python -m src.surveillance --source "rtsp://USER:PASSWORD@HOST/stream" --show
```

Export frame-level tracking metadata:

```powershell
python -m src.surveillance --source path\to\video.mp4 --export-jsonl outputs\tracks.jsonl
```

Report only selected classes in exported/summary metadata:

```powershell
python -m src.surveillance --source path\to\video.mp4 --report-classes "uav,vehicle" --export-jsonl outputs\tracks.jsonl
```

Do not commit real stream credentials.

## Quality checks

```powershell
python -m compileall -q src scripts tests
ruff check .
python -m pytest -q
```

CI runs these checks on **Python 3.10, 3.11, and 3.12**.

## Benchmarking

```powershell
python scripts/benchmark.py --model yolo11n.pt --source path\to\video.mp4
```

## Metadata analysis

```powershell
python scripts/summarize_jsonl.py outputs\tracks.jsonl
```

The summary reports processed frames, track observations, unique track IDs, and class observations.

## Documentation

- [Architecture](docs/architecture.md)
- [Code tour](docs/code-tour.md)
- [Deployment](docs/deployment.md)
- [Performance](docs/performance.md)
- [Verification](docs/verification.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

## Branches

- `main` — stable branch
- `develop` — development and integration
- `docs` — documentation work

## Author

**Dewansh Pandey**  
AI/ML Engineer | Computer Vision & Autonomous Systems  
[LinkedIn](https://www.linkedin.com/in/dewansh-pandey-9b564a317) · [GitHub](https://github.com/dewanshpandey04)
