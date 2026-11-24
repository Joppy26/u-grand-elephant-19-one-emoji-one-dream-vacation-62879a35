#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt (or the directory named by
MAKEFUN_OUTPUT_DIR). Python 3, standard library only, no network, no clock,
no randomness. Every run produces the exact same file.
"""

import os

# The entry: a single emoji, nothing else.
# A shooting star: the wish itself. A dream vacation is not a beach, it is
# one night far from city lights, lying back, catching a wish as it streaks
# across the dark. Rarer and more specific than sun, sand or plane.
ENTRY = "\U0001f320"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
