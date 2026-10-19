# Chapter-to-Skill Crosswalk

> These are transformative, high-level study notes: they are meant to change how you approach architecture, not replace the books. The source PDFs are **not included in this repository**.

The map below turns each successful chapter analysis into a compact learning route through the repository's skills. Use the chapter note to orient yourself, then follow the linked skill for reusable methods, checklists, and design patterns.

## Designing Data-Intensive Applications (DDIA)

### Chapter 1 — Reliable, Scalable, and Maintainable Applications

Useful systems preserve correct behavior through expected faults, sustain acceptable performance as workload grows, and remain understandable and changeable for the people operating them. Those qualities become concrete only when workload assumptions, failure modes, performance distributions, and operational responsibilities are explicit.

**Practical takeaways**
- Define workload shape, throughput, latency percentiles, and growth assumptions before judging a design.
- Design recovery, observability, safe rollout, and rollback alongside the happy path.
- Make cross-component guarantees explicit, especially for caches and derived data.

**Matching skill:** [System Architect Orchestrator](../skills/00-system-architect-orchestrator/SKILL.md)

### Chapter 2 — Data Models and Query Languages

A data model makes some relationships and queries natural while making others expensive or awkward; relational, document, and graph approaches are tools for different access patterns rather than ideological camps. Choose the model from query shapes, relationship density, update behavior, locality, and the cost of enforcing consistency.

**Practical takeaways**
- Start with access patterns and relationship boundaries, not a SQL-versus-NoSQL preference.
- Use aggregates deliberately and account for duplication, large documents, and many-to-many updates.
- Prefer declarative queries when optimizer freedom and future physical changes matter.

**Matching skill:** [Data Models and Storage](../skills/01-data-models-storage/SKILL.md)

### Chapter 3 — Storage and Retrieval

Storage-engine structures determine the cost of writes, point lookups, range scans, and analytical scans. Log-structured and tree-based indexes serve different operational trade-offs, while columnar layouts, compression, and materialization can make scan-heavy analysis efficient at the cost of update complexity.

**Practical takeaways**
- Measure the mix of lookups, range scans, writes, and scans before selecting an engine.
- Treat each index as a workload-specific write and storage commitment.
- Separate latency-sensitive transactions from large analytical workloads when their access patterns conflict.

**Matching skill:** [Data Models and Storage](../skills/01-data-models-storage/SKILL.md)

### Chapter 4 — Encoding and Evolution

Data crosses database, service, and process boundaries in representations that must survive independently changing readers and writers. Format selection, compatibility rules, historical records, message contracts, and rolling upgrades are one architecture problem: safely evolving shared data.

**Practical takeaways**
- Define backward and forward compatibility before changing a persisted or transported schema.
- Test old-reader/new-writer and new-reader/old-writer combinations during rollout planning.
- Treat encodings and contracts as versioned interfaces, not incidental serialization details.

**Matching skill:** [Data Encoding and Evolution](../skills/02-data-encoding-evolution/SKILL.md)

### Chapter 5 — Replication

Replication improves availability, read capacity, and geographic reach, but every topology exposes choices about freshness, durability, latency, conflicts, and repair. Leader/follower, multi-leader, and leaderless designs should be selected by explicit guarantees, not by assuming that more copies automatically mean stronger correctness.

**Practical takeaways**
- Document acknowledgment, failover, freshness, and durability expectations for each replicated path.
- Define conflict resolution and repair behavior before enabling multi-leader or leaderless writes.
- Monitor lag and divergence, and test recovery rather than assuming convergence.

**Matching skill:** [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md)

### Chapter 6 — Partitioning

Partitioning distributes storage and query work, but its success depends on key distribution, hot-spot behavior, index placement, rebalancing, and routing metadata. Range, hash, compound, local-index, and global-index choices each trade locality, fan-out, write cost, and operational complexity.

**Practical takeaways**
- Select keys from measured read/write patterns and test skew, including hot keys.
- Design rebalancing for growth and node loss while the system remains usable.
- Make partition ownership authoritative and routing changes consistent; use scatter/gather knowingly.

**Matching skill:** [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md)

### Chapter 7 — Transactions

