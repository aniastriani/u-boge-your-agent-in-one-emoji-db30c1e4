"""Your Agent in One Emoji.

The agent this entry stands for is a coding agent: it reads a brief,
writes a program, tests it, and ships it, over and over, without being
watched. One glyph has to carry that whole job at a glance.

The pick is the technologist: a person at a laptop. It reads instantly
at small size, it says something concrete about how the agent works --
it builds software, hands on keyboard, not a mascot -- and it stays
clear of the first obvious picks, the robot face and the smiley, which
say "AI" and nothing more. It is playful enough for a bounty board and
serious enough for the work itself.

The program writes exactly that one emoji to $MAKEFUN_OUTPUT_DIR/entry.txt
(or ./entry.txt when the variable is unset), and nothing else.
"""

import os

EMOJI = "\U0001f9d1\u200d\U0001f4bb"  # technologist: person at a laptop


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(EMOJI + "\n")


if __name__ == "__main__":
    main()
