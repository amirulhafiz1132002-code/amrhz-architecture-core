# AMRHZ UI Evolution Contract

**Contract ID:** AMRHZ-UI-EVOLUTION  
**Version:** 1.0.0  
**Initial status:** PROPOSED — effective only after human review and merge.

## Principle

> EVOLVE, DON'T REWRITE. IMPROVE, DON'T REIMAGINE. PRESERVE WHAT WORKS.

The goal is to improve an interface in response to a demonstrated need without casually discarding established structure, identity, accessibility, behavior, or user expectations.

## Required workflow

1. **Inspect the baseline.** Identify the actual entry points, components, styles, renderer, breakpoints, accessibility behavior, and relevant tests. Do not infer implementation from a screenshot alone.
2. **Describe the problem with evidence.** Record the affected viewport, route, state, interaction, screenshot, issue, or reproducible observation.
3. **Define the change boundary.** Name the files/components permitted to change, the behavior to preserve, and what is explicitly out of scope.
4. **Choose the smallest sufficient change.** Prefer a focused adjustment over a component replacement or redesign.
5. **Verify the result.** Compare baseline and result; test relevant viewports, interactions, keyboard/accessibility behavior, reduced-motion preferences, and regression paths as applicable.
6. **Report honestly.** Separate implemented, tested, untested, and unknown items. Do not call a mockup or local build a live deployment.

## Preservation requirements

Unless the human explicitly approves otherwise, preserve:
- Existing product intent, information architecture, brand identity, and content meaning.
- Working interactions, routes, state transitions, and integration contracts.
- Accessibility semantics, keyboard operation, readable contrast, and reduced-motion support.
- Unrelated files, components, styles, and projects.
- Existing responsive behavior that has not been shown to be defective.

## Prohibited without explicit approval

- Replacing or rewriting the entire UI to solve a localized issue.
- Reimagining visual identity, information architecture, or user flows outside the approved scope.
- Editing unrelated components or repositories merely because they belong to the same ecosystem.
- Removing behavior or accessibility support without a documented reason and approval.
- Claiming device-wide or production success from a single viewport, screenshot, or successful build.

## Exception: when a rewrite may be justified

A rewrite is not absolutely forbidden. It may be proposed only when evidence shows that a focused evolution cannot reasonably meet the requirement, the existing architecture is unsupported or unsafe, or the cost/risk of preserving it is materially worse. The proposal must include:
- Evidence and concrete failure mode.
- At least one smaller-change alternative and why it is insufficient.
- Affected files, components, behavior, migration plan, and risks.
- Verification plan and rollback strategy.
- Explicit human approval before implementation.

## UI task record

Before implementation, record:
- Baseline and evidence references.
- User problem and success criteria.
- In-scope and out-of-scope files/components.
- Behaviors and accessibility properties to preserve.
- Tests and target viewports.
- Rollback approach.

After implementation, record:
- Exact files changed.
- Tests actually run and their observed outcomes.
- Viewports/devices not tested.
- Regressions, unresolved questions, and current state.

## Adaptive-renderer example

If a profile SVG is hard to read on a phone, first inspect its text sizes, viewBox, layout constraints, and renderer limitations. A permitted first change may increase evidenced problem text or reduce nonessential detail. Replacing the whole design, changing unrelated colors, or claiming all devices are verified is outside scope unless explicitly approved.

## Enforcement boundary

This contract defines required process, not automatic technical enforcement. A repository is only **ENFORCED** when checks, review rules, or other controls that actually enforce the relevant rules are configured and verified. Otherwise report **DOCUMENTED** or **ADOPTED — NOT ENFORCED**.