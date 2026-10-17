# AMRHZ Dual-Layer Documentation Standard

**Contract ID:** AMRHZ-DUAL-DOCS  
**Version:** 1.0.0  
**Initial status:** PROPOSED — effective only after human review and merge.

## Objective

Every evolving project should offer two complementary documentation views:
1. **Human documentation:** readable explanations that help people understand purpose, architecture, decisions, operation, trade-offs, and limitations.
2. **AI-oriented documentation/data:** explicit entry instructions, structured state, repository maps, change boundaries, evidence references, and verification records that reduce ambiguity during AI-assisted work.

These are two views of one project reality, not competing sources of truth.

## Human layer

Use Markdown and diagrams where helpful. Explain:
- What the project is and who/what it serves.
- High-level architecture and important data flows.
- How to run, test, operate, and recover the system.
- Important design decisions and their rationale.
- Known limitations, risks, and unresolved work.
- Where implementation evidence and machine-readable records are maintained.

Possible files include `README.md`, `docs/architecture-overview.md`, `docs/operations.md`, and `docs/decisions/`.

## AI layer

Provide a clear entrypoint such as `AGENTS.md` or `ai/README.md`. It must tell an AI:
- Which documents to read first.
- Which repository branch and paths are in scope for the task.
- Which sources are authoritative for code, tests, configuration, and deployment state.
- Which actions require explicit human approval.
- How to label uncertainty and report evidence.
- How to validate and reconcile project-state data.

Where useful, keep structured files such as:
- `ai/project-state.json`
- `ai/repository-map.json`
- `ai/change-boundaries.json`
- `ai/verification-index.json`

Do not create every file by default. Add only data that has a clear owner, a defined schema, and a reliable update path.

## Shared truth and precedence

- Source code and configuration establish implementation facts; executed tests establish only the tested behavior; deployment/provider evidence establishes only the observed deployment state.
- Human documentation explains the system and decisions but cannot override contrary implementation evidence.
- AI-oriented data is a structured index of facts and evidence, not a substitute for inspecting the repository.
- If layers disagree, mark the conflict, identify the sources and timestamps/commits, and reconcile before relying on the disputed claim.
- Never fabricate test results, deployment status, component relationships, dates, or evidence references.
- Use `UNKNOWN` when the evidence is missing, inaccessible, stale, or insufficient.

## Freshness and validation

Every mutable state or verification record should include, where applicable:
- Repository and branch/ref.
- Commit SHA or other reproducible source reference.
- Evidence source or artifact.
- Timestamp in ISO 8601 UTC.
- Verification method and scope.
- Result, limitations, and responsible actor/tool.

Do not claim a record is current unless its source ref and freshness have been checked. Use schema validation for machine-readable data. A valid JSON file is not necessarily factually correct.

## Minimum review checklist

- [ ] A human can understand the purpose and main constraints.
- [ ] An AI has a deterministic entrypoint and explicit boundaries.
- [ ] Structured records follow a declared schema.
- [ ] Important state claims link to inspectable evidence.
- [ ] Unknowns and contradictions are visible.
- [ ] Documentation changes are reviewed alongside the implementation change that made them necessary.

## Enforcement boundary

The presence of documentation alone does not guarantee an AI will follow it. Adoption is **DOCUMENTED** until the entrypoint is wired into the workflow and tested. Automated validation and repository rules must be separately verified before using **ENFORCED**.