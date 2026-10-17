# AMRHZ Evidence and State Contract

**Contract ID:** AMRHZ-EVIDENCE-STATE  
**Version:** 1.0.0  
**Initial status:** PROPOSED — effective only after human review and merge.

## Core rule

INTENT → ACTION → EVIDENCE → VERIFIED STATE.

A claim is not proof of itself. A successful command proves only what that command actually tested, under the recorded conditions.

## State vocabulary

- **CONCEPT** — an idea or experiment; not yet a committed plan.
- **PROPOSED** — suggested for review; not approved for implementation.
- **PLANNED** — approved or accepted for future work, but implementation has not been established.
- **DEVELOPMENT** — implementation is actively being built; completeness is not established.
- **PARTIAL** — some scoped behavior exists, with specific gaps remaining.
- **VERIFIED** — a defined claim passed a named verification method at a known source revision and scope. This label must not imply production deployment.
- **LIVE** — evidence confirms the specific feature/service is deployed and reachable in the stated environment at the observed time. A green build alone is insufficient.
- **BLOCKED** — progress or verification cannot safely continue because of a named dependency, permission, failure, or missing prerequisite.
- **UNKNOWN** — evidence is absent, inaccessible, stale, contradictory, or insufficient to assign another state.

## Evidence quality requirements

For each material claim, record:
- The exact claim and its scope.
- Evidence type and reference (test output, commit, configuration, provider/deployment record, reproducible observation, or issue).
- Repository/ref and commit SHA where applicable.
- When and how the evidence was collected.
- Result and limitations.
- Any relevant negative evidence or contradictory observations.

Never invent a URL, commit, test, timestamp, or result. If evidence cannot be retrieved, report the gap.

## State transition rules

- `PROPOSED` does not become `PLANNED` without a clear decision/approval.
- `DEVELOPMENT` or `PARTIAL` does not become `VERIFIED` without a scoped verification result.
- `VERIFIED` does not become `LIVE` without environment-specific deployment evidence.
- A prior successful result does not automatically verify a newer commit or different environment.
- Conflicting evidence requires reconciliation; do not select the more optimistic result by default.
- A status record must be scoped: a whole repository is rarely simply “verified” or “live.”

## Minimal verification record

Use [verification-record.schema.json](../../schemas/verification-record.schema.json) as the machine-readable format. A record should identify the claim, repository/ref, evidence, method, timestamp, result, and limitations.

## Human approval boundaries

Require explicit human approval before:
- A broad rewrite or out-of-scope change.
- A destructive operation or data deletion.
- Production deployment or external side effects not already authorized for the task.
- Relaxing an existing safety, security, or verification requirement.
- Promoting a disputed or unverified claim to a stronger state.

## Reporting template

- **Claim:**
- **State:**
- **Scope / revision:**
- **Evidence inspected:**
- **Verification performed:**
- **Result:**
- **Not tested / unknown:**
- **Next smallest action:**

## Enforcement boundary

These rules are a documented contract until validation, review, and repository controls are implemented and tested. Do not describe a policy as automatically enforced merely because it exists in Markdown.