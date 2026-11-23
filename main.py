"""Make the AI Judge Laugh: Office Jokes - a make.fun entry.

The whole entry is one single-line joke about office life (under 200
characters). This program's only job is to deliver that text to
/output/entry.txt, deterministically.
"""

import os
from pathlib import Path

TEXT = (
    "I told my calendar I needed focus time, so it booked a meeting to "
    "discuss why I'm always in meetings."
)

# The competition's gate: entry.txt must be UTF-8 text of 1 to 199
# characters, a single line. Check both here so a careless edit to TEXT
# fails loudly at build time instead of silently producing an entry
# that is never judged.
MAX_CHARS = 199


def check_text(text: str) -> None:
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke is {len(text)} characters, gate allows 1-{MAX_CHARS}")
    if "\n" in text:
        raise ValueError("joke must be a single line")


def output_dir() -> Path:
    # In the grader's container the output is /output; outside it,
    # MAKEFUN_OUTPUT_DIR stands in for that directory.
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    check_text(TEXT)
    target = output_dir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
