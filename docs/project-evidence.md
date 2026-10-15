# Project evidence and implementation map

This page connects the public repository to the broader **GOBABYGO / VTOL AI / detection-model** work without implying that private code or datasets are published.

| Work area | Public evidence | Verification |
| --- | --- | --- |
| Live camera and video processing | [`src/surveillance.py`](../src/surveillance.py), [`src/stream.py`](../src/stream.py) | [Stream tests](../tests/test_stream.py) |
| Object detection and multi-object tracking | [`src/surveillance.py`](../src/surveillance.py), [`src/result_adapter.py`](../src/result_adapter.py) | [Adapter tests](../tests/test_result_adapter.py) |
| Class-based reporting | [`src/class_filter.py`](../src/class_filter.py), [`src/track_summary.py`](../src/track_summary.py) | [Filter tests](../tests/test_class_filter.py) |
| Structured tracking metadata | [`src/export.py`](../src/export.py), [`scripts/summarize_jsonl.py`](../scripts/summarize_jsonl.py) | [Export tests](../tests/test_export.py) |
| Reproducibility and quality | [`scripts/benchmark.py`](../scripts/benchmark.py), [CI](../.github/workflows/ci.yml) | Run `python -m pytest -q` and `ruff check .` |
| Embedded edge deployment | [Deployment notes](deployment.md), [Performance notes](performance.md) | Hardware/runtime-specific benchmarking required |

## Related engineering work not distributed here

- **VTOL AI integration:** vehicle-specific onboard integrations are not included or independently demonstrated here.
- **Detection-model training:** private datasets, experiment outputs, checkpoints, and trained company weights are not published. This repository demonstrates inference and tracking interfaces, not a reproducible model-training result.
- **Hailo AI HAT deployment:** the professional project included Raspberry Pi 5 + Hailo AI HAT edge-inference work. Device-specific compiled model artifacts, private production weights, and deployment configuration are not published.
- **GOBABYGO system:** the public code is a standalone implementation of reusable perception/tracking components; it is not a copy of the complete original system.

## How to verify

1. Follow the [quick start](../README.md#quick-start).
2. Run the automated tests and lint commands in the README.
3. Use a public or self-recorded, authorized test video to reproduce tracking and metadata export.
4. Record hardware, accelerator/runtime, model, input resolution, dataset permissions, and measured results before publishing benchmarks.

No production camera addresses, access tokens, private footage, model weights, compiled accelerator artifacts, or proprietary flight software should be committed.
