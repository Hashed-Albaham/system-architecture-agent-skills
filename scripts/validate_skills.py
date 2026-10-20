#!/usr/bin/env python3
"""Validate the bilingual portable AI system-design skill package."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "ai-skill"
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
    if not name_match:
        errors.append(f"{rel}: missing name field")
    else:
        name = name_match.group(1)
        if name in seen_names:
            errors.append(f"{rel}: duplicate skill name {name}")
        seen_names.add(name)
    if not re.search(r"(?m)^description:\s*.+$", frontmatter):
        errors.append(f"{rel}: missing description field")
    body = text[closing + 5:]
    if len(body.splitlines()) > 500:
        errors.append(f"{rel}: body exceeds 500-line guidance")
    if not re.search(r"(?m)^# .+", body):
        errors.append(f"{rel}: missing H1 title")
    if not re.search(r"(?m)^## .+", body):
        errors.append(f"{rel}: missing H2 section")


required_routing_headings = {
    PACKAGE / "SKILL.md": "## Automatic request routing and skill invocation",
    PACKAGE / "ar" / "SKILL.md": "## التوجيه التلقائي للطلب واستدعاء المهارات",
    PACKAGE / "references" / "skill-router.md": "## Automatic routing from the user's request",
    PACKAGE / "ar" / "references" / "skill-router.md": "## التوجيه التلقائي من طلب المستخدم",
}
for routing_file, heading in required_routing_headings.items():
    if not routing_file.is_file() or heading not in routing_file.read_text(encoding="utf-8"):
        errors.append(f"{routing_file.relative_to(ROOT)}: missing automatic skill-routing section")


for relative in (Path("SKILL.md"), Path("ar/SKILL.md")):
    path = PACKAGE / relative
    if path.is_file():
        validate_skill(path)
    else:
        errors.append(f"Missing ai-skill/{relative.as_posix()}")

english_skills = sorted((PACKAGE / "skills").glob("*/SKILL.md"))
arabic_skills = sorted((PACKAGE / "ar" / "skills").glob("*/SKILL.md"))
for path in english_skills + arabic_skills:
    validate_skill(path)
if len(english_skills) != 11:
    errors.append(f"Expected 11 English specialist skills, found {len(english_skills)}")
if len(arabic_skills) != 11:
    errors.append(f"Expected 11 Arabic specialist skills, found {len(arabic_skills)}")

for lang_path in (PACKAGE / "references" / "chapter-to-skill-crosswalk.md", PACKAGE / "ar" / "references" / "chapter-to-skill-crosswalk.md"):
    if not lang_path.is_file():
        errors.append(f"Missing {lang_path.relative_to(ROOT)}")
        continue
    text = lang_path.read_text(encoding="utf-8")
    chapter_count = len(re.findall(r"(?m)^### Chapter \d+ — ", text))
    # Arabic crosswalk uses a localized heading format: ### الفصل رقم — title
    if " /ar/" in lang_path.as_posix() or lang_path.parts[-3] == "ar":
        chapter_count = len(re.findall(r"(?m)^### الفصل \d+ — ", text))
    if chapter_count != 28:
        errors.append(f"{lang_path.relative_to(ROOT)}: expected 28 chapters, found {chapter_count}")
    if not re.search(r"(?m)^## (Synthesis|الخلاصة)", text):
        errors.append(f"{lang_path.relative_to(ROOT)}: missing synthesis section")

# Validate relative Markdown links across both language trees and root docs.
for markdown_file in [*PACKAGE.rglob("*.md"), ROOT / "README.md", ROOT / "README.ar.md", ROOT / "AGENTS.md"]:
    if not markdown_file.is_file():
        continue
    text = markdown_file.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        local_target = target.split("#", 1)[0]
        if local_target and not (markdown_file.parent / local_target).resolve().exists():
            errors.append(f"{markdown_file.relative_to(ROOT)}: broken local link {target}")

if errors:
    print("Validation failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print(f"Validated root skills, {len(english_skills)} English and {len(arabic_skills)} Arabic specialists, both chapter maps, and Markdown links.")
