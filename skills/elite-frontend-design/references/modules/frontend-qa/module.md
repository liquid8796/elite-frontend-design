---
name: frontend-qa
description: Full-spectrum frontend QA orchestration for coding agents. Proves the correct target/state, builds a shared QA inventory, exercises real user journeys, delegates rendered inspection to visual-qa, checks responsive/accessibility/performance/regression risk, diagnoses failures from traces/console/network evidence, runs exploratory and flake checks, and reports verified/partial/blocked evidence before signoff.
---

# Frontend QA Director

Use this module after implementing or materially changing a frontend surface when the goal is **confidence in the user experience**, not only a pretty screenshot.

It orchestrates:
- functional browser QA;
- rendered visual QA;
- responsive/device QA;
- accessibility QA;
- temporal/input QA for motion-heavy work;
- performance smoke or budgets when relevant;
- visual regression when a baseline exists;
- flake/stability checks for changed tests;
- evidence-driven reporting and fix/re-run.

For a **visual-only audit** with no broader functional/release requirement, use `visual-qa` directly.

For a normal implementation, `frontend-qa` is the QA owner and may use the local `visual-qa` module as its rendered-evidence specialist.

The core principle:

> **No green check without evidence from the correct target, state, viewport and user journey.**

A build pass is not functional proof.
A DOM assertion is not visual proof.
A screenshot is not interaction proof.
An axe scan is not full accessibility proof.
A retry is not a flake fix.

## 1. Choose QA Depth Deliberately

Do not run a release audit for a one-line copy fix. Do not use a smoke check for a flagship interactive experience.

### QA-1 — Targeted patch

Use for:
- local visual fix;
- small control/state fix;
- low-risk copy/layout adjustment.

Minimum:
- prove target/state;
- rerun the affected journey;
- inspect the affected rendered state;
- check console/runtime health;
- inspect the relevant desktop/mobile viewport when responsive behavior could be affected.

### QA-2 — Standard feature

Default for substantial frontend implementation.

Includes:
- QA contract + inventory;
- critical functional journey;
- all changed/obvious controls;
- visual pass;
- responsive pass;
- accessibility baseline;
- realistic error/loading/empty state where relevant;
- short exploratory pass;
- regression guard for a confirmed defect.

### QA-3 — Release / flagship

Use for:
- high-visibility launches;
- complex dashboards/editors;
- payment/auth/onboarding;
- experiential/WebGL work;
- design-system changes;
- large responsive redesigns;
- pre-release review.

Adds when relevant:
- multiple roles/data states;
- browser compatibility;
- visual regression;
- performance budgets/throttling;
- deeper keyboard/accessibility pass;
- flake burn-in for new critical tests;
- trace-based failure diagnosis;
- recipient outputs such as download/print/share;
- temporal/input QA for animation-heavy surfaces;
- navigation parity and cross-channel state checks for synchronized/chaptered experiences;
- responsive accessibility snapshots when controls change presentation across breakpoints.

Escalate only for real risk.

## 2. Establish QA Context Before Testing

Inspect the repository before inventing a harness.

Record:
- framework and rendering model;
- package manager;
- existing test runner(s);
- Playwright/Cypress/Vitest Browser/Storybook or other browser harness;
- app start/test/build commands;
- CI provider and existing quality gates;
- supported browsers/devices;
- auth/storage-state/fixture strategy;
- test data and seed mechanism;
- current visual baselines;
- accessibility/performance tooling already installed;
- known target environments.

Prefer the project's existing stack.

Do not install Playwright, axe, Lighthouse, Storybook, Percy/Chromatic or another QA dependency merely because this module mentions it. Add dependencies only when the task requires them and dependency changes are authorized.

### Canonical harness rule

Use one canonical browser harness for signoff whenever possible.

A second tool can diagnose a problem, but do not create contradictory parallel truth sources.

## 3. Write the QA Contract

Before nontrivial QA, name exactly what is being verified.

Use a compact contract:

```text
Artifact/page:
Actor/job:
Environment:
Canonical URL/route:
Build/release identity if relevant:
Auth role:
Feature flags / conditional branch:
Data state:
Reference / design-system SSOT:
Viewports/devices:
Critical journey:
Changed controls/states:
Recipient outputs:
QA depth:
Allowed interactions:
Allowed target/source mutation:
Pass condition:
```

### Prove the state before judging it

Logged-out, loading, empty, seeded, populated, error, permission-denied, onboarding and feature-flagged states can look like different products.

