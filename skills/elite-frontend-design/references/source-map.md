# Source map and synthesis notes

This skill is a local synthesis. It does not blindly stack all upstream instructions. It adopts complementary ideas, records conflicts explicitly, and routes to a small profile per task.

The files below were deep-read again for the 3.2.0 review. External projects remain references/influences; this local skill does not require their hosted services or CLIs unless the user separately chooses to use them.

## Anthropic — skills

Repository:
https://github.com/anthropics/skills

Deep-read:
- `skills/frontend-design/SKILL.md`
- `skills/webapp-testing/SKILL.md`
- `skills/web-artifacts-builder/SKILL.md`

Adopted:
- art direction grounded in the subject, audience and actual job;
- typography as a primary visual system rather than neutral delivery;
- one memorable design idea with restraint elsewhere;
- structural decoration only when it communicates real information;
- limited non-user-triggered motion instead of animation on every section;
- compact design plan followed by self-critique against the actual brief;
- screenshot self-review when visual tooling exists;
- plain, task-oriented UI copy and consistent action naming;
- inspect dynamic/rendered state before interaction testing rather than assuming the first DOM/source view is the target.

Changed or rejected:
- no blanket font/style prohibition; established brand/system rules win;
- browser/testing mechanics remain host-tool agnostic.

The bundled local `frontend-design` module carries most of the visual-direction principles.

## OpenAI — current Build Web Apps plugin guidance

Repository:
https://github.com/openai/plugins

Deep-read:
- `plugins/build-web-apps/skills/frontend-app-builder/SKILL.md`
- `plugins/build-web-apps/skills/frontend-app-builder/references/imagegen-website-concepts.md`
- `plugins/build-web-apps/skills/frontend-testing-debugging/SKILL.md`
- `plugins/build-web-apps/skills/react-best-practices/SKILL.md`
- `plugins/build-web-apps/skills/shadcn-best-practices/SKILL.md`

Adopted:
- complete requested surface before coding; a hero-only concept is insufficient for a full app/page request;
- large readable section/state/detail references when one overview loses implementation detail;
- fresh detail references instead of cropping a tiny old overview;
- accepted reference/concept as a production specification, not an invitation to reinterpret the palette or container model;
- explicit copy, color, icon and hero-media treatment locks for high-fidelity work;
- small extracted design system before repeated implementation;
- real app working surfaces before marketing wrappers;
- browser-rendered validation as part of completion;
- target-flow definition and baseline runtime checks: correct page, not blank, no framework overlay, console health, screenshot evidence and interaction proof;
- reference mismatch ledger and cleanup of temporary QA artifacts;
- stack-specific performance/component guidance only when that stack is actually present.

Changed or rejected:
- image generation is optional in this local skill unless the user's workflow calls for it;
- React + Vite is not a universal default inside an existing repository;
- no dependency may be introduced merely because an upstream recipe prefers it.

## OpenAI — current Skills repository

Repository:
https://github.com/openai/skills

Deep-read:
- `skills/.curated/playwright/SKILL.md`
- `skills/.curated/playwright-interactive/SKILL.md`
- `skills/.curated/screenshot/SKILL.md`
- `skills/.curated/figma-implement-design/SKILL.md`
- `skills/.curated/figma-create-design-system-rules/SKILL.md`

Adopted:
- QA inventory built from user requirements, implemented behavior and final claims;
- important controls/states mapped to functional and visual evidence;
- at least a couple of relevant exploratory/off-happy-path checks for non-trivial work;
- functional QA and visual QA are distinct passes;
- viewport fit is a separate signoff concern;
- screenshots are primary evidence for clipping; document-level scroll dimensions alone are insufficient for fixed/internal panes;
- inspect required region bounds when clipping is plausible;
- structured design source + visual screenshot together are stronger than either alone;
- when structured design context is too large, inspect metadata/high-level structure then fetch only relevant children;
- reuse existing components/tokens and translate design data into repository conventions;
- progressive disclosure: the small set of high-impact rules should remain in the entrypoint, detailed rules belong in references.

Important provenance correction:
- the public benchmark's `frontend-skill` snapshot is **not** present as a current `frontend-skill` file in the cloned `openai/skills` repository. It is documented separately under the benchmark section below.

## Codex Frontend Design Skill

