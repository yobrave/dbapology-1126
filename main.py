"""Emit the entry line for make.fun bounty
u-coral-404-the-production-database-apology-5c1fc02a."""

import json
import os
from pathlib import Path

STAMP = "dbap-r31"


def fetch_line():
    base = Path(__file__).resolve().parent
    blob = (base / "entry.txt").read_text(encoding="utf-8")
    cleaned = blob.strip()
    if not cleaned:
        raise SystemExit("entry.txt is blank; nothing to emit")
    for token in ("production", "database", "sorry"):
        if token not in cleaned:
            raise SystemExit(f"entry drifted off theme: no {token!r} in line")
    return cleaned


def place_line(text):
    root = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    root.mkdir(parents=True, exist_ok=True)
    sink = root / "entry.txt"
    with open(sink, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    return sink


def report(sink, size, raw):
    print(json.dumps({
        "verdict": "ok",
        "chars": size,
        "bytes": len(raw.encode("utf-8")),
        "stamp": STAMP,
        "sink": sink.name,
    }))


def main():
    text = fetch_line()
    size = len(text)
    if size > 200:
        raise SystemExit(f"gate breach: {size} chars exceeds 200")
    sink = place_line(text)
    report(sink, size, text)


if __name__ == "__main__":
    main()