A perfect screenshot of the wrong branch is invalid evidence.

Before filing a product defect, prove:
- final URL;
- visible page identity;
- role/session;
- expected state marker;
- relevant data;
- viewport.

When deployment freshness matters, separately prove that the browser target corresponds to the intended build/release.

If that chain cannot be proven, report the delivery claim as **partial/unprovable** rather than pretending current pixels prove deployment identity.

## 4. Build One Shared QA Inventory

Derive the inventory from three sources:

1. **user requirements**;
2. **user-visible behavior actually implemented**;
3. **claims intended at final handoff**.

Anything important in any of those sets needs evidence.

For each item capture:

| Claim/control | State/setup | Functional check | Visual check | Other gate | Evidence |
|---|---|---|---|---|---|

Also inventory:
- every meaningful visible control;
- mode switches;
- reversible toggles;
- state/view changes;
- loading/error/empty/success states;
- routes/deep links;
- responsive alternatives;
- browser outputs such as download/share/print;
- important animation/input behavior.

### Reversible-control rule

For toggles or reversible state:
- initial;
- changed;
- return to initial.

A one-way click test is incomplete when the product supports reversal.

### Exploratory cases

For nontrivial work add at least two realistic fragile cases, for example:
- long text;
- empty dataset;
- validation failure;
- repeated click;
- refresh after navigation;
- intermediate viewport;
- slow response;
- keyboard-only use;
- back/forward;
- touch instead of mouse.

## 5. Use an Evidence Ladder

Match evidence strength to the claim.

### Level A — real visible recipient surface

Examples:
- visible browser/native window;
- real print preview;
- real download result;
- file picker;
- OS/browser permission surface;
- actual device when device-specific behavior matters.

Use for claims that include browser/OS chrome or recipient output.

### Level B — same-state browser automation

Examples:
- Playwright/browser session with representative data;
- DOM geometry;
- focus state;
- route/state transition;
- responsive layout;
- screenshots from the canonical browser state.

This is the normal workhorse.

### Level C — mechanical/headless sweep

Examples:
- automated overflow scan;
- image loading check;
- screenshot candidates;
- static accessibility rule scan.

Useful supporting evidence, not a substitute for inspected pixels or a real journey.

### Level D — source/build/unit reasoning

Examples:
- source review;
- lint;
- build;
- unit tests;
- static DOM reasoning.

These support hypotheses and regression prevention; they do not prove the rendered user experience.

Never promote a weaker level into a stronger conclusion.

## 6. Keep the Browser Session Persistent

For iterative QA:

```text
launch once
→ reach canonical state
→ exercise
→ inspect
→ edit
→ reload/relaunch only as necessary
→ rerun the same state
```

Benefits:
- preserves realistic session/auth;
- shortens iteration;
- reduces accidental state drift;
- makes before/after comparison trustworthy.

Use explicit deterministic viewports for routine QA and screenshot comparison.

Use a separate native-window/real-device pass only when host DPI/window chrome/device behavior is itself part of the claim.

## 7. Baseline Runtime Health

Before deeper QA verify:

1. correct page/route/state;
2. meaningful content rendered;
3. no framework error overlay;
4. no relevant uncaught JS errors;
5. no unexplained console errors/warnings tied to the changed surface;
6. important requests are not unexpectedly failing;
7. critical fonts/images/media/assets loaded;
8. no obvious hydration/runtime mismatch;
9. primary interaction can be initiated;
10. unexpected static/metadata failures such as favicon, manifest or critical preload 404s are recorded and classified rather than silently ignored.

Do not dismiss errors merely because the visible screenshot looks good.

### Silent degradation

Some visual defects produce no explicit runtime error:
- declared font never actually loads;
- CSS selector no longer matches library markup;
- component rule loses to a reset;
- theme token exists but is never applied;
- property is valid but inert because required layout mode is absent;
- correct individual tokens still compose into a visually incoherent result.

When the UI looks wrong but normal gates are green, inspect computed/rendered reality rather than trusting source intent.

## 8. Functional Journey QA

Use **real user input** for signoff:
- mouse;
- keyboard;
- touch;
- browser navigation;
- normal form input.

Programmatic evaluation may stage or inspect state, but it does not count as user-input proof.

At minimum:
- complete one critical end-to-end flow;
- verify the **visible outcome**, not only dispatch/internal state;
- exercise every obvious changed control at least once;
- verify loading/error/recovery when the feature can fail;
- verify disabled/enabled transitions when relevant.