Transactions are a tool for protecting application invariants across coordinated changes, but ACID labels do not specify every concurrency guarantee. Choose transaction boundaries and isolation from the anomalies the application cannot tolerate, and make retries safe when commits or external effects are ambiguous.

**Practical takeaways**
- Name the invariant and forbidden anomaly before choosing an isolation level.
- Use multi-object transactions when related records or indexes must change together.
- Bound retries, add backoff where useful, and prevent duplicate external effects.

**Matching skill:** [Transactions, Consensus, and Consistency](../skills/04-transactions-consensus-consistency/SKILL.md)

### Chapter 8 — The Trouble with Distributed Systems

Distributed components can fail, stall, lose messages, drift in time, or continue after another node has suspected them dead; a timeout therefore represents uncertainty, not proof. Robust designs state their timing and failure model, separate safety from liveness, and use quorum agreement or fencing when one node's belief is insufficient.

**Practical takeaways**
- Specify behavior for partial failure, slow processes, retries, takeover, and duplicate work.
- Use monotonic time for durations and fencing tokens to block stale lease holders.
- Test the assumptions behind clocks, timeouts, recovery, and quorum decisions.

**Matching skills:** [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md), [Transactions, Consensus, and Consistency](../skills/04-transactions-consensus-consistency/SKILL.md), [Infrastructure Primitives](../skills/06-infrastructure-primitives/SKILL.md)

### Chapter 9 — Consistency and Consensus

Replicated systems can offer eventual, causal, or linearizable behavior, and stronger real-time ordering generally requires coordination that costs latency or availability during partitions. Consensus and atomic commit support decisions such as leader election and all-or-nothing coordination, but neither makes failures or in-doubt outcomes disappear.

**Practical takeaways**
- Derive consistency guarantees from user-visible invariants and stale-read tolerance.
- Preserve causal dependencies when effects must not appear before their causes.
- Specify failover and in-doubt behavior instead of treating a timeout as an abort.

**Matching skill:** [Transactions, Consensus, and Consistency](../skills/04-transactions-consensus-consistency/SKILL.md)

### Chapter 10 — Batch Processing

Batch systems turn bounded, usually immutable inputs into derived outputs by partitioning work, shuffling related keys, and retrying safe tasks. Join strategy and materialization boundaries should reflect data size, locality, failure recovery cost, and the need for reproducible results.

**Practical takeaways**
- Keep inputs immutable and outputs explicit so jobs can be inspected and rerun.
- Choose joins around key locality and input sizes, while budgeting for shuffle.
- Prefer deterministic, side-effect-free operations and checkpoint where recomputation is costly.

**Matching skill:** [Batch and Stream Processing](../skills/05-batch-stream-processing/SKILL.md)

### Chapter 11 — Stream Processing

Stream processing continuously derives views from unbounded event flows, using durable logs and replay to support low-latency results. Correctness hinges on event-time windows, late data, state recovery, offsets, and idempotent or coordinated external effects.

**Practical takeaways**
- Decide retention, replay, ordering, lag, and loss semantics before choosing a broker pattern.
- Define late-event and correction policies using event time where occurrence time matters.
- Make state, progress, and outputs recoverable; exactly-once effects require more than a delivery label.

**Matching skill:** [Batch and Stream Processing](../skills/05-batch-stream-processing/SKILL.md)

### Chapter 12 — The Future of Data Systems

Large applications often combine specialized stores through explicit dataflows: an authoritative record emits changes that rebuild asynchronous, replayable projections. This architecture must manage lag, ordering, idempotence, lineage, and the ethical consequences of collecting and retaining personal data.

**Practical takeaways**
- Identify the system of record, every derived dataset, and the propagation path between them.
- Make projections deterministic and replayable, with clear lag and consistency expectations.
- Minimize personal-data collection, restrict access, and define deletion and retention behavior.

**Matching skills:** [Batch and Stream Processing](../skills/05-batch-stream-processing/SKILL.md), [Data Models and Storage](../skills/01-data-models-storage/SKILL.md), [Product Architecture Blueprints](../skills/07-product-architecture-blueprints/SKILL.md)

## Alex Xu — System Design Interview / Architecture Chapters

