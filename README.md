# Elite Frontend Design Plugin

A portable ChatGPT + Codex plugin containing one profile-routed frontend design skill focused on one outcome: ship frontend work that is distinctive, useful, responsive, and visually verified after render.

Current version: 3.32.1

## Resend whole-site audit (3.30.0)

Re-audited 11 nested Resend sitemaps containing **1,015 distinct URLs**: 1,014 returned HTTP 200 and one stale /shop URL returned 404. Retained the homepage design/runtime evidence and expanded the corpus to full product, feature, docs, integration, migration, release, customer, handbook, people, clubs and event route families.

A durable 1,015-row route inventory and route-family spec now accompany 10 new patterns, 8 route recipes, 1 motion recipe, 3 responsive recipes, 3 anti-patterns, 6 component recipes and 4 UX guidelines.

Toolkit totals: **15 sites, 118 patterns, 51 route recipes, 24 motion recipes, 38 responsive recipes, 47 anti-patterns, 56 component recipes, 38 UX guidelines**. Remains **17 modules, 13 skins**.

## Battlez full-site distillation (3.31.0)

Version 3.31 adds Battlez with a complete **75/75 URL** sitemap census and representative desktop/mobile audits across campaign, company, store, 53 product details, game categories, news, news categories, pricing, FAQ, contact and 404. Resolved 74 200 and one authored 404. Separates reusable gaming-commerce patterns from unrelated toy/beauty/home/sports CMS fixtures.

New totals: **16 sites, 125 patterns, 56 route recipes, 24 motion recipes, 40 responsive recipes, 51 anti-patterns, 60 component recipes, 42 UX guidelines**. The deterministic 13 skins and 17 modules are unchanged.

## Nouva full-site distillation (3.32.0)

Version 3.32 audits all 8 Nouva sitemap URLs plus linked /404 across desktop/mobile Chrome. This adds dark AI productivity SaaS marketing, task/screenshot proof, in-view numeric reveals, contact-first lead CTAs, three pricing plans, FAQ, FrameAuth-branded sign-up/sign-in/OTP/account routes, and two long-form legal pages.

Added 7 patterns, 6 route recipes, 1 motion recipe, 2 responsive recipes, 3 anti-patterns, 4 components, 4 UX guidelines, and a dated route inventory with evidence boundaries. Toolkit totals: **17 sites, 132 patterns, 62 route recipes, 25 motion, 42 responsive, 54 anti-patterns, 64 components, 46 UX guidelines**. The 13 baseline skins and 17 modules remain unchanged.

## Echoes of Mars three-mode re-audit (3.32.1)

The original 1-route / 13-chapter 2026-10-07 site audit was correct. A fresh 2026-10-08 Chrome re-audit verifies three actual spatial-survey breakpoints: <=809px vertical; 810–1199px pinned 4280px track; >=1200px pinned 5320px track. It also finds that the live template **does not honor reduced-motion** for its -3880px scroll transform. This adds one responsive recipe, one anti-pattern, one accessibility UX guideline and a nine-row runtime viewport snapshot, rather than duplicating the five existing core design patterns.

Toolkit totals: **17 audited sites, 132 patterns, 62 route recipes, 25 motion recipes, 43 responsive recipes, 55 anti-patterns, 64 components, 47 UX guidelines**. 13 skins and 17 modules unchanged.

## Plugin packaging

Version 3.8 converts the standalone skill folder into the current OpenAI plugin package shape:

- `plugin.json` is the portable Agent Plugins manifest used as the canonical package identity;
- `.codex-plugin/plugin.json` is retained as the Codex/OpenAI compatibility fallback;
- `skills/elite-frontend-design/SKILL.md` is the runtime skill entrypoint;
- `skills/elite-frontend-design/agents/openai.yaml` enables the skill for both `CHAT` and `CODEX` and allows implicit invocation;
- the plugin is skills-only: it does not require an MCP server, `.app.json`, or hosted backend;
- `scripts/package_plugin.py` builds a ZIP suitable for the ChatGPT plugin upload flow.

### ChatGPT web

Build the upload archive:

~~~bash
python scripts/package_plugin.py
~~~

Upload the resulting `dist/elite-frontend-design-3.32.1.zip` through the ChatGPT Plugins upload flow as **Skills only**. After the plugin is installed in the workspace/account, start a new ChatGPT Work conversation and invoke it explicitly with `@elite-frontend-design` when needed; implicit routing is also enabled by the skill policy.

For public distribution, the same package can be submitted to the universal plugin directory. Public submission still requires the publisher to complete verified developer identity and policy attestations in the OpenAI submission flow.

### Codex

Codex discovers plugin skills from the package `skills/` directory. For local development, expose this plugin through a local/repository plugin marketplace and install it from `/plugins`; for public distribution, install the published plugin from the universal plugin directory. Start a new Codex conversation after installation so the skill catalog is refreshed.

## What this version changes

Version 3.29 re-audits Refokus as a complete ecosystem rather than a homepage reference. The audit covers 102 main-site sitemap URLs plus the 19-route Webflow Tools companion sitemap advertised from Refokus robots.txt: 121 declared public URLs in total.

Version 3.29 adds:

- full route-family evidence for service, audience, authority, work/project, news/article, careers, resource, contact and 404 surfaces;
- Refokus Webflow Tools as the 15th audited site/profile while the deterministic baseline remains 13 skins;
- re-verification of the WebGL2/Three/GLTF hero, model.glb, postprocessing, GSAP/ScrollTrigger/SplitText/CustomEase and DPR 1.5 runtime;
- Service Narrative Landing System, Audience-Specific Proof Binding, Evidence-Dependent Case Depth, Media-Dense Proof Directory and Long-Form Outline -> Flow;
- Copy -> Configure -> Verify Documentation, Public Implementation Styleguide as Product Trust and Sticky Technical Context Band;
- route-level QA for canonical mismatch/missing canonical, missing document language and multi-H1 fragmentation;
- toolkit totals of 15 sites, 108 patterns, 43 route recipes, 23 motion recipes, 35 responsive recipes and 44 anti-patterns;
- design-system totals of 15 profiles, 15 color systems, 15 typography systems, 50 component recipes and 34 UX guidelines.

