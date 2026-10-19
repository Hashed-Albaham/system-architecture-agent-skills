---
name: product-architecture-blueprints
description: Draft or review architectures for common web-scale product capabilities such as feeds, chat, notifications, search suggestions, media delivery, file sync, crawling, and growth planning. Use as a starting pattern that must be adapted to actual requirements and measured load.
---

# Product Architecture Blueprints

## 1. Use blueprints as hypotheses

For every blueprint, first establish functional scope, data ownership, workload, SLOs, privacy and operations using the orchestrator skill. Treat patterns below as starting points, not vendor-specific reference architectures or guarantees. Identify hot keys, fan-out, consistency, abuse and recovery before selecting components.

## 2. Reusable patterns

### Web crawler

Frontier scheduler → deduplicated URL store → politeness/domain queues → fetch workers → parser → content/index store. Enforce robots policy and per-domain rate limits, canonicalization, URL normalization, retry limits, loop prevention, content-size/time limits, malware handling and crawl budget. Partition by domain when politeness/order matters; track fetch versions and recrawl policy.

### Notifications

Transactional outbox → notification orchestrator → preference/template/policy evaluation → channel queues → provider adapters → delivery status store. Separate intent from delivery; apply retries with idempotency and per-provider limits. Handle token invalidation, quiet hours, consent, localization, bounce/feedback, priority, expiry and duplicate suppression. Delivery success means provider accepted, not necessarily user read.

### News/feed timeline

For write-heavy fanout, precompute recipient inbox entries; for read-heavy or very large audiences, compute on read; a hybrid can treat high-fanout publishers specially. Store canonical posts separately from feed projections. Address celebrity hot keys, ranking freshness, deletions, privacy changes, pagination cursors, dedupe and backfill. Measure write amplification versus read fan-out.

### Chat and presence

Persistent message store plus connection gateway, routing, delivery state and notification fallback. WebSockets provide a transport, not durable delivery semantics. Define message IDs, ordering scope (conversation), acknowledgment, offline sync, group fanout, edits/deletes, membership authorization, retention and end-to-end encryption requirements. Presence is ephemeral and approximate; do not rely on it for authorization or safety-critical state.

### Search autocomplete

Prefix index (e.g., trie/FST or search engine prefix fields) over curated/popular terms; optionally combine personalized and trending signals. Precompute top suggestions per prefix or score at query time. Bound input length and result size; handle Unicode normalization, typo tolerance, abuse, freshness, privacy, cache invalidation and hot prefixes. Track quality and latency separately.

### Video delivery

Ingest → validate/transcode into multiple renditions → package/manifest → object storage/origin → CDN → adaptive client. Model encoding as a DAG of jobs with retries and immutable output IDs. Define codec/device matrix, bitrate ladder, DRM/access policy, subtitles, thumbnail generation, upload resumability, CDN invalidation and storage lifecycle. Adaptive bitrate relies on client/network feedback; estimate egress from views × delivered bytes, not source upload size alone.

### File synchronization/storage

Metadata service tracks namespace, permissions, version and block manifest; data plane stores immutable chunks/blocks with integrity hashes. Clients use resumable uploads and version-aware sync; delta transfer can reduce network use but adds CPU and reconciliation complexity. Define conflict behavior, concurrent edits, rename/move semantics, share revocation, malware scanning, deduplication privacy, block-level encryption, deletion and cold-tier restore time.

### URL/content discovery at scale

Use bounded fetch and asynchronous processing, canonical keys, durable work queues and idempotent indexing. Partition by stable ownership key, isolate slow or abusive tenants, and use backpressure. Ensure crawl or discovery policy respects laws, terms and access controls.

## 3. Scale from small to large

Start with a modular application and a reliable primary datastore where feasible. Add cache, queue, read replicas, specialized search/analytics or partitioning only after measurements show a constraint. At each scale step state the bottleneck, evidence, expected benefit, new failure modes and rollback. Before sharding, verify query plans, connection pools, indexes, caching, batching and vertical headroom. Scale-out is not automatically cheaper or simpler.

## 4. Blueprint review checklist

- [ ] Data plane and control plane responsibilities are separated.
- [ ] Source of truth versus derived projections is clear.
- [ ] Fan-out, hot-key and tenant-skew cases are modeled.
- [ ] Durable delivery, retries, idempotency and ordering are explicit.
- [ ] Privacy, deletion, authorization and abuse prevention are included.
- [ ] Backfill/rebuild, retention and disaster recovery are planned.
- [ ] Topology and sizing are adapted to measured requirements; no scale claim is unsupported.

## Source alignment

Aligned with Alex Xu Chapters 1 and 8–15, with dataflow and derived-state context from DDIA Chapters 10–12. See the concise English [chapter-to-skill crosswalk](../../references/chapter-to-skill-crosswalk.md); this skill is original engineering guidance, not a substitute for the books.
