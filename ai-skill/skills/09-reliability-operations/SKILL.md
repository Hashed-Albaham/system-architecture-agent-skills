---
name: reliability-operations
description: Design or review production reliability, SLIs/SLOs, observability, incident response, capacity, deployment, backup, restore, and disaster recovery. Use when a system will be operated in production or reliability and recovery requirements affect architecture.
---

# Reliability and Operations

## 1. Define service objectives

Translate user expectations into SLIs and SLOs for availability, latency percentiles, freshness, correctness, durability, and recovery. Define measurement windows, error-budget policy, dependency contribution and exclusions. Availability figures are not meaningful without the operation, population, interval and measurement method.

Set RTO (maximum acceptable recovery time) and RPO (maximum acceptable data loss window) by workload. Verify they are compatible with backup frequency, replication acknowledgment, restore throughput and staffing. A replicated system is not a backup against deletion or corruption.

## 2. Failure and capacity model

List component and common-cause failures: process/node, disk, network, zone/region, identity provider, DNS, control plane, external provider, deployment, configuration and operator action. Identify the user-visible failure mode and safe degraded behavior. Calculate headroom for peak, failover, repair, compaction, rebuild, traffic shifts and restore; do not operate every tier at its saturation boundary.

Set timeouts by end-to-end budget. Retries need bounded attempts, exponential backoff with jitter, retry budgets, idempotent semantics and overload protection. Use circuit breakers, bulkheads and load shedding only with explicit recovery behavior. Queues need bounded backlog, age/lag objectives, poison handling, and a safe drain/replay plan.

## 3. Observability

For each SLO, define metrics and alerts that represent user impact. Use structured logs, traces, dependency health, saturation, resource pressure, error rates, replica lag, queue age, cache behavior, shard skew, backup jobs and data-integrity checks. Avoid high-cardinality or sensitive labels. Alerts need an owner, severity, actionable runbook and escalation path; page on symptoms that require action, not every transient anomaly.

## 4. Change and incident management

Use staged rollout, canary or progressive delivery where suitable; monitor, pause and rollback on defined signals. Database and message-schema changes need expand/migrate/contract steps, backfill progress, compatibility and recovery. Test failover, backup restore, regional recovery, credential compromise, overload and queue replay. Run incident reviews that prioritize system learning and prevention.

## 5. Backup and disaster recovery

Define backup scope, consistency, encryption, access separation, retention, immutability where needed, and restore order. Test end-to-end restoration at realistic volume; measure restore time and verify data invariants after recovery. Document dependencies such as keys, schemas, images, DNS, credentials and runbooks. Plan for corruption/deletion detection and point-in-time recovery, not just copy success.

## 6. Operational handoff

For every stateful component, identify owner, on-call, dashboards, alerts, runbook, capacity limits, backup/restore method, failure domain, upgrade strategy and decommission path. Confirm operational capability matches proposed complexity; otherwise simplify or resource the operations plan.

- [ ] SLOs, SLIs, RTO/RPO and degraded behavior are measurable.
- [ ] Retries, timeouts, queues and load shedding cannot amplify overload unchecked.
- [ ] Common-cause failure, failover capacity, repair and restore headroom are covered.
- [ ] Alerting is actionable and tied to owners/runbooks.
- [ ] Rollout, migration, rollback and incident review processes are explicit.
- [ ] Backups are restorable, isolated, monitored and validated at realistic scale.
- [ ] Operational ownership and complexity are appropriate to the team.
