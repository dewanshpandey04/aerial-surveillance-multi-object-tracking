# AI-Powered Aerial Surveillance & Multi-Object Tracking System

![CI](https://github.com/dewanshpandey04/aerial-surveillance-multi-object-tracking/actions/workflows/ci.yml/badge.svg)

## Overview

Real-time aerial surveillance and multi-object tracking system built with **YOLO, ByteTrack, OpenCV, and edge-AI deployment practices**.

The project processes webcam, recorded-video, and network-stream inputs; performs detection and persistent tracking; normalizes tracked-object metadata; exposes runtime metrics; and supports offline JSONL export for analysis.

Private footage, credentials, proprietary datasets, production model weights, and confidential deployment configuration are not included.

## Key capabilities

- YOLO object detection
- ByteTrack multi-object tracking
- Persistent track IDs
- Webcam, video, and RTSP-style stream input
- Credential-safe stream labeling
- Class and confidence filtering
- Track summaries and class counts
- JSONL metadata export
- Offline metadata summarization
- FPS and inference-latency monitoring
- Unit tests and GitHub Actions CI
- Jetson / Raspberry Pi deployment documentation

## Project results

The original project work included detection and tracking of **humans, UAVs, tanks, vehicles, and other ground objects** from aerial imagery.

| Metric | Result |
|---|---:|
| Custom detector | mAP50 > 0.92 |
| Optimized live UAV camera pipeline | 50+ FPS |

These results refer to the original project configuration. The private training data, production weights, and exact deployment environment are not distributed with this repository.

## Tech stack

**Python · YOLO · PyTorch · OpenCV · ByteTrack · RTSP · NVIDIA Jetson · Raspberry Pi · CUDA**

## Repository structure

| Path | Purpose |
|---|---|
| `src/surveillance.py` | Main detection + tracking pipeline |
| `src/stream.py` | Video-source wrapper |
| `src/track_record.py` | Normalized tracked-object record |
| `src/result_adapter.py` | Tracker-result normalization |
| `src/track_summary.py` | Active-track and class summaries |
| `src/class_filter.py` | Class/confidence filtering |
| `src/export.py` | JSONL tracking-metadata export |
| `src/metrics.py` | Rolling latency / FPS metrics |
| `src/utils.py` | Source parsing and stream-label sanitization |
| `scripts/benchmark.py` | Inference benchmark |
| `scripts/summarize_jsonl.py` | Offline track-metadata summary |
| `tests/` | Unit tests |
| `docs/` | Architecture, deployment, and verification notes |

## Installation

```powershell
git clone https://github.com/dewanshpandey04/aerial-surveillance-multi-object-tracking.git
cd aerial-surveillance-multi-object-tracking

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Usage

Webcam:

```powershell
python src/surveillance.py --source 0 --show
```

Recorded video:

```powershell
python src/surveillance.py --source path\to\video.mp4 --show
```

Network stream:

```powershell
python src/surveillance.py --source "rtsp://USER:PASSWORD@HOST/stream" --show
```

Do not commit real stream credentials.

## Testing

```powershell
pytest -q
```

## Benchmarking

```powershell
python scripts/benchmark.py --model yolo11n.pt --source path\to\video.mp4
```

## Metadata analysis

```powershell
python scripts/summarize_jsonl.py outputs\tracks.jsonl
```

## Documentation

- [Architecture](docs/architecture.md)
- [Code tour](docs/code-tour.md)
- [Deployment](docs/deployment.md)
- [Performance](docs/performance.md)
- [Verification](docs/verification.md)

## Branches

- `main` — stable branch
- `develop` — development and integration
- `docs` — documentation work

## Author

**Dewansh Pandey**  
AI/ML Engineer | Computer Vision & Autonomous Systems  
[LinkedIn](https://www.linkedin.com/in/dewansh-pandey-9b564a317) · [GitHub](https://github.com/dewanshpandey04)
