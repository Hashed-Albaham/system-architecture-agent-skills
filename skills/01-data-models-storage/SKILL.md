---
name: data-models-storage
description: Choose and review data models, databases, indexes, and storage-engine designs for application, transactional, analytical, or search workloads. Use when schema, query patterns, write/read trade-offs, or storage behavior materially affect the system.
---

# Data Models and Storage Engines

## 1. Trigger and mandate

Activate when selecting or changing a datastore, schema, index, storage engine, or OLTP/OLAP flow. Start from required queries, invariants, data lifecycle and workload; avoid selecting a database by popularity. Consult the orchestrator for system-wide sizing and the transaction skill for isolation guarantees.

## 2. Model from access patterns

Create a query catalog: entity/key, filters, sort order, cardinality, read/write frequency, consistency, response size, pagination and latency target. Define ownership and relationships, uniqueness, nullability, referential integrity, retention, deletion and audit needs.

- Relational: use for explicit relationships, constraints, joins, multi-row transactions and evolving ad-hoc queries. Normalize canonical writes; add deliberate denormalization for measured read paths.
- Document: use when aggregates are commonly read/written together and schema variation is useful. Avoid duplicating mutable facts across documents without a consistency/update plan.
- Key-value: use when primary-key lookup is dominant and access paths are known. Secondary access must be modeled deliberately.
- Graph: use when multi-hop relationship traversals are central and path queries dominate; validate scale and traversal bounds.
- Search index: treat as derived, eventually consistent query projection, not usually the source of truth. Define reindex/rebuild behavior.
- Columnar/analytical: use for scans, aggregations and large analytical queries; do not assume it is suitable for high-volume transactional point mutations.

## 3. Storage mechanics and implications

### B-tree family

Page-oriented balanced indexes keep keys ordered and support point and range lookups with logarithmic tree depth. Updates may touch pages and generate random I/O; write-ahead logging (WAL) supports recovery. Page splits, fragmentation, cache behavior, checkpoints, vacuum/purge and index maintenance influence real performance. Use when mixed transactional workloads, range access, mature constraints and predictable indexed reads matter. Validate write amplification and page/cache pressure in the actual engine.

### LSM family

A typical log-structured design appends mutations to a WAL and in-memory sorted structure; immutable sorted files are flushed and merged in background compaction. Reads may consult memory and multiple files; indexes, block caches and Bloom filters can reduce lookup work. Compaction strategy trades write amplification, read amplification, space amplification and temporary disk needs. It is attractive for sustained write throughput and sequential ingestion, but compaction contention, tombstones, read fan-out and tail latency must be measured.

| Workload signal | Starting hypothesis | Verify |
|---|---|---|
| Sustained high writes; mostly key reads | LSM-oriented engine | Compaction debt, read amplification, tombstones, disk headroom |
| Mixed transactional updates; range scans/constraints | B-tree relational engine | WAL/checkpoint pressure, locks, index count, cache hit |
| Large scans and aggregates | Columnar analytical store | Ingest freshness, partition pruning, scan cost |
| Flexible aggregate fetched as a unit | Document model | Duplication, atomicity scope, index/selectivity |

No engine label alone determines latency or durability; configuration, hardware, workload and failure model matter.

## 4. Indexes and query costs

An index accelerates selected access paths while consuming storage and adding write/maintenance cost. For composite indexes, reason about leftmost prefixes and sort direction; keep predicates selective and inspect execution plans. Distinguish covering indexes from table lookups. For full-text search, use a dedicated inverted-index model where appropriate. Use secondary indexes only with a plan for write fan-out, consistency, hot terms and pagination. Validate with representative data distributions and query plans, not tiny fixtures alone.

## 5. OLTP, OLAP and data products

Keep transactional workloads optimized for small, selective operations; analytical workloads often prefer scans, compression and columnar layout. Separate via replicas, CDC or batch/stream pipelines where isolation is required. Specify lag, schema evolution, replay, deletion propagation and ownership. Do not treat a warehouse projection as instantly consistent.

## 6. Decision procedure

1. Enumerate invariants and query shapes.
2. Choose the simplest model satisfying constraints and transaction boundaries.
3. Add indexes from measured queries; estimate their disk/write cost.
4. Check partition locality, skew, hot keys, cardinality and operational maturity.
5. Load-test realistic skew, concurrency, data size and retention; inspect p95/p99 and resource saturation.
6. Design backup, restore, migration, reindex and deletion before production.

## 7. Failure modes and review

Test WAL recovery, disk-full behavior, replica lag, compaction backlog, index corruption/rebuild, long transactions, lock contention, hot partitions, vacuum/cleanup stalls, backup consistency and restore duration. For any change, specify dual-read/write or backfill strategy, validation, cutover and rollback.

- [ ] Each query has an access path and latency/correctness target.
- [ ] Indexes have an owner and measured justification.
- [ ] Engine-specific amplification and maintenance are understood.
- [ ] Logical versus physical storage, replicas and backup capacity are distinguished.
- [ ] Restore and migration are exercised with production-like scale.
