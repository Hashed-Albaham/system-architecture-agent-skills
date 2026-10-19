#!/usr/bin/env python3
"""Validate the portable AI system-design skill package using only Python's standard library."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "ai-skill"
SKILLS = PACKAGE / "skills"
errors: list[str] = []
seen_names: set[str] = set()


def validate_skill(skill_file: Path) -> None:
    rel = skill_file.relative_to(ROOT)
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{rel}: missing YAML frontmatter start")
        return
    closing = text.find("\n---\n", 4)
    if closing < 0:
        errors.append(f"{rel}: missing YAML frontmatter end")
        return
    frontmatter = text[4:closing]
    name_match = re.search(r"(?m)^name:\s*([^\s]+)\s*$", frontmatter)
    description_match = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
    if not name_match:
        errors.append(f"{rel}: missing name field")
    else:
        name = name_match.group(1)
        if name in seen_names:
            errors.append(f"{rel}: duplicate skill name {name}")
        seen_names.add(name)
    if not description_match:
        errors.append(f"{rel}: missing description field")
    elif len(description_match.group(1)) > 1024:
        errors.append(f"{rel}: description exceeds 1024 characters")

    body = text[closing + 5:]
    if len(body.splitlines()) > 500:
        errors.append(f"{rel}: body exceeds 500-line guidance")
    if not re.search(r"(?m)^# .+", body):
        errors.append(f"{rel}: missing H1 title")
    if not re.search(r"(?m)^## .+", body):
        errors.append(f"{rel}: missing H2 section")

root_skill = PACKAGE / "SKILL.md"
if not root_skill.is_file():
    errors.append("Missing ai-skill/SKILL.md")
else:
    validate_skill(root_skill)

specialists = sorted(SKILLS.glob("*/SKILL.md"))
for skill_file in specialists:
    validate_skill(skill_file)
if len(specialists) != 11:
    errors.append(f"Expected 11 specialist skills, found {len(specialists)}")

crosswalk = PACKAGE / "references" / "chapter-to-skill-crosswalk.md"
if not crosswalk.is_file():
    errors.append("Missing ai-skill/references/chapter-to-skill-crosswalk.md")
else:
    text = crosswalk.read_text(encoding="utf-8")
    chapter_count = len(re.findall(r"(?m)^### Chapter \d+ — ", text))
    if chapter_count != 28:
        errors.append(f"Expected 28 chapter entries in crosswalk, found {chapter_count}")
    if "## Synthesis" not in text:
        errors.append("Crosswalk is missing the synthesis section")

# Validate relative Markdown links in every document shipped inside the package.
for markdown_file in PACKAGE.rglob("*.md"):
    text = markdown_file.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        local_target = target.split("#", 1)[0]
        if not (markdown_file.parent / local_target).resolve().exists():
            errors.append(f"{markdown_file.relative_to(ROOT)}: broken local link {target}")

if errors:
    print("Validation failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"Validated the root skill, {len(specialists)} specialist skills, all 28 chapter entries, and package Markdown links.")