The router remains at 17 modules and the baseline remains 13 skins.
Version 3.28 deep-audits the complete Echoes of Mars Framer campaign at `ready-material-053719.framer.app`. Its public topology is intentionally one indexable route, so the audit covers the full chapter system, anchor jobs, custom world-survey runtime, desktop/mobile substitution, external conversion integrity and generic 404 rather than pretending the site has hidden route families.

Version 3.28 adds:

- `references/design-intelligence/sites/ready-material-053719.framer.app.md` with complete 1/1 sitemap coverage plus hero, trailer, premise, world, story, gameplay, systems, media, character, sound, release, press, final conversion and 404 evidence;
- Echoes of Mars as the **14th audited website** while keeping the baseline at **13 skins**; it becomes the first full-site audited anchor for the existing `cinematic-game` skin;
- **Telemetry as Narrative UI**, **Pinned Sector Survey**, **Recovered Footage Proof**, **Numbered Field-Report Chapters** and **Mechanics Survey Rows**;
- desktop evidence for a ~5320px world track inside one pinned viewport, with the complete spatial sequence transformed to normal vertical flow on 390px mobile;
- live evidence of a ~1425x18690 desktop campaign and 390x17608 mobile campaign with **47 images, 0 HTML video, 0 canvas**, and zero mobile document-level overflow;
- QA evidence for empty home language metadata, repeated mechanic H1s, touch-inappropriate `HOVER TO SURVEY` copy, anonymous press proof and high-intent actions that resolve only to platform roots/example domains;
- 5 reusable patterns, 1 route recipe, 1 motion recipe, 2 responsive recipes and 5 anti-patterns;
- the design-system layer now covers **14 design profiles, 14 color systems, 14 typography systems, 43 component recipes and 29 UX guidelines**.

The router remains at **17 modules** and the baseline remains **13 skins**. The audited toolkit corpus now contains **14 sites, 100 patterns, 37 route recipes, 22 motion recipes, 32 responsive recipes and 40 anti-patterns**.
Version 3.27 deep-audits the complete Indiex Framer game-studio template rather than treating its hero as the site. The public topology is intentionally compact: **2/2 sitemap URLs** (`/` and `/404`) plus the complete **15-section anchor-driven homepage**.

Version 3.27 adds:

- `references/design-intelligence/sites/indiex.framer.ai.md` with full homepage, `/404`, desktop/mobile, media, form, interaction-semantic, SEO and content-integrity coverage;
- Indiex as the **13th audited website** while keeping the deterministic baseline at **13 skins** because it strengthens the existing `game-studio` family rather than creating a redundant skin;
- **One-Page Studio Conversion Spine**, **Sticky Game Selector**, **Poster-First Media Interlude**, **Proof -> Objection -> People -> Contact**, and **Template Residue Firewall** as new evidence-backed mechanisms;
- explicit QA evidence for mixed Indiex/Nexira/ThemeForest identity, gym/fitness FAQ residue, conflicting contact data, dead service links, GET-to-self placeholder forms and focusable DIV controls without role/state semantics;
- live evidence of a 1425x11401 desktop home and 390x17793 mobile home with **0 canvas**, **2 video elements**, desktop sticky game selection that releases on mobile, and no mobile document-level horizontal overflow;
- 6 reusable patterns, 2 route recipes, 1 motion recipe, 2 responsive recipes and 4 anti-patterns;
- the audited design-system layer now covers **13 design profiles, 13 color systems, 13 typography systems, 39 component recipes and 26 UX guidelines**.

The router remains at **17 modules** and the baseline remains **13 skins**. The audited toolkit corpus now contains **13 sites, 95 patterns, 36 route recipes, 21 motion recipes, 30 responsive recipes and 35 anti-patterns**.
Version 3.26 revisits all **12 audited websites live through Chrome** and upgrades the Distilled Web Toolkit from a provenance-backed pattern library into a broader audited design recommendation engine.

Version 3.26 adds:

- **12 audited design profiles** with product fit, style keywords, composition, visual signature, VARIANCE/MOTION/DENSITY descriptors, performance and accessibility watches;
- **12 semantic color systems** with role-based accent/contrast strategies and explicit transfer rules instead of cloneable palette presets;
- **12 typography systems** covering display/heading/body/utility roles plus observed desktop-to-mobile scale behavior;
- **36 component recipes** with component job, anatomy, interaction, responsive transformation, accessibility contract and anti-pattern;
- **24 site-derived UX guidelines** expressed as practical do/don't rules;
- a 12-site desktop/mobile primitive ledger captured from the current live renders;
- new searchable domains: `style`, `color`, `typography`, `component` and `ux`;
- `--design-system` retrieval, which selects one coherent audited source profile and composes its style, color, typography, components, supporting patterns, responsive/motion recipes and UX watches;
- optional `--variance`, `--motion` and `--density` selectors for closer design-profile matching;
- a strict provenance rule: transfer mechanisms and role systems, never source identity, proprietary fonts/assets, exact palettes, copy, claims, metrics or brand-specific artwork.

The router remains at **17 modules**, with **13 baseline skins** and the same 12-site pattern corpus. The toolkit now additionally exposes **12 design profiles, 12 color systems, 12 typography systems, 36 component recipes and 24 UX guidelines**.

