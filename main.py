#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun bounty entry.

Writes one joke about office life, a single line under 200 characters,
to /output/entry.txt. Fully deterministic: no randomness, no network,
no environment input — the same line every run.
"""

import os

JOKE = "My boss said we're a family here, so I asked for a raise and got grounded."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
