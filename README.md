# AI-Powered Aerial Surveillance & Multi-Object Tracking System

A public portfolio implementation of a real-time **aerial detection and multi-object tracking pipeline** built with YOLO, ByteTrack, OpenCV, and edge-AI deployment practices.

The professional project involved processing live UAV camera feeds, detecting multiple object classes, maintaining persistent track identities, monitoring inference performance, and deploying low-latency vision workloads on embedded hardware.

> This repository contains no private company footage, customer streams, credentials, proprietary datasets, internal model weights, or production-only source code.

## My contribution

- Developed real-time aerial object-detection and tracking workflows using YOLO, PyTorch, OpenCV, and ByteTrack.
- Built live video / network-stream processing paths for continuous camera inference.
- Maintained persistent object IDs and structured metadata for tracked objects.
- Added credential-safe stream labeling so sensitive RTSP information is not exposed in logs or displays.
- Implemented active-track summaries and runtime metrics for monitoring.
- Worked with NVIDIA Jetson and Raspberry Pi-class hardware for edge-AI deployment.
- Added benchmark scripts, deployment documentation, unit tests, and CI for a professional public presentation.

## Professional project scope

The original system detected and tracked object classes including **humans, UAVs, tanks, vehicles, and other ground objects** from aerial imagery. Custom YOLO detectors achieved **mAP50 above 0.92** in the professional project, and optimized edge pipelines achieved **50+ FPS** on live UAV camera feeds.

These figures describe the original project environment. The private training dataset, production weights, and exact deployment configuration are not included in this public repository.

## Technical stack

**Python · YOLO · PyTorch · OpenCV · ByteTrack · RTSP · NVIDIA Jetson · Raspberry Pi · CUDA**

## Repository structure

| Path | Purpose |
|---|---|
| `src/surveillance.py` | Live/video/network-stream detection + tracking |
| `src/track_summary.py` | Track-count and class-summary utilities |
| `src/metrics.py` | Runtime FPS / latency metrics |
| `src/utils.py` | Input parsing and credential-safe stream labels |
| `config/` | Public-safe configuration template |
| `scripts/benchmark.py` | Inference performance benchmark |
| `tests/` | Unit tests |
| `docs/` | Architecture, deployment, verification, and code-tour notes |
| `.github/workflows/` | CI checks |

## Quick start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

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

Never commit real stream credentials.

Run tests:

```powershell
pytest -q
```

## Engineering documentation

- [Architecture](docs/architecture.md)
- [Code tour](docs/code-tour.md)
- [Deployment notes](docs/deployment.md)
- [Verification plan](docs/verification.md)
- [Professional results and public scope](docs/performance.md)

## Branch strategy

- `main` — stable recruiter-facing portfolio version
- `develop` — development and integration work
- `docs` — documentation-focused changes

## Author

**Dewansh Pandey**  
AI/ML Engineer | Computer Vision & Autonomous Systems
