# Code Tour

## `src/surveillance.py`

Main live/video/network-stream entry point. It runs YOLO + ByteTrack, renders optional annotated output, reports active tracks, and avoids showing full stream credentials.

## `src/track_summary.py`

Provides a small reusable data model and summary function for active tracks. It is independent of the inference engine and easy to unit test.

## `src/utils.py`

Parses webcam sources and sanitizes stream labels so usernames, passwords, and private endpoints are not exposed by the UI.

## `src/metrics.py`

Maintains rolling latency and approximate FPS metrics without depending on GPU libraries.

## `scripts/benchmark.py`

Runs a repeatable inference timing measurement for a reviewer-selected model, source, image size, and device.

## `tests/`

Validates source parsing, credential redaction, track summaries, and metrics.

## Engineering intent

The project separates ingestion, inference, tracking metadata, metrics, and documentation so reviewers can understand the design without needing access to private datasets or production infrastructure.
