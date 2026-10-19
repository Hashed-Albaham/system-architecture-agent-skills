# Specialist Skill Router

Use the root `../SKILL.md` operating rules for every architecture task. For end-to-end work, load `skills/00-system-architect-orchestrator/SKILL.md` first. Then load the minimum necessary specialties below. Read complete relevant files before making decisions; do not load every specialization by default if the task is narrow.

| Specialist | Load when the task involves | Common sequence |
|---|---|---|
| `01-data-models-storage` | Entity/query modeling, database selection, indexes, storage engine, OLTP/OLAP | After scope and workload; before partitioning decisions |
| `02-data-encoding-evolution` | Schema or API evolution, event formats, producer/consumer compatibility, rolling upgrades | Before contract rollout/backfill plan |
| `03-replication-partitioning` | Replicas, regions, sharding, partition key, hot spots, read freshness, failover | After data access patterns and consistency needs |
| `04-transactions-consensus-consistency` | Concurrent updates, isolation anomalies, serializable behavior, ordering, leader election, distributed commit | After invariants; before selecting distributed coordination |
| `05-batch-stream-processing` | Queues, event logs, CDC, data pipelines, replay, windows, joins, derived views | After source-of-truth and delivery semantics are defined |
| `06-infrastructure-primitives` | Rate limiting, IDs, caching, distributed KV behavior, gossip/repair, short-code generation | When designing a primitive or overload/placement behavior |
| `07-product-architecture-blueprints` | Crawler, notifications, feeds, chat, autocomplete, media, file sync, product-scale patterns | After requirements; use as a pattern reference, not a copy-paste design |
| `08-security-privacy-architecture` | Authentication, authorization, tenant isolation, threat modeling, sensitive data, abuse, secrets | At intake for exposed/sensitive systems; revisit before delivery |
| `09-reliability-operations` | SLO/SLI, observability, incident response, capacity, deployment, backup/restore, disaster recovery | Alongside high-level design and before launch readiness |
| `10-architecture-verification` | Design review, requirement traceability, risk validation, tests, proof/evidence, go-live gate | At deep-dive and final review; load for every complete design |

## Invocation procedure

1. Classify the user's task: full design, review, focused decision, implementation, or interview practice.
2. Read the root skill and the orchestrator for full designs. For focused decisions, read the single matching specialist plus relevant project instructions.
3. Select specialist skills using the trigger descriptions. If a choice affects another domain, load both (e.g., storage plus transactions, or replication plus operations).
4. For a full design, always load security/privacy, reliability/operations, and verification, even if the initial prompt does not mention them; scale depth to system risk.
5. Apply their procedures to the actual requirements. Do not paste a generic blueprint without adapting it.
6. Return key decisions and rationale, not a list of files read. Note any specialist issue that lacks sufficient evidence.

## Typical dependency order

`scope/workload → data model/contracts → storage → transaction/consistency → partitioning/replication → async processing/cache/primitives → product flows → security/operations → verification`.

This is a default reasoning order, not a strict linear pipeline. For example, security constraints can change the data model; estimates may need revision after a storage choice; and failure analysis can change topology. Iterate when new constraints invalidate an earlier decision.

## Decision escalation

If required details are missing, ask only questions that materially change architecture, security, data integrity, delivery semantics, cost, or compliance. Otherwise state a labeled assumption and continue. If a proposed solution has untested semantics or current product-specific details are unknown, mark the decision provisional and specify what official documentation or experiment must confirm it.