Version 3.25 deep-audits the complete Tobi Mallory Framer portfolio and expands the Distilled Web Toolkit from 11 to **12 audited websites**.

Version 3.25 adds:

- `references/design-intelligence/sites/tobi-mallory.framer.website.md` with **30/30 sitemap URL coverage**: 10 core/utility routes, 7 Fieldbook project details, 6 Type details, 4 Journal details and 3 Quest/service details;
- a new evidence-backed **Whimsical World Portfolio** skin, increasing the deterministic baseline set from 12 to **13 skins**;
- **World Metaphor as Information Architecture** for mapping one coherent fictional/collectible vocabulary onto real project, category, service, content and contact jobs;
- **Taxonomy as Visual Physics** so categories can consistently control bounded accent/badge/illustration/map variables without becoming color-only navigation;
- **Mnemonic Case-Study Encoding** so memorable creature/object/number identities sit on top of real client/year/scope/problem/result evidence;
- **Metaphor Translation Contract** so playful labels remain operationally decodable through URLs, headings, metadata, form labels, prices, durations and accessible names;
- **Project Evolution as Relationship Proof**, using real follow-on engagements to demonstrate system scalability and client continuity;
- a Tobi Mallory toolkit spec plus 8 reusable patterns, 5 route recipes, 2 motion recipes, 3 responsive recipes and 5 anti-patterns;
- live evidence that a playful game-like portfolio can use **239 Framer/DOM animations with 0 canvas and 0 HTML video**, rather than defaulting to heavy WebGL;
- responsive evidence across Home, Fieldbook, Type, Isles, Journal, Quest and Contact at 390x844 with no document-level horizontal overflow;
- SEO/QA evidence for systematic canonical-host drift to `eternal-fade-087901.framer.app` and semantic H1 gaps on Fieldbook/Journal detail templates.

The router remains at **17 modules**. The baseline set increases to **13 skins**. The audited toolkit corpus now contains **12 sites, 89 patterns, 34 route recipes, 20 motion recipes, 28 responsive recipes and 31 anti-patterns**.

Version 3.24 converts the eleven audited website references into a **searchable Distilled Web Toolkit** after revisiting every live reference through Chrome on 2026-10-07.

Version 3.24 adds:

- a seventeenth router module, `distilled-web-toolkit`, for provenance-backed pattern retrieval and composition without loading all site profiles;
- eleven standardized implementation-oriented specs covering Refokus, Resend, Rockstar Games VI, Tokenmeter, NovaOS, Powder, Nudge Folio, OrbAI, Nexira, Ten Billion Years and VoxAI;
- a live cross-site audit ledger recording current sitemap/topology signals, rendered document/overflow behavior, media/canvas counts, fixed/sticky ownership, typography roles and current runtime/platform evidence;
- **81 audited reusable patterns**, **29 route recipes**, **18 motion recipes**, **25 responsive recipes**, and **26 anti-patterns**, all with source provenance;
- `scripts/distilled_toolkit_search.py`, supporting keyword search plus `--domain`, `--site`, `--archetype`, result limits and JSON output;
- a Pattern Composition Contract: **1 archetype + 1 primary composition grammar + up to 3 supporting patterns + 1 responsive strategy + 1 proof strategy**;
- explicit **Live Snapshot vs Audited Profile** handling so current topology drift does not silently overwrite historical deep-audit evidence;
- current live drift evidence including Refokus' expanded 102-URL sitemap and the live runtime/framework snapshots across all eleven sources;
- regression and validator coverage for dataset sizes, exactly 11 specs, module registration and search-tool smoke queries.

The router now contains **17 modules**. The baseline set remains at **12 skins**.

Toolkit lookup example:

```bash
python "<skill-root>/scripts/distilled_toolkit_search.py" "integration setup proof" --domain proof
```

Version 3.23 deep-audits the complete VoxAI Framer site instead of treating the homepage as the product. The audit covers all 36 sitemap URLs plus the indexed `/404` utility surface and promotes route-family integrity as a first-class design/QA concern.

Version 3.23 adds:

- `references/design-intelligence/sites/voxai.framer.ai.md` with 36/36 sitemap coverage across core pages, 6 case studies, 8 blog details, 13 integration details, 2 legal routes, and the `/404` utility route;
- **Integration Detail as Implementation Proof**: identity/job -> capabilities -> installation -> operational metadata -> setup action -> sales fallback -> related integrations;
- **Route-Family Binding Integrity**: verify slug/canonical/title/H1/summary/media/metadata/body/metrics/related items/CTA resolve to the same CMS record across an entire dynamic family;
- frontend-QA coverage for same-CMS-record checks, duplicate-content canaries, and server/default versus hydrated route identity;
- explicit quarantine of VoxAI template residue such as integration copy routes, placeholder domains, wrong connector instructions, duplicated article bodies, shared case-study heroes, and unresolved legal placeholders;
- responsive evidence showing representative 390x844 routes remain overflow-free while desktop video/product media is reduced on mobile without losing semantic order;
- cleanup of the duplicated Prompt-to-Experience Compile Contract / Narrative Parameter Matrix / Event Peaks block introduced in the prior release;
- no new baseline skin: VoxAI's transferable value is route ecosystem/proof/data integrity rather than a new dark-AI surface recipe.

The router remains at 16 modules and the baseline set remains at 12 skins.

Version 3.22 deep-audits the live Ten Billion Years / Opus 5 experience as a complete single-route scroll world and converts its prompt-to-runtime system into reusable design intelligence.

Version 3.22 adds:

