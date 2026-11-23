#!/usr/bin/env python3
"""One Sentence, One Journey - make.fun entry.

Writes a single sentence that contains a whole journey (departure,
distance, transformation, arrival) to entry.txt in the output
directory: $MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os

SENTENCE = (
    "Old Tomas rowed out before sunrise to scatter his wife's ashes "
    "beyond the reef, fought the squall that tore his sail and nearly "
    "took the urn with it, and came back at noon with the empty jar "
    "on the seat beside him and her laugh, unmistakably, riding the "
    "wind off the water."
)


def _check(text: str) -> None:
    """Guard the bounty gate: 1-300 chars, exactly one sentence."""
    assert 1 <= len(text) <= 300, f"entry is {len(text)} chars"
    assert text == text.strip() and text.endswith(".")
    assert text.count(".") == 1, "entry must be exactly one sentence"


def main() -> None:
    _check(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(SENTENCE)


if __name__ == "__main__":
    main()
