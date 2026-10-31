# Governance and Lifecycle Model

**Status:** Proposed for owner review. This document describes the intended model; it does not itself prove enforcement.

## 1. Two independent state machines

Project implementation state and documentation lifecycle answer different questions. They MUST never be collapsed into one status.

### Project implementation state

| State | Meaning |
|---|---|
| CONCEPT | Idea or experiment; no committed plan |
| PROPOSED | Suggested for review; not approved for implementation |
| PLANNED | Accepted for future work; implementation not established |
| DEVELOPMENT | Work is actively being implemented |
| PARTIAL | Some scoped behavior exists; known gaps remain |
| VERIFIED | A specific claim passed a named test at a known revision and scope |
| LIVE | Environment-specific evidence confirms the scoped feature is deployed and reachable |
| BLOCKED | A named dependency, failure, permission, or prerequisite prevents safe progress |
| UNKNOWN | Evidence is absent, stale, inaccessible, contradictory, or insufficient |

The primary progression is CONCEPT → PROPOSED → PLANNED → DEVELOPMENT → PARTIAL/VERIFIED → LIVE. BLOCKED and UNKNOWN are exception/knowledge states, not achievement milestones. A record must state the reason and evidence for either state. Resolving an exception requires a new observed record; do not silently rewrite history.

A VERIFIED record requires a repository ref, commit SHA, non-empty evidence, and at least one test, CI, or runtime-verification item. A LIVE record additionally requires a deployment_record item. A successful build alone never establishes LIVE.

### Documentation lifecycle

| State | Meaning |
|---|---|
| DRAFT | Authored; not yet independently reviewed |
| REVIEWED | Review completed and evidence/comments recorded; not yet approved |
| APPROVED | Explicit human approval exists for this exact document revision |
| DEPRECATED | Superseded or withdrawn, with a traceable reason |

The documentation lifecycle is independent. An APPROVED document may describe an implementation still in DEVELOPMENT. A VERIFIED implementation may still have DRAFT documentation.

Permitted transitions:
- DRAFT → REVIEWED
- REVIEWED → APPROVED or DRAFT (if changes are required)
- APPROVED → DEPRECATED
- Same-state updates are allowed when evidence or metadata is refreshed without changing lifecycle state.

A changed document revision returns to DRAFT unless the review record explicitly covers the new revision. Never carry approval across a changed revision.

## 2. Approval evidence

A text field such as approved_by = AMIRUL is not proof of identity or approval. An approval record must identify:
- The actor's stable account identity (login and numeric account ID where available).
- The exact document path and revision SHA.
- The decision and timestamp.
- A traceable approval event reference.

The schema checks record structure and revision consistency. It cannot independently authenticate a GitHub event or prove that the account holder personally made the decision. Review the event through the trusted platform before treating approval as authentic.

## 3. Human approval gates

The repository owner retains final authority. Do not merge to main, deploy to production, alter branch protection, delete data, weaken security requirements, or perform unrelated external side effects without explicit approval for that action.

Implementation authorization permits work within the approved scope; it does not automatically approve merge or production deployment.

## 4. Evidence and state reconciliation

Every material claim must identify its scope, source revision, evidence, observation time, method, result, and limitations. If sources conflict or are missing, report BLOCKED or UNKNOWN. A schema-valid record is structurally valid data, not proof that its claim is true.

## 5. Enforcement levels

- DOCUMENTED: a rule exists in documentation.
- VALIDATED: machine-readable records and schemas pass the repository validator.
- CI-CHECKED: the validator ran in CI and its result is observable.
- ENFORCED: required repository controls prevent non-compliant changes, and those controls have been independently inspected and tested.

Do not claim ENFORCED from a passing workflow alone. Required branch protection/ruleset settings and review requirements must be inspected separately.