- references/design-intelligence/sites/cosmos-10-billion-years-opus5.vercel.app.md with explicit **1/1 public-route coverage** plus the complete 9-chapter entry/HUD/WebGL/audio/input/responsive/replay runtime;
- current live corroboration of one fixed canvas, a 1029vh weighted scroll track, React Three Fiber + three.js r185 + custom GLSL, Lenis 1.3.25, procedural Web Audio, mobile 390x844 behavior, reduced motion, and adaptive DPR/quality;
- **Prompt-to-Experience Compile Contract** for translating a short high-ambition creative prompt into ordered narrative states, world mechanics, input roles, performance/fallback requirements, and a payoff before implementation;
- **Narrative Parameter Matrix** for making chapter copy, palette, particle/world state, camera, post-FX, HUD and audio describe the same authored moment;
- **Event Peaks on Continuous Timeline** for combining reversible scroll interpolation with sparse high-energy narrative events such as ignition, implosion, supernova and arrival;
- a Ten Billion Years audited real-time anchor in scroll-world, adding Weighted Narrative Timeline, Shared Progress Bus, analytic shared-world synthesis, two-layer rendering, Adaptive Renderer Budget, and procedural score guidance;
- explicit separation between the existing Cosmos model-comparison benchmark and the new live-site design-intelligence profile;
- no new skin: the lesson is experience architecture rather than a reusable cosmic visual skin.

The router remains at 16 modules and the baseline set remains at 12 skins.

Version 3.21 splits the Nexira-derived studio/service system into a dedicated Game Studio skin instead of overloading the generic Cinematic Game baseline.

Version 3.21 adds:

- a new `game-studio.md` skin backed by the audited Nexira full-site profile for game development studios, outsourcing/service companies, indie studio portfolios, team/about ecosystems, service detail families, case-study proof, blogs and contact;
- an explicit **Game Studio Routing Boundary**: organization/studio-as-product -> Game Studio; generic game/entertainment marketing -> Cinematic Game; flagship single-game/franchise launch -> Open World Cinematic Launch;
- a restored `cinematic-game.md` as a generic game/entertainment marketing baseline with no single audited site ownership, keeping Cinematic Without Heavy Rendering as a general mechanism without inheriting Nexira-specific service/case architecture;
- preservation of `open-world-cinematic-launch.md` as the GTA VI-backed high-ambition franchise/game-launch skin;
- skin registry, validator and regression updates for an exact 12-skin baseline set;
- the Nexira audited anchor moved from Cinematic Game to Game Studio without duplicating the site profile or promoted design-intelligence patterns.

The router remains at 16 modules while the baseline set increases from 11 to **12 skins** so lower-capability execution gets a clearer deterministic routing choice instead of one oversized game skin.

Version 3.20 deep-audits the entire Nexira Framer game-studio template and upgrades Cinematic Game from a curated baseline into an audited studio/entertainment scaffold without adding a twelfth skin.

Version 3.20 adds:

- references/design-intelligence/sites/nexira.framer.ai.md with explicit **28/28 sitemap coverage**: seven primary routes, all 7 service detail pages, all 7 case detail pages, and all 7 blog detail pages, plus separately quarantined /404 utility coverage;
- sitemap/search-index/internal-link parity checks confirming the same 28 public routes and no additional same-origin public route;
- source/runtime evidence for Framer b8d5a97, Oswald/Inter typography roles, bundled Fragment Mono, #adff00/#ffd335 accents, #1d1d1d deep shell, 810px/1360px breakpoints, Framer Motion runtime, static image-led rendering, and desktop/mobile sticky behavior;
- **Cinematic Without Heavy Rendering** for game/studio sites that can achieve premium world identity with still art, authored crop, condensed typography, HUD-like metadata, sticky sequencing and lightweight motion instead of unnecessary WebGL/video;
- **Capability-to-Case Pairing** for separating what a studio offers from proof of what it has delivered through service index/detail and case index/detail route families;
- a substantial upgrade to cinematic-game.md, now using Nexira as an audited game-studio/template anchor while preserving open-world-cinematic-launch.md for franchise/game-launch campaigns such as GTA VI;
- responsive sticky guidance from Nexira: release desktop service-card and case-detail sticky geometry when it harms mobile reading, but preserve the mobile case deck when each card remains a readable full-stage chapter;
- explicit quarantine for Nexira template/vendor identity, fake awards, player/backer counts, team data, clients, budgets, results, article history, contact data, exact palette/fonts/art and REDDEVS/Framer chrome;
- regression and validator coverage for the Nexira full-site profile, both promoted patterns and the upgraded Cinematic Game anchor.

The router remains at 16 modules and the baseline set remains at 11 skins; this release adds deeper game-studio intelligence without increasing routing complexity.

Version 3.19 deep-audits the entire OrbAI Framer AI-agency template and upgrades Clean Product Light from a curated baseline into an audited template-backed scaffold without adding a twelfth skin.

Version 3.19 adds:

- references/design-intelligence/sites/orbai-template.framer.website.md with explicit **8/8 sitemap coverage**: home, contact, privacy, changelog, and all 4 changelog detail pages, plus separately quarantined /404 utility coverage;
- sitemap/search-index/internal-link parity checks confirming the eight public routes and no additional same-origin public routes;
- source/runtime evidence for Framer 3db8496, Satoshi/Inter typography roles, the #f5f5f5 light shell, #814fff accent, #04070d deep accent, 810px/1200px breakpoints, Framer Motion runtime, and the shared aMPvRVYHFQxBoB0v2qyJln83jI.mp4 ambient hero/footer media;
- **Commercial Core + Trust Satellites** for focused B2B/service sites whose benefits, features, services, process, projects, pricing, comparison, team and FAQ fit one commercial page while contact/privacy/changelog remain independent support routes;
- **Pricing-to-Comparison Bridge** for placing defensible differentiation directly after plans/packaging while prohibiting vague or invented "Us vs Others" superiority claims;
- a substantial upgrade to clean-product-light.md with explicit commercial-core grammar, benefits/features/service bento guidance, service process, proof, pricing, comparison, changelog/privacy/contact satellites, ambient-media boundaries, responsive contracts and stronger template-convergence safeguards;
- OrbAI classified as an audited Framer template reference and linked through the skin/reference landscape while its placeholder clients, project metrics, team, pricing, release history, legal copy, exact palette/fonts/media and Framer chrome are quarantined from transferable truth;
- regression and validator coverage for the OrbAI full-site profile, both promoted patterns and the upgraded Clean Product Light anchor.

