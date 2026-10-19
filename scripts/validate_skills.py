#!/usr/bin/env python3
"""Validate portable agent skill directories in this repository."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED_SECTIONS = ("## ",)
errors: list[str] = []
count = 0

for skill_file in sorted(SKILLS.glob("*/SKILL.md")):
    count += 1
    text = skill_file.read_text(encoding="utf-8")
    rel = skill_file.relative_to(ROOT)
    if not text.startswith("---\n"):
        errors.append(f"{rel}: missing YAML frontmatter start")
        continue
    closing = text.find("\n---\n", 4)
    if closing < 0:
        errors.append(f"{rel}: missing YAML frontmatter end")
        continue
    frontmatter = text[4:closing]
    if not re.search(r"(?m)^name:\s*[^\s]+\s*$", frontmatter):
        errors.append(f"{rel}: missing name field")
    if not re.search(r"(?m)^description:\s*.+$", frontmatter):
        errors.append(f"{rel}: missing description field")
    body = text[closing + 5:]
    if len(body.splitlines()) > 500:
        errors.append(f"{rel}: body exceeds 500-line guidance")
    if not re.search(r"(?m)^# .+", body):
        errors.append(f"{rel}: missing H1 title")
    if not re.search(r"(?m)^## .+", body):
        errors.append(f"{rel}: missing H2 section")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
        if "://" not in target and not target.startswith("#"):
            if not (skill_file.parent / target).resolve().exists():
                errors.append(f"{rel}: broken local link {target}")

if count == 0:
    errors.append("No skills/*/SKILL.md files found")
if errors:
    print("Skill validation failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"Validated {count} skill files successfully.")
