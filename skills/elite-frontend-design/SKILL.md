---
name: elite-frontend-design
description: "Elite frontend design, implementation, and full-spectrum QA orchestration for landing pages, product UIs, dashboards, immersive interactive/WebGL experiences, redesigns, screenshot/image-to-code work, and release verification. Combines brief-specific art direction, practical product structure, high-ambition experience engineering, one-progress-domain synchronization, reference-first design, reference-derived design intelligence, functional browser journeys, cross-channel rendered evidence, responsive accessibility, performance/regression QA, and evidence-driven signoff while avoiding generic AI UI."
metadata:
  version: "3.27.0"
  architecture: "profile-router-plus-visual-loop"
---

# Elite Frontend Design

Build frontend work that looks intentionally designed, fits the actual product, remains usable, and survives visual inspection after it renders.

This skill is not a style preset. It is an orchestration layer over focused design capabilities. Do not load every module or apply every rule at once. Pick a small profile that fits the job, commit to a visual thesis, implement it, render it, inspect screenshots, and refine.

## Prime Directive

A strong result must satisfy all four:

1. Product fit — the interface serves the real job, audience, content, and workflow.
2. Distinctive direction — the page has a specific visual point of view rather than generic AI defaults.
3. Production discipline — semantics, responsiveness, accessibility, states, maintainability, and the existing stack remain intact.
4. Rendered proof — when browser tools are available, completion requires visual QA of the actual running UI, not confidence from source code alone.

When these conflict, use this precedence:

user/repository requirements → product usability → accessibility → accepted reference/design → visual distinctiveness → decorative ambition.

## Do Not Over-Stack Guidance

More design instructions can make a result less decisive. For a normal task, load 2–4 modules maximum unless a separate concern truly requires another one.

Start with one profile:

| Task | Load first | Usually add |
|---|---|---|
| Marketing / landing / portfolio / launch page | elite-core + frontend-design | frontend-qa; motion-direction only when motion matters |
| Dashboard / admin / operations / dense product UI | elite-core + ui-ux-pro-max | frontend-qa, ui-styling |
| Product detail / commerce / configurable product | elite-core + frontend-design | frontend-qa; ui-ux-pro-max when product UX depth is needed |
| Screenshot, mockup, reference image, existing website/video recreation | reference-first + elite-core | visual-qa; use frontend-qa when interactions/release confidence also matter |
| Inspiration URL/source distillation - learn the quality or design language without cloning | reference-first + design-intelligence | frontend-design when applying the distilled patterns; frontend-qa when implementing |
| Audited pattern lookup / compose from distilled website library | elite-core + distilled-web-toolkit | frontend-design, frontend-qa |
| Scaffolded visual system / uncertain design primitives / prior visual drift | elite-core + design-intelligence | frontend-design; Adaptive Capability Routing chooses LOCKED/GUIDED/BESPOKE, then frontend-qa |
| Existing UI redesign | elite-core + ui-ux-pro-max | frontend-design, frontend-qa |
| Cinematic / Awwwards-style experience | elite-core + frontend-design | motion-direction, frontend-qa |
| High-ambition interactive / WebGL / mouse-reactive 3D experience | elite-core + experience-engineering | frontend-qa; frontend-design only for extra art-direction ideation |
| Continuous pre-rendered scroll-scrub camera world / fly-through narrative | elite-core + scroll-world | frontend-qa; reference-first when recreating evidence |
| Design tokens / component system | design-system + ui-ux-pro-max | ui-styling, frontend-qa |
| Brand / banner / presentation asset | corresponding legacy module | only the module owning a separate concern |

Read references/index.md for exact module locations.

## Ambition Escalation Gate

Before treating a brief as an ordinary landing page, scan for explicit ambition signals such as:

- "most impressive";
- "scroll-stopping";
- "immersive";
- "interactive 3D";
- "mouse-reactive";
- "WebGL";
- "cinematic journey";
- "Awwwards-level";
- a named transformation sequence whose visuals are the main product.

