---
name: data-encoding-evolution
description: Design durable schemas and wire formats, or evolve APIs, events, and stored data without unsafe producer-consumer incompatibility. Use for REST/RPC contracts, message brokers, schema registries, serialization, and rolling upgrades.
---

# Data Encoding and Evolution

## 1. Contract first

Separate in-memory objects, persisted representation and wire encoding. Identify every producer, consumer, historical record, replay path, cache and external client. Define ownership, field meaning, units, nullability, defaults, enum evolution, unknown-field behavior, ordering and compatibility window.

## 2. Encoding choices

- JSON: readable and broadly interoperable; account for size, parsing cost, number precision and ambiguous optional/null semantics.
- XML: useful where ecosystem contracts require it; account for verbosity and parser security.
- Binary schema formats (e.g., Protocol Buffers, Avro, Thrift): can improve compactness and typed contracts, but require disciplined field identity, schema distribution and cross-language compatibility.
- Never reuse a field identifier with a new meaning. Preserve deleted identifiers where the format requires reservation.
- For timestamps, define timezone and precision; for money, use integer minor units or a decimal representation with explicit currency/scale. Define integer bounds and string normalization.

Do not assume an encoding guarantees schema compatibility: rules differ by format and runtime. Verify official specifications and generated code behavior.

## 3. Compatibility rules

Backward compatible: a new reader can interpret old data/messages. Forward compatible: an old reader can safely tolerate data/messages produced by a newer writer. Full compatibility requires both directions over the chosen version window. Compatibility is about actual reader/writer pairs, not merely schema syntax.

| Change | Typical risk | Safer method |
|---|---|---|
| Add optional field | Old reader may reject unknown fields | Confirm unknown-field behavior; provide safe default |
| Make optional field required | Historical rows/messages lack value | Backfill and staged enforcement |
| Rename field | Breaks name-based serializers/clients | Add new field, dual-read/write, deprecate old |
| Change type/units/meaning | Silent corruption or overflow | Introduce a new versioned field and conversion |
| Remove enum value | Old consumers may still emit/use it | Deploy tolerant readers before retiring producers |
| Change event semantics | Replay changes business meaning | Version event type and preserve historical semantics |

For every change test old-writer/new-reader and new-writer/old-reader combinations, plus replay of representative historical payloads.

## 4. Safe rollout protocol

1. Inventory consumers and establish supported version overlap.
2. Deploy readers that tolerate both old and new representations.
3. Deploy writers that emit the new representation, optionally dual-write temporarily.
4. Backfill stored records with resumable, idempotent jobs; measure lag and errors.
5. Verify counts, checksums/business invariants and consumer behavior.
6. Stop old writes only after all relevant producers are migrated.
7. Remove compatibility code only after retention, replay and rollback windows expire.

Do not dual-write unrelated stores without reconciliation; partial success creates divergence. Use an outbox or durable change capture where atomic publication with a database transaction is needed.

## 5. API and event contracts

Define request/response schemas, status/error types, pagination consistency, idempotency, authentication, authorization, deadlines and retry semantics. For events, include stable event identity, event type/schema version, aggregate/entity identifier, occurrence time (and document its clock semantics), tenant/context needed for consumption, and correlation/causation identifiers where useful. Keep event meaning immutable; represent corrections as new facts rather than rewriting history without explicit policy.

## 6. Security and operations

Limit payload size and nesting; validate before allocation or expensive parsing. Reject malformed encodings safely. Avoid deserialization mechanisms that instantiate arbitrary classes. Protect sensitive fields in logs and dead-letter queues. Define schema registry availability/caching behavior, compatibility policy, retention and disaster recovery.

## 7. Review checklist

- [ ] All producers, consumers, old data, replays and external clients are inventoried.
- [ ] Field identity, defaults, nullability, precision and semantic units are explicit.
- [ ] Compatibility is tested across actual version combinations and language runtimes.
- [ ] Rollout and backfill are resumable, observable and reversible within a stated window.
- [ ] Event history semantics and duplicate handling are defined.
- [ ] Payload limits, validation, sensitive-data handling and dead-letter access are covered.
