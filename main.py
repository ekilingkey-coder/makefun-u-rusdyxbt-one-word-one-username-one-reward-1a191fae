#!/usr/bin/env python3
"""Write the entry text to /output/entry.txt.

program/v1 entry: offline, deterministic, Python 3 standard library only.
Run with no arguments to write the file; run with --check to read it back
and confirm the bytes match.
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


def check_entry(path=OUTPUT_PATH, text=ENTRY_TEXT):
    """Read back the written file and report whether its bytes match exactly."""
    expected = text.encode("utf-8")
    try:
        with open(path, "rb") as handle:
            actual = handle.read()
    except OSError as exc:
        sys.stderr.write("check: MISMATCH (read failed: %s)\n" % exc)
        return 1

    match = actual == expected
    verdict = "MATCH" if match else "MISMATCH"
    sys.stdout.write(
        "check: %s path=%s expected_bytes=%d actual_bytes=%d expected=%r actual=%r\n"
        % (verdict, path, len(expected), len(actual), expected, actual)
    )
    return 0 if match else 1


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv == ["--check"]:
        return check_entry()
    if argv:
        sys.stderr.write("usage: main.py [--check]\n")
        return 2
    write_entry()
    return 0


if __name__ == "__main__":
    sys.exit(main())