When these signals are central to the brief, **do not begin with component composition**.

Load `experience-engineering` and choose the rendering architecture first.

The quality question becomes:

> What rendering/timeline/input architecture can actually deliver the promised experience at production quality?

not:

> What is the quickest frontend implementation that technically satisfies the nouns in the prompt?

For high-ambition experiential work, implementation complexity must be commensurate with visible ambition. Do not stop at a tutorial/prototype architecture if a deeper renderer, shader, timeline or multisensory system materially increases the result.

After choosing the renderer, define an **authored-world contract** before implementation:

- world mechanics / story physics for each major beat;
- temporal staging: dwell/hold → transform → settle;
- one Experience Director or equivalent shared frame-state model;
- input grammar: distinct jobs for scroll, pointer, tap/touch and sound;
- performance tiers plus runtime quality feedback when the scene is expensive;
- narrative specificity and typography roles;
- one authoritative progress domain shared or explicitly calibrated across layout, director, HUD, navigation and audio;
- spec-to-implementation traceability for material experiential promises.

If the chapters mainly differ by headline, color and one generic shape morph, the experience is still under-authored.

Use `scroll-world` instead when the defining mechanic is a **pre-rendered continuous camera film scrubbed by scroll** rather than a live interactive 3D world.

## Step 0 — Inspect Before Designing

Before inventing a stack or style:

- Inspect framework, routes, package dependencies, styling approach, design tokens, fonts, assets, existing components, lint/build/test commands, and project conventions.
- Preserve the existing framework and component system unless migration is explicitly requested.
- Look for brand truth before creating new brand truth.
- For existing UI, inspect the **actual render branch** for the target route and viewport. Responsive branches, feature flags, route variants, and conditional shells outrank what an import name suggests.
- Keep design context selective: target route, UI-touching dependencies, compact token/theme truth, and required assets. Do not flood the model with the entire repository when a smaller faithful context exists.
- For redesigns, follow **scan → diagnose → targeted fix**. Preserve useful interaction and architecture; do not rewrite from scratch merely to restyle.
- For an existing app, build the real working surface; do not wrap an unfinished product in a marketing hero.

## Step 1 — Ground the Design in the Product

Extract or infer:

- product / subject;
- target audience;
- primary user job;
- page/screen type;
- content that must be visible;
- conversion or workflow goal;
- brand constraints;
- technical constraints;
- reference material;
- accessibility and device expectations.

If the brief is incomplete but the task is still actionable, choose sensible defaults and continue. Do not block implementation on subjective questions unless the user's decision is genuinely required.

## Step 2 — Set Three Design Dials

Choose deliberately. Do not randomize.

### VARIANCE
- 0 — conservative: existing system, minimal visual change.
- 1 — refined: polished but familiar.
- 2 — expressive: one memorable composition or signature visual move.
- 3 — experimental: unconventional layout/art direction justified by the brief.

### MOTION
- 0 — no decorative motion.
- 1 — interaction feedback and small transitions.
- 2 — one orchestrated reveal/scroll moment plus interaction motion.
- 3 — cinematic choreography, only when the product and performance budget justify it.

### DENSITY
- 0 — sparse/editorial.
- 1 — balanced.
- 2 — information-rich.
- 3 — operational: dense, scannable, tool-like.

Typical defaults:
- landing page: VARIANCE 2 / MOTION 1–2 / DENSITY 0–1;
- product page: 2 / 1 / 1;
- dashboard: 1 / 0–1 / 2–3;
- settings/admin: 0–1 / 0–1 / 2;
- cinematic campaign: 3 / 2–3 / 0–1;
- live experiential 3D/WebGL: 3 / 3 / 0–1.

## Step 3 — Write a Compact Design Contract

Before substantial implementation, establish:

