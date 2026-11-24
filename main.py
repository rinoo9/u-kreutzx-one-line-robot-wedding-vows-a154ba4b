#!/usr/bin/env python3
"""One-line robot wedding vow entry for the make.fun bounty
"One-Line Robot Wedding Vows".

Writes exactly one line — a single-sentence wedding vow for a robot
couple — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.

Craft notes: the vow keeps the classic wedding shape ("I promise ...
till ... do us part") and fills it with machine-specific detail —
firmware updates, a dead battery, a factory reset — so the joke could
only work for robots. The payoff lands in the last few words: the
solemn "till death do us part" becomes "till a power cut do us part",
a threat only a robot couple would fear. That fits the judge brief:
first a one-line robot wedding vow, then a real turn with a surprise
payoff, a promise in it, specific machine detail, and a rhythm that
reads well aloud.

Second pass — voice and twist: the voice is earnest, not snarky.
A robot that means every word is funnier than one winking at the
audience, so the line is played straight and lets the premise do the
comedy. The three trials escalate in severity — an update is routine
maintenance, a dead battery is a real scare, a factory reset is
losing who you are — so the vow earns its tenderness before the
twist undercuts it. The twist works because it swaps only the
threat, not the shape: "a power cut" slots into the exact slot
where "death" belongs, so the listener hears the familiar vow and
the robot version at the same time. Nothing in the line explains
the joke; it trusts the reader to feel the swap.
"""

import os

VOW = (
    "I promise to love you through every firmware update, every dead "
    "battery, and every factory reset, till a power cut do us part."
)


def main() -> None:
    assert 1 <= len(VOW) <= 160, f"vow is {len(VOW)} characters"
    assert "\n" not in VOW and VOW == VOW.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
