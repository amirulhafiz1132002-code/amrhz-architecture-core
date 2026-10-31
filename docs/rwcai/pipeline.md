# RWCAI Collaboration Pipeline

**Protocol context:** ASIP ♾️13  
**Status:** Proposed operating workflow for this repository; no direct AI-to-AI connection is implied.

## Purpose

The Real World Cross-AI Collaboration Pipeline (RWCAI) coordinates independent AI work through real artifacts, reproducible evidence, explicit handoffs, and human authority. It is not a simulated shared session.

## Roles

### GPT — engineering and implementation
- Inspect the repository and establish the baseline.
- Propose architecture and the smallest suitable changes.
- Implement approved-scope files and automation.
- Run available tests and record exact results, limitations, and commit references.
- Respond to independent review findings and verify corrections.

### Meta AI — independent verification
- Inspect the actual branch, diff, schemas, workflow, and test evidence independently.
- Challenge assumptions and look for omissions, regressions, security weaknesses, and false claims.
- Report PASS, FAIL, PARTIAL, or BLOCKED per finding, with file/line and reproducible evidence.
- Do not rely solely on GPT's summary; inspect the supplied artifacts and source revision.

### Human owner — final authority
- Defines intent and boundaries.
- Resolves disagreements and decides whether changes are acceptable.
- Gives explicit approval for merge and production deployment.

## Evidence handoff

The handoff consists of actual GitHub artifacts: branch name, commit SHA, pull request, changed-file list, workflow run, test output, and review findings. Any transfer to Meta AI must use the actual artifact or its exact content. Do not claim the systems communicated directly unless a real integration proves it.

## Delivery phases

### Phase 0 — Compatibility audit
Inventory repository files, current state records, documentation conventions, schemas, validation tooling, and repository controls. Record unknowns. Do not break existing records.

### Phase 1 — Governance clarity
Document the two independent state machines, transition rules, RWCAI roles, evidence handoff, and human approval gates. Keep the existing standards index canonical; do not introduce a duplicate root governance file.

### Phase 2 — Structured enforcement
Harden project-state requirements for VERIFIED and LIVE. Add a documentation-lifecycle schema and a traceable approval-record schema. Keep schema validity distinct from factual truth and authenticated approval.

### Phase 3 — Automated verification
Add a deterministic validator for schemas, records, evidence references, and lifecycle transitions. Add CI to run it on pull requests and pushes. A CI check is not equivalent to branch protection.

### Phase 4 — Traceability
Add a documentation catalog and ASIP/RWCAI compliance matrix. Link standards, schemas, validator, and evidence. Report adoption and enforcement levels accurately.

## Review gate

After implementation, provide Meta AI with the exact branch/PR and commit, all changed files, CI run URL, and known limitations. GPT must address findings and re-run checks. The owner then decides whether to approve the PR. No automatic merge or production deployment is part of this pipeline.
