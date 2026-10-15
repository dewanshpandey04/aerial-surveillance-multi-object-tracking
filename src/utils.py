from __future__ import annotations


def parse_source(value: str | int) -> int | str:
    """Normalize webcam indexes while preserving file paths and URLs."""
    if isinstance(value, int):
        return value
    text = str(value).strip()
    return int(text) if text.isdigit() else text


def safe_stream_label(source: str) -> str:
    """Return a display-safe source label without exposing URL credentials."""
    if "://" not in source:
        return source
    scheme = source.split("://", 1)[0]
    return f"{scheme}://<redacted-stream>"
