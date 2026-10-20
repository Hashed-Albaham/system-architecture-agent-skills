# System Design Agent Skill Package

[English](README.md) · [العربية](ar/README.md)

A portable, vendor-neutral skill suite for AI agents that design, review, and evolve production systems. The root `SKILL.md` is the single entry point: it reads the user's request and designated task brief, then automatically selects one or more relevant specialist skills—the user does not need to choose them. Keep this entire directory together when installing the package.

## Architecture workflow

![Bilingual system design workflow](assets/architecture-workflow.png)

The process begins with scope and measurable requirements, proceeds through workload sizing, data contracts and architecture, then reviews security and operations. Verification closes the loop; new evidence may require revisiting earlier requirements or estimates.

## How the agent selects skills

![Bilingual specialist skill routing](assets/skill-routing.png)

For a full design, load the root skill, the orchestrator, and the relevant domain specialties. Security, reliability/operations, and verification are expected reviews for full designs. For focused tasks, load only the relevant specialist and its dependencies.

## Package contents

| Path | Purpose |
|---|---|
| `SKILL.md` | Main agent skill: activation, quality rules, end-to-end workflow, and output contract |
| `skills/00-system-architect-orchestrator/` | Requirements, workload sizing, architecture flow, and output discipline |
| `skills/01-data-models-storage/` | Data models, indexes, storage engines, and workload fit |
| `skills/02-data-encoding-evolution/` | Schema, API, and event compatibility across versions |
| `skills/03-replication-partitioning/` | Replicas, partitioning, sharding, consistency, and rebalancing |
| `skills/04-transactions-consensus-consistency/` | Transactions, isolation, ordering, coordination, and consensus |
| `skills/05-batch-stream-processing/` | Batch, queues, event logs, CDC, streams, replay, and derived views |
| `skills/06-infrastructure-primitives/` | Rate limiting, identifiers, caching, key-value behavior, and related primitives |
| `skills/07-product-architecture-blueprints/` | Product-scale design patterns for common service types |
| `skills/08-security-privacy-architecture/` | Threat modeling, identity, access control, tenant boundaries, and privacy |
| `skills/09-reliability-operations/` | SLOs, observability, incidents, capacity, backup, and recovery |
| `skills/10-architecture-verification/` | Traceability, tests, evidence, design review, and release gates |
| `references/` | Skill router, design template, review checklist, decision record, and 28-chapter study map |
| `assets/` | Editable Mermaid diagram sources and rendered PNG guides |
| `agent-manifest.yaml` | Machine-readable package metadata and specialist triggers |

## Install and use

If the AI agent supports the Agent Skills format, add the **whole `ai-skill/` directory** to the skill location documented by that agent. Keep `SKILL.md`, `skills/`, `references/`, `assets/`, and the manifest together. Agent-specific installation paths and activation syntax differ; do not assume one product's location works for another.

If automatic skill discovery is unavailable, provide the directory in the agent workspace and prompt:

> Use the System Design Agent skill. Read `ai-skill/SKILL.md` and `ai-skill/references/skill-router.md`. Follow the workflow, load the relevant specialist skills, then deliver a design with assumptions, trade-offs, failure semantics, security, operations, verification, and residual risks.

For a focused task, name the specialist path directly, such as `ai-skill/skills/02-data-encoding-evolution/SKILL.md`. Replace `ai-skill/` with the actual installed path when the folder has a different name. The Arabic counterpart is under `ai-skill/ar/` and mirrors the same structure.

## Useful references

- [Main skill](SKILL.md)
- [Specialist router](references/skill-router.md)
- [Architecture design template](references/architecture-design-template.md)
- [Architecture review checklist](references/architecture-review-checklist.md)
- [Architecture decision record](references/architecture-decision-record.md)
- [Chapter-to-skill study map](references/chapter-to-skill-crosswalk.md)
- [Arabic guide](ar/README.md)

## Automated validation

The GitHub Actions workflow `.github/workflows/validate-skills.yml` runs on pushes to `main`, pull requests, and manual dispatch. It checks skill frontmatter, package links, required skill count, and chapter coverage. Run the same dependency-free check locally from the repository root with `python3 scripts/validate_skills.py`. These checks validate package structure; they do not prove a system design correct or secure.

## Limitations and source notes

No design process can guarantee zero errors. The package aims to reduce omissions through explicit assumptions, verification and residual-risk reporting. The English chapter map uses original concise summaries and does not include or replace the books; source PDFs are not included.
