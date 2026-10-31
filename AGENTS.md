# AI Working Contract — AMRHZ Architecture Core

Before changing this repository, read:
1. [Standards index](docs/standards/README.md)
2. [Governance lifecycle](docs/governance/lifecycle.md)
3. [RWCAI pipeline](docs/rwcai/pipeline.md)
4. [Documentation catalog](docs/_index.md)
5. [UI Evolution Contract](docs/standards/UI-EVOLUTION-CONTRACT.md) for UI-related work
6. [Dual-Layer Documentation Standard](docs/standards/DUAL-LAYER-DOCUMENTATION-STANDARD.md) for documentation or AI-context work
7. [Evidence and State Contract](docs/standards/EVIDENCE-AND-STATE-CONTRACT.md) for claims, status, verification, or project-state updates

## Non-negotiable operating rules
- Inspect the current repository, branch, files, tests, and relevant deployment configuration before proposing or making changes.
- Treat code, configuration, test output, and deployment evidence as evidence sources. Documentation is an interpretation of state, not proof by itself.
- Distinguish CONCEPT, PROPOSED, PLANNED, DEVELOPMENT, PARTIAL, VERIFIED, LIVE, BLOCKED, and UNKNOWN. Never promote a state without the evidence required by the Evidence and State Contract.
- Project implementation state and documentation lifecycle are independent state machines. Never conflate them.
- Make the smallest change that solves the evidenced problem. Preserve working behavior and unrelated files.
- Do not rewrite, broaden scope, merge, deploy, alter branch protection, delete data, or change unrelated repositories without explicit human approval for that action.
- State what was inspected, changed, tested, not tested, and remains unknown.
- If evidence is missing or contradictory, stop at BLOCKED or UNKNOWN and explain the gap.
- Keep human-facing documentation readable and AI-facing data structured; both must trace back to the same verified project reality.
- Do not claim a check passed unless the check actually ran and its result was observed.
- A schema-valid record is not proof that its claim is true. A text label naming an approver does not authenticate human approval.

## RWCAI role boundaries
- GPT: repository inspection, architecture proposals, scoped implementation, tests, evidence packaging, and corrections.
- Meta AI: independent review of actual artifacts, diffs, tests, assumptions, and limitations; it may disagree and report failure.
- Human owner: intent, boundaries, dispute resolution, and final approval for merge and production deployment.
- Exchange evidence through real artifacts and explicit handoffs. Do not claim direct AI-to-AI communication unless an actual integration proves it.

## Change workflow
INTENT → INSPECT → BASELINE → MINIMAL CHANGE → TEST → EVIDENCE → STATE RECONCILIATION → REPORT.

## Governance validation
Run:
- python -m pip install "jsonschema>=4.23,<5"
- python -m py_compile verification/validate.py
- python verification/validate.py

The GitHub Actions workflow runs the same validator on pull requests and pushes to main. A passing workflow is CI evidence, not proof that branch protection or required reviews are enabled.

These instructions do not override repository security requirements, applicable platform controls, or explicit human change boundaries.
