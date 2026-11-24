#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

Writes one line of weather forecast for a city that does not exist
to /output/entry.txt and prints it. Gate: 1-140 UTF-8 characters.
"""

import os

LINE = "In Brollywood, rain falls upward this morning, so umbrellas are decorative and the 8:15 bus is somehow on time for once."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text.encode("utf-8")) <= 140, f"entry is {len(text)} chars, gate is 1-140"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
