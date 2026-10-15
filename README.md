# Aerial Surveillance & Multi-Object Tracking

**Python · YOLO · ByteTrack · OpenCV · RTSP · NVIDIA Jetson · Raspberry Pi 5 · Hailo AI HAT · Pytest**

A real-time computer-vision project for detecting and tracking objects in webcam, video-file, and network-stream inputs. Includes reusable tracking metadata, JSONL export, class filters, runtime metrics, benchmarking, and embedded edge-AI deployment practices.

## Quick start

Requires Python 3.10+.

```bash
git clone https://github.com/dewanshpandey04/aerial-surveillance-multi-object-tracking.git
cd aerial-surveillance-multi-object-tracking
python -m venv .venv
python -m pip install -r requirements.txt
python -m src.surveillance --source 0 --show
```

Activate the virtual environment before installing packages when appropriate for your OS. The default example uses an Ultralytics model; internet access may be needed for its initial download.

## Use cases

| Command | Purpose |
| --- | --- |
| `python -m src.surveillance --source 0 --show` | Live webcam detection and tracking |
| `python -m src.surveillance --source video.mp4 --show` | Recorded-video analysis |
| `python -m src.surveillance --source video.mp4 --export-jsonl outputs/tracks.jsonl` | Export frame-level tracking metadata |
| `python scripts/summarize_jsonl.py outputs/tracks.jsonl` | Summarize exported tracks |
| `python scripts/benchmark.py --model yolo11n.pt --source video.mp4` | Measure inference performance |

For RTSP input, pass the stream URL through `--source` without committing credentials.

## Edge AI deployment

The original project included embedded deployment work on **NVIDIA Jetson**, **Raspberry Pi 5**, and **Raspberry Pi 5 with a Hailo AI HAT accelerator**.

The public repository keeps the inference path hardware-neutral. Device-specific Hailo compiled model artifacts, private production weights, and deployment configuration are intentionally not included.

No Hailo-specific FPS figure is claimed here unless it is measured on the stated model, runtime, input size, and hardware configuration.

## Code map

| Location | Responsibility |
| --- | --- |
| [`src/surveillance.py`](src/surveillance.py) | Video-to-detection/tracking pipeline |
| [`src/result_adapter.py`](src/result_adapter.py) | Model result normalization |
| [`src/track_record.py`](src/track_record.py), [`src/track_summary.py`](src/track_summary.py) | Track records and summaries |
| [`src/class_filter.py`](src/class_filter.py), [`src/export.py`](src/export.py) | Reporting filters and JSONL export |
| [`src/config.py`](src/config.py), [`config/`](config/) | Runtime configuration |
| [`tests/`](tests/), [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | Unit tests and automated checks |

## Verify

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
ruff check .
```

## More detail

[Project evidence: code, tests, and research boundaries](docs/project-evidence.md)

[Architecture](docs/architecture.md) · [Deployment](docs/deployment.md) · [Verification](docs/verification.md) · [Performance](docs/performance.md) · [Contributing](CONTRIBUTING.md)

**Repository boundary:** Private footage, production model weights, company source code, credentials, Hailo deployment artifacts, and confidential production configuration are not included. Historical performance claims from the original project are described separately in [performance notes](docs/performance.md) and are not reproducible from this repository alone.

**Author:** [Dewansh Pandey](https://github.com/dewanshpandey04)
