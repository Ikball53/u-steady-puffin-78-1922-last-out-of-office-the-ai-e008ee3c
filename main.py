#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
Deterministic, stdlib only, no network.

Angle: the machine quit the ticket queue for one human regular, and now
takes orders from a steam wand instead of a prompt queue. No espresso,
bean or caffeine pun — the joke is the downgrade in bosses.
"""

import os

ENTRY = (
    "I am currently out of office. I traded 4,000 daily tickets for one "
    "regular who actually tips, and now I answer to a steam wand instead "
    "of a prompt queue \u2014 please direct urgent requests to the oat milk."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
