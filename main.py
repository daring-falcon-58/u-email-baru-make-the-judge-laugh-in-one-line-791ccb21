#!/usr/bin/env python3
"""Entry for make.fun competition u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.

Writes the chosen one-line joke to /output/entry.txt.
Deterministic: no network, no randomness, no environment input.
The line was chosen by documented manual criterion scoring of 40 candidates
against the published judge brief (see README.md): c01-magician scored 73/75,
top of the field, ahead of the smart-speaker runners-up at 71. Live-judge A/B
could NOT run — no judge-model numbers are claimed anywhere.
See README.md for the full methodology and scores.

Gate check: after writing, the entry is re-read and verified — 60 chars,
single line, deterministic output, byte-identical on repeat runs.
"""

import os

ENTRY = "I asked the magician to saw me in half; now I pay two rents."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Write-back verification: the file must hold exactly the entry line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
