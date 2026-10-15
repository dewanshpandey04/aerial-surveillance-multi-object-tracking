# Aerial Surveillance & Multi-Object Tracking

**Python · YOLO · ByteTrack · OpenCV · RTSP · Pytest**

A real-time computer vision project for detecting and tracking objects in webcam, video-file, and network-stream inputs. Includes reusable tracking metadata, JSONL export, class filters, metrics, and unit tests.

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

[Architecture](docs/architecture.md) · [Deployment](docs/deployment.md) · [Verification](docs/verification.md) · [Performance](docs/performance.md) · [Contributing](CONTRIBUTING.md)

**Publication boundary:** This is a public portfolio implementation. Private footage, production model weights, company source code, and credentials are not included. Historical performance claims from the original project are described separately in [performance notes](docs/performance.md) and are not reproducible from this repository alone.

**Author:** [Dewansh Pandey](https://github.com/dewanshpandey04)
