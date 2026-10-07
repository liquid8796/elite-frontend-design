# Adaptive Capability Routing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make execution mode adaptive to task complexity, design certainty, and rendered QA instead of relying on model self-assessment.

**Architecture:** Keep routing inside the existing root skill and `design-intelligence` module. Add deterministic selection/downgrade rules and reuse baseline skin packs for `LOCKED`/`GUIDED`; do not add a new module.

**Tech Stack:** Markdown skill orchestration, Python structural regression tests, existing validator/package scripts.

**Spec:** `docs/superpowers/specs/2026-10-06-adaptive-capability-routing.md`

## Global Constraints

- Default mode is `GUIDED` when evidence is inconclusive.
- Runtime metadata is optional evidence, never the sole authority.
- Never select `BESPOKE` because of model self-assertion alone.
- Rendered QA can downgrade or escalate mode.
- Preserve the existing 16-module router and 8 baseline skins.

## Review Focus

- Missing runtime metadata should still produce a deterministic mode.
- A complex brief must not automatically imply `BESPOKE`.
- Ambiguous preflight design primitives should increase scaffolding.
- Rendered drift must trigger downgrade rules.
- User-requested experimentation must not bypass accessibility/usability QA.

---

### Task 1: Adaptive routing contract

**Files:**
- Modify: `tests/test_structure.py`
- Modify: `skills/elite-frontend-design/references/modules/design-intelligence/module.md`
- Modify: `skills/elite-frontend-design/SKILL.md`

- [ ] Add a failing structural test for Adaptive Capability Routing, three execution modes, Task Complexity Score, Design Preflight, default `GUIDED`, downgrade threshold, and no self-assessment rule.
- [ ] Run the targeted test and confirm it fails because the contract is missing.
- [ ] Add the minimal routing contract to the module and root orchestration.
- [ ] Re-run the targeted test and confirm it passes.

### Task 2: Release metadata and verification

**Files:**
- Modify: `plugin.json`
- Modify: `.codex-plugin/plugin.json`
- Modify: `skills/elite-frontend-design/skill.json`
- Modify: `scripts/validate_skill.py`
- Modify: `README.md`
- Modify: `CHANGELOG.md`

- [ ] Bump synchronized versions and document the routing behavior.
- [ ] Extend validator contracts for the new adaptive-routing phrases.
- [ ] Run validator and full unit suite.
- [ ] Rebuild ZIP and verify required files/CRC.
- [ ] Commit and push `master` with `type(scope): message` if this directory is a Git repository.
