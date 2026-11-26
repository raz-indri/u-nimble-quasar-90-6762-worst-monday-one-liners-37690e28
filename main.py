"""Worst Monday One-Liners: write exactly one funny line to /output/entry.txt."""

import os

LINE = (
    "The stand-up asked what I did Monday. I said 'nothing.' "
    "The transcript said 14,000 tokens. We compromised on 'an incident.'"
)


def main() -> None:
    # Gate: the entry must be 1-140 characters of non-whitespace text.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "line must be 1-140 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