Repository:
https://github.com/dobromirdikov/codex-frontend-design-skill

Deep-read:
- `skills/frontend-design/SKILL.md`
- repository README

Adopted:
- inspect codebase and actual task before choosing a visual direction;
- literal product/brand signal in the first viewport;
- do not default to split-hero composition;
- tools/dashboards start with the working surface, not a marketing hero;
- concrete domain copy instead of generic UI filler;
- asset discipline;
- desktop/tablet/mobile browser QA;
- console/runtime review;
- text overflow and loading/empty/error state checks.

## Image-first Frontend

Repository:
https://github.com/jinshiqwq/image-first-frontend

Deep-read:
- root `SKILL.md`
- repository README/workflow documentation

Adopted:
- inspect project/content/viewport before visual generation;
- versioned preview paths and no silent overwrite;
- explicit approve / targeted revise / redo loop when the user requests image-first approval;
- targeted revisions expressed as `Preserve` + `Change`;
- redo as a materially different generation rather than image-conditioned drift;
- approved reference as visual source of truth;
- measured implementation-spec extraction;
- macro-geometry-first recreation;
- same-viewport screenshot comparison;
- real semantic/responsive implementation rather than screenshot embedding.

Changed:
- external generation/edit endpoints are optional;
- the strict approval gate applies only to explicit image-first/approval workflows.

## UI/UX Pro Max

Repository:
https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

Deep-read:
- current `.claude/skills/ui-ux-pro-max/SKILL.md`
- current repository README
- local bundled `references/modules/ui-ux-pro-max/module.md` for comparison

Result:
- the local bundled core search workflow remains aligned with the current upstream skill in the areas used here;
- the upstream skill also uses variance/motion/density design dials, supporting the local router's same conceptual axes.

Adopted and retained locally:
- searchable product/style/color/typography/UX intelligence;
- accessibility, touch, responsive, performance and stack guidance;
- master design-system + page override pattern;
- explicit search-result verification and no fabrication on zero results;
- design dials and domain/stack-specific lookup.

## Superdesign

Repository:
https://github.com/superdesigndev/superdesign-skill

Deep-read:
- `skills/superdesign/SKILL.md`
- `skills/superdesign/references/INIT.md`
- `skills/superdesign/references/SUPERDESIGN.md`
- `skills/superdesign/references/WEBSITE.md`
- `skills/superdesign/references/RESUME.md`

Adopted:
- inspect a real codebase before redesigning it;
- read the **actual render branch**, including responsive/feature/route conditions, instead of inferring UI from import names;
- trace the UI-touching dependency set for the target;
- context quality/budget over dumping the entire repository;
- compact token/theme summaries for repeated design work;
- reproduction structure/content should be evidence-based, not replaced by aesthetic adjectives;
- separate asset purposes: durable identity, final content, UI glyphs and temporary references;
- maintain design context across related screens when useful;
- when reference URLs are involved, distinguish content structure from style/design DNA.

Changed or rejected:
- no dependency on Superdesign remote projects, CLI state or SaaS;
- its resume/cache schema is too tool-specific for the root skill, so only the durable-context principle is adopted.

## Meng To — Skills

Repository:
https://github.com/MengTo/Skills

Deep-read:
- `agent-skills/ui/design-first-ui-prompting/SKILL.md`
- `agent-skills/codex/video-to-superprompt/SKILL.md`
- `agent-skills/codex/stitched-full-page-capture/SKILL.md`
- `agent-skills/codex/html-to-interaction-prompts/SKILL.md`
- `agent-skills/web-design/build-awwwards-quality-sites/SKILL.md`

Adopted:
- prompt like a design system: goal → format → layout → type → color/material → imagery → copy → constraints → negative constraints;
- variants over rerolls: change only 1–2 variables after a promising direction appears;
- local reference pack instead of relying on model memory for taste;
- video/reference → builder-ready spec with representative frames and asset map;
- source HTML/CSS/JS behavior as stronger interaction evidence than screenshot inference;
- reliable full-page evidence via warm-scroll + settled viewport capture + stitching when native full-page capture fails;
- concrete motion mechanisms rather than vague animation language;
- one smooth-scroll engine only, reduced-motion/mobile fallback and cleanup for GSAP/WebGL;
- honest assets/proof rather than fabricated logos, partnerships, testimonials or real-person endorsements.

