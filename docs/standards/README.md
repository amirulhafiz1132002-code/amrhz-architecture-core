# AMRHZ Governance Standards

**Status:** PROPOSED for owner review. A merged document is not automatically approved or technically enforced.  
**Purpose:** Establish a shared, evidence-first contract for controlled UI evolution and human–AI collaboration across AMRHZ repositories.

## Standards
- [UI Evolution Contract](UI-EVOLUTION-CONTRACT.md) — how interfaces may change while preserving intent and working behavior.
- [Dual-Layer Documentation Standard](DUAL-LAYER-DOCUMENTATION-STANDARD.md) — how human-readable explanations and AI-oriented structured data coexist.
- [Evidence and State Contract](EVIDENCE-AND-STATE-CONTRACT.md) — how project facts, verification, and state labels are grounded in evidence.
- [Governance lifecycle](../governance/lifecycle.md) — independent project and documentation state machines, approval gates, and enforcement levels.
- [RWCAI pipeline](../rwcai/pipeline.md) — engineering, independent verification, evidence handoff, and human authority.

## Machine-readable schemas
- [Project State Schema v2.0.0](../../schemas/project-state.schema.json)
- [Verification Record Schema](../../schemas/verification-record.schema.json)
- [Documentation Lifecycle Schema](../../schemas/doc-lifecycle.schema.json)
- [Human Approval Record Schema](../../schemas/approval-record.schema.json)

## Validation
Run the repository validator with jsonschema installed:
- python -m py_compile verification/validate.py
- python verification/validate.py

The [Governance validation workflow](../../.github/workflows/validate-governance.yml) runs on pull requests targeting main and pushes to main. A passing workflow does not establish branch protection, required approvals, or factual truth of evidence.

## Adoption model
1. Read the standards and inspect the target repository.
2. Add a local AI entrypoint that links to these standards and records repository-specific constraints.
3. Create state and verification records only from inspected evidence. Use UNKNOWN where evidence is absent.
4. Validate schemas and records; test automation before describing it as CI-checked.
5. Adopt changes through a reviewed pull request. Do not merge automatically.

## Authority and conflict handling
The canonical standards define shared process expectations. Each repository remains authoritative for its own implementation details, tests, and deployment evidence. A local repository may add stricter requirements, but must not silently weaken these standards. If local files conflict with actual code or observed test/deployment evidence, record the conflict and reconcile it; do not guess.

A link to a standard is not proof that a repository has adopted or enforced it. Adoption status must be tracked separately.