### Chapter 1 — Scale from Zero to Millions of Users

Scaling is an incremental separation of bottlenecks: add tiers, statelessness, caches, queues, redundancy, geographic distribution, and sharding as evidence demands. Each layer improves capacity or availability while introducing new freshness, failover, synchronization, and operational responsibilities.

**Practical takeaways**
- Start simply, then scale the measured bottleneck rather than adding layers by habit.
- Keep request servers interchangeable and move session state to shared durable services.
- Plan cache invalidation, queue behavior, shard keys, observability, and automation with each scale step.

**Matching skills:** [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md), [Infrastructure Primitives](../skills/06-infrastructure-primitives/SKILL.md), [System Architect Orchestrator](../skills/00-system-architect-orchestrator/SKILL.md)

### Chapter 2 — Back-of-the-Envelope Estimation

Rough estimates turn vague scale claims into testable design constraints: convert assumptions into average and peak request rates, storage growth, latency budgets, availability targets, and approximate capacity. The method matters more than false precision—state units, round sensibly, and expose assumptions.

**Practical takeaways**
- Estimate traffic and data volume before selecting components or sizing capacity.
- Compare local, disk, and cross-region costs when evaluating latency-sensitive paths.
- Translate availability targets into an explicit downtime budget.

**Matching skills:** [System Architect Orchestrator](../skills/00-system-architect-orchestrator/SKILL.md), [Data Models and Storage](../skills/01-data-models-storage/SKILL.md), [Infrastructure Primitives](../skills/06-infrastructure-primitives/SKILL.md)

### Chapter 3 — A Framework for System Design Interviews

Good design work begins by clarifying scope, requirements, assumptions, and scale; it then moves from a component-level blueprint to focused deep dives and an operational review. The workflow treats architecture as collaborative reasoning, with time and attention spent on the risks that matter most.

**Practical takeaways**
- Write down requirements and assumptions before drawing components.
- Validate the high-level flow against use cases and capacity estimates before deep diving.
- Close with bottlenecks, failure modes, observability, rollout, and growth paths.

**Matching skill:** [System Architect Orchestrator](../skills/00-system-architect-orchestrator/SKILL.md)

### Chapter 4 — Design a Rate Limiter

Rate limiting protects capacity and controls abuse by applying a quota to a defined identity, scope, and time model. Token, leaky, fixed-window, sliding-log, and sliding-counter approaches trade burst tolerance, precision, memory, coordination, and failure behavior.

**Practical takeaways**
- Choose algorithm and parameters from quota, burst, precision, and memory requirements.
- Make concurrent counter updates safe and decide what happens when shared limiter state fails.
- Return clear client feedback such as 429 responses and retry guidance, then monitor false drops.

**Matching skill:** [Infrastructure Primitives](../skills/06-infrastructure-primitives/SKILL.md)

### Chapter 5 — Design Consistent Hashing

A ring-based hash space limits key movement when servers join or leave, making it useful for caches and partitioned data. Virtual nodes improve balance but add metadata, and monitoring is still needed because placement strategy cannot eliminate workload skew or hot keys.

**Practical takeaways**
- Use consistent hashing when membership changes should not remap the whole keyspace.
- Tune virtual-node count against balance, capacity differences, and metadata overhead.
- Redistribute only affected ranges and watch for skew after topology changes.

**Matching skill:** [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md)

### Chapter 6 — Design a Key-Value Store

A distributed key-value store combines partitioning, replication, consistency choices, failure detection, hinted handoff, anti-entropy, and a log-structured storage path. The central exercise is to make capacity, availability, repair, conflict reconciliation, and read/write latency explicit rather than hiding them behind simple `get` and `put` operations.

**Practical takeaways**
- Define quorum behavior and user-visible semantics during partitions.
- Plan replica placement across failure domains, temporary handoff, and durable repair.
- Match memory, disk, indexes, and Bloom-filter trade-offs to the workload.

**Matching skills:** [Data Models and Storage](../skills/01-data-models-storage/SKILL.md), [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md)

### Chapter 7 — Design a Unique ID Generator in Distributed Systems

