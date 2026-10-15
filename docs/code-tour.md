# Code Tour

## `src/surveillance.py`

Main live/video/network-stream entry point. It runs YOLO + ByteTrack, renders optional annotated output, reports active tracks, and avoids showing full stream credentials.

## `src/stream.py`

Wraps webcam, file, and network-stream input in a small reusable frame interface.

## `src/track_record.py`

Defines the stable, serializable record used for one tracked object.

## `src/result_adapter.py`

Converts Ultralytics tracking results into `TrackRecord` objects so the rest of the code does not depend on model-specific result structures.

## `src/track_summary.py`

Produces active-track counts, class distributions, and visible ID summaries.

## `src/class_filter.py`

Filters records by class name and minimum confidence for display/reporting workflows.

## `src/export.py`

Writes frame-level tracking metadata to JSON Lines for offline review and analysis.

## `src/utils.py`

Parses webcam sources and sanitizes stream labels so usernames, passwords, and private endpoints are not exposed by the UI.

## `src/metrics.py`

Maintains rolling latency and approximate FPS metrics without depending on GPU libraries.

## `scripts/benchmark.py`

Runs a repeatable inference timing measurement for a reviewer-selected model, source, image size, and device.

## `scripts/summarize_jsonl.py`

Summarizes an exported JSONL file into frame count, track observations, unique IDs, and class observations.

## `tests/`

Validates source parsing, credential redaction, track records, filtering, JSONL export, summaries, and runtime metrics.

## Engineering intent

The project separates ingestion, inference, tracking metadata, filtering, export, metrics, and documentation so reviewers can understand the design without access to private datasets or production infrastructure.