The router remains at 16 modules and the baseline set remains at 11 skins; this release improves deterministic light product/service execution without increasing routing complexity.

Version 3.18 deep-audits the entire Nudge Folio Framer portfolio template and strengthens the existing Creative Agency Editorial skin instead of adding a redundant twelfth skin.

Version 3.18 adds:

- references/design-intelligence/sites/nudge-folio.framer.website.md with explicit **19/19 sitemap coverage**: seven primary routes, all 8 blog detail pages, and all 4 case-study detail pages;
- sitemap/search-index/internal-link parity checks confirming there are no additional same-origin public routes outside the audited set;
- source/runtime evidence for Framer bc64f0a, Flux Variable, Inter Display, DM Mono, Just Me Again Down Here, the neutral + saturated accent token family, 810px/1200px breakpoints, lenis runtime state, GSAP/Draggable code, sticky portfolio stages, persistent context rails, and the viewport-locked draggable playground;
- **Reflective Case Study Arc** for truthful portfolio narratives that include problem, intervention, result, constraints/tradeoffs, what would change next, and learning;
- **Persistent Context Rail** for long editorial/portfolio routes that benefit from sticky local navigation or metadata without sacrificing mobile reading;
- **Experimental Surface Isolation** so high-risk drag/collage/cursor interaction can express personality inside a bounded playground route without contaminating case studies, articles, contact, or conversion;
- a substantial upgrade to creative-agency-editorial.md, now using both Refokus and Nudge Folio as complementary audited anchors: Refokus for high-ambition agency/world-building and Nudge for deterministic portfolio execution;
- Nudge classified as both an audited portfolio/experiential reference and an audited template-commodity reference, with BUY NUDGE / Framer vendor identity quarantined from transferable DNA;
- regression and validator coverage for the Nudge full-site profile, all three promoted patterns, and the upgraded Creative Agency Editorial anchor.

The router remains at 16 modules and the baseline set remains at 11 skins; this release adds deeper portfolio intelligence without increasing routing complexity.

Version 3.17 deep-audits the entire Powder Framer template and uses the findings to strengthen the existing Premium SaaS Dark skin instead of adding a redundant twelfth skin.

Version 3.17 adds:

- references/design-intelligence/sites/powder.framer.website.md with explicit **21/21 sitemap coverage**: home, about, blog, changelog, get-started, pricing, three legal routes, /404, /page, and all 10 blog detail pages;
- sitemap/search-index/internal-link cross-checking so full-site coverage includes public utility/template residue without giving every route equal design weight;
- source-confirmed Framer a050651 typography/tokens and breakpoint evidence including Inter Variable, Inter Display, Fragment Mono, 810px/1280px primary branches, and a 1024px utility/conversion branch;
- **Conversation-to-Action Proof** for AI-agent products that need to prove intent -> contextual answer -> source/trust -> artifact/action -> next state rather than stopping at a chat transcript;
- **Template Residue Quarantine** so 404s, component/demo pages, editor/remix controls, placeholder CMS content, and vendor chrome stay in the coverage manifest without polluting core Design DNA;
- audited **Sticky Capability Stack** guidance from Powder's desktop runtime, including responsive release on mobile rather than forcing the wide sticky stage into a narrow viewport;
- a substantial upgrade to premium-saas-dark.md, which now uses Powder as a full-site audited template anchor and includes route-system grammar, conversation/action proof, sticky-narrative rules, responsive contracts, residue quarantine, stronger anti-template guardrails, and QA;
- Powder classified as an audited template-commodity reference while preserving the exact 11-skin set to avoid near-duplicate dark AI skins;
- regression and validator coverage for the Powder profile, the two promoted design-intelligence patterns, and the upgraded Premium SaaS Dark evidence anchor.

The router remains at 16 modules and the baseline set remains at 11 skins; this release improves template-grounded execution quality without expanding routing complexity.

Version 3.16 deep-audits the entire NovaOS Framer site rather than sampling a landing page, covering all 23 public sitemap routes and turning the template into a guarded enterprise-AI skin rather than a clone recipe.

Version 3.16 adds:

- references/design-intelligence/sites/novaos.framer.website.md with explicit **23/23 sitemap coverage**: 11 top-level routes, all 6 career detail pages, and all 6 blog article pages;
- source-confirmed Framer 95da0c7 breakpoints, design tokens, font roles, Framer appear behavior, and the custom Lenis 1.3.26 lifecycle including reduced-motion and scroll-lock coordination;
- **Operational Pipeline Storytelling** for products best explained as model/engine -> context/data -> agent/workspace -> tools -> workflow -> observable output;
- **Proof Surface Cropping** so mobile marketing proof can preserve readable UI scale inside a clipped viewport without document-level horizontal overflow;
- **Credibility Through Route Ecosystem** so enterprise trust is reinforced across integrations, pricing, company, technical content, legal/security, careers, contact/demo, and FAQ routes;
- enterprise-ai-platform-light.md as the eleventh baseline skin, using NovaOS as a full-site audited template anchor while keeping the Template Archetype Firewall active;
- explicit classification of NovaOS as an audited template-commodity/product-precision reference because the live site exposes a Get This Template action;
- regression and validator coverage for the NovaOS profile, three promoted patterns, and exact 11-skin set.

