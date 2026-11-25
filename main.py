#!/usr/bin/env python3
"""Entry for make.fun's "The One-Line Exit".

Writes the funniest single-line resignation letter to /output/entry.txt
(UTF-8, 1-140 characters, no trailing newline).
"""
import os

ENTRY = (
    "Consider this my two weeks' notice, compressed: I resign, and "
    "I'm taking the plant - it never scheduled a meeting."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
