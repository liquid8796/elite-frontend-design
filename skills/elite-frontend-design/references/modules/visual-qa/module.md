---
name: visual-qa
description: Browser-based frontend design verification. Uses a claim-driven QA inventory, rendered screenshots, interaction proof, viewport-region fit checks, reference comparison, console/runtime review, and iterative refinement before frontend signoff.
---

# Visual QA

Source review cannot prove rendered correctness. A passing build cannot prove visual correctness. Use the running UI when browser/computer tooling is available.

This module is the **rendered visual specialist**. For full frontend signoff across functional journeys, accessibility, performance, regression and evidence status, use `frontend-qa` as the QA owner and this module as its visual pass.

## Browser Selection

Use the best browser/computer tool the host provides and reuse the same session across edit/reload cycles when possible.

If no browser/vision tool exists:
- perform a source-level fallback;
- inspect responsive rules and states;
- run build/tests when appropriate;
- state clearly that rendered visual verification was not performed.

Do not install a new browser/testing dependency merely for QA unless the task requires it and dependency changes are authorized.

## 1. Define the QA Inventory

Before testing a substantial change, derive the QA inventory from three sources:

1. the user's visible requirements;
2. the user-facing features/states actually implemented;
3. the claims you expect to make at handoff.

Anything important in those sets must map to at least one observable check.

For the main workflow write one sentence:

> entry route → user action/state → expected rendered result

List important controls and the state/view changes they can cause.

For each important claim/state, identify:
- the functional check;
- the visual state in which it must be inspected;
- the evidence expected.

Convert subjective requirements into observable checks. Instead of "the layout looks cleaner", use facts such as:
- the primary CTA is visible in the initial laptop viewport;
- the mobile sidebar is replaced by a menu control;
- the selected tab has the intended active treatment;
- the error message is visible below the invalid field.

For non-trivial work, add at least two relevant exploratory/off-happy-path checks when the product flow permits it: long text, empty data, validation failure, narrow intermediate width, slow/loading state, repeated interaction, or another plausible fragile case.

## 2. Visual Claim Discipline

A useful visual claim describes one visible fact.

Rules:
- one fact per claim;
- use exact visible copy when text matters;
- specify the viewport when responsive behavior matters;
- keep setup/navigation separate from the fact being judged;
- test small related batches rather than a large collection of unrelated claims.

If a state requires setup, first navigate/interact to reach it, then judge the claim from the resulting rendered evidence.

## 3. Baseline Runtime Checks

Before claiming the UI works, verify when tooling supports it:

1. **Page identity** — route/title/content correspond to the intended target.
2. **Not blank** — meaningful application content rendered.
3. **No framework error overlay** — no obvious Vite/Next/Webpack/runtime crash screen.
4. **Console health** — no relevant unexplained runtime errors/warnings.
5. **Asset health** — important images, fonts and media loaded.
6. **Screenshot evidence** — the relevant viewport/state was visually inspected.
7. **Interaction proof** — at least one primary target-flow interaction was exercised and its resulting state checked.

Reload the same target after code changes and rerun the failing check rather than switching to an easier scenario.

## 4. Viewport Matrix

For substantial work inspect at least:

| View | Suggested size | Purpose |
|---|---:|---|
| Desktop | 1440 × 1000 | overall composition |
| Laptop | 1280 × 800 | initial viewport, headline wrapping, density |
| Mobile | 390 × 844 | priority, text wrapping, controls |
| Tablet | ~768 × 1024 | add when layout structure changes here |

Use exact reference dimensions for fidelity tasks.

Test an intermediate width when breakpoints or wrapping make it a realistic failure point.

## 5. Viewport Fit Is a Separate Check

Define the intended initial view before signoff.

For a scrollable marketing/content page, the initial viewport must communicate the core experience and expose the expected starting action/context.

For a fixed-shell dashboard, editor, game or tool, required primary controls and working regions must fit the intended shell. Page scrolling is not a valid workaround for clipping an essential fixed interface.

Use screenshots as primary evidence. Numeric/document checks are supporting evidence only.

Do not rely only on document-level scroll width/height:
- an internal pane may be clipped while the document itself does not overflow;
- fixed/sticky controls can obscure content;
- hidden-overflow containers can cut off required UI.