- Visual thesis: one sentence describing the page's character and why it fits the subject.
- Signature: the one memorable element or interaction. Spend boldness here.
- Palette: base, surface, text, muted, border, accent, semantic state colors.
- Typography: family roles, weight/width character, scale, line length.
- Layout: container logic, grid, alignment, section rhythm, density.
- Component language: radius/border/shadow/icon/media treatment.
- Motion language: what moves, why, and what remains still.
- Anti-goals: 3–6 defaults this design must avoid.
- Responsive contract: what compresses, stacks, scrolls, hides, or changes priority on smaller screens.

For a new visual direction, query the bundled UI/UX database when it can improve decisions:

~~~bash
python "<skill-root>/scripts/ui_ux_search.py" "<product industry style keywords>" --design-system -p "Project Name"
~~~

Treat search output as input, not authority. The final direction must still fit the brief.

### Adaptive Capability Routing ? LOCKED / GUIDED / BESPOKE

Do not ask whether the model is "strong" or "weak" and do not trust model self-assessment. Choose an execution mode from evidence. **GUIDED is the default** when the evidence is inconclusive.

Before implementation:

1. honor explicit user intent about conservative/guided/experimental execution;
2. use host/runtime metadata only when explicitly available, never as the sole authority;
3. compute a **Task Complexity Score** using real risk signals such as complex responsive transformation, information architecture, bespoke identity, multiple references, advanced motion, accessibility/input complexity, existing-code constraints, and +2 for live WebGL/3D or continuous camera worlds;
4. run a **Design Preflight** over typography roles, spacing rhythm, surface hierarchy, composition grammar, responsive transformation, signature mechanism, motion ownership, and proof/content strategy;
5. route unresolved primitives: 3+ -> LOCKED, 1?2 -> GUIDED, 0 -> stay GUIDED by default, with BESPOKE merely eligible when product/user intent justifies it.

Mode meaning:

- **LOCKED** ? one baseline skin, explicit token ranges, Skin Lock, fixed composition grammar, narrow Controlled Mutation;
- **GUIDED** ? one coherent skin/pattern baseline, bounded token/composition mutation, one bespoke signature;
- **BESPOKE** ? custom art direction/system/composition/interaction, only after a fully resolved preflight and with strong rendered QA.

A high Task Complexity Score raises the evidence required for freedom; it does not automatically choose BESPOKE.

After the first representative render, inspect coherence. If there are **two or more material coherence failures**, downgrade one step (`BESPOKE -> GUIDED`, `GUIDED -> LOCKED`) and repair the inconsistent layers. Escalate only when the current mode is coherent on representative desktop/mobile, the contract is fully resolved, and additional freedom materially benefits the product.

When LOCKED or GUIDED uses a skin, choose exactly one from `references/design-intelligence/skins/index.md`; do not average several skins to look "more premium."

### Audited Website Pattern Toolkit

When the task benefits from patterns already distilled from the audited reference library, load `distilled-web-toolkit` and query it instead of loading all site profiles:

```bash
python "<skill-root>/scripts/distilled_toolkit_search.py" "<dominant intent>" [--domain <domain>] [--site <site-id>] [--archetype <archetype>]
```

Use the returned provenance to read only the relevant standardized site spec. Compose with **1 archetype + 1 primary composition grammar + up to 3 supporting patterns + 1 responsive strategy + 1 proof strategy**. Do not average unrelated references.

## Step 4 — Reference-First When Evidence Exists

If the user supplies screenshots, images, a live reference, or video, load reference-first.

Choose the reference branch deliberately:

- **faithful recreation** - the reference is the target; use accepted-reference lock and preserve visible evidence unless a concrete constraint requires deviation;
- **inspiration distillation** - the reference is a teacher, not the target; load `design-intelligence`, inspect rendered/runtime/source evidence, extract transferable Design DNA, and ensure the new result belongs to the new product rather than resembling the source.

