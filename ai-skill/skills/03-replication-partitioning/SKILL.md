---
name: replication-partitioning
description: Design or troubleshoot replication, sharding, partition keys, replica consistency, secondary indexes, and rebalancing. Use when scaling data across nodes, regions, or failure domains or when replica lag and skew affect correctness.
---

# Replication and Partitioning

## 1. Define the problem separately

Replication places copies of the same logical data for availability, locality or read scaling. Partitioning splits distinct subsets of data for capacity and parallelism. A system may need one, both or neither. State required write/read semantics, durability, acceptable lag, failover time, conflict policy, geography and recovery objectives.

## 2. Replication modes

- Single leader: writes route to a leader; followers replay changes. Simplifies ordering per shard; asynchronous followers can lag and lose acknowledged writes on failover depending on durability/ack policy. Prevent split brain with fencing/epochs and quorum-aware leader control.
- Multi-leader: multiple write regions improve local availability/latency but create concurrent conflict resolution and ordering complexity. Use only with explicit conflict semantics, deterministic merge or ownership partitioning.
- Leaderless/quorum: clients/nodes coordinate replicas; read/write quorum intersection can improve freshness under stated assumptions. Quorum arithmetic alone does not guarantee linearizability or resolve all concurrent writes. Define versioning, read repair, hinted handoff, anti-entropy and failure behavior.

Read-your-writes, monotonic reads, bounded staleness, causal consistency and linearizability are distinct guarantees. Choose the weakest semantics that safely meet product requirements and state the user-visible consequence of lag.

## 3. Partition key selection

A good key distributes throughput and storage while keeping common transactions/queries local. Evaluate cardinality, temporal skew, tenant skew, hot entities, range scans, growth and rebalancing. Hash partitioning spreads keys but weakens ordered locality; range partitioning supports ranges but can create hot boundaries. Composite or bucketed keys can mitigate skew at the cost of fan-out and more complex reads.

Estimate per-partition load from the skewed distribution, not only average. IF one key/tenant can exceed a node's capacity, THEN use sub-partitioning, bucketing, admission controls or dedicated placement; ELSE a straightforward key strategy may suffice.

## 4. Placement and rebalancing

Modulo hashing causes broad remapping when node count changes. Consistent hashing and virtual nodes can reduce remapping and balance placement, but do not eliminate skew or operational cost. Alternatives include fixed logical partitions assigned to nodes or range splits/merges. Select by predictable operations, locality and recovery needs.

A safe rebalance stages ownership change, copies data, catches up writes, verifies completeness, switches routing, and retires old copies after a grace period. Define throttling, dual-read behavior, idempotency and rollback. Rebalancing consumes network/disk and can destabilize production; reserve headroom and rate-limit it.

## 5. Secondary indexes

Local indexes are partition-scoped and often require scatter-gather if query key differs from partition key. Global indexes add write coordination/replication and their own partitioning. An inverted index partitions by term or document; this changes hot-term behavior and update fan-out. For each secondary access path, declare freshness, failure independence, rebuild and pagination semantics.

## 6. Failure and consistency plan

Model leader crash, stale replica promotion, network partition, delayed/reordered replication, duplicate replay, conflicting writes, clock skew in timestamp-based resolution, replica loss and correlated regional outage. Use monotonic epochs/fencing tokens to reject stale leaders where supported. Define whether acknowledged writes survive failover under the selected acknowledgment policy; never imply all replicas are synchronously durable by default.

Monitor per-replica lag, quorum availability, partition skew, hot keys, repair backlog, rebalance progress, dropped/duplicate events and data divergence. Run failover and restore exercises.

## 7. Review checklist

- [ ] Replication goal and partitioning goal are explicit and separate.
- [ ] Read/write consistency is described as observable semantics.
- [ ] Partition key analysis includes skew, hot keys and query locality.
- [ ] Failover fencing and acknowledged-write guarantees are documented.
- [ ] Conflict resolution is deterministic and auditable when multi-writer is used.
- [ ] Rebalancing is staged, throttled, monitored and reversible.
- [ ] Secondary indexes have freshness, fan-out and rebuild strategies.

## Source alignment

Aligned with DDIA Chapters 5–6 and 8–9 and Alex Xu Chapters 1, 5–6. See the concise English [chapter-to-skill crosswalk](../../references/chapter-to-skill-crosswalk.md) for the chapter mapping; this skill is original engineering guidance, not a substitute for the books.