When clipping is plausible, inspect the bounds of the required regions themselves, using DOM/layout measurements such as their bounding rectangles when the tool supports it.

## 6. First Screenshot Review

Check in this order:

1. **Silhouette** — does the composition look intentional at a glance?
2. **Hierarchy** — is the primary job/action obvious?
3. **Typography** — awkward wraps, tiny chrome text, oversized headings, poor numeric scanning?
4. **Spacing** — accidental voids, cramped groups, inconsistent rhythm?
5. **Container/grid** — misalignment, oversize panels, broken columns?
6. **Color** — contrast, accidental tint drift, too many accents?
7. **Components** — repeated card soup, inconsistent geometry, wrong control sizing?
8. **Assets/icons** — bad crop, missing asset, wrong icon metaphor/stroke/fill?
9. **Polish** — borders, focus, shadows, hover/active treatment?

Fix the largest visible problem first.

## 7. Interaction and State QA

For the primary flow, test relevant states:

- hover;
- keyboard focus;
- pressed/active;
- selected;
- disabled;
- loading;
- error/validation;
- empty;
- success/confirmation;
- modal/drawer/popover open;
- table/filter interaction;
- navigation transitions.

A beautiful default screenshot is insufficient if interaction states fail or become visually inconsistent.

## 8. Responsive QA

Look for:

- horizontal overflow;
- clipped controls or panels;
- broken sticky/fixed elements;
- overlapping text;
- excessively tall first viewport;
- unreadably small dense UI;
- tables that merely shrink instead of adopting a mobile strategy;
- navigation that wraps into unusable shapes;
- cards/panels that become absurdly tall;
- media crops that lose the subject;
- headline widows/orphans;
- controls pushed outside internal scroll panes.

Long copy, realistic data and intermediate widths are valuable stress cases.

## 9. Reference QA and Mismatch Ledger

When a reference exists, compare at the same viewport whenever practical.

Inspect:
- page silhouette;
- anchor positions;
- typography scale/wrapping;
- section boundaries;
- image frame/crop/tint;
- component geometry;
- exact background/surface relationships;
- icon style and placement;
- visible states.

Keep a short mismatch ledger for material differences:

| Mismatch | Reference evidence | Render evidence | Resolution |
|---|---|---|---|
| example | what the accepted design shows | what the browser shows | fix made or intentional deviation |

Fix in this priority:
1. geometry/composition;
2. typography/wrapping;
3. spacing;
4. imagery/assets/icons;
5. color/surfaces;
6. borders/shadows;
7. small details.

Do not claim high fidelity from DOM similarity alone. Do not call a deliberate deviation "matching"; document the reason.

## 9A. Cross-System Render Parity

A beautiful screenshot can still represent a semantically inconsistent moment.

For chaptered, cinematic or synchronized interfaces, inspect simultaneous visible channels in the same rendered state:
- primary narrative/content;
- HUD/status;
- active navigation;
- final-mode chrome;
- overlays/cues that are visible.

If the navigation/HUD says state X while the main visible content still communicates state Y, log a mismatch even when each element looks polished on its own.

When practical, capture the deciding screenshot so both conflicting channels are visible at once.

## 10. Refinement Loop

~~~text
reach target state
→ screenshot
→ judge concrete claims
→ identify largest failing mismatch
→ edit
→ reload/rerender
→ rerun the same claim/state
→ repeat
~~~

Usually 2–4 focused passes beat dozens of tiny speculative CSS edits.

If a claim fails or is inconclusive, inspect the screenshot that decided it before editing.

## 11. Cleanup and Stop Condition

Remove temporary QA screenshots, traces, scratch scripts and unused generated artifacts from the project unless the user asked to keep them. Evidence may live outside the repo when the environment supports it.

Stop when:
- required claims have observable passing evidence or a documented blocker;
- primary composition is coherent;
- required content is present;
- intended desktop/laptop/mobile views do not break;
- important states work;
- no blocking runtime issue remains;
- reference differences are minor or explicitly justified;
- another pass would mostly produce subjective micro-adjustments.

Visual QA is targeted rendered evidence; it does not replace the broader `frontend-qa` contract, full end-to-end, accessibility, performance or regression coverage when those are required.