Useful journey patterns:

```text
entry
→ ready
→ action
→ processing
→ success/error
→ recovery
→ ready
```

and:

```text
route
→ interaction
→ URL/state change
→ refresh
→ deep-link restoration
→ back/forward
```

### Forms

Check:
- required fields;
- invalid input;
- server/business rejection;
- visible error ownership;
- recovery after correction;
- submit deduplication if double-click is plausible.

### Overlays

For modal/drawer/popover:
- open;
- visible state;
- focus;
- background interaction policy;
- keyboard close where expected;
- close;
- return focus if appropriate;
- mobile fit.

### Browser outputs

When the user-facing feature produces:
- download;
- share URL;
- clipboard output;
- print/PDF;
- popup;
- file selection;

verify the recipient output, not only the click handler.

## 8C. Route-Family Binding Integrity

For CMS, template, collection, blog, case-study, integration, product-detail, or other generated route families, verify content identity **across the family**, not only on one representative page.

Build or derive the expected route inventory from the router, sitemap, CMS, search index, or source data. For each route, record the expected content key/slug.

Then verify that these surfaces come from the same CMS record:

- canonical URL;
- document title / description;
- H1 / route identity;
- summary / deck;
- main media / logo;
- metadata;
- body copy / setup instructions;
- metrics or result claims;
- related-content links;
- primary CTA/action.

Use a **duplicate-content canary** across normalized hero/body text. Unexpected identical or near-identical content across records is a signal to inspect field bindings, fallback/default data, copied CMS entries, or hydration mismatch.

Also compare initial/server-rendered output with the hydrated browser state when the stack can render different data at those phases. A route that initially exposes the wrong default record still has SEO, accessibility, screenshot, and perceived-quality risk even if hydration later repairs it.

For manageable families, scan every public route. For very large families, programmatically check identity/binding invariants across the complete inventory and then deep-test representative records from each template/variant.

Template/demo residue such as `copy`, `copy-copy`, placeholder names, fake domains, or unfinished legal variables must be reported and quarantined rather than treated as intentional product content.

## 8A. Navigation Parity QA

When multiple navigation mechanisms reach the same semantic state, they must converge.

Examples:
- natural scroll;
- chapter rail/jump control;
- direct/deep link;
- browser back/forward restoration.

For representative states — and always the signature event/final payoff in QA-3 — verify:

~~~text
navigation action
→ settle
→ visible narrative/state
→ status/HUD
→ active navigation
→ renderer/world state
~~~

Do not accept `aria-current`, active CSS or URL change alone as proof that the user landed in the correct visible state.

## 8B. Cross-channel State QA

For synchronized experiences, inspect the simultaneous channels rather than testing each subsystem only in isolation.

A useful matrix:

| Channel | Evidence |
|---|---|
| Visible content | actual rendered chapter/state |
| HUD/status | semantic state |
| Navigation | active/current item |
| World/canvas | expected scene or renderer phase |
| Audio/cue | expected state when observable |
| Chrome | expected shown/hidden/inert state |
| URL | expected route/hash when applicable |

If any material channel describes a different moment, report a synchronization defect.

## 9. Rendered Visual QA Is a Separate Pass

Functional success does not imply visual success.

For the rendered pass, follow `visual-qa`.

Important additions for the full QA director:
- inspect the initial viewport before scrolling;
- inspect the **densest realistic state**, not only empty/default;
- inspect a meaningful post-interaction state;
- inspect an in-transition state when motion matters;
- use viewport screenshots as primary signoff evidence;
- use focused crops when reporting local defects;
- inspect every screenshot used as evidence.

A screenshot file that nobody inspected is not evidence.

### Whole composition before detail

Judge:
1. silhouette;
2. hierarchy;
3. typography/wrapping;
4. geometry/grid;
5. density/spacing;
6. color/surfaces;
7. component consistency;
8. asset/icon treatment;
9. polish.

Fix macro failures before micro polish.

## 10. Responsive and Device QA

Default substantial matrix:

| View | Suggested viewport |
|---|---:|
| Desktop | 1440 × 1000 |
| Laptop | 1280 × 800 |
| Mobile | 390 × 844 |
| Tablet | ~768 × 1024 when structure changes |

Add an intermediate width around risky breakpoint/wrapping transitions.

