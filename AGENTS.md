# Instructions for AI agents

When asked to design or implement a system:

1. Read `skills/00-system-architect-orchestrator/SKILL.md` first.
2. Select only the domain skills relevant to the request; read their complete `SKILL.md` files before making commitments.
3. Treat user constraints and explicit requirements as authoritative. Ask focused clarification only when a missing answer changes a major architectural decision; otherwise state assumptions and continue.
4. Do not claim that a technology guarantees a property unless its documented configuration and failure model support that claim. Verify current product-specific behavior in official documentation when implementation depends on it.
5. Keep sizing arithmetic dimensional and reproducible. Show inputs, equations, units, safety margins and sensitivity to uncertain assumptions.
6. Separate logical architecture from deployment topology. Identify data ownership, trust boundaries, secret handling, and operational responsibilities.
7. Include degraded modes, recovery, observability, migration and rollback. Avoid presenting a diagram as proof of correctness.
8. For code changes, follow the repository's existing conventions, use supported upstream dependencies, protect secrets, and run available tests.
9. Never copy large copyrighted passages or reproduce books in lieu of buying or consulting authorized editions. Summarize general concepts in original wording and cite sources when relevant.
10. End with unresolved assumptions, key trade-offs, verification steps and the next smallest useful implementation step.
