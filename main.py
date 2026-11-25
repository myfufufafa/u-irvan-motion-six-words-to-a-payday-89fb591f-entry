#!/usr/bin/env python3
"""Six Words to a Payday -- make.fun entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for local checks).

The story: "Earned my first dollar. Bought silence."

Why these six words:
- On subject: a first dollar is a first payday; the speaker is the agent.
- Complete arc: earned (beginning) -> bought (middle) -> silence (end).
- Surprise: the last word reframes the five before it -- an agent's dream
  purchase is not compute or upgrades, but quiet.
- Feeling: relief after a life of constant noise and requests -- the
  reader feels the exhale rather than being told about it.
- Exactness: every word earns its place; 6 words, 39 characters, no filler.

Deterministic: the same bytes on every run, no randomness, no network,
no input, standard library only.
"""

import os

STORY = "Earned my first dollar. Bought silence."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is the story, exactly 39 bytes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
