"""Office joke entry for make.fun: "Make the AI Judge Laugh: the Office Joke Open".

Writes the single joke line to /output/entry.txt.

The joke follows the winning joke pattern (K21): a 3-beat reversal.
Setup: an AI assistant doing ordinary office work (emails, meetings).
Escalation: it takes on more and more of the owner's job.
Punchline in the final clause: the tool turns on its owner — it is asked
to write the owner's own performance review.
"""

import os

ENTRY = (
    "My AI assistant now answers my emails, attends my meetings, "
    "and just got asked to write my performance review — about me."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate from RULES: entry must be 1-200 characters of non-blank UTF-8.
    text = ENTRY
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be blank")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
