from __future__ import annotations


def parse_source(value: str):
    """Convert webcam index strings to int; keep paths/URLs as strings."""
    value = value.strip()
    return int(value) if value.isdigit() else value


def safe_stream_label(source: str) -> str:
    """Return a display-safe source label without exposing URL credentials."""
    if "://" not in source:
        return source
    scheme = source.split("://", 1)[0]
    return f"{scheme}://<redacted-stream>"
