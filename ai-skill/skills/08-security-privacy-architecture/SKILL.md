---
name: security-privacy-architecture
description: Design or review system security, identity, access control, tenant boundaries, sensitive data, threat models, abuse controls, secrets, audit, and privacy. Use for public-facing systems, multi-tenant services, regulated or personal data, and security-sensitive architecture decisions.
---

# Security and Privacy Architecture

## 1. Threat-model before selecting controls

Identify assets, actors, entry points, trust boundaries, data flows, assumptions, and likely adversary capabilities. Model misuse and failure as well as normal usage: account takeover, privilege escalation, cross-tenant access, injection, replay, scraping, denial of service, insider misuse, leaked credentials, compromised dependency, and backup exposure. Rank risks by impact and likelihood; distinguish mitigations from residual risk.

## 2. Identity and authorization

Separate authentication (who/what is calling) from authorization (what it may do). Prefer short-lived, scoped identities and least privilege for users, services, operators, and automation. Enforce authorization at the resource/data boundary, not only at the UI or gateway. Define tenant/object ownership checks, delegation, revocation, break-glass access, audit and policy propagation. Avoid trusting client-supplied role or tenant identifiers without verification.

## 3. Data protection

Classify data by sensitivity and purpose. Collect the minimum needed; define lawful purpose, retention, deletion, residency and access. Protect transport and persistent storage with appropriate encryption and key management; separate keys from data, scope key access, and plan rotation and compromise response. Mask secrets and sensitive fields from logs, metrics, traces, test fixtures and error messages. Ensure backups, queues, analytics projections and dead-letter stores inherit the data policy.

## 4. Secure service boundaries

Validate input at the boundary, enforce size/time/complexity limits, use safe parsers and parameterized data access, and apply output encoding where relevant. Define authentication between services, service-to-service authorization, request signing or replay protection when needed, and network exposure rules. Rate-limit expensive or abuse-prone operations. Do not assume internal networks are trusted.

## 5. Operational security

Externalize secrets; do not commit credentials, include them in prompts/logs, or expose them to untrusted workers. Use managed secret stores or the environment's approved secret mechanism. Establish rotation, access audit, emergency revocation and incident response. Review dependency sources, software supply chain, CI/CD privileges, image/artifact provenance and deployment permissions. Provide safe security logging without collecting excess personal data.

## 6. Verification and decision record

For each critical threat, record asset, entry point, likelihood/impact, preventive control, detection, recovery, owner, and residual risk. Verify controls with negative tests: unauthorized tenant access, expired/revoked token, malformed/oversized payload, replay, rate exhaustion, secret scanning and log inspection. For regulated or safety-critical systems, require qualified human security/privacy review and applicable compliance expertise.

- [ ] Identity, authorization, and service trust boundaries are explicit.
- [ ] Tenant/object access is verified at the data boundary.
- [ ] Data collection, retention, deletion, backups, and derived copies are governed.
- [ ] Secrets are externalized and rotation/revocation tested.
- [ ] Abuse and resource exhaustion are bounded and observable.
- [ ] Threats, mitigations, residual risks, and human review needs are documented.
