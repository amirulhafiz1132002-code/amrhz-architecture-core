# AMRHZ Governance Standards

**Status:** PROPOSED until reviewed and merged by the repository owner.  
**Purpose:** Establish a shared, evidence-first contract for controlled UI evolution and human–AI collaboration across AMRHZ repositories.

## Standards
- [UI Evolution Contract](UI-EVOLUTION-CONTRACT.md) — how interfaces may change while preserving intent and working behavior.
- [Dual-Layer Documentation Standard](DUAL-LAYER-DOCUMENTATION-STANDARD.md) — how human-readable explanations and AI-oriented structured data coexist.
- [Evidence and State Contract](EVIDENCE-AND-STATE-CONTRACT.md) — how project facts, verification, and state labels are grounded in evidence.

## Machine-readable schemas
- [Project State Schema](../../schemas/project-state.schema.json)
- [Verification Record Schema](../../schemas/verification-record.schema.json)

## Adoption model
1. Read the standards and inspect the target repository.
2. Add a local AI entrypoint that links to these standards and records any repository-specific constraints.
3. Create local state and verification records only from inspected evidence. Use `UNKNOWN` where evidence is absent.
4. Validate documentation and schemas; test any automation before describing it as enforced.
5. Adopt changes through a reviewed pull request. Do not merge automatically.

## Authority and conflict handling
The canonical standards define shared process expectations. Each repository remains authoritative for its own implementation details, tests, and deployment evidence. A local repository may add stricter requirements, but must not silently weaken these standards. If local files conflict with actual code or observed test/deployment evidence, record the conflict and reconcile it; do not guess.

A link to a standard is not proof that a repository has adopted or enforced it. Adoption status must be tracked separately.