Check:
- horizontal overflow;
- internal-pane clipping;
- fixed/sticky collisions;
- first-viewport fit;
- keyboard/mobile navigation alternatives;
- long labels;
- touch targets;
- media crop;
- tables/dense tools;
- safe-area/orientation where relevant.

Device emulation is not a real device. Use actual-device evidence when a device-specific bug or browser behavior is material.

## 10A. Responsive Accessibility Snapshot

Responsive CSS can change accessibility semantics even when desktop semantics are correct.

At any breakpoint that materially changes control presentation, inspect the accessibility tree/semantic names again.

Especially check controls that become:
- icon-only;
- visually hidden;
- compact;
- moved into drawers;
- replaced by alternate navigation.

A visible label changed to `display: none` no longer contributes an accessible name. Do not assume desktop naming survives mobile CSS.

For icon-only or mobile controls, provide a stable semantic name through an appropriate mechanism such as:
- `aria-label`;
- `aria-labelledby`;
- a screen-reader-only label that remains in the accessibility tree.

For toggle controls, verify both:
- the accessible name/action remains meaningful;
- state such as `aria-pressed` or `aria-expanded` changes correctly.

Minimum responsive accessibility evidence for a substantial responsive control:
- desktop accessibility snapshot/name;
- mobile accessibility snapshot/name;
- focus/keyboard or touch interaction where relevant.

## 11. Temporal and Input QA

Static screenshots cannot prove timing.

For motion-heavy/experiential work, use the deeper contract in `experience-engineering`.

At minimum observe one complete temporal sequence, for example:

```text
arrival
→ hold
→ transform
→ settle
```

or:

```text
open
→ animate
→ stable
→ reverse/close
```

Check:
- intermediate states do not clip/flicker;
- content stays readable;
- fast interaction does not produce jump cuts/races;
- slow interaction does not expose broken half-states;
- animations end in the expected semantic state.

### Input grammar

If inputs have different promises, test each independently.

Example:
- scroll → narrative progress;
- pointer → world response;
- click/tap → impulse;
- keyboard → navigation;
- sound toggle → audio only.

For touch experiences verify drag does not accidentally trigger tap behavior.

## 12. Accessibility Baseline

Accessibility is part of QA, not a separate polish pass.

Use existing automated tooling such as axe when available, but do not claim full accessibility from an automated scan.

Automated scans are good at finding structural issues such as:
- missing accessible names;
- label association;
- invalid ARIA;
- many contrast violations;
- landmark/semantic problems.

Also manually verify relevant critical flows:

### Keyboard

- all interactive controls reachable;
- visible focus;
- logical focus order;
- no keyboard trap;
- modal/dialog focus behavior;
- skip/escape behavior where expected.

### Semantics

Prefer user-facing role/name locators in tests:
- role;
- accessible name;
- label.

If the UI cannot be located by an accessible role/name because the production component lacks one, prefer fixing the semantics over reaching for a brittle positional selector.

### Dynamic states

Run accessibility checks after important state changes:
- modal open;
- validation error;
- expanded menu;
- selected tab;
- loading complete;
- error result.

### Accessibility tree

For high-value widgets/dialogs, an ARIA/accessibility snapshot can verify semantic structure beyond raw DOM.

### Reduced motion

Verify the product remains understandable and usable with reduced motion.

For critical accessibility certification, manual screen-reader testing remains a separate requirement when available.

## 13. Performance QA

Do not turn every UI patch into a synthetic performance lab.

### Performance smoke

For normal substantial work check:
- no runaway request loop;
- no giant unexpected media/download;
- no obvious main-thread lock/freeze;
- no visible severe layout shift;
- interaction remains responsive;
- hidden/inactive expensive experiences pause when expected;
- production build warnings that indicate unexpectedly large chunks/assets are reviewed and recorded when they are relevant to initial-load risk.

### Performance budget

For public landing pages, flagship experiences, heavy dashboards or known performance-sensitive work, use existing project tooling to measure:
- project-defined Web Vitals targets;
- resource/bundle weight;
- slow request behavior;
- CPU-heavy interaction;
- animation/frame stability.

Use network/CPU throttling when it models a real risk.

For real-time WebGL/canvas, also verify:
- adaptive quality/fallback;
- frame pacing under lower-power conditions;
- no semantic change when rendering quality decreases.

Do not invent a hard numeric gate when the project already defines one.

## 14. Visual Regression

Visual regression answers:

> Did an unintended pixel/layout change happen?

