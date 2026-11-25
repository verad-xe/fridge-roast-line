#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — write one roast of a smart fridge.

The entry is a single line, at most 200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt. The gate self-check below enforces the
competition's limits before anything is written: 1 to 200 characters,
not only whitespace, a single line.
"""

import os
import sys

LINE = (
    "My smart fridge caught me eating cake at 2 a.m., emailed my doctor, "
    "then ran out of ice. It can judge me \u2014 it just can't chill."
)


def main() -> int:
    text = LINE
    # Gate self-check: exactly the limits the sealed scorer enforces.
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if text != text.strip():
        print("entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back and re-check: a truncated or mangled write must fail here,
    # not in the grader's sandbox.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("output file does not match the entry text", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