Distributed identifiers must balance uniqueness, ordering, size, throughput, coordination, and availability. A Snowflake-style layout illustrates how timestamp, worker identity, and sequence fields can avoid a central allocator while making bit capacity, identity assignment, clock behavior, and epoch limits operational concerns.

**Practical takeaways**
- Turn identifier requirements into explicit bounds for rate, lifetime, workers, and ordering.
- Allocate fields deliberately and protect worker identities from accidental reuse.
- Monitor clock assumptions and plan for generator failover, epoch migration, and exhaustion.

**Matching skills:** [Infrastructure Primitives](../skills/06-infrastructure-primitives/SKILL.md), [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md)

### Chapter 8 — Design a URL Shortener

A URL shortener is a durable mapping service wrapped in a compact alias-generation path and a read-optimized redirect path. Capacity estimates, collision handling, redirect semantics, caching, abuse controls, and analytics determine whether the simple core remains reliable at scale.

**Practical takeaways**
- Persist mappings and cache read-heavy short-to-long lookups.
- Ensure aliases are globally unique before encoding and resolve collisions deliberately.
- Choose redirect behavior based on load reduction versus tracking needs, then add rate limits as abuse grows.

**Matching skills:** [Product Architecture Blueprints](../skills/07-product-architecture-blueprints/SKILL.md), [Data Models and Storage](../skills/01-data-models-storage/SKILL.md), [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md)

### Chapter 9 — Design a Web Crawler

A crawler is a resilient, modular pipeline for discovering, scheduling, fetching, validating, deduplicating, and storing web content. Its frontier must balance priority, freshness, throughput, and host politeness while workers and state survive malformed input, traps, failures, and enormous queues.

**Practical takeaways**
- Route and pace work by host, persist frontier state, and honor robots.txt.
- Separate download, parsing, filtering, deduplication, and storage so stages can evolve independently.
- Use durable checkpoints, bounded waits, and resumable workers for fault recovery.

**Matching skills:** [Batch and Stream Processing](../skills/05-batch-stream-processing/SKILL.md), [Infrastructure Primitives](../skills/06-infrastructure-primitives/SKILL.md), [Data Models and Storage](../skills/01-data-models-storage/SKILL.md)

### Chapter 10 — Design a Notification System

A notification platform separates intake, durable event records, channel queues, workers, and external providers so one provider or channel cannot block the rest. Retries improve delivery but can duplicate effects, making event IDs, preferences, rate limits, authentication, and backlog monitoring part of the product design.

**Practical takeaways**
- Persist notifications before asynchronous dispatch and use bounded, observable retries.
- Isolate channels with queues and scale workers from backlog, not just request traffic.
- Validate requests, honor opt-in settings, enforce recipient limits, and tolerate duplicates.

**Matching skills:** [Product Architecture Blueprints](../skills/07-product-architecture-blueprints/SKILL.md), [Infrastructure Primitives](../skills/06-infrastructure-primitives/SKILL.md), [Data Models and Storage](../skills/01-data-models-storage/SKILL.md)

### Chapter 11 — Design a News Feed System

A feed architecture separates publishing from retrieval and chooses where to perform fanout. Push-on-write makes reads fast but strains high-follower accounts, pull-on-read saves write work but makes reads heavier, and a workload-sensitive hybrid can combine both with queues and layered caches.

**Practical takeaways**
- Choose fanout per user or account class rather than applying one policy universally.
- Queue asynchronous distribution and cache bounded ID lists before hydrating content.
- Include privacy, mute rules, rate limits, CDN delivery, and peak-latency monitoring in the design.

**Matching skills:** [Product Architecture Blueprints](../skills/07-product-architecture-blueprints/SKILL.md), [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md), [Batch and Stream Processing](../skills/05-batch-stream-processing/SKILL.md)

### Chapter 12 — Design a Chat System

Chat combines persistent real-time connections with durable message history, offline delivery, multi-device synchronization, and presence. Separating connection services, APIs, persistence, notifications, and presence makes scaling possible, while group size determines whether per-recipient fanout or on-demand reads are practical.

**Practical takeaways**
- Use persistent connections only where real-time delivery requires them, and isolate their stateful tier.
- Design message IDs and per-device cursors around ordering, replay, and missed messages.
- Bound presence fanout and adapt strategy as groups become large.

