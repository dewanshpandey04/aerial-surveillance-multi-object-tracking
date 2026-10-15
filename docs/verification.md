# Verification

## Automated quality gates

GitHub Actions runs the following checks on Python 3.10, 3.11, and 3.12:

```powershell
python -m compileall -q src scripts tests
ruff check .
python -m src.surveillance --help
python scripts/benchmark.py --help
python scripts/summarize_jsonl.py --help
python -m pytest -q
```

## Unit-test coverage

The test suite validates:

- webcam/source parsing
- credential-safe network-stream labels
- YAML configuration validation
- tracker-result normalization using lightweight test doubles
- normalized track-record serialization
- class-name parsing and confidence filtering
- track summaries and persistent IDs
- context-managed JSONL metadata export
- rolling frame-time and approximate FPS metrics

## Performance verification

Use `scripts/benchmark.py` to record:

- measured frame count
- mean inference latency
- p95 inference latency
- approximate inference FPS
- model
- image size
- compute device

Only compare performance values measured with a stated model, precision, input size, device, and source pipeline.