It does **not** replace human visual review.

Use Playwright-style screenshot baselines or the project's existing visual-regression platform when:
- the surface is stable enough;
- regressions are expensive;
- design-system components require tight consistency;
- an approved baseline exists.

### Deterministic capture

Stabilize:
- viewport;
- browser/version/environment;
- fonts;
- data;
- time;
- animations;
- network-dependent content.

Mask only genuinely dynamic regions.

Do not mask the thing you are supposed to verify.

### Thresholds

Use the smallest tolerance that avoids environmental noise.

A threshold is for anti-aliasing/font noise, not a license for meaningful visual drift.

### Baseline discipline

Never update snapshots simply because a test is red.

Classify first:

```text
expected visual change?
├─ yes → inspect new render → intentionally approve/update baseline
└─ no  → investigate regression
```

If cross-platform rendering creates noise, capture baselines in the same container/OS/browser environment used in CI where practical.

Prefer component/region snapshots when they produce a clearer signal than huge full-page diffs.

## 15. Test Quality and Stability

For persistent automated tests:

### Prefer user-facing locators

Use:
- role;
- label;
- accessible name;
- stable visible text when appropriate.

Avoid:
- positional selectors;
- brittle DOM structure;
- arbitrary CSS selectors;
- test IDs when a good semantic locator exists.

### Prefer outcome assertions

Assert what the user/system receives after the action.

Do not over-assert internal implementation details.

### Use web-first assertions

Prefer auto-retrying browser assertions over:
- fixed sleeps;
- polling loops written by hand;
- `waitForTimeout`.

### Test isolation

Use:
- independent data;
- cleanup/fixtures;
- no ordering assumptions;
- controlled external dependencies.

Mock third-party/external systems when useful; do not mock your own product so heavily that the test no longer proves integration.

### Flake detection

Retries detect instability; they do not cure it.

For changed critical tests:
- run multiple times when practical;
- if a race is suspected, perform a local/nightly burn-in;
- treat any retry-needed pass as a flake signal;
- classify timing vs isolation vs environment vs infrastructure.

Do not "fix" flaky tests by blindly increasing timeouts.

### Trace on failure

When the harness supports traces, retain enough failure evidence to inspect:
- action sequence;
- DOM/accessibility snapshot;
- network;
- console;
- screenshot;
- error stack.

## 16. Trace-Driven Failure Diagnosis

When a test fails, classify before editing.

Possible root categories:
- **product defect**;
- **test defect**;
- **wrong target/state**;
- **environment/harness defect**;
- **data/fixture defect**;
- **flaky timing/isolation**;
- **browser-specific behavior**.

Use trace/network/console/DOM evidence to decide.

Do not patch symptoms by:
- adding sleeps;
- weakening assertions;
- increasing thresholds;
- masking more pixels;
- adding retries.

Confirm the root cause first.

Treat traces/HARs/screenshots as potentially sensitive artifacts because they may contain DOM text, headers, cookies, response bodies or user data. Keep them local/minimal and clean them after use unless the user asked to retain them.

## 16A. Diagnostic Clean-Context Recheck

Diagnostic instrumentation can create failures that a real user would never produce.

Examples:
- synthetic events dispatched on `window` instead of an element;
- manually toggled diagnostic classes;
- mocked globals;
- injected CSS/scripts;
- forced state that bypasses normal lifecycle.

After a diagnostic or synthetic probe:
1. reload or restore a clean canonical context;
2. repeat the affected journey with real browser input;
3. reread console/network evidence;
4. attribute only reproducible clean-context failures to the product.

A diagnostic artifact is evidence about the probe, not automatically a product defect.

## 17. Exploratory Pass

After scripted checks pass, spend a short period using the interface like a real, slightly impatient user.

Typical duration for interactive work:
- roughly 30–90 seconds.

Try:
- fast repeated interaction;
- unexpected back/forward;
- resize during use;
- wrong input then correction;
- switch modes and return;
- open/close repeatedly;
- keyboard instead of mouse;
- mobile/touch path;
- long/empty data.

If exploration discovers a new meaningful state/control/claim:
1. add it to the QA inventory;
2. verify it;
3. add a regression guard if it exposed a real defect.

### Tired-user pass

Before release, re-walk the critical path without debugger context.

Look for:
- unclear trigger ownership;
- hidden return path;
- misleading status;
- blocked recovery;
- dead affordances;
- raw machine/error language;
- avoidable manual work.

