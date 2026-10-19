# Architecture Review Checklist

Use as a risk-based gate. Mark each item **Pass**, **Fail**, **Not applicable**, or **Unverified**. A missing answer is not a pass. For each failure, record owner, impact, and a verification/fix step.

## Scope and requirements
- [ ] Users, core flows, explicit exclusions, interfaces, and system boundaries are stated.
- [ ] Confirmed facts are separated from assumptions and estimates.
- [ ] Quality goals are measurable and have a measurement method.
- [ ] Tenant, geography, compliance, retention, budget, and operational constraints are considered.
- [ ] Every material requirement maps to a component, contract, or explicit out-of-scope decision.

## Workload and capacity
- [ ] Average and peak QPS are stated by operation, with units and source assumptions.
- [ ] Payload sizes, read/write ratio, concurrency, burst duration, growth, and skew are considered.
- [ ] Storage estimate includes retention, indexes, metadata, replication, backups, and growth headroom.
- [ ] Network and replication traffic are estimated in consistent byte/bit units.
- [ ] Cache memory uses realistic key cardinality/value overhead; hit ratio is not assumed without evidence.
- [ ] Bottlenecks, recovery capacity, queue drain time, and rebalancing load are considered.
- [ ] High-impact calculations were independently checked; precision matches evidence.

## Data and correctness
- [ ] Source of truth and ownership are named for each important entity.
- [ ] Queries, indexes, access patterns, consistency, ordering, and transaction boundaries are mapped.
- [ ] Invariants and concurrency anomalies that must be prevented are explicit.
- [ ] Duplicate requests, retries, ambiguous timeouts, and idempotency are handled.
- [ ] Event/API schema compatibility covers rolling versions, replay, and stored history.
- [ ] Deletion, retention, backup, restore, and derived-data propagation are specified.
- [ ] Cache invalidation, stale reads, and data rebuild/reconciliation are addressed.

## Distributed and failure behavior
- [ ] Network partition, node/process crash, slow dependencies, and partial failure are modeled.
- [ ] A timeout is not treated as proof that an operation did not happen.
- [ ] Leader failover includes fencing/epoch behavior where stale writers are possible.
- [ ] Replication guarantees cover acknowledged writes, lag, conflicts, and repair.
- [ ] Partition keys are evaluated for skew, hot keys, tenant concentration, and query fan-out.
- [ ] Backpressure, queue saturation, poison messages, retry storms, and dead-letter/replay policy are defined.
- [ ] Clocks are not used as causal proof without explicit assumptions; leases and expiration tolerate skew as required.
- [ ] Common-cause failures and regional/provider dependencies are considered.

## Security and privacy
- [ ] Assets, trust boundaries, actor types, and abuse cases are identified.
- [ ] Authentication and authorization are distinct, least privilege is applied, and service identities are scoped.
- [ ] Tenant isolation and object-level access checks are enforced on every relevant path.
- [ ] Secrets are externalized; key rotation and incident revocation are possible.
- [ ] Sensitive data is minimized, encrypted appropriately, masked in logs, and deleted according to policy.
- [ ] Public endpoints have validation, rate limits, resource bounds, and abuse protections.
- [ ] Supply-chain, dependencies, deployment permissions, and audit needs are considered.
- [ ] Residual threats and assumptions are documented rather than labeled “secure.”

## Reliability and operations
- [ ] SLIs/SLOs, latency percentiles, freshness, durability, RTO, and RPO are defined where relevant.
- [ ] Metrics, structured logs, traces, dashboards, and actionable alert owners are specified.
- [ ] Graceful degradation, load shedding, bulkheads, timeouts, retry budgets, and backoff are coherent.
- [ ] Rollout, migration, rollback, and recovery are safe under partial completion.
- [ ] Backup integrity and restore time have been tested or are explicitly unverified.
- [ ] Capacity thresholds, operational ownership, runbooks, and incident escalation are clear.
- [ ] Deployment and data migrations have a reversible or recoverable path.

## Architecture quality and evidence
- [ ] Each major choice satisfies a stated requirement and has at least one alternative considered.
- [ ] Extra services, caches, queues, regions, and shards are justified by evidence or a clear constraint.
- [ ] Current product guarantees/limits are verified against official documentation when material.
- [ ] Cost drivers and complexity introduced by the proposal are disclosed.
- [ ] Diagrams match the described contracts and flows; arrows and boundaries are unambiguous.
- [ ] Tests and checks claimed as passed were actually run; unverified claims are labeled.
- [ ] Specialist skills were loaded for high-impact data, security, reliability, and consistency decisions.
- [ ] Remaining uncertainty, risks, next steps, and review owners are stated.

## Decision gate

A design should not be called launch-ready while a critical correctness, security, recovery, or data-loss risk remains **Fail** or **Unverified**. Escalate critical items to an accountable human owner. This checklist reduces omissions; it is not a proof of safety or correctness.
