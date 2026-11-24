#!/usr/bin/env python3
"""One-line office joke entry.

Writes a single original one-line joke about office life to
/output/entry.txt (at most 200 characters, one line).
"""

import os

JOKE = (
    "I renamed our weekly meeting 'This Could Have Been an Email' and "
    "attendance doubled \u2014 apparently everyone wanted to watch "
    "somebody finally say it."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    # The gate refuses anything but 1-200 characters of non-blank text on a
    # single line, so enforce that here instead of trusting the constant.
    joke = JOKE.strip()
    assert joke, "joke must not be blank"
    assert "\n" not in joke, "joke must be a single line"
    assert len(joke) <= MAX_CHARS, f"joke is {len(joke)} chars, over {MAX_CHARS}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    # The grader runs as nobody (uid 65534): the file must be world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
