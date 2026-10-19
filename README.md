# System Architecture Agent Skills

A portable, vendor-neutral skill suite for AI agents and engineers designing, reviewing, and implementing production systems. The material is original engineering guidance, not a reproduction of any book or proprietary training corpus.

## Included skills

| Skill | Focus |
|---|---|
| `00-system-architect-orchestrator` | Discovery, requirements, sizing, architecture flow and quality gates |
| `01-data-models-storage` | Data-model selection, indexes, B-tree/LSM concepts, OLTP/OLAP |
| `02-data-encoding-evolution` | Schemas, wire formats, compatibility, API and event evolution |
| `03-replication-partitioning` | Replication, sharding, consistency options, rebalancing |
| `04-transactions-consensus-consistency` | Isolation, coordination, consensus, clocks and failure semantics |
| `05-batch-stream-processing` | Batch, messaging, logs, CDC, stream state and event time |
| `06-infrastructure-primitives` | Rate limits, IDs, caches, KV services, URL shortening |
| `07-product-architecture-blueprints` | Reusable blueprints for common high-scale product capabilities |

## Use with any agent

Each skill is a standalone directory containing `SKILL.md` with standard YAML `name` and `description` frontmatter. Copy the relevant directory into the agent's supported skills folder, or paste its `SKILL.md` into an agent's project instructions. For repository-aware agents, retain the whole `skills/` tree and point the agent at `skills/00-system-architect-orchestrator/SKILL.md`.

The orchestration skill selects domain skills and requires the agent to state assumptions, calculate capacity, show trade-offs, model failure modes, and verify decisions. Use domain skills directly when the task is narrow.

## Design principles

- Top-down: establish scope, interfaces and workload before choosing components.
- Bottom-up: verify storage, ordering, replication, concurrency and failure behavior.
- Quantitative: use explicit units, peak factors, retention assumptions and percentile SLOs.
- Portable: no proprietary runtime, vendor SDK or agent-specific tool dependency.
- Honest: distinguish guarantees from common implementations; verify current product behavior against official documentation before implementation.

## Copyright and sources

This repository provides original explanations of widely used engineering concepts. It does not contain full-text excerpts, chapter-by-chapter substitutes, or a claim of reproducing any source book. For deeper reading, consult the publishers' authorized editions of *Designing Data-Intensive Applications* by Martin Kleppmann and *System Design Interview* by Alex Xu. Do not add copyrighted source PDFs or long verbatim excerpts to this repository.

## Validation

Run `python3 scripts/validate_skills.py` from the repository root. The validator checks frontmatter, required sections, links and line limits. It does not certify the correctness of a particular architecture; domain review and workload-specific tests remain necessary.

## License

Original repository text is licensed under MIT; see `LICENSE`. Third-party names are used only for identification. No third-party book content is included.
