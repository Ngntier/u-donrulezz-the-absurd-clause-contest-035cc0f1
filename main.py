"""Entry for The Absurd Clause Contest.

The joke angle: the line is built as a routine consent clause, the kind a
reader skims past without thinking, and the thing being consented to is a
quietly menacing real-world intrusion, softened only by courteous legal
qualifiers. The humour comes from the register doing the work: the clause
never winks, never raises its voice, and the politeness of the wording is
exactly what makes the intrusion funny.
"""

import os

ENTRY = (
    "The User consents to being followed home by a Company representative, "
    "at a respectful distance, for quality-assurance purposes."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    # The file is written as bytes, so enforce the byte budget directly
    # too — for ASCII text this equals the char count, but it stays
    # correct if the entry ever gains a non-ASCII character.
    if len(ENTRY.encode("utf-8")) > 200:
        raise ValueError("entry must be at most 200 bytes")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
