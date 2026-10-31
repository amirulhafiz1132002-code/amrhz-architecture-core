# Meta AI Independent Review — RWCAI / ASIP-13

**Target:** Pull request #2, Implement RWCAI governance lifecycle and verification  
**Repository:** amirulhafiz1132002-code/amrhz-architecture-core  
**Branch:** rwcai/asip-governance-enforcement-v1  
**Review rule:** Inspect the actual PR diff and source files at the PR head commit. Do not rely only on GPT's summary or this checklist.

## Review boundaries
- Read-only review. Do not push commits, edit files, merge, or deploy.
- Treat every statement as a claim requiring evidence.
- Report disagreement directly. A finding is not invalid merely because GPT disagrees.
- Distinguish verified, partially verified, untested, and unknown.
- Do not claim direct communication with GPT; this is an artifact-based handoff.

## Required inspection

### Phase 0 — Compatibility and baseline
- Confirm the PR base and head commits.
- Inspect all changed files and relevant pre-existing standards/schemas.
- Check whether existing records or consumers are compatible with project-state schema v2.0.0.
- Assess whether the repository inventory limitation is accurately disclosed.

### Phase 1 — Governance clarity
- Confirm project implementation state and documentation lifecycle are independent.
- Review transition tables, exception states, and human approval gates.
- Check RWCAI role separation and evidence handoff for false claims or ambiguous authority.

### Phase 2 — Structured enforcement
- Validate every JSON schema against Draft 2020-12.
- Test VERIFIED requires ref, commit SHA, and test/CI/runtime evidence.
- Test LIVE requires ref, commit SHA, and deployment evidence.
- Test APPROVED documentation requires a traceable approval record for the exact revision.
- Check schema versioning and compatibility impact.
- Challenge any implication that schema validity authenticates a human or proves evidence truth.

### Phase 3 — Automated verification
- Inspect verification/validate.py line by line.
- Check transition rules, date-time format checking, local path traversal protection, Git blob revision matching, and error handling.
- Inspect unit tests and actual GitHub Actions run logs.
- Confirm CI triggers on the intended events.
- Distinguish a passing workflow from required branch protection or merge enforcement.

### Phase 4 — Traceability
- Check documentation catalog links and compliance-matrix claims.
- Verify each listed artifact exists and links resolve.
- Check that adoption/enforcement labels match observed platform state.
- Identify missing evidence, stale claims, duplicate sources of truth, or undocumented limitations.

## Required report format

For each finding include:
- Severity: BLOCKER / HIGH / MEDIUM / LOW / INFO
- Status: PASS / FAIL / PARTIAL / NOT TESTED
- Exact file and line (or GitHub URL)
- Evidence observed
- Reproduction or validation method
- Recommended correction

End with:
1. Overall assessment: PASS / PASS WITH CONDITIONS / FAIL / BLOCKED
2. Blockers that must be fixed before owner approval
3. Tests or platform settings not independently verified
4. Whether the PR is safe to present to the human owner for final decision

Do not approve or merge the PR. The repository owner retains that decision.
