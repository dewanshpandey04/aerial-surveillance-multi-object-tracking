# AI-Powered Aerial Surveillance & Multi-Object Tracking System

Public portfolio implementation of a real-time aerial surveillance pipeline using **YOLO, ByteTrack, OpenCV, and live/video/RTSP-style stream inputs**.

The professional project work involved detecting and tracking multiple object classes from aerial camera feeds, running low-latency inference on edge hardware, and maintaining persistent track identities in real time.

> **IP / privacy note:** this repository contains no private company footage, credentials, proprietary datasets, internal model weights, or customer data. It uses public tooling and safe configuration examples.

## What this repository demonstrates

- Real-time YOLO object detection
- ByteTrack multi-object tracking
- Webcam, recorded video, and network-stream input
- Persistent track IDs
- Class/confidence/box metadata extraction
- FPS and inference-latency monitoring
- Simple event/track summaries
- Edge-AI deployment structure for NVIDIA Jetson and Raspberry Pi
- Unit tests and benchmark utilities

## Tech stack

**Python · YOLO · PyTorch · OpenCV · ByteTrack · RTSP · NVIDIA Jetson · Raspberry Pi**

## High-level architecture

```text
Camera / Video / Network Stream
              |
              v
        Frame Acquisition
              |
              v
          YOLO Detector
              |
              v
       ByteTrack Tracker
              |
              v
 IDs + Classes + Boxes + Confidence
              |
              v
 Visualization / Metrics / Event Summary
```

See [docs/architecture.md](docs/architecture.md).

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

## Repository layout

```text
config/
docs/
scripts/
src/
tests/
.github/workflows/
```

## Branches

- `main` — stable portfolio version
- `develop` — development/integration branch
- `docs` — documentation-focused branch

## Author

**Dewansh Pandey**  
AI/ML Engineer | Computer Vision & Autonomous Systems
