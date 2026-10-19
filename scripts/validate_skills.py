#!/usr/bin/env python3
"""Validate portable agent skills and the chapter study map."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors: list[str] = []
count = 0


def check_local_links(markdown: str, source: Path, label: str) -> None:
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", markdown):
        if "://" not in target and not target.startswith("#"):
            if not (source.parent / target.split("#", 1)[0]).resolve().exists():
                errors.append(f"{label}: broken local link {target}")


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
    check_local_links(body, skill_file, str(rel))

if count != 8:
    errors.append(f"Expected 8 skill files, found {count}")

crosswalk = ROOT / "references" / "chapter-to-skill-crosswalk.md"
if not crosswalk.is_file():
    errors.append("Missing references/chapter-to-skill-crosswalk.md")
else:
    text = crosswalk.read_text(encoding="utf-8")
    chapter_count = len(re.findall(r"(?m)^### Chapter \d+ — ", text))
    if chapter_count != 28:
        errors.append(f"Expected 28 chapter entries in crosswalk, found {chapter_count}")
    if "## Synthesis" not in text:
        errors.append("Crosswalk is missing the synthesis section")
    check_local_links(text, crosswalk, "references/chapter-to-skill-crosswalk.md")

if errors:
    print("Validation failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"Validated {count} skill files and all 28 chapter entries successfully.")
