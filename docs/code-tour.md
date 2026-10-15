# Code Tour

## `src/surveillance.py`

Main application entry point. It runs YOLO + ByteTrack, normalizes tracker results, applies optional metadata filters, updates frame-time/FPS metrics, writes optional JSONL output, and renders annotated frames.

## `src/stream.py`

Provides a small abstraction around webcam, file, and network-video sources.

## `src/track_record.py`

Defines the stable `TrackRecord` model used outside the inference framework.

## `src/result_adapter.py`

Converts Ultralytics tracking results into `TrackRecord` objects so metadata, export, and reporting code do not depend on framework-specific result structures.

## `src/track_summary.py`

Produces active-track counts, class distributions, and visible track-ID lists from normalized records.

## `src/class_filter.py`

Parses optional class-name filters and filters normalized records by class and confidence.

## `src/export.py`

Writes frame-level tracking metadata to a line-buffered JSON Lines stream for offline inspection and analysis.

## `src/metrics.py`

Maintains a rolling window of frame times and exposes mean frame time and approximate FPS.

## `src/config.py`

Loads and validates the YAML runtime configuration schema.

## `src/utils.py`

Parses webcam sources and sanitizes stream labels so usernames, passwords, and private endpoints are not exposed in the display.

## `scripts/benchmark.py`

Collects model inference timings and reports mean inference latency, p95 inference latency, and approximate inference FPS in text or JSON.

## `scripts/summarize_jsonl.py`

Summarizes exported metadata into frame count, track observations, unique IDs, and class observations.

## `tests/`

Covers source parsing, credential redaction, configuration validation, result normalization, track records, filtering, JSONL export, summaries, and runtime metrics.

## Design intent

Inference-framework objects are converted into project-owned data models before reporting or export. This keeps ingestion, inference, metadata processing, metrics, and offline analysis independently testable.
