#!/usr/bin/env python3
"""Two-Sentence Horror - make.fun entry."""
from pathlib import Path

LINES = (
    "I waved at my neighbor through his window every evening for a year.",
    "The police say his house has stood empty since the fire, "
    "but the waving never stopped.",
)
ENTRY = "\n".join(LINES)
OUTPUT = Path("/output/entry.txt")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
