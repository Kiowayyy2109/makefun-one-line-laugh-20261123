"""Write one funny line to the entry file.

Deterministic, Python 3.13 standard library only, no network access,
no reads of files outside this repo.
"""

import os
from pathlib import Path

LINE = "I bought a standing desk to fix my posture \u2014 now I just slouch vertically."

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    output_path = Path(os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