Changed:
- no mandatory Awwwards/GSAP treatment for normal product UI;
- no dependency on article/content repo conventions.

## Taste Skill

Repository:
https://github.com/tasteskill/tasteskill

Deep-read:
- `tasteskill/gpt-taste/SKILL.md`
- `tasteskill/image-to-code/SKILL.md`
- `skills/redesign-skill/SKILL.md`
- `skills/output-skill/SKILL.md`
- `skills/imagegen-frontend-web/SKILL.md`
- repository README

Adopted:
- strong anti-slop awareness;
- explicit design/motion/density calibration;
- avoid 5–6-line hero headings on ordinary laptop widths;
- section-specific readable design references for image-to-code work;
- fresh detail generation rather than crop-based guessing;
- multi-reference consistency across palette/type/component/media treatment;
- redesign sequence: scan → diagnose → targeted fix rather than rewrite;
- responsive/mobile resilience;
- loading, empty, error, focus and pressed states;
- transform/opacity motion and cleanup/performance guardrails;
- semantic HTML and dependency verification;
- optical alignment and tabular numeric treatment where useful.

Changed or rejected:
- no fake/randomized art direction;
- no mandatory AIDA structure;
- static interfaces are allowed;
- no universal GSAP/Framer/Three.js requirement;
- no universal font/color/icon/layout bans;
- no fabricated "organic" metrics, people or business proof;
- no forced one-image-per-section rule when fewer references still provide readable implementation evidence;
- product type and repository truth determine the appropriate visual drama.

## Frontend Visual QA

Repository:
https://github.com/yutori-ai/frontend-visualqa

Deep-read:
- `skills/frontend-visualqa/SKILL.md`
- `skills/frontend-visualqa/references/claim-writing.md`
- `skills/frontend-visualqa/references/protocol.md`

Adopted:
- screenshot evidence as first-class proof;
- visual checks expressed as concrete observable claims;
- one visible fact per claim;
- exact copy and explicit viewport where relevant;
- setup/navigation separate from the visible fact being judged;
- small related claim batches;
- baseline screenshot when route/state is uncertain;
- rerun the same failed claim after a fix;
- failed/inconclusive claims require inspection of the deciding screenshot.

Changed:
- no dependency on Yutori's hosted verification service;
- claim-based QA complements rather than replaces open-ended design critique, functional testing or E2E coverage.

## Scroll World

Repository:
https://github.com/oso95/scroll-world

Reviewed commit:
`71cc36d3bb150248ae36a2c552f9cbf88802a79c` (2026-07-28)

Deep-read:
- root `README.md`;
- `skills/scroll-world/SKILL.md`;
- `skills/scroll-world/references/prompts.md`;
- `skills/scroll-world/references/pipeline.md`;
- `skills/scroll-world/references/scrub-engine.js`;
- `skills/scroll-world/references/index-template.html`;
- `skills/scroll-world/references/knockout.py`.

Adopted:
- continuous camera/world experiences should often use pre-rendered media whose time is driven by scroll, rather than approximating the camera with unrelated DOM effects;
- story beats and camera grammar are defined before asset generation;
- one coherent style/render source across the chain to reduce perceptual drift;
- seamless chains require **position continuity** from actual rendered boundary frames and **velocity continuity** across handoffs, including when the visitor scrubs backward;
- crossfade is seam insurance, not a substitute for correct boundary frames;
- continuous-forward architecture for grounded/realistic walkthroughs;
- dive + connector architecture for stylized/isometric/map-like worlds where pull-out travel is intentional;
- cheap previz/draft chain before expensive final rendering when external generation has material cost;
- a renderer/model is suitable for chaining only when it supports the required start/end-frame conditioning, regardless of standalone visual quality;
- segmented media encoded for seeking, with short GOP, consistent settings, native resolution, fast-start and no unnecessary audio;
- scroll → time mapping with per-section pacing and a monotone linger/dwell remap that preserves seam endpoints; expressive movement belongs primarily inside the rendered clip while the scrub remap stays restrained;
- nearby lazy loading/prefetch instead of eager decoding of the entire journey;
- seek coalescing while a mobile decoder is busy;
- poster remains visible until the first real video frame paints;
- iOS muted-inline video priming on first gesture;
- ignore touch-browser URL-bar height-only resizes but react to real width/orientation changes;
- native portrait/mobile chain when high-quality mobile composition matters; a center crop is an explicit fallback;
- reduced-motion mode uses still scenes and preserves the full narrative without loading cinematic motion;
- flat-background floating scenes can use border-connected background knockout so interior regions sharing the background hue are preserved;
- seam QA compares just-before/just-after evidence and judges visible composition/motion rather than raw PSNR alone.

Strengthened locally beyond the source:
- production implementations must expose lifecycle teardown: cancel animation loops, remove listeners, abort pending fetches where possible and revoke Blob object URLs;
- Blob media is a useful bounded fallback for seekability, but proper HTTP range serving is preferred for large/long production media to avoid excessive memory use;
- provider/model names, prices and command-line flags are treated as volatile and must be verified at execution time;
- no Monid/Higgsfield dependency is introduced;
- no required clay/isometric art direction;
- no assumption that cinematic scroll requires video when DOM/GSAP or real-time WebGL is the better technical fit.

Local module:
`references/modules/scroll-world/module.md`

## Frontend Skills Benchmark

Repository:
https://github.com/leoisadev1/skills-gpt-bench

Deep-read:
- `README.md`
- `RESULTS.md`
- `BENCHMARK_SOURCE_NOTES.md`
- `bench/rubric.md`
- benchmark snapshots:
  - `bench/skills/frontend-skill/SKILL.md`
  - `bench/skills/design-taste-frontend/SKILL.md`
  - `bench/skills/frontend-design/SKILL.md`
  - relevant GPT-Taste snapshot

Adopted lesson:
- route narrowly; more simultaneous design guidance is not automatically better;
- expressive direction benefits from practical product restraint;
- dashboard/operational work needs different guidance from marketing/public surfaces;
- product fit, hierarchy, distinctiveness, information architecture, responsive resilience, state/motion appropriateness and technical execution all belong in the quality bar.

Benchmark limitations recorded by the source:
- one controlled qualitative benchmark run;
- created/reported in May 2026;
- GPT-5.5 Codex worker setup;
- one generation per profile;
- qualitative, not blind grading;
- image generation intentionally disabled;
- 15 skill profiles, 7 routes × 2 viewports = 210 screenshots;
- results do not prove a universal best skill combination.

### Benchmark-only OpenAI frontend-skill snapshot

The benchmark includes `bench/skills/frontend-skill/SKILL.md`, attributed there to an OpenAI frontend-skill snapshot. This file is treated as **benchmark evidence**, not as a currently verified file in the cloned `openai/skills` repository.

Useful principles adopted from that snapshot:
- visual thesis + content plan + interaction thesis;
- each section has one job and one dominant idea;
- composition before component count;
- cards only when they communicate real grouping/interaction;
- sticky/fixed header counts against first-viewport hero height;
- product UI uses utility copy and exposes the working surface immediately;
- motion should be a few intentional moments rather than constant decoration.

## Local three-way regression — "Ten Billion Years"

Case-study document:
`references/benchmarks/cosmos-gpt56-case-study.md`

Three local implementations of the same high-ambition prompt were inspected source-by-source:

1. an earlier ChatGPT Web / elite-skill result;
2. a Codex Ultra result;
3. a Claude Desktop / Opus 5 result.

The regression is not used as a universal model ranking. It is used to extract **architectural and art-direction behaviors** that the local skill can require.

### Lessons retained from the Codex Ultra implementation

- explicit experience design spec and implementation plan before coding;
- clean timeline/geometry/shader/renderer/audio/overlay subsystem boundaries;
- deterministic seeded procedural geometry;
- GPU-first particle morphing;
- pure/testable timeline and one-shot cue semantics;
- device-aware performance tiers;
- low-frequency semantic framework state;
- designed WebGL fallback;
- explicit resource cleanup;
- unit-test contracts around timeline/shader/geometry/audio behavior.

### Additional lessons from the Opus 5 implementation

- **story physics**: chapter motion is derived from causal meaning rather than only interpolating generic target shapes;
- compact base attributes can analytically synthesize many shader states, enabling a very large single particle draw call without N full morph-position buffers;
- structured phenomena such as a molecular cloud can be sampled from a density field instead of approximated with a Gaussian smear;
- weighted chapter dwell plus hold-before-transform pacing lets each beat land;
- per-particle transition delays turn a uniform morph into flowing material;
- a central **Experience Director** synchronizes geometry, camera/FOV, sky, bloom/chroma, flash, accent and audio mix;
- one shared frame clock can feed renderer plus direct DOM presentation updates while framework state stays semantic;
- pointer input can be projected into world space for scale-consistent local forces;
- tap/click can own a separate world impulse while drag/scroll remains navigation;
- dynamic performance feedback can adjust DPR/post-FX quality at runtime rather than relying only on initial hardware tiers;
- post-processing is a narrative channel with authored peaks, not a static "premium" filter;
- a continuous procedural sound bed plus sparse semantic one-shots can reinforce the story;
- deliberate type assets and causal/domain-specific copy raise perceived authorship.

### Combined local target

The skill keeps **Codex-style engineering discipline** and adds **Opus-style world authorship**.

It should not trade:
- tests for spectacle;
- fallback for particle count;
- architecture for aesthetic complexity;
- narrative specificity for vague poetry.

The target is a system that is both engineered and authored.

Local module:
`references/modules/experience-engineering/module.md`

## Frontend QA synthesis — v3.6

Local module:
`references/modules/frontend-qa/module.md`

The goal is not to reproduce any proprietary hidden QA harness from a named model. The local target is the **observable QA behavior** associated with strong frontend coding agents: prove the target, exercise real journeys, inspect rendered evidence, test temporal/input behavior, and close with explicit evidence.

The synthesis reuses previously reviewed ideas from:
- OpenAI `playwright-interactive`: one shared QA inventory, persistent browser sessions, real user input, separate functional/visual passes, viewport-fit checks, in-transition/dense-state inspection, exploratory use and explicit final coverage;
- Anthropic `webapp-testing`: Playwright-based interaction with the running app, screenshot/browser-log evidence and choosing the smallest appropriate testing path;
- Yutori `frontend-visualqa`: claim-driven visual verification, screenshot evidence and recovery from wrong-page navigation.

### daymade/claude-code-skills — frontend-visual-qa

Repository:
https://github.com/daymade/claude-code-skills

Reviewed commit:
`72dc01ffe8a99b8be12f1bc8f7a87afb37e2b7bc` (2026-09-19)

Deep-read:
- `frontend-visual-qa/SKILL.md`;
- `frontend-visual-qa/references/browser-driving-and-observation-traps.md`;
- `frontend-visual-qa/references/history-derived-checklist.md`;
- `frontend-visual-qa/references/silent-degradation-and-evidence.md`.

Adopted:
- scope contract before auditing;
- exact target/state/data/viewport identity before judging pixels;
- evidence levels that distinguish real visible surfaces, browser automation, mechanical sweeps and source reasoning;
- VERIFIED / PARTIAL / BLOCKED status instead of false green;
- whole-composition evidence before local zoom;
- visual evidence must be actually inspected;
- state/journey and recipient-output verification;
- same-target/state/viewport re-run after a fix;
- silent degradation checks for fonts, CSS/library selectors, inert rules and other valid-but-nonfunctional styling;
- severity separated from defect category;
- evidence crop/context and explicit not-verified sections.

Changed locally:
- privacy/authorization ideas are retained as a compact QA contract rather than reproducing the source's full audit-governance machinery;
- bundled scripts are not copied into the local skill.

### practicajs/the-frontend-testing-skill

Repository:
https://github.com/practicajs/the-frontend-testing-skill

Reviewed commit:
`ae1b7bc8b58a77d3cd70e1d775fa73ecb8767154` (2026-09-14)

Deep-read from the pinned Git object:
- `plugin/frontend-testing/skills/frontend-testing/SKILL.md`;
- `.../references/test-workflow.md`;
- `.../references/rules/testing-with-dom.md`;
- `.../references/rules/assertions.md`;
- `plugin/frontend-testing/agents/testskill.verifier.md`;
- `plugin/frontend-testing/agents/testskill.page-analyzer.md`;
- `plugin/frontend-testing/agents/testskill.mutator.md`.

Adopted:
- test intent/definition before implementation for substantial work;
- analyze the actual page/runtime before writing nontrivial browser tests;
- user-facing ARIA/role/name locators over positional DOM selectors;
- web-first/auto-retrying assertions instead of fixed sleeps;
- result-focused minimal assertions;
- verification must close the loop;
- run tests repeatedly to expose flakiness;
- trace-driven failure fixing;
- optional mutation/sanity validation to prove a critical test catches real behavior changes;
- final report should distinguish planned vs actual coverage and stability.

Changed locally:
- mandatory `test-plan.md` and `page-analysis.md` for every small change are replaced by QA-1 / QA-2 / QA-3 depth;
- mutation testing is optional for high-value tests and must always revert immediately;
- no repo-specific config or agent command format is imported.

### maxrihter/claude-skill-visual-regression

Repository:
https://github.com/maxrihter/claude-skill-visual-regression

Reviewed commit:
`7fa2ea4fdac37867ba3686ef6936fd791a622fab` (2026-07-09)

Deep-read:
- `SKILL.md`;
- `references/comparison/README.md`;
- baseline/setup guidance.

Adopted:
- visual regression is distinct from manual visual-quality review;
- classify a failed diff as intentional change vs possible regression before baseline updates;
- deterministic environment/font/browser consistency matters;
- mask only legitimately dynamic regions;
- thresholds exist to absorb rendering noise, not meaningful layout drift;
- same-environment/container baselines reduce false CI failures.

Changed locally:
- never automatically update or commit baselines just to make a test pass;
- baseline mutation requires an intentionally accepted visual change.

### testdino-hq/playwright-skill

Repository:
https://github.com/testdino-hq/playwright-skill

Reviewed commit:
`400e4256cd22669ad69c18d31d3e5541e4e1c2a3` (2026-09-06)

Deep-read:
- `SKILL.md`;
- `core/accessibility.md`;
- `core/performance-testing.md`;
- `core/visual-regression.md`;
- `core/trace-analysis.md`;
- `core/flaky-tests.md`.

Adopted:
- axe/automated accessibility plus manual keyboard/critical-flow checks;
- accessibility/ARIA snapshots for high-value semantic widgets;
- automated accessibility is partial evidence, not a full WCAG verdict;
- Web Vitals/resource/network/CPU testing only when performance is materially in scope;
- screenshot thresholds/masks/animation control for visual regression;
- trace inspection across DOM, network, console, screenshot and stack;
- retries detect flakiness rather than fixing it;
- burn-in/repeat runs and isolation diagnosis for intermittent failures;
- no arbitrary `waitForTimeout` as a stability strategy;
- trace/HAR/screenshot artifacts may contain sensitive data and should be minimized/cleaned.

### Local QA architecture

The final local split is:

```text
frontend-qa
  owns overall QA contract
       │
       ├── functional journey
       ├── responsive/device
       ├── accessibility
       ├── performance when in scope
       ├── visual regression when baseline exists
       ├── stability/trace/exploratory
       │
       └── visual-qa
            owns rendered visual evidence
```

This keeps the normal router narrow while allowing QA-3 release/flagship work to become comprehensive when risk justifies it.

## Local Cosmos rerun — synchronization hardening for v3.7

On 2026-09-20 the rebuilt `cosmos-gpt-5.6-sol-extra-high` source and production deployment were re-reviewed after applying the latest skill.

The rerun showed that the skill had materially improved solution architecture, but also exposed an integration failure that isolated subsystem tests did not catch:
- abstract journey weights drove semantic timeline state;
- DOM sections used independent viewport-height geometry;
- chapter rail jumps were calculated from abstract timeline progress;
- visible narrative, HUD/rail and final-mode state could therefore disagree.

Retained lesson:
- one authoritative/calibrated progress domain must connect layout, director, navigation, HUD, audio and payoff state;
- browser QA must assert cross-channel parity, not only timeline math or screenshots in isolation;
- responsive accessibility semantics must be rechecked after breakpoint presentation changes;
- synthetic diagnostics require a clean-context rerun before product attribution.

Local modules updated:
- `references/modules/experience-engineering/module.md`;
- `references/modules/frontend-qa/module.md`;
- `references/modules/visual-qa/module.md`.

No new external source was required for v3.7; this is a local regression-derived hardening pass.

## Reviewed snapshot pins

See `source-snapshots.md` for the exact upstream commits reviewed through 2026-09-20.

## Local provenance

