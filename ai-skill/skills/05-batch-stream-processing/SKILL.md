---
name: batch-stream-processing
description: Design batch jobs, messaging, durable logs, CDC, event-sourced flows, stream joins/windows, and fault-tolerant state. Use when data is processed asynchronously, continuously, replayed, joined, or delivered to analytical projections.
---

# Batch and Stream Processing

## 1. Workload and semantics

Specify source, volume, arrival pattern, freshness target, ordering scope, delivery semantics, replay horizon, state size, late-data policy, output sink and recovery objective. Separate processing-time from event-time. Decide whether the system needs a queue (work distribution/acknowledgment) or retained log (replayable ordered history); some platforms provide both abstractions with different guarantees.

## 2. Batch execution

Batch pipelines process bounded inputs and can retry partitions or stages. Map-style transforms are parallelizable; shuffle operations redistribute records by key and often dominate network/disk. Join plans include broadcast small-side, partitioned hash, and sort-merge; choose based on relation sizes, key distribution, memory, skew and ordering requirement. File/object-storage input needs partition sizing, schema evolution, idempotent output and atomic commit/manifest behavior. Checkpoint intermediate stages only when recomputation cost justifies it.

## 3. Messaging and logs

For each topic/queue define partition key, ordering scope, retention, replication, acknowledgment, consumer group behavior, retry, dead-letter, replay and schema policy. Ordering is usually per partition rather than global. More partitions can increase parallelism but add overhead and may change key placement. Consumer lag is a capacity signal; require sustained service rate greater than arrival rate to drain backlog.

At-least-once delivery implies duplicate handling. Exactly-once claims are scope-specific (broker transaction, state store, or end-to-end side effect). Use idempotency keys, transactional offset/state commits or inbox/outbox patterns where warranted. Do not acknowledge before durable processing unless loss is acceptable.

## 4. CDC and event sourcing

CDC captures database changes, often from a transaction log; define ordering, snapshot bootstrap, schema changes, deletes/tombstones, retention and recovery from offsets. Avoid independently writing a database and message broker without a consistency mechanism. Event sourcing stores domain events as source of truth; it requires immutable event semantics, versioned consumers, replay-safe handlers, projections, snapshot policy and privacy/deletion strategy. CDC is not automatically a domain-event stream.

## 5. Stream state and windows

Window types (tumbling, sliding, session) express different aggregation semantics. Event-time systems use watermarks/allowed lateness to balance completeness against latency. Late and out-of-order records require correction, side output or discard policy. Stateful joins need retention bounds and key cardinality estimates. Checkpoints capture operator state and source offsets consistently; restore compatibility must be tested across deployments.

## 6. Failure and sizing

Model worker crash, rebalance, poison record, hot key, source outage, sink throttling, checkpoint failure, state-store loss, duplicate/reordered event, schema mismatch and replay storm. Bound retries and use exponential backoff with jitter. Rate-limit replay and protect downstream services. Estimate backlog growth: backlog change ≈ (arrival rate − processing rate) × interval; drain time ≈ backlog / (processing rate − arrival rate) when processing exceeds arrivals. Include per-record bytes, replication and retained history in storage estimates.

## 7. Checklist

- [ ] Bounded versus unbounded data and freshness goals are explicit.
- [ ] Ordering key/scope and delivery semantics are documented.
- [ ] Duplicates, replay, poison messages and idempotency are handled.
- [ ] CDC bootstrap, offset recovery, deletes and schema evolution are covered.
- [ ] Event-time, watermark, late-data and state-retention policies are bounded.
- [ ] Checkpoint/restore and sink side effects are consistent and tested.
- [ ] Lag, skew, throughput, errors, checkpoint health and drain capacity are monitored.

## Source alignment

Aligned with DDIA Chapters 10–12 and selected product-design patterns from Alex Xu Chapters 9–15. See the concise English [chapter-to-skill crosswalk](../../references/chapter-to-skill-crosswalk.md) for the chapter mapping; this skill is original engineering guidance, not a substitute for the books.
