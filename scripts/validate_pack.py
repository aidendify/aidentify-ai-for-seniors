#!/usr/bin/env python3
"""Pack-specific validator for the Everyday AI for Seniors pack.

Checks the PRD P0 requirements:
  - 12 large-print prompt cards (prompt-cards/*.md) present and non-empty
  - 6 no-code skill files (skills/*.md) present and non-empty

Run from inside products/ai-for-seniors/:
    python3 scripts/validate_pack.py
Exits 0 on success, 1 on any failure.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXPECTED_PROMPT_CARDS = 12
EXPECTED_SKILLS = 6


def nonempty_md_files(subdir: str, expected: int) -> tuple[list[Path], list[str]]:
    d = ROOT / subdir
    problems: list[str] = []
    if not d.is_dir():
        return [], [f"missing directory: {subdir}/"]
    files = sorted(d.glob("*.md"))
    if len(files) < expected:
        problems.append(f"{subdir}/ has {len(files)} .md files, expected at least {expected}")
    for f in files:
        text = f.read_text(encoding="utf-8").strip()
        if len(text) < 50:
            problems.append(f"{f.relative_to(ROOT)} look empty or near-empty")
    return files, problems


def main() -> int:
    problems: list[str] = []

    cards, card_problems = nonempty_md_files("prompt-cards", EXPECTED_PROMPT_CARDS)
    skills, skill_problems = nonempty_md_files("skills", EXPECTED_SKILLS)
    problems.extend(card_problems)
    problems.extend(skill_problems)

    if problems:
        print("PACK VALIDATION FAILED:")
        for p in problems:
            print(" -", p)
        print(f"  prompt-cards found: {len(cards)}, skills found: {len(skills)}")
        return 1

    print(
        "PACK VALIDATION OK: "
        f"{len(cards)} prompt cards, {len(skills)} skills — all present and non-empty."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())