The original base in this folder was a unified UI/UX Pro Max assembly with imported design/styling modules.

Version 3.7.0 keeps the v3.6 full-spectrum QA director and hardens cross-system experiential synchronization:
- one progress domain across narrative layout, Experience Director, HUD, navigation, audio and payoff state;
- timeline ↔ layout calibration rather than trusting isolated timeline math;
- navigation parity across natural scroll, intentional jumps and restoration paths;
- cross-channel state QA at representative chapter boundaries;
- responsive accessibility snapshots after breakpoint presentation changes;
- diagnostic clean-context reruns;
- spec-to-implementation traceability for flagship experiential promises.

Version 3.6.0 keeps the v3.5 authored-world / experience-engineering contracts and adds a dedicated `frontend-qa` director:
- QA-1 / QA-2 / QA-3 depth routing;
- canonical target/state/role/data/viewport proof;
- one shared QA inventory across requirements, implementation and handoff claims;
- evidence-level discipline rather than promoting source/build evidence into rendered/user-journey proof;
- critical functional journeys through real user input;
- `visual-qa` as the rendered/pixel/reference specialist;
- responsive/device, accessibility, performance and visual-regression gates only when risk justifies them;
- semantic locators, web-first assertions and deterministic test-state guidance;
- trace-driven diagnosis, flake burn-in and optional critical-test mutation sanity;
- exploratory/tired-user passes;
- same-target/state/viewport fix-and-reverify;
- VERIFIED / PARTIAL / BLOCKED signoff with explicit unknowns.

The v3.4 planning/tests/fallback and v3.5 authored-world contracts remain mandatory. The 3.3 `scroll-world` path remains the specialist for pre-rendered camera journeys, while the earlier reference/visual QA hardening remains intact.

No external repo is copied wholesale into the root prompt. The router continues to prefer the smallest useful capability set.

## Local audited website corpus ? Distilled Web Toolkit

The local `distilled-web-toolkit` is built from fifteen live website/reference audits already present in this plugin. These are not external package dependencies; they are evidence sources whose transferable mechanisms are normalized into searchable local data with provenance.

Audited reference corpus:
- https://www.refokus.com/
- https://www.webflow-tools.refokus.com/
- https://resend.com/
- https://www.rockstargames.com/VI
- https://tokenmeter.info/
- https://novaos.framer.website/
- https://powder.framer.website/
- https://nudge-folio.framer.website/
- https://orbai-template.framer.website/
- https://nexira.framer.ai/
- https://cosmos-10-billion-years-opus5.vercel.app/
- https://voxai.framer.ai/
- https://tobi-mallory.framer.website/
- https://indiex.framer.ai/
- https://ready-material-053719.framer.app/

2026-10-07 live re-audit method:
- connected to Chrome through the local browser MCP;
- revisited all fifteen live references;
- attempted a common desktop/mobile resize pass and recorded the viewport actually observed;
- checked current sitemap availability/count, rendered document dimensions, outer overflow, major type roles, media/canvas counts, fixed/sticky ownership, and runtime/platform signals;
- compared those live snapshots against the deeper historical site profiles already stored under `references/design-intelligence/sites/`;
- preserved topology drift rather than silently rewriting historical audits (for example, current Refokus exposes a much larger sitemap than the original profile scope);
- standardized each reference into one implementation-oriented toolkit spec;
- promoted only transferable layout/proof/route/motion/media/responsive/QA mechanisms and quarantined proprietary identity, fake/template content, vendor chrome, and route residue.

Toolkit outputs:
- `references/modules/distilled-web-toolkit/data/sites.csv`;
- `references/modules/distilled-web-toolkit/data/live-audit-2026-10-07.csv`;
- `references/modules/distilled-web-toolkit/data/patterns.csv`;
- `references/modules/distilled-web-toolkit/data/route-recipes.csv`;
- `references/modules/distilled-web-toolkit/data/motion-recipes.csv`;
- `references/modules/distilled-web-toolkit/data/responsive-recipes.csv`;
- `references/modules/distilled-web-toolkit/data/anti-patterns.csv`;
- `references/modules/distilled-web-toolkit/specs/*.md`;
- `scripts/distilled_toolkit_search.py`.

Design principle: provenance before prescription. The toolkit is a retrieval/composition layer over audited evidence, not a clone library.

