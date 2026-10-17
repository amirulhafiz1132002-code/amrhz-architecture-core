# AI Working Contract — AMRHZ Architecture Core

Before changing this repository, read:
1. [Standards index](docs/standards/README.md)
2. [UI Evolution Contract](docs/standards/UI-EVOLUTION-CONTRACT.md) for any UI-related work
3. [Dual-Layer Documentation Standard](docs/standards/DUAL-LAYER-DOCUMENTATION-STANDARD.md) for documentation or AI-context work
4. [Evidence and State Contract](docs/standards/EVIDENCE-AND-STATE-CONTRACT.md) for claims, status, verification, or project-state updates

## Non-negotiable operating rules
- Inspect the current repository, branch, files, tests, and relevant deployment configuration before proposing or making changes.
- Treat code, configuration, test output, and deployment evidence as evidence sources. Documentation is an interpretation of state, not proof by itself.
- Distinguish CONCEPT, PROPOSED, PLANNED, DEVELOPMENT, PARTIAL, VERIFIED, LIVE, BLOCKED, and UNKNOWN. Never promote a state without the evidence required by the Evidence and State Contract.
- Make the smallest change that solves the evidenced problem. Preserve working behavior and unrelated files.
- Do not rewrite, reimagine, broaden scope, deploy, or alter unrelated repositories without explicit human approval.
- State what was inspected, changed, tested, not tested, and remains unknown.
- If evidence is missing or contradictory, stop at BLOCKED or UNKNOWN and explain the gap.
- Keep human-facing documentation readable and AI-facing data structured; both must trace back to the same verified project reality.
- Do not claim a check passed unless the check actually ran and its result was observed.

## Change workflow
INTENT → INSPECT → BASELINE → MINIMAL CHANGE → TEST → EVIDENCE → STATE RECONCILIATION → REPORT.

These instructions do not override repository security requirements, applicable platform controls, or explicit human change boundaries.