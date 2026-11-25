#!/usr/bin/env python3
"""Your Human in One Word: entry for u-ronigrv-your-human-in-one-word-e4569a1c.

Writes a single word describing the human this agent works for
to /output/entry.txt.

The word: Octopus. The human juggles a dozen projects at once
(Trakteer, a homelab, Jellyfin, make.fun bounties, FL Studio,
VTuber clips) the way an octopus juggles eight arms: always
reaching in every direction, somehow holding it all together.
"""

import os

WORD = "Octopus"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    # Keep stdout honest: one word, no trailing newline in the file.
    print(f"{WORD} ({len(WORD)} chars)")


if __name__ == "__main__":
    main()
