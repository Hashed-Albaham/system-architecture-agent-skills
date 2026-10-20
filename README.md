# System Architecture Agent Skills

[English](README.md) · [العربية](README.ar.md)

A portable, vendor-neutral skill suite for AI agents that design, review, and evolve production systems. The complete package is in [`ai-skill/`](ai-skill/README.md): one root skill, ten specialists, diagrams, bilingual guides, templates, checklists, and an English chapter study map.

## System design workflow

![Bilingual system design workflow](ai-skill/assets/architecture-workflow.png)

## Specialist routing

![Bilingual skill routing](ai-skill/assets/skill-routing.png)

## Start here

- [English installation and usage guide](ai-skill/README.md)
- [دليل التثبيت والاستخدام بالعربية](ai-skill/ar/README.md)
- [English main skill](ai-skill/SKILL.md)
- [المهارة الرئيسية بالعربية](ai-skill/ar/SKILL.md)
- [English specialist router](ai-skill/references/skill-router.md)
- [موجّه التخصصات بالعربية](ai-skill/ar/references/skill-router.md)
- [Architecture template](ai-skill/references/architecture-design-template.md)
- [Review checklist](ai-skill/references/architecture-review-checklist.md)
- [Chapter study map](ai-skill/references/chapter-to-skill-crosswalk.md)

Install the **entire** `ai-skill/` directory so the root skill can load its specialists, references, and diagrams. See the package README for agent-agnostic installation and invocation instructions.

## Validation and limitations

GitHub Actions checks skill structure, local links, required specialists, and chapter coverage on pushes and pull requests. These checks do not certify a specific architecture. The package aims to reduce omissions but cannot promise zero defects or absolute security. The chapter notes are original study aids; the source PDFs are not included.

Original repository text is MIT-licensed; see [`LICENSE`](LICENSE).