For inspiration distillation from a live site, prefer the smallest relevant site profile under `references/design-intelligence/sites/` after the general module. Do not load every inspiration profile or average unrelated visual languages together.

Extract design evidence before coding:

- viewport and page regions;
- grid/container geometry;
- typography hierarchy;
- colors and surfaces;
- component families;
- asset framing/crop;
- section rhythm;
- states and interactions;
- motion timing/spatial behavior;
- responsive behavior that is visible or can be reasonably inferred.

Never use a screenshot as the production page/background to fake fidelity.

If an image-generation tool is available and the task benefits from concepting, a visual concept may be generated before implementation. User approval is mandatory only when the user asks for an approval gate or when the workflow explicitly requires one; otherwise continue with the strongest usable concept and state any meaningful assumption.

## Step 5 — Implement Through a Small System

- Prefer a small set of reusable primitives and explicit variants over one-off styling.
- Reuse repository components when they fit; do not replace good infrastructure for aesthetic novelty.
- Keep app shells, data display, forms, tables, navigation, and feature modules structurally clear.
- Use semantic HTML and accessible primitives.
- Preserve loading, empty, error, success, focus, hover, active, disabled, selected, and validation states where relevant.
- Do not introduce a dependency only to create a minor visual effect.
- For animation, prefer transform/opacity and existing libraries. Load motion-direction for advanced DOM/GSAP choreography. Load experience-engineering when the brief depends on live WebGL/3D/pointer-reactive rendering. Load scroll-world instead when the defining experience is a continuous pre-rendered camera journey whose media time is driven by scroll.
- Make typography and spacing fluid enough that the page survives laptop and mobile widths without emergency patches.

## Step 6 — Anti-Slop Pass

Before rendering, remove unjustified defaults:

- generic purple/blue gradient SaaS treatment;
- repeated identical rounded cards;
- cards nested inside cards inside cards;
- decorative pills, badges, fake status chips, fake metrics, or fake testimonials;
- eyebrow labels above every heading;
- repeated left-copy/right-card section formulas;
- generic icon grids used as filler;
- a huge headline that becomes 5–7 lines on a laptop;
- the same radius, shadow, border, and spacing on every hierarchy level;
- animation on every section/card;
- dashboard content framed as a marketing landing page;
- stock copy that could be pasted into any competitor;
- default typefaces chosen only because they are familiar.

These patterns are not forbidden. Use them when the content or established design system genuinely calls for them.

## Step 7 — Full Frontend QA + Rendered Visual QA Is the Default Finish

For a substantial implementation, load `frontend-qa` and verify the running product through the correct target/state. `frontend-qa` owns functional, visual, responsive, accessibility, performance/regression risk and evidence reporting.

Use `visual-qa` directly when the task is specifically a rendered visual/reference audit without the broader QA surface.

Choose QA depth deliberately:
- **QA-1** targeted patch;
- **QA-2** standard feature — default for substantial work;
- **QA-3** release/flagship — complex or high-risk work.

When a browser or computer-use tool is available, inspect the real rendered interface rather than relying only on source/tests.

Minimum useful viewport set for substantial work:

- desktop: around 1440 × 1000;
- small laptop: around 1280 × 800;
- mobile: around 390 × 844;
- add tablet when layout structure changes materially around that width.

Before testing a substantial surface, define a small **QA inventory** from the user's requirements, the user-visible behavior implemented, and the claims you intend to make at handoff. Every important claim should map to observable evidence.

For each important surface:

1. define the target flow: entry route → action/state → expected rendered result;
2. render and confirm the intended page is not blank and has no framework error overlay;
3. take a screenshot;
4. inspect hierarchy, geometry, type wrapping, spacing, color, asset crop, and obvious state problems;
5. test the main interaction and its resulting state;
6. inspect browser console errors when supported;
7. verify required viewport regions are actually visible; document-level scroll metrics do not prove that a fixed shell or internal pane is unclipped;
8. fix the largest visible mismatch;
9. rerun the same evidence check until the remaining issues are minor and explainable.

