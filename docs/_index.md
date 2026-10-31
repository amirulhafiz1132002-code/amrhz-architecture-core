# Documentation Catalog

This catalog is a navigation aid, not a substitute for reading the source documents.

## Entry points
- [AI Working Contract](../AGENTS.md) — repository-specific instructions, boundaries, and validation commands.
- [Project README](../README.md) — human-facing project overview.

## Governance
- [Standards index](standards/README.md) — canonical index for governance standards.
- [Governance lifecycle](governance/lifecycle.md) — project and documentation state machines, approval, and enforcement.
- [Evidence and State Contract](standards/EVIDENCE-AND-STATE-CONTRACT.md) — evidence quality and state vocabulary.
- [Dual-Layer Documentation Standard](standards/DUAL-LAYER-DOCUMENTATION-STANDARD.md) — human and AI-oriented documentation.
- [UI Evolution Contract](standards/UI-EVOLUTION-CONTRACT.md) — preservation-first UI changes.
- [RWCAI pipeline](rwcai/pipeline.md) — role boundaries and independent verification.
- [Meta AI review checklist](rwcai/meta-review-checklist.md) — independent review protocol and required report format.
- [ASIP-13 compliance matrix](asip-13/compliance-matrix.md) — implementation status and evidence limitations.

## Machine-readable contracts
- [Project state schema](../schemas/project-state.schema.json)
- [Verification record schema](../schemas/verification-record.schema.json)
- [Documentation lifecycle schema](../schemas/doc-lifecycle.schema.json)
- [Approval record schema](../schemas/approval-record.schema.json)
- [Governance validator](../verification/validate.py)
- [CI workflow](../.github/workflows/validate-governance.yml)