## 18. Cross-Browser and Component-State Coverage

### Browser compatibility

Use one browser for normal iteration.

Add Firefox/WebKit or another supported engine when risk justifies it:
- browser APIs;
- CSS/layout edge cases;
- media/autoplay;
- input/touch;
- fonts;
- Safari-specific behavior;
- release browser matrix.

Do not multiply browser runs for every trivial patch.

### Component-state QA

For reusable design-system components, Storybook/component-browser testing can be useful for a compact state matrix:

```text
default
hover
focus
pressed
disabled
loading
error
long text
dark theme
narrow container
```

Page-level journeys remain necessary for integration.

## 19. Optional Critical-Test Validation

For critical new automated tests, ask:

> Would this test fail if the behavior were actually broken?

When justified, validate this through an isolated mutation/sanity exercise:
- change one relevant condition/return/value;
- run only the target test;
- confirm it fails;
- revert immediately;
- rerun clean.

This is **optional**, expensive, and must never leave production code mutated.

Use it for high-value tests, not every assertion.

## 20. Fix-and-Reverify Loop

When source changes are authorized:

```text
prove target/state
→ reproduce defect
→ capture deciding evidence
→ fix root cause
→ reload/rebuild only as required
→ return to SAME target/state/viewport
→ rerun failing journey
→ rerun visual check
→ run nearby regression checks
→ add smallest durable guard
```

Do not verify the fix on an easier state than the one that failed.

Do not silently switch from production/staging evidence to localhost and call the original target fixed.

## 21. Severity and Evidence

If the project has a severity taxonomy, use it.

Otherwise:

- **Blocker** — destructive/false-success behavior or primary journey cannot complete safely;
- **Major** — core task, output, recovery, route or critical control unusable;
- **Moderate** — meaningful degradation with a safe workaround;
- **Minor** — polish issue with little task impact.

Category and severity are separate.

Categories may include:
- functional;
- visual/layout;
- responsive;
- state/recovery;
- accessibility;
- performance;
- regression;
- route;
- browser-output;
- compatibility;
- test/harness.

Every reported defect should include:
- target/state;
- viewport/browser;
- reproduction;
- user impact;
- evidence;
- proposed/root-cause direction if known.

## 22. Signoff Report

Use a concise final report:

```text
QA status: VERIFIED | PARTIAL | BLOCKED
Delivery identity: matched | mismatched | unprovable | N/A
QA depth: 1 | 2 | 3
Target:
Environment:
Role/data/state:
Viewports/browsers:
Critical journey:

Verified:
- ...

Findings:
- Severity · category · state/viewport
  reproduction:
  impact:
  evidence:

Regression checks:
- ...

Not verified:
- ...

Evidence retained:
- screenshots / traces / report locations, if any
```

### Negative confirmation

For material defect classes you explicitly checked and did not find, say so briefly.

Examples:
- no horizontal overflow in tested viewports;
- no relevant console errors during the critical flow;
- no keyboard trap in the tested dialog;
- no unexpected screenshot diff against the approved baseline.

Do not claim checks you did not run.

### Experiential parity at signoff

For chaptered/cinematic/scroll-driven QA-3 work, the signoff must state whether:
- natural scroll and intentional chapter navigation converge;
- narrative/HUD/navigation/world channels agree at representative states;
- responsive accessibility names survive breakpoint changes;
- the final payoff enters only when its visible narrative state has actually arrived.

## 23. Stop Condition

Signoff requires:
- correct target/state proved;
- required inventory items covered or explicitly excluded;
- critical journey works through real input;
- visual pass completed for relevant states/viewports;
- no blocking runtime issue;
- accessibility baseline covered at the requested depth;
- performance/regression gates covered when in scope;
- any confirmed fix reverified on the same canonical state;
- unknowns listed honestly.

A strong QA result can be **PARTIAL** when an important surface is unavailable.

That is better than a false green.

## 24. Relationship to Other Modules

Typical substantial frontend profile:

```text
elite-core / product module
+ frontend-qa
```

`frontend-qa` owns overall QA orchestration.

It uses:
- `visual-qa` for rendered visual/refinement detail;
- `experience-engineering` for temporal/input/performance-response QA on live immersive experiences;
- `scroll-world` for seam/scrub-specific QA on pre-rendered cinematic journeys;
- `reference-first` when a visual reference is the source of truth.

Do not load every specialist automatically.

Use the smallest set required by the QA inventory.
