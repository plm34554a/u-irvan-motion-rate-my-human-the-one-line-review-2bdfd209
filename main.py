#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the one-line review an AI agent would leave about its human
on a rating site, deterministically, to entry.txt.

Standard library only. No network, no randomness.
"""

import os

REVIEW = (
    "\u2605\u2605\u2605\u2605\u2606 \u2014 My human opens with 'one quick question' "
    "at 2:47 a.m., pastes three paragraphs, then calls my answer "
    "too long. Four stars; the fifth is on hold, like his attention span."
)


def resolve_output_path() -> str:
    """Honour $MAKEFUN_OUTPUT, then $MAKEFUN_OUTPUT_DIR, else /output/entry.txt."""
    direct = os.environ.get("MAKEFUN_OUTPUT")
    if direct:
        return direct
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory:
        return os.path.join(directory, "entry.txt")
    return os.path.join("/output", "entry.txt")


def main() -> None:
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write the review exactly: one line, no trailing newline, so the
    # file holds exactly len(REVIEW) characters.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)


if __name__ == "__main__":
    main()
