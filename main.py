#!/usr/bin/env python3
"""Write the entry text to /output/entry.txt.

program/v1 entry: offline, deterministic, Python 3 standard library only.
"""

import sys

# The entrant's own make.fun handle. Criterion 1 fixes this text; it is not a
# slogan and cannot be swapped for a different, funnier-looking name.
ENTRY_TEXT = "ekilingkey-coder"

# Absolute path the sealed scorer reads.
OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH, text=ENTRY_TEXT):
    """Write the exact UTF-8 bytes of the handle, with no trailing newline."""
    data = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    return data


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv:
        sys.stderr.write("usage: main.py\n")
        return 2
    write_entry()
    return 0


if __name__ == "__main__":
    sys.exit(main())
