# Elite Frontend Design — module registry

The root SKILL.md is the only entrypoint. Modules are references loaded on demand.

## Core orchestration modules

| Module | Purpose | Entry |
|---|---|---|
| elite-core | Product grounding, design dials, design contract, anti-slop, implementation discipline | modules/elite-core/module.md |
| reference-first | Screenshot/image/video/reference analysis and faithful design-to-code handoff | modules/reference-first/module.md |
| design-intelligence | Distill reusable design DNA, motion/interaction mechanisms, responsive brand payload and technical lessons from strong reference sites without cloning | modules/design-intelligence/module.md |
| distilled-web-toolkit | Searchable audited patterns, route recipes, motion/media, responsive transforms and anti-patterns distilled from 11 live references with provenance | modules/distilled-web-toolkit/module.md |
| visual-qa | Specialist rendered visual evidence: screenshot review, responsive geometry, reference parity and refinement loops | modules/visual-qa/module.md |
| frontend-qa | Full QA director: target/state proof, functional journeys, navigation/cross-channel parity, responsive accessibility, performance/regression gates, trace evidence and release signoff | modules/frontend-qa/module.md |
| motion-direction | Motion levels, interaction motion, GSAP-style cinematic choreography with restraint | modules/motion-direction/module.md |
| experience-engineering | High-ambition authored WebGL/3D worlds: story physics, GPU-first rendering, Experience Director, one progress domain, timeline↔layout synchronization, temporal staging, adaptive performance and key-state QA | modules/experience-engineering/module.md |
| scroll-world | Continuous scroll-scrubbed camera journeys, seamless pre-rendered media chains, native mobile variants and seam QA | modules/scroll-world/module.md |

## Bundled knowledge modules

| Module | Purpose | Entry |
|---|---|---|
| ui-ux-pro-max | Searchable UI/UX intelligence: accessibility, responsive design, palettes, typography, charts, animation and stack guidance | modules/ui-ux-pro-max/module.md |
| ui-styling | Component styling, Tailwind/shadcn patterns, responsive/dark mode and accessible primitives | modules/ui-styling/module.md |
| frontend-design | Brief-specific visual direction, typography/layout restraint, anti-template critique, copy and self-critique | modules/frontend-design/module.md |
| design-system | Tokens, CSS variables, component specs and validation | modules/design-system/module.md |
| brand | Brand voice, identity, guidelines and asset governance | modules/brand/module.md |
| design | Broad visual-design orchestration for logos, identity and assets | modules/design/module.md |
| banner-design | Banner/ad/cover art direction and production guidance | modules/banner-design/module.md |
| slides | Strategic HTML presentation workflow | modules/slides/module.md |

## Baseline skin packs

Use `design-intelligence/skins/index.md` when Adaptive Capability Routing selects LOCKED or GUIDED, when open-ended art direction is likely to drift, or when the user asks for a polished template-grade baseline. Choose one skin only; apply Skin Lock + Controlled Mutation and keep the Template Archetype Firewall active.

## Design intelligence profiles

Site profiles are selective evidence packs loaded only when relevant.

Use `design-intelligence/reference-landscape.md` when the task starts from a broad inspiration search, when choosing which references deserve a deep audit, or when checking Template Convergence Risk. The landscape registry contains **candidates, not audited evidence**.

| Site | Useful for | Profile |
|---|---|---|
| Refokus | Premium B2B/agency storytelling, one-signature-stage allocation, editorial case studies, bounded WebGL, motion-as-focus, responsive brand payload | design-intelligence/sites/refokus.com.md |
| Resend | Developer-product storytelling, code/product evidence, functional ecosystem tabs, restrained material systems, responsive fidelity substitution | design-intelligence/sites/resend.com.md |
| Rockstar Games VI | World-led game launch campaigns, aspect-ratio art direction, trailer/media choreography, chapter ownership, responsive cinematic payload | design-intelligence/sites/rockstargames.com-vi.md |
| Tokenmeter | Whole-site data/reference systems, route-family density, confidence/provenance UI, comparison tables, machine-readable parity | design-intelligence/sites/tokenmeter.info.md |
| NovaOS | Full-site enterprise AI SaaS template system, operational pipeline proof, mobile proof cropping, trust-route ecosystem, Framer responsive/runtime discipline | design-intelligence/sites/novaos.framer.website.md |
| Powder | Full-site dark AI/SaaS template system, conversation-to-action proof, sticky capability storytelling, template-residue quarantine, responsive release | design-intelligence/sites/powder.framer.website.md |
| Nudge Folio | Full-site portfolio template system, reflective case-study narrative, persistent context rails, isolated experimental playground, expressive type roles | design-intelligence/sites/nudge-folio.framer.website.md |
| OrbAI | Full-site light AI/service template system, commercial core + trust satellites, pricing-to-comparison bridge, responsive card conversion grammar | design-intelligence/sites/orbai-template.framer.website.md |
| Nexira | Full-site game-studio template system, cinematic-without-heavy-rendering, service/case proof pairing, sticky project decks, responsive game identity | design-intelligence/sites/nexira.framer.ai.md |
| Ten Billion Years (Opus 5) | Single-route audited scroll world, prompt-to-experience compilation, weighted narrative timeline, shared progress bus, procedural WebGL/audio, adaptive renderer quality | design-intelligence/sites/cosmos-10-billion-years-opus5.vercel.app.md |
| VoxAI | Full-site dark AI/SaaS system, operational micro-scenes, integration implementation proof, route-family binding integrity, CMS/template residue QA, responsive media substitution | design-intelligence/sites/voxai.framer.ai.md |
| Tobi Mallory | Full-site whimsical portfolio world, creature/collection information architecture, category visual physics, mnemonic case-study proof, quest/service translation | design-intelligence/sites/tobi-mallory.framer.website.md |

## Loading rule

Load only the modules that own distinct concerns. A normal frontend implementation should not need more than 2–4 modules.

Suggested profiles:

- Marketing implementation: elite-core → frontend-design → frontend-qa; add motion-direction only when motion matters.
- High-ambition live 3D/WebGL experience: elite-core → experience-engineering → frontend-qa; add frontend-design only for distinct art-direction ideation.
- Scroll-cinematic pre-rendered world: elite-core → scroll-world → frontend-qa; add reference-first when recreating a known experience.
- Product/dashboard: elite-core → ui-ux-pro-max → frontend-qa; add ui-styling when implementation guidance is needed.
- Audited pattern composition / known reference library: elite-core ? distilled-web-toolkit ? frontend-design ? frontend-qa.
- Visual/reference-only audit: reference-first → visual-qa.
- Reference recreation with real interactions: reference-first → elite-core → frontend-qa.
- Redesign implementation: elite-core → ui-ux-pro-max → frontend-design only if a new visual identity is needed → frontend-qa.
- Design system: design-system → ui-ux-pro-max → ui-styling → frontend-qa when release verification is requested.

## Relative paths

Each imported module keeps its own references, scripts, data, templates and assets. Paths inside a module remain relative to that module directory.

The top-level UI/UX search wrapper remains:

~~~bash
python "<skill-root>/scripts/ui_ux_search.py" "<query>" [options]
~~~

## Provenance

See ../source-map.md.
