---
name: architecture-verification
description: Verify a system design against requirements, assumptions, calculations, contracts, failure semantics, security, operations, tests, and evidence. Use for architecture reviews, readiness assessments, design approvals, or any complete system-design deliverable.
---

# Architecture Verification

## 1. Establish traceability

Turn each requirement into a verifiable claim and link it to its owning component, contract, metric or test. Classify evidence as measured, formally specified, test result, vendor-documented, calculated estimate, assumption, or unknown. A diagram or confident narrative is not evidence by itself.

## 2. Verify calculations and semantics

Recalculate high-impact sizing using a second path or independent review. Check units, factors, retention, replication, indexes, overhead, peak/concurrency, queue drain rate, failover and restore headroom. For concurrency, state invariants and create adversarial schedules. For distributed delivery, check duplicate, reorder, timeout-after-commit, partition, failover and replay behavior. Verify actual database/broker/provider semantics in current official documentation.

## 3. Test strategy

Map risks to test types: unit/property tests for invariants and encoders; contract compatibility tests for APIs/events; integration tests for transaction and retry behavior; load/stress/soak tests for saturation and tail latency; fault injection/chaos tests for recovery; security tests for authorization boundaries and abuse; migration tests for backfill/cutover/rollback; restore drills for RTO/RPO. Define representative workload and test data distribution, including skew and hot keys.

Tests should be deterministic where possible, safe against production data, observable, and repeatable. Separate checks that were run from proposed tests. Preserve evidence: command, environment, version, result, limitations and owner where meaningful.

## 4. Release gates

Use `references/architecture-review-checklist.md`. Critical correctness, security, data-loss and recovery risks must not be marked pass without evidence. A failing or unverified critical item requires remediation, explicit risk acceptance by an accountable human, or a release hold. Do not invent approval or imply that the model has authority to accept organizational risk.

## 5. Architecture decision records

For consequential decisions record: context, requirement, options, decision, assumptions, trade-offs, failure modes, security/operational consequences, verification plan, owner and revisit trigger. Set a revisit condition such as traffic threshold, regulatory change, team capability change, SLO breach, or vendor behavior change.

## 6. Final report

State what was checked, what passed, what failed, what is unverified, and what evidence was used. List the highest-priority risks in order of impact and provide concrete next validation or remediation steps. Never state “zero errors,” “fully secure,” or “guaranteed correct”; report the scope and limits of verification.

- [ ] Requirements trace to components and evidence.
- [ ] Critical estimates and semantics were independently checked.
- [ ] Tests cover expected failures, skew, retries, security and recovery.
- [ ] Current external product guarantees are documented from authoritative sources.
- [ ] Critical unverified items are clearly escalated; risk acceptance is assigned to a human owner.
- [ ] Verification limits and next steps are explicit.
