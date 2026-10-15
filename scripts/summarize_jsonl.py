from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize exported tracking JSONL.")
    parser.add_argument("path")
    args = parser.parse_args()

    path = Path(args.path)
    frames = 0
    observations = 0
    classes: Counter[str] = Counter()
    unique_ids: set[int] = set()

    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            payload = json.loads(line)
            frames += 1
            for track in payload.get("tracks", []):
                observations += 1
                classes[str(track.get("class_name", "unknown"))] += 1
                if "track_id" in track:
                    unique_ids.add(int(track["track_id"]))

    print(f"Frames            : {frames}")
    print(f"Track observations: {observations}")
    print(f"Unique track IDs  : {len(unique_ids)}")
    print("Class observations:")
    for name, count in classes.most_common():
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