The router remains at 16 modules; this release expands whole-site design intelligence and template-safe scaffolding without adding an always-on module.

Version 3.15 deep-audits the entire Tokenmeter site rather than a single page, covering all 26 public sitemap URLs and turning its data-reference system into reusable design intelligence.

Version 3.15 adds:

- references/design-intelligence/sites/tokenmeter.info.md with explicit **26/26 sitemap coverage**: home, Compare, Directory, Methodology, Glossary, FAQ, and all 20 provider detail pages;
- site-wide route-family analysis showing how one dataset is projected at different densities across summary, directory, comparison, detail, methodology, glossary, FAQ, and machine-readable surfaces;
- **Confidence as Interface** so uncertain/editorial data carries visible confidence, provenance, freshness, and methodology context rather than hiding caveats in footer copy;
- **Route-Family Density Ladder** for selecting low-, medium-, high-, and one-record information density by user task while preserving one system grammar;
- **Contain Horizontal Density, Don't Crush It** for readable comparison tables that own internal horizontal overflow without destabilizing the outer document;
- **Human + Machine Surface Parity** for keeping sitemap, robots, llms.txt, structured metadata, route names, scope, and confidence caveats aligned with the human-facing product;
- evidence-first-data-directory.md as the tenth baseline skin, using Tokenmeter's full-site audit as an evidence anchor for directories, comparison engines, benchmarks, catalogs, and technical reference products;
- regression and validator coverage for the Tokenmeter profile, four promoted patterns, full 10-skin set, and synchronized package metadata.

The router remains at 16 modules; this release expands site-wide reference intelligence without adding an always-on module.

Version 3.14 deep-audits Rockstar Games VI and adds an evidence-anchored Open-World Cinematic Launch skin for fictional-world/franchise campaigns.

Version 3.14 adds:

- a Rockstar Games VI site profile audited at desktop and 390x844 mobile, covering canvas/media state, custom typography, Next.js server payload, tracked campaign chapters, responsive media branches, and accessibility caveats;
- **Aspect-Ratio Art Direction** so image-led hero compositions can select portrait, landscape, and ultra-wide assets/crops instead of relying on width breakpoints alone;
- **World-Led Campaign Chapters** so cinematic pages assign one clear campaign job to hero, trailer, offer, story/world, exploration, news, and outro regions;
- an Open-World Cinematic Launch baseline skin with Trailer as User-Invoked Proof, Back-of-Box Chapter, media-cost ladder, responsive world payload, and anti-clone guardrails;
- GTA VI promoted from candidate reference to audited game/cinematic evidence while preserving the rule that proprietary ArtDeco typography, shard art, exact palette, logos, copy, and campaign assets must not transfer;
- validator and regression coverage for the third audited site profile and the exact nine-skin baseline set.

The router remains at 16 modules; this release expands design intelligence and skins without adding an always-on module.

Version 3.13 adds **Adaptive Capability Routing** so the plugin no longer depends on a model correctly judging whether it is "strong" or "weak." Execution freedom is selected from observable task and render evidence.

Version 3.13 adds:

- three execution modes: **LOCKED**, **GUIDED**, and **BESPOKE**;
- **GUIDED as the default** when capability evidence is inconclusive;
- a **Task Complexity Score** that increases the evidence/QA bar without automatically granting BESPOKE freedom;
- an eight-primitive **Design Preflight** covering typography, spacing, surfaces, composition, responsive transformation, signature mechanism, motion ownership, and proof/content strategy;
- optional runtime capability metadata as a supporting signal only ? never the sole authority and never a substitute for output evidence;
- an explicit ban on using model self-assessment or model-name prestige to enter BESPOKE;
- rendered-QA feedback: two or more material coherence failures downgrade `BESPOKE -> GUIDED` or `GUIDED -> LOCKED`, while escalation requires coherent representative desktop/mobile evidence plus a fully resolved contract;
- skin-pack routing updated from low/high-capability labels to the adaptive execution modes, while preserving Skin Lock, Controlled Mutation, and the Template Archetype Firewall.

The mode describes **execution scaffolding**, not visual ambition: a visually bespoke result can still use GUIDED or LOCKED internals when that produces more coherent output.

Version 3.12 added **Baseline Skin Packs** so drift-prone or constrained executions can start from a coherent visual system instead of inventing typography, spacing, radius, surfaces, motion and composition simultaneously.

Version 3.12 adds:

- eight deterministic skin scaffolds: Premium SaaS Dark, Clean Product Light, Developer Infrastructure, Creative Agency Editorial, Luxury Editorial, Bento Product, Cinematic Game, and Premium Ecommerce;
- **Skin Lock** for typography roles, surface hierarchy, radius family, spacing rhythm, action treatment and motion language;
- **Controlled Mutation** slots for brand accent, hero composition, imagery, product proof, signature interaction and narrative order;
- root-level baseline skin routing with the rule `1 archetype + 1 skin + 1 composition grammar` (superseded in 3.13 by Adaptive Capability Routing);
- per-skin Token Scaffold, Composition Grammar, Responsive Contract, Anti-Template Guard and QA Rubric;
- Resend as the audited evidence anchor for `developer-infra.md`, carrying Product Evidence Before Feature Claims, Code as Product Proof and Responsive Fidelity Substitution;
- Refokus as the audited evidence anchor for `creative-agency-editorial.md`, carrying one-signature-stage allocation, quiet-shell/project-world contrast, editorial case-study grammar and Responsive Brand Payload;
- validator and regression coverage that pins the exact eight-skin baseline set.

The Template Archetype Firewall remains active: a skin is a safe baseline, not permission to ship a generic clone.

Version 3.11 turns the broad inspiration research backlog into a safer reference-selection system instead of treating every admired website as audited design evidence.

