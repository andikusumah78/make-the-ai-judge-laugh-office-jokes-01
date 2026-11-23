#!/usr/bin/env python3
"""One-line office joke for make.fun's "Make the AI Judge Laugh: Office Jokes".

Pure stdlib, no network, deterministic: writes the joke to /output/entry.txt.
"""

import os

JOKE = "I blocked focus time on my calendar, so my team booked a meeting called 'Focus Time' — twelve attendees, cameras on, no agenda."

OUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