For screenshot/image recreation, compare the rendered result against the reference at the same viewport.

For `experience-engineering`, do not validate only the entry screen. Capture the named QA storyboard: representative middle states, the signature event before/peak/after, the final payoff, mobile, reduced motion, and fallback when practical. Also observe at least one complete hold → transform → settle transition, exercise each promised input role independently, and verify adaptive quality/fallback does not change the story. Verify navigation parity and cross-channel state too: visible narrative, HUD, active navigation and renderer/director state must describe the same chapter after natural scroll and representative intentional jumps.

A passing build is not a passing design review.

## Step 8 — Responsive and Accessibility Pass

Verify:

- no unintended horizontal scroll;
- primary content is visible without zooming;
- touch targets are usable;
- keyboard focus is visible;
- color contrast is sufficient;
- controls have meaningful names;
- responsive controls retain accessible names after labels become icon-only/hidden or move between breakpoint variants;
- reduced-motion preferences are respected;
- long strings, empty states, and error messages do not break layout;
- tables/dense controls have an intentional mobile strategy;
- text does not clip or collide at intermediate widths.

## Motion Rules

Motion must explain state, hierarchy, or spatial relationships.

Default:
- interaction feedback first;
- one signature orchestrated moment second;
- decorative ambient motion last.

Do not make a dense tool feel like a campaign website. Do not use cinematic scroll choreography merely because GSAP is available.

See references/modules/motion-direction/module.md. For live high-ambition WebGL/3D experiences, use references/modules/experience-engineering/module.md. For continuous pre-rendered scroll-scrubbed camera/media worlds, use references/modules/scroll-world/module.md instead of stacking generic motion guidance on top.

## Reference Fidelity Rules

When an accepted reference exists, fidelity outranks generic design heuristics. Preserve its:

- hierarchy;
- visible copy;
- section order;
- container logic;
- typography proportions;
- density;
- exact palette/background character, including true-white vs tinted/off-white choices;
- imagery/media treatment, crop, mask and overlay/tint behavior;
- icon/glyph metaphor, stroke/fill character and optical weight where visible;
- interaction model.

Do not "tastefully" reinterpret an accepted reference. Adapt only what is required for responsiveness, accessibility, missing assets, browser behavior, or another concrete technical constraint, and record the deviation.

## Completion Definition

Do not call substantial frontend work finished until:

- the required content and workflow are implemented;
- the design has one coherent visual thesis;
- generic filler has been removed;
- the canonical target/state used for signoff is known;
- at least one critical journey has been exercised through real user input;
- desktop and mobile are usable;
- important states exist;
- accessibility basics pass at the requested QA depth;
- browser-rendered visual QA has been performed when tools allow it;
- reference-based work has been compared against its reference;
- high-ambition experiential work has been inspected across its key-state storyboard, including the signature event and final payoff;
- timeline/layout/navigation channels remain synchronized at representative chapter boundaries and the final payoff;
- performance/regression gates were exercised when they are materially in scope;
- there are no known blocking console/runtime errors;
- the final QA status is stated honestly as VERIFIED, PARTIAL or BLOCKED rather than implying unverified coverage.

If visual tools are unavailable, explicitly perform a source-level fallback review and do not claim screenshot verification occurred.

## Path Contract

<skill-root> is the directory containing this SKILL.md.

Imported module paths remain module-relative:

~~~text
<skill-root>/references/modules/<module>/module.md
<skill-root>/references/modules/<module>/references/...
<skill-root>/references/modules/<module>/scripts/...
~~~

The stable UI/UX search facade is always:

~~~bash
python "<skill-root>/scripts/ui_ux_search.py" ...
~~~

## Source Map

This orchestration synthesizes ideas from multiple public frontend/design-agent skills while keeping the existing bundled UI/UX modules. See references/source-map.md for provenance and the specific ideas adopted.
