---
name: transactions-consensus-consistency
description: Analyze transaction boundaries, isolation anomalies, distributed coordination, consensus, clocks, and consistency guarantees. Use when correctness depends on concurrent updates, leader election, cross-service workflows, or ordering across nodes.
---

# Transactions, Consensus, and Consistency

## 1. State invariants first

Write the business invariant mathematically or as executable assertions. Identify the transaction's read/write set, scope, concurrent actors, retry behavior and external side effects. Separate local atomicity from distributed coordination. Select guarantees by the invariant, not by terminology in a product brochure.

## 2. Isolation and anomalies

- Read committed prevents some dirty reads but may allow non-repeatable reads and other anomalies depending on engine.
- Snapshot isolation/MVCC gives a transaction a consistent snapshot but can permit write skew when concurrent transactions update disjoint rows after reading a shared invariant.
- Lost update occurs when concurrent read-modify-write operations overwrite one another without detection/serialization.
- Serializable execution is equivalent to some serial order. Implementations include locking approaches (e.g., two-phase locking) and optimistic conflict detection (e.g., serializable snapshot techniques); each has different blocking, abort and predicate-tracking behavior.

Do not infer exact semantics from an isolation-level label: consult the database's official documentation and test the anomaly relevant to the invariant. Mitigations include unique/check constraints, explicit locking, compare-and-swap/version checks, serializable transactions, or redesigning ownership.

## 3. Local versus distributed transactions

Use a database transaction when required writes share a transactional boundary. For a workflow across services, prefer explicit state machine/saga where each step is idempotent, progress is durable and compensation is a business action, not magical rollback. Use an outbox/inbox pattern to atomically persist local state and intent to publish; consumers deduplicate by stable message identity.

Two-phase commit coordinates prepare and commit across participants but introduces blocking/coordinator and availability concerns. Use only where participant support, failure recovery and operational ownership are explicit. A timeout does not prove a transaction aborted; resolve in-doubt outcomes safely.

## 4. Ordering, consistency and consensus

Linearizability orders operations as if atomic at a point between invocation and response; it is stronger and can increase coordination/latency. Serializability concerns equivalence to a serial transaction order, not real-time ordering. Causal consistency preserves cause-before-effect without requiring one global order. Total-order broadcast provides a common delivery order under its model; know the relationship between ordering and consensus protocols.

Consensus protocols (e.g., Raft/Paxos families) rely on terms/epochs, quorum intersection, durable protocol state and carefully handled membership changes. Explain leader election, log replication, commit rule, fencing, snapshot/compaction and reconfiguration for the actual implementation. Do not state that a quorum works through arbitrary partitions; availability depends on reachable quorum and protocol assumptions.

CAP is about trade-offs during network partition for operations requiring atomic consistency versus availability; it is not a permanent binary label for an entire database. Define the actual operation and failure condition.

## 5. Clocks and timestamps

Wall clocks can jump or skew; monotonic clocks measure elapsed time locally but are not comparable globally. Timestamps alone do not establish causality. Lamport clocks provide an ordering consistent with causality but not a complete causal relation; version vectors can expose concurrent histories at metadata cost. Last-write-wins may discard valid concurrent updates and depends on timestamp policy. Use logical versions/causal metadata or domain-specific merge where data loss is unacceptable. TrueTime-like bounded uncertainty requires the specific system's documented assumptions.

## 6. Decision rules

- IF an invariant is local to one database, THEN enforce it in the narrowest transaction/constraint boundary.
- IF concurrent operations can violate a cross-row rule, THEN demonstrate the anomaly and use serializable/locking/constraint/ownership strategy that closes it.
- IF external side effects follow a commit, THEN use an outbox or durable workflow; make handlers idempotent.
- IF multi-region writes are required, THEN define conflict semantics before selecting multi-leader or leaderless topology.
- IF strict real-time order is essential, THEN budget coordination and test partition behavior; otherwise choose a weaker explicit guarantee.

## 7. Verification checklist

- [ ] Invariants and transaction boundaries are explicit.
- [ ] Relevant anomalies are tested with concurrent schedules.
- [ ] Product-specific isolation semantics are verified from official documentation.
- [ ] Retries cannot duplicate non-idempotent effects.
- [ ] In-doubt commit, coordinator loss and timeout outcomes have recovery paths.
- [ ] Consensus claims include quorum, epoch, persistence and reconfiguration assumptions.
- [ ] Clock-derived decisions account for skew, jumps and concurrent updates.
- [ ] User-visible staleness, conflict or reduced availability is documented.
