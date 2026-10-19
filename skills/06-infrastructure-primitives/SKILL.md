---
name: infrastructure-primitives
description: Design or select reusable system primitives such as rate limiters, unique identifiers, caches, key-value services, gossip-based membership, and URL shorteners. Use when a component's algorithmic guarantees, distribution, or overload behavior matters.
---

# Core Infrastructure Primitives

## 1. Rate limiting

Define subject (user, tenant, IP, API key), operation, quota, burst, time basis, distributed scope and behavior on limiter outage. Token bucket permits a configured burst while replenishing at a sustained rate; leaky bucket smooths output; fixed windows are simple but permit boundary bursts; sliding logs are accurate but store events; sliding counters approximate a moving window with less state. Choose based on burst and precision requirements.

Distributed enforcement can use a centralized atomic store, partitioned counters, local limits with global reconciliation, or leases. Each trades accuracy, latency and availability. Define clock assumptions, race behavior, retry-after response, fairness and fail-open/closed policy. Protect the limiter itself from hot keys and cardinality attacks.

## 2. Unique identifiers

Choose identifiers for uniqueness scope, ordering, index locality, privacy, size and generation availability. Random UUID-like identifiers reduce coordination but may be bulky or poorly localized in some indexes. Ticket servers coordinate and can bottleneck. Time/worker/sequence layouts (Snowflake-style) reduce coordination but require explicit bit allocation, worker identity uniqueness, sequence overflow and clock rollback handling. Do not expose sensitive counters or timestamps unintentionally. State whether collision probability is probabilistic or uniqueness is guaranteed by coordination.

## 3. Cache design

Identify cache key, value freshness, TTL/jitter, invalidation, eviction policy, stampede prevention, negative caching, stale-while-revalidate and source-of-truth behavior. Cache-aside is simple but has race windows; write-through/write-behind change consistency and failure semantics. Use request coalescing, jittered expiry and bounded concurrency to reduce thundering herd. Cache failure should not overload the origin; define bulkheads, load shedding and graceful degradation. Avoid caching authorization-sensitive data across principals.

## 4. Distributed key-value behavior

Specify key placement, replication, read/write path, consistency level, quorum assumptions, membership, anti-entropy, hinted handoff, repair and tombstone retention. Gossip can disseminate membership/state but convergence is not instantaneous and does not itself provide consensus. Merkle-tree comparisons can localize replica differences but require correct version/repair semantics. Sloppy quorum improves availability at the cost of temporary placement divergence. Never treat these as interchangeable with linearizable commit.

## 5. URL shortener pattern

Separate code generation, mapping storage, redirect handling, analytics and abuse controls. Random/Base62 codes require collision detection and retry; deterministic hashes require collision policy and may leak predictability. Estimate code space from alphabet size^length, while reserving blocked/expired codes. Use cache for hot mappings with invalidation/expiry rules. Prevent open redirects, malware abuse, enumeration and analytics amplification; define ownership and deletion.

## 6. Selection and tests

For each primitive document API, state, invariants, failure behavior, distribution and operational limits. Test burst boundaries, clock skew/rollback, duplicate IDs, node loss, partition, hot keys, cache outage, stale invalidation, collision and adversarial inputs. Use load tests reflecting skew and retry storms, not only uniform synthetic traffic.

- [ ] Accuracy/availability trade-off is explicit.
- [ ] State cardinality, expiration and storage bounds are estimated.
- [ ] Clock and coordination assumptions are explicit.
- [ ] Fail-open/closed, retry and overload policies are defined.
- [ ] Security and abuse controls match exposure.