Version 3.11 adds four design-intelligence capabilities:

- **Reference Landscape Routing** ? classify potential teachers as product precision, experiential/agency, luxury/editorial, game/cinematic, developer product, or template commodity before deep audit;
- **Template Archetype Firewall** ? detect convergence on repeated SaaS/AI/devtool/template grammar and require structural differentiation instead of cosmetic reskinning;
- **Breadth-to-Depth Funnel** ? move from broad discovery to archetype comparison, a 1?3 source shortlist, deep audit, Design DNA, and selective pattern promotion;
- **Game/Experiential Audit Lens** ? inspect HUD/content hierarchy, world continuity, diegetic UI, media choreography, chapter transitions, input grammar, audio dependency, sensory density, performance fallback, and mobile reduction before routing implementation to `experience-engineering`/`scroll-world` when appropriate.

The new `references/design-intelligence/reference-landscape.md` records representative candidate references and common template archetypes while explicitly enforcing **Candidate, Not Evidence**. Refokus and Resend remain the only audited site profiles at this stage.

The router remains at 16 modules; this version improves reference selection and anti-template reasoning without adding another always-on module.

Version 3.10 deepens the reference-derived design intelligence system with Resend as the second independently audited site profile and promotes several durable developer-product patterns into reusable guidance.

Version 3.10 adds:

- `references/design-intelligence/sites/resend.com.md`, audited from live desktop/mobile rendering, accessibility structure, computed typography, shipped client source, runtime media state, and network evidence;
- **Product Evidence Before Feature Claims** so mature software can make authentic product state, logs, editors, analytics, and implementation evidence the main marketing visual instead of decorative mockups;
- **Code as Product Proof** for developer products where the shortest truthful integration path is itself persuasive evidence;
- **Responsive Fidelity Substitution**, separating the perceptual/brand job from the renderer technology so a richer desktop signature can become a cheaper equivalent on mobile;
- Resend-specific lessons around functional ecosystem tabs, persisted SDK/framework context, semantic accent budgets, pre-rendered 3D chapter punctuation, and developer trust ladders;
- cross-site synthesis with Refokus: allocate ambition asymmetrically, preserve type-role contrast and responsive brand payload, but route the proof mechanism to the product rather than averaging both references into one style.

The router remains at 16 modules; design-intelligence grows through selective profiles and promoted patterns rather than adding another always-on module.

Version 3.9 adds **reference-derived design intelligence** so strong live websites and inspectable source can improve future work without turning the skill into a clone library.

Version 3.9 adds:

- a routed `design-intelligence` module for inspiration distillation distinct from faithful reference recreation;
- a reusable Design DNA schema covering composition, typography, color/material, media/rendering, motion, input grammar, narrative/proof, responsive behavior, performance and accessibility;
- Observed / Source-confirmed / Inferred evidence confidence so technical claims are not guessed from pixels;
- Distill, Don't Clone, Pattern Promotion and Adopt / Adapt / Avoid transfer contracts;
- Bounded Immersive Rendering and Responsive Brand Payload patterns for high-craft experiences;
- the first deep site profile, `references/design-intelligence/sites/refokus.com.md`, distilled from live desktop/mobile rendering plus runtime/source inspection;
- Refokus-derived regression lessons around one signature stage, motion-as-focus, quiet-shell/vivid-project-world contrast, editorial case studies, proof sequencing, optional sound, and bounded WebGL cost.

The router now contains 16 modules. Site profiles remain selective references and are not loaded by default.

The previous base was a unified UI/UX Pro Max facade with a local frontend-design module. Version 3.x keeps that useful knowledge and adds a routing/orchestration layer informed by several public frontend-agent workflows.

Version 3.7 hardens **cross-system experience synchronization** after rerunning the Cosmos prompt with the latest skill and QA-ing the rebuilt production experience.

Version 3.7 adds:

- **One Progress Domain** — layout, director, HUD, chapter navigation, audio and final-mode semantics must share or explicitly calibrate one story-progress mapping;
- **Timeline ↔ Layout Synchronization** — pure timeline tests no longer count as sufficient when actual DOM geometry owns scroll distance;
- **Navigation Parity QA** — natural scroll, rail jumps and deep-link/restoration paths must converge on the same visible semantic state;
- **Cross-channel State QA** — narrative copy, HUD, navigation, world, audio and chrome must describe one coherent moment;
- **Spec-to-Implementation Traceability** — flagship Experience Spec promises require an implementation owner and observable evidence;
- **Responsive Accessibility Snapshot** — accessibility names/roles are rechecked after breakpoint CSS changes presentation;
- a clean-context recheck after synthetic diagnostics so test instrumentation is not misreported as a product defect;
- a permanent Cosmos regression lesson: `HUD says chapter X while visible narrative says chapter Y = failure`.

No new module was added; the registry remains 15 modules.

Version 3.6 adds a dedicated **`frontend-qa` director** so substantial frontend work finishes with evidence-driven QA rather than only a screenshot pass.

The QA synthesis combines previously reviewed OpenAI/Anthropic/Yutori browser-visual workflows with fresh deep reads of Daymade Frontend Visual QA, Practica Frontend Testing Skill, a Playwright pixel-regression skill, and TestDino's Playwright QA guidance.

Version 3.6 adds:

