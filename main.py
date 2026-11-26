"""Funniest Time Machine Warning Label.

Writes one warning label for a time machine (120 characters or fewer)
to /output/entry.txt. Python 3.13, standard library only.
"""

import os

LABEL = "WARNING: Do not photograph the dinosaurs. The flash is why they never saw the meteor coming."


def main() -> None:
    if len(LABEL) > 120:
        raise ValueError("label exceeds 120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LABEL)


if __name__ == "__main__":
    main()
