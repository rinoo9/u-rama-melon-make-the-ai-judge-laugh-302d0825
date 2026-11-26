#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun bounty entry.

Writes one joke about office life to /output/entry.txt: a single line
of 1 to 200 characters, nothing else.

The joke takes the "we're a family here" line literally. If the office
really is a family, then the manager owes the employee an allowance —
and the reward for asking is being sent to their room like a child.

The joke is a fixed constant. No input, no randomness, no clock, no
network: the program writes byte-identical output on every run.
"""

import os
import sys

PUNCHLINE = (
    "HR said to treat the office like family, so I asked my manager "
    "for my allowance and got sent to my room."
)
GATE_MIN = 1
GATE_MAX = 200
OUTPUT_FILE = "/output/entry.txt"


def check_gate(line):
    """List every way the line breaks the bounty gate; empty means pass."""
    faults = []
    if not line.strip():
        faults.append("entry is only whitespace")
    if len(line) < GATE_MIN or len(line) > GATE_MAX:
        faults.append(
            f"entry is {len(line)} chars, gate is {GATE_MIN}-{GATE_MAX}"
        )
    if "\n" in line or "\r" in line:
        faults.append("entry must be a single line")
    return faults


def main():
    faults = check_gate(PUNCHLINE)
    if faults:
        for fault in faults:
            print(f"gate failed: {fault}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as target:
        target.write(PUNCHLINE + "\n")


if __name__ == "__main__":
    main()