- QA depth routing: **QA-1 targeted patch / QA-2 standard feature / QA-3 release or flagship**;
- canonical target/state/role/data/viewport proof before any verdict;
- one shared QA inventory derived from requirements, implemented behavior and handoff claims;
- an evidence ladder separating real recipient surfaces, browser automation, mechanical sweeps and source reasoning;
- functional journey QA through real user input, including reversible controls, recovery and recipient outputs;
- `visual-qa` as a dedicated rendered/pixel/reference specialist rather than the entire QA program;
- accessibility baseline: semantic locators, automated scans when available, keyboard/focus, dynamic-state checks and ARIA snapshots for high-value widgets;
- performance QA only when risk justifies it, including throttling/adaptive-quality checks for heavy experiences;
- intentional visual-regression baseline governance — no blind snapshot updates;
- flake detection, trace-driven root-cause diagnosis and optional mutation sanity checks for critical tests;
- a short exploratory/tired-user pass plus VERIFIED / PARTIAL / BLOCKED signoff.

The local QA target is the observable discipline associated with strong coding agents; it does not claim access to proprietary hidden QA harnesses.

Version 3.5 remains the authored-world / experience-engineering baseline, and `scroll-world` remains the specialist for pre-rendered cinematic journeys.

The architecture still favors better routing over simply stacking more rules:

- marketing pages get stronger art direction;
- dashboards get more product/UX discipline;
- screenshot/image work uses an evidence-first path;
- motion is opt-in and calibrated;
- substantial frontend work ends with browser screenshot QA when tools are available.

## Architecture

~~~text
elite-frontend-design/
├── plugin.json
├── .codex-plugin/
│   └── plugin.json
├── README.md
├── CHANGELOG.md
├── skills/
│   └── elite-frontend-design/
│       ├── SKILL.md
│       ├── skill.json
│       ├── agents/
│       │   └── openai.yaml
│       ├── scripts/
│       │   └── ui_ux_search.py
│       └── references/
│           ├── index.md
│           ├── source-map.md
│           └── modules/
│               └── ... 15 routed modules
├── scripts/
│   ├── validate_skill.py
│   └── package_plugin.py
└── tests/
    └── test_structure.py
~~~

## Core idea

Do not load every module.

The skill first classifies the task and sets three dials:

- VARIANCE — conservative → experimental;
- MOTION — static → cinematic;
- DENSITY — sparse → operational.

Then it chooses the smallest module set that covers the job.

Example profiles:

~~~text
Landing page
  elite-core
  + frontend-design
  + frontend-qa
  + motion-direction only if justified

Dashboard
  elite-core
  + ui-ux-pro-max
  + frontend-qa
  + ui-styling when implementation detail is needed

Visual/reference-only audit
  reference-first
  + visual-qa

High-ambition live 3D / WebGL experience
  elite-core
  + experience-engineering
  + frontend-qa

Scroll-scrubbed camera world
  elite-core
  + scroll-world
  + frontend-qa
  + reference-first only when recreating a known reference
~~~

## Why the visual loop matters

A frontend can build successfully, pass DOM assertions, and still look visibly wrong.

The default substantial workflow is:

~~~text
GROUND
→ ART DIRECT
→ CONTRACT
→ IMPLEMENT
→ QA CONTRACT / INVENTORY
→ FUNCTIONAL JOURNEY
→ NAVIGATION / CROSS-CHANNEL PARITY WHEN SYNCHRONIZED
→ RENDER / SCREENSHOT
→ VISUAL CRITIQUE
→ RESPONSIVE / ACCESSIBILITY
→ PERFORMANCE / REGRESSION WHEN IN SCOPE
→ EXPLORE / RE-RUN
→ VERIFIED | PARTIAL | BLOCKED
~~~

## UI/UX search

The bundled UI/UX Pro Max database remains available through the stable wrapper:

~~~bash
python "<plugin-root>/skills/elite-frontend-design/scripts/ui_ux_search.py" "fintech operations dashboard" --design-system -p "Ops Console"
python "<plugin-root>/skills/elite-frontend-design/scripts/ui_ux_search.py" "focus not obscured" --domain ux
python "<plugin-root>/skills/elite-frontend-design/scripts/ui_ux_search.py" "table overflow responsive" --stack html-tailwind
~~~

## Design principles

The root skill intentionally balances three forces:

1. concept / distinctiveness — the interface should not look like a generic model default;
2. practical product judgment — workflow clarity beats spectacle on tool-like surfaces;
3. rendered evidence — screenshots and interaction testing settle questions that source code cannot.

## Sources

The local synthesis was informed by public work from Anthropic frontend-design/webapp-testing, OpenAI frontend and Playwright guidance, Codex frontend-design port, Image-first Frontend, UI/UX Pro Max, Superdesign, Meng To Skills, Taste Skill, multiple Frontend Visual QA projects, Practica Frontend Testing, Playwright QA/visual-regression guidance, and oso95/scroll-world.


See references/source-map.md for upstream source decisions and references/source-snapshots.md for pinned review commits. Historical QA lessons remain encoded in the modules.

The external projects are inspirations/references; this folder does not require their CLIs or hosted services.

## Validation

~~~bash
python scripts/validate_skill.py
python -m unittest discover -s tests -p "test_*.py"
python scripts/package_plugin.py
~~~

Validation checks:
- portable `plugin.json` and Codex compatibility manifest consistency;
- ChatGPT/Codex skill interface and product policy metadata;
- manifest/module registry consistency;
- exactly one packaged skill entrypoint;
- no nested SKILL.md;
- required orchestration modules;
- source-map documentation;
- bundled UI/UX search engine;
- distilled-web-toolkit datasets, 11 standardized specs and search facade;
- plugin, semantic and assembly version sync;
- root skill name and current version documentation.

## Existing bundled modules

The existing UI/UX Pro Max-derived modules and their internal data/scripts are retained to avoid throwing away useful design intelligence. The local Distilled Web Toolkit adds audited website-derived patterns with provenance and its own search facade. The orchestration does not copy every module/profile into one prompt; it routes to the smallest useful subset.

## License / provenance

The local assembly remains MIT as declared in skill.json. Imported modules retain their own provenance inside the bundle. Review references/source-map.md before redistributing derived upstream content.