**Matching skills:** [Product Architecture Blueprints](../skills/07-product-architecture-blueprints/SKILL.md), [Data Models and Storage](../skills/01-data-models-storage/SKILL.md), [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md)

### Chapter 13 — Design a Search Autocomplete System

Autocomplete is a low-latency prefix lookup backed by aggregated usage data, often served from an in-memory trie or snapshot with popular results precomputed per prefix. Separating event collection, aggregation, index building, and serving makes freshness, memory, rebuilds, filtering, language, and skew manageable.

**Practical takeaways**
- Set latency and freshness targets before choosing rebuild cadence.
- Keep serving simple with immutable or replaceable index snapshots and caches.
- Filter unsafe results and account for geographic, language, and popularity skew.

**Matching skills:** [Product Architecture Blueprints](../skills/07-product-architecture-blueprints/SKILL.md), [Data Models and Storage](../skills/01-data-models-storage/SKILL.md), [Batch and Stream Processing](../skills/05-batch-stream-processing/SKILL.md)

### Chapter 14 — Design YouTube

Video systems have a control path for metadata and a data path for large uploads, blob storage, transcoding, and CDN playback. Resumable uploads, parallel retryable processing, adaptive renditions, access controls, and popularity-aware delivery connect user experience to storage and egress cost.

**Practical takeaways**
- Split uploads into resumable chunks and authorize direct object-storage transfers.
- Model transcoding as durable, retryable stages with persisted intermediate state.
- Use CDN and adaptive quality for playback, then tune renditions and distribution from real demand.

**Matching skills:** [Product Architecture Blueprints](../skills/07-product-architecture-blueprints/SKILL.md), [Batch and Stream Processing](../skills/05-batch-stream-processing/SKILL.md), [Data Models and Storage](../skills/01-data-models-storage/SKILL.md), [Infrastructure Primitives](../skills/06-infrastructure-primitives/SKILL.md)

### Chapter 15 — Design Google Drive

File synchronization becomes tractable when metadata and content are separated, content is chunked, and versions, manifests, notifications, and conflict handling are explicit. The design must balance bandwidth, consistency, offline recovery, storage history, deduplication, security, and lifecycle cost.

**Practical takeaways**
- Define conflict and metadata-consistency rules before selecting sync mechanisms.
- Use chunking, resumable transfer, compression, encryption, and delta updates deliberately.
- Make offline notifications, versions, replica promotion, and reconnect behavior recoverable and testable.

**Matching skills:** [Product Architecture Blueprints](../skills/07-product-architecture-blueprints/SKILL.md), [Data Models and Storage](../skills/01-data-models-storage/SKILL.md), [Replication and Partitioning](../skills/03-replication-partitioning/SKILL.md)

### Chapter 16 — The Learning Continues

Architecture judgment grows through sustained study of real systems, technologies, and engineering practice rather than a single shortcut. Case studies and engineering publications are most valuable when they reveal the problem a technique solves and the trade-offs behind its use.

**Practical takeaways**
- Read deployed-system case studies for transferable principles, not templates to copy.
- Study each technology's motivating problem, constraints, and failure modes.
- Maintain a deliberate learning loop through technical writing and design retrospectives.

**Matching skill:** [System Architect Orchestrator](../skills/00-system-architect-orchestrator/SKILL.md)

## Coverage Notes

- **Successful chapters:** DDIA Chapters 1–12 and Alex Xu Chapters 1–16 are included above (**28 chapters total**).
- **Failed chapters:** None; no chapters were reported as uncovered.

## Synthesis

DDIA supplies the internals-first lens: data models, storage engines, encodings, replication, partitioning, transactions, consistency, batch, streams, and replay explain what a system can guarantee and what each guarantee costs. Alex Xu supplies the top-down design workflow: clarify requirements, estimate scale, decompose a product into services and data paths, choose pragmatic patterns, and revisit operations, failure, and evolution. Studied together, the books create a tighter loop: use Xu's workflow to frame the problem and expose bottlenecks, then use DDIA's mechanisms to test whether the proposed architecture is actually correct, scalable, recoverable, and evolvable.
