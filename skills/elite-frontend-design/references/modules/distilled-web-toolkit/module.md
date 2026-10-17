---
name: distilled-web-toolkit
description: "Searchable audited design recommendation toolkit distilled from 25 live references. Use for provenance-backed style, color, typography, component, route-system, proof, motion, responsive, interaction, performance, UX, and QA retrieval plus audited design-system synthesis."
---

# Distilled Web Toolkit

This module turns audited live websites into a searchable pattern library. It is complementary to `design-intelligence` and `ui-ux-pro-max`: `ui-ux-pro-max` provides broad UI/UX guidance; this toolkit provides **reference-derived web patterns with explicit provenance**.

## Audited Pattern Retrieval

Use the bundled search tool:

```bash
python "<skill-root>/scripts/distilled_toolkit_search.py" "<query>" [--domain <domain>] [--site <site-id>] [--archetype <archetype>] [-n <count>] [--json]
```

Search domains:
- `layout`
- `route-system`
- `proof`
- `motion`
- `media`
- `responsive`
- `interaction`
- `performance`
- `typography`
- `navigation`
- `qa`
- `style`
- `color`
- `component`
- `ux`

Use one dominant intent per search. Good examples:
- `integration setup proof --domain proof`
- `sticky case study rail --site nudge-folio`
- `particle scroll narrative --site ten-billion-years`
- `mobile crop product UI --domain responsive`

## Audited Design-System Retrieval

The toolkit also exposes a higher-level recommendation mode inspired by the useful retrieval shape of `ui-ux-pro-max`, while keeping every recommendation tied to an audited website:

```bash
python "<skill-root>/scripts/distilled_toolkit_search.py" "<product/style query>" --design-system [--site <site-id>] [--archetype <archetype>] [--variance 1-10] [--motion 1-10] [--density 1-10] [--json]
```

This mode returns one coherent audited source profile with:

- style/composition and audited variance-motion-density dials;
- semantic color strategy and transfer rules;
- typography roles plus desktop-to-mobile scale behavior;
- component recipes with anatomy, interaction, responsive and accessibility contracts;
- supporting route/pattern/motion/responsive recipes;
- UX watch rules and failure modes.

Treat this as **reference-derived design scaffolding**, not a skin copier. Exact source identity, proprietary fonts/assets, brand copy, claims, metrics, artwork and literal palettes do not transfer automatically.

## Provenance Before Prescription

Every result must identify one or more audited source sites. Treat provenance as evidence, not authority.

Rules:
1. Read the matching pattern record.
2. Read the relevant standardized site spec when the pattern materially affects composition or behavior.
3. If current live truth matters, compare the 2026-10-07 live snapshot with the historical audited profile.
4. Transfer the mechanism, not the brand identity, copy, proprietary media, exact typography, fake metrics, template vendor chrome, or one-off implementation details.
5. Never combine patterns solely because they are individually impressive.

## Pattern Composition Contract

Compose a new design from:

**1 archetype + 1 primary composition grammar + up to 3 supporting patterns + 1 responsive strategy + 1 proof strategy**

Only add a motion/media pattern when it has a clear narrative or interaction job.

Before implementation, write:
- product/job fit;
- chosen archetype;
- primary composition grammar;
- selected pattern IDs and provenance;
- what will be adapted;
- what must not transfer;
- responsive substitution;
- QA/failure-mode checks.

Do not average visual languages from unrelated references.

## Live Snapshot vs Audited Profile

`data/live-audit-2026-10-07.csv` is a cross-site runtime snapshot collected with Chrome using standardized desktop/mobile resize attempts; the CSV records the viewport actually observed when the browser imposed a different minimum. The existing `references/design-intelligence/sites/*.md` profiles remain the deeper historical audit.

When they differ:
- current live topology/runtime wins for claims about the site **now**;
- historical profile remains valid evidence for previously audited mechanisms;
- the toolkit must not silently rewrite historical route counts;
- record the difference as drift or evolution.

## Dataset Map

- `data/sites.csv` ? 25 reference identities and archetypes.
- `data/live-audit-2026-10-07.csv` ? standardized live desktop/mobile snapshot.
- `data/patterns.csv` ? reusable audited patterns.
- `data/route-recipes.csv` ? route and route-family structures.
- `data/motion-recipes.csv` ? motion/media choreography patterns.
- `data/responsive-recipes.csv` ? responsive substitutions and transformations.
- `data/anti-patterns.csv` ? failure modes and residue to avoid.
- `data/design-profiles.csv` ? 25 audited style/product profiles with dials, fit, performance and accessibility watches.
- `data/color-systems.csv` ? semantic color-role strategies with transfer constraints.
- `data/typography-systems.csv` ? audited display/heading/body/utility type-role systems and responsive scales.
- `data/component-recipes.csv` ? Component Recipes with job, anatomy, interaction, responsive and accessibility contracts.
- `data/ux-guidelines.csv` ? site-derived UX rules expressed as do/don't guidance.
- `data/design-primitives-live-2026-10-07.csv` ? live desktop/mobile primitive ledger for the 25-site corpus.
- `specs/*.md` ? one standardized implementation-oriented spec per audited site.

## Retrieval Workflow

1. Determine page/product archetype and design dials.
2. Use `--design-system` when a coherent audited style/color/type/component scaffold is useful; otherwise search one domain directly.
3. Narrow by `--domain`, `--site`, or `--archetype` when results are broad.
4. Read the matching site spec for context and provenance.
5. Select a small pattern set under the Pattern Composition Contract.
6. Materialize decisions into the design contract; mutate source-derived tokens/identity rather than copying them.
7. Use `frontend-qa` for rendered, route-family, accessibility, responsive, and data-binding verification.

## Evidence Strength

`high` ? repeated or runtime/source-confirmed mechanism.
`medium` ? strongly observed but less structurally verified.
`contextual` ? useful only within a narrow archetype or campaign.

Do not promote contextual evidence into a universal default.

## Whole-Site Route Census Evidence

For Resend, the audit from 2026-10-08 recurses 11 child sitemaps into 1,015 declared routes. The per-route metadata inventory is stored at data/resend-route-inventory-2026-10-08.csv (1,014 HTTP 200 and /shop HTTP 404 in that dated snapshot).

Use route-job recipes alongside aesthetic patterns: products/features, integrations, migration, docs with internal scroll, changelog, blog, customer proof, handbook and people. The inventory is a full HTTP census, not a claim of detailed interaction tests on all 1,015 routes.

## Battlez whole-site game commerce corpus

The 2026-10-08 audit verified 75/75 declared sitemap URLs: 53 store detail records, 4 game-category destinations, 6 news details, 3 editorial archives and multiple core/utility routes. 74 returned 200 and the purpose-built /404 returned 404. Full inventory: data/battlez-route-inventory-2026-10-08.csv.

Battlez contributes hybrid game-marketing to storefront conversion, linkable category shopping, product purchase + lore, membership vs one-off checkout separation and public genre editorial. The crucial failure mode is cross-vertical CMS fixture leakage: the template displays toys, cosmetics, home, drones and sports goods as game products.

This full HTTP census is not evidence that every product interaction was completed. Zero outer mobile overflow was inspected across representative routes.

## Nouva Full-Site SaaS Conversion and Auth Evidence

The Nouva audit (2026-10-08) covers 8/8 sitemap URLs (HTTP 200) and an extra footer-linked /404 (HTTP 404), with nine rendered desktop/mobile route states. Inventory: data/nouva-route-inventory-2026-10-08.csv.

The differentiator is **marketing-to-contact conversion plus a separate branded passwordless auth quartet** (sign-up, sign-in, OTP and account). Homepage metrics are scroll-triggered and initially render zero placeholders. All pricing CTA routes lead to contact. The Yearly 20% billing selector was not observed changing prices after a sampled click; preserve this as a QA obligation, not a functioning design feature.

Template claims/metrics, FrameAuth backend security, actual email delivery and signup or contact submission are not verified by this UI audit. Preserve transferable route grammar and accessible semantics only.

## Echoes of Mars Three-Mode Breakpoint Re-Audit

The 2026-10-08 Chrome runtime re-audit of the original 1-route, 13-chapter Echoes of Mars campaign records exact survey layout breakpoints in data/echoes-survey-breakpoints-2026-10-08.csv. A horizontal track switches from vertical <=809px, to compact 4280px at 810–1199px, to 5320px at >=1200px. prefers-reduced-motion: reduce still gives the full sticky/horizontal transform, a documented source accessibility shortfall. Implement a static ordered escape rather than assuming motion settings are automatically honored. No new site, route or skin was created.

## Ten Billion Years Runtime Census — 2026-10-08

One authored root route, nine chapter sections, a scroll-driven HUD/world and endcap replay, not nine pages. All eight sampled public paths/statuses appear in data/cosmos-route-census-2026-10-08.csv; time-scoped HUD chapter/year samples and mobile/reduced-motion checkpoints are stored in data/cosmos-runtime-checkpoints-2026-10-08.csv. Root is HTTP 200, while sitemap/robots and nonroot candidate paths return HTTP 404. The browser confirms silent audio choice and interactive Galaxy chapter jump. New accessibility guidance covers CSS-only active chapter states without aria-current. Historical source-derived particle tiers are not new GPU measurements.


## Fizens Finance SaaS Whole-Site System

Audit (2026-10-08): 43/43 declared sitemap routes returned HTTP 200: home+9 core marketing/utility, 2 legal, 9 integrations, 8 people, 4 jobs and 10 editorial. Four extra paths returned HTTP 404. Inspected 17 desktop and 15 mobile representative route states. Inventory: data/fizens-route-inventory-2026-10-08.csv.

Reusable logic includes financial confidence supported by dashboard evidence, partner directory -> scoped integration detail, related finance apps -> verified download target, tier pricing and feature matrix, financial editorial as topical community continuity, team/careers content integrity and separating Framer template-vendor checkout from end-user fintech conversion.

The most severe source QA failure: all four job detail URLs display the same Product Designer H1 despite correct differing titles. A separate SEO problem affects 21 of 43 declared URLs with one generic template document title. Neither real finance APIs, security claims, store apps nor billing transactions were independently verified.

## Tobi Mallory Quest-to-Contact Re-Audit — 2026-10-08

The full original Tobi Mallory route taxonomy was reconfirmed: 30 declared sitemap paths, 29 HTTP 200 content and an authored /404 with actual HTTP 404 on both browsed and advertised canonical hosts. All 30 canonicals on tobi-mallory.framer.website point to eternal-fade-087901.framer.app, and the public sitemap incorrectly includes /404. Representative Chrome rendered 15 desktop and 15 mobile routes with no positive horizontal document overflow. Saved in data/tobi-dual-host-routes-2026-10-08.csv and data/tobi-rendered-states-2026-10-08.csv.

New conversion recipe: Quest-to-Contact Intent Continuity. Chrome clicked all three detail CTA links: Identity -> Contact preselect Identity (correct), Website -> Contact preselect Identity (wrong), Motion -> Contact preselect Identity (wrong). Implement query/route context propagation and matching form select. See data/tobi-quest-contact-state-2026-10-08.csv. Six icon-only type links have aria-label and are a positive semantics example, not a broken control.

## BridgeMind Whole-Site Native Agent-Workspace System — 2026-10-09

143 sitemap URLs on www.bridgemind.ai plus 10 companion docs.bridgemind.ai routes, **153/153 declared HTTP 200**. Additional 12 account/redirect/invalid probes yielded 7 HTTP 200 and 5 HTTP 404. The audit includes 120 individual changelog versions, eight blog details, product/pricing/voice/spatial marketing, community, developer, legal, branded non-sitemap account screens and ten distinct documentation paths. A 165-row route census, same-ecosystem link graph, 46 Playwright desktop/mobile rendered states, and 13 interaction probes are saved in data/bridgemind-*-2026-10-09.csv.

Reusable lessons: **Operational Simulator with Authority Boundary**, three workflow modes requiring distinct proof, simulated voice/mic privacy truth, local/cloud speech model data-flow, long versioned release directories, credits versus BYO provider subscription expenses, and cross-host docs/platform availability consistency. Marketing and docs disagree at audit time over Windows/Linux support. The website's BridgeVerse 3D product stills and homepage canvas nodes do not by themselves establish live marketing WebGL. No real coding agent, mic, checkout, or account was tested. See specs/bridgemind.md and references/design-intelligence/sites/bridgemind.ai.md.

## Arpeggio Whole-Site Editorial Agency + Membership — 2026-10-09

Audited **22/22 sitemap pages HTTP 200**, seven Work case studies, seven Journal long reads, three legal routes, full home/about/contact/work/journal journey; eight extra missing/404 probes were HTTP 404, including linked /404 and /pricing (Membership is homepage #pricing). Evidence in data/arpeggio-route-inventory-2026-10-09.csv (30 routes), arpeggio-internal-links-2026-10-09.csv, arpeggio-rendered-states-2026-10-09.csv (46 Chromium 1440/390 states with zero document overflow), arpeggio-interaction-probes-2026-10-09.csv (10 bounded checks).

Lessons: one expressive editorial typography stage followed by genuine case-story argument; Work archive search/filter results require functional checks; two-tier recurring service offer can live as homepage anchor; scope/budget-qualified Contact; credited results not template fixture metrics; strict vendor-template versus real agency boundary. Some source controls had inconclusive search/tier state, and source media node duplication cannot be equated with network cost. Existing creative-agency-editorial skin retained; deep profile at references/design-intelligence/sites/arpeggio.framer.website.md and spec at specs/arpeggio.md.

## Spector Entire-Site Creative Agency, Canvas and Lab — 2026-10-09

Audited **19/19 official sitemap routes HTTP 200** covering agency home/positional About/scope-qualified Contact, six long-form project details, five Lab articles, two archives and three legal routes. Ten additional HTTP 404 probes include demo /404 and a malformed /instagram.com route referenced across all 19 official pages. The indexed /projects archive links **only 4/6 cases**, and /lab links **only 4/5 articles**; auditing sitemap independently prevents omissions. All 19+404 routes rendered at 1440x900 and 390x844 = **40 Chromium states, zero positive outer overflow**; **11 bounded UI probes**, 29-route inventory and link graph in data/spector-*-2026-10-09.csv.

The transferable signature is near-black oversized Plus Jakarta Sans on white, editorial project stills, a six-item 3D client carousel, six service roles, a showreel and bounded canvas motion (8 sampled home desktop canvases, 10 mobile; WebGL unconfirmed), scoped homepage #pricing and mandatory Budget/Name/Email/Message Contact. Special QA: source Lab article H1 incorrectly marks MORE LABS and case headline is H3, Contact has no H1, social links point to platform roots/vendor alias, fake recognition/client copy cannot become production proof. Reuse creative-agency-editorial skin; source detail at references/design-intelligence/sites/spector.framer.website.md and specs/spector.md.

## Fabrica — Complete Dark Digital Agency Site (2026-10-11)

Full **20/20 sitemap page HTTP 200** census: agency homepage + Studio + Projects/6 detail cases + Blog/7 articles + Contact + two legal. Ten additional paths HTTP 404, including /404, /about, /pricing and /work. All 20 real routes plus /404 rendered at 1440x900 and 390x844 = **42 browser states without positive outer overflow**. Proof files: data/fabrica-route-inventory-2026-10-11.csv (30 paths), fabrica-internal-links-2026-10-11.csv, fabrica-rendered-states-2026-10-11.csv, fabrica-interaction-probes-2026-10-11.csv (11 bounded checks).

Notable visual language: dark rgb(18,18,18), Inter inner-page 148px/64px H1, home giant secondary headline 144px/62px, six photo case stories, four media-led service rows, two video DOM nodes and zero canvas. Project filter **works in sampled states** (Search Boltshift 6->1, Web design category 6->3), seven article permalinks discoverable from Blog. On-home Per project/Monthly pricing is shown but tier click/price changes not confirmed. Contact has **Name and Email only**, validated natively but not submitted. Source QA: article about color psychology oddly includes Speed/SEO headings, projects archive lacks H1, all project/blog/legal title tags end with "My Framer Site", and source Framer creator store + sample metrics/clients must not be production proof. Existing creative-agency-editorial skin reused, dark variant captured via style/color/type profile. Full spec at specs/fabrica.md; profile at design-intelligence/sites/fabrica.framer.media.md.

## CreateStudio / Create® — Entire Swiss-Editorial Agency Website (2026-10-16)

Official 21/21 sitemap paths return HTTP 200 in Chromium (one initial requests/TLS EOF on Numeriq recovered by two rendered browser 200s). Entire route family: home, Work index + five campaign cases, Studio, Contact, Whispers index + seven essay pages, plus FOUR legal URLs — Privacy, Disclaimer and **two separately indexed self-canonical Terms versions**. Ten supplementary URLs 404 including linked /404 and no /pricing route. Data/createstudio-route-inventory-2026-10-16.csv (31 rows), -internal-links-, -rendered-states- (44 Chromium 1440px and 390px pages with zero outer overflow) and -interaction-probes- (12 bounded observations) record scope and confidence.

Signature: #F2F2F2 warm-neutral Swiss graphic magazine, enormous Figtree headings, degree/serial markers, image/video showreel, precise media-driven client work, six agency service chapters, Core/Studio/Scale project plan ladder on homepage, local Los Angeles time/availability and four-field inquiry form. Homepage desktop sample 99 image/6 video/0 canvas and mobile 252 image/7 video/0 canvas (duplicated responsive media possible, not downloaded byte counts). Work index only three initial distinct case links vs five sitemap details; work and Whispers search interactions did not prove result-set reduction; category changed membership but not number. Source Contact/Whispers/Legal H1 semantics weak, competing Terms canonicals and stale 2025 Next Availability, inconsistent studio addresses/emails, example awards/metrics and creator template promotions require remediation. Reuse creative-agency-editorial baseline; profile design-intelligence/sites/createstudio.framer.media.md; spec specs/createstudio.md.

## BridgeBench Opus 5.5 Sunset Ocean — One-Screen Shader-Driven World (2026-10-17)

**This is a SINGLE ROUTE WebGL ocean scene**, not a multi-page Framer template. Provenance: local source at D:\Project\test\bridgebench-opus55-sunset-ocean, source prompt and user-uploaded prompt matched SHA-256 95dfb8bc6d6fdc73bb0cbb577446f097ccead852787f7313b732ceff446c983c. Single HTML source adjusted to import locally vendored Three.js 0.182.0; local start.bat uses localhost:8765. No source redesign was performed.

Full source-to-contract audit in design-intelligence/sites/bridgebench-opus55-sunset-ocean.md; focused spec in specs/bridgebench-opus55-sunset-ocean.md; preserved prompt in specs/bridgebench-opus55-sunset-ocean-source-prompt.txt. Evidence CSVs: bridgebench-opus55-sunset-ocean-prompt-trace-2026-10-17.csv (T1–T11), -source-components-2026-10-17.csv (20 subsystems with source anchors), -render-states-2026-10-17.csv (five independent states). Evidence screenshots: design-intelligence/sites/bridgebench-opus55-sunset-ocean-1280.webp and -390.webp. Source-provided smoke test passed at 1280×800, live controls 0.9/8, zero console/HTTP shader errors. Independent Chrome WebGL2 runtime confirmed 1280×800, shader content and controls; direct file:// initialization fails.

Physics/render transfer: near-weighted polar mesh **384x330** (127,435 vertices, 253,440 triangles); 8 seeded Gerstner wave families with deep-water dispersion; derivative analytic normals, Jacobian foam, 16 fragment ripple slopes filtered by screen-space footprint; Fresnel Schlick F0=.02, Beckmann-like light spec, dynamic half-float sky cubemap, teal/turquoise scattering and horizon color fog; handmade sky gradient with FBM directional clouds, single sun state; ACEs/sRGB native antialias and gentle near-sea camera drift. **Critical gaps**: not two scrolling normal-map textures, not formally physical Rayleigh/Mie, no bloom/vignette/composer, no Low/High quality, cubemap refreshed six sky faces per frame, no true local wave camera bob, visible UI panel, direct file:// not working, mobile buffer resize inconclusive, and 1080p 60 FPS on a hardware laptop unverified. No unsupported acceptance claims.

## PlatForm / Platform® — Complete Dark AI Infrastructure Website (2026-10-18)

Official **19/19 sitemap paths HTTP200** (homepage, Services, eight Labs essay details + Labs archive, four FrameAuth-shaped Sign Up/Sign In/OTP/Account routes, four legal/data pages), 12 extra URL probes HTTP404 (including TWO broken internal links /404 and /labs/:LGnOksssn). Route inventory 31 rows, same-domain link graph **224 pairs**, **42 successful Chromium 1440x900 and 390x844 states without positive document overflow**, **18 interaction probes** including corrected Labs Load More **seven initial distinct article hrefs → eight**. Source is a commercial **Framer template**, not verified enterprise automation, customer/uptime/compliance data.

Visual signature: dark **#161719**, **Inter Display** oversized H1 **100px desktop →54px mobile**, coral-orange type highlights/CTA, neural-glimmer hero, modular infrastructure case/product tiles, analytics, process, FAQ/team/testimonials, contact and Labs. Home document height ~21.4k desktop/~28.1k mobile, DOM 68 images +4 videos+2 canvases desktop and 60/2/2 mobile (DOM counts, not performance). Most homepage nav routes are fragment anchors; **/pricing and /contact HTTP404**, pricing and contact exist on home. Three initial sample tiers **Studio $49 / Scale $89 / Supreme $249**; one Plan Switch clicked but observed price copy did not change. No successful billing/auth/form submission established.

Auth source explicitly says **Powered by FrameAuth**, Google/GitHub, email/OTP/account routes; front-end inputs not required and true OAuth/provider/session delivery unknown. QA warnings: Labs page no H1, four auth pages no H1, mobile services H1 absent, CMS articles use extra H1 for More Articles; home/newsletter has Emaiil typo and hidden trap fields; generic metadata on legal routes; broken CMS slug and 404 linked in menu; source Netherlands Platform B.V. address and $129 template seller widget must be quarantined from genuine client/business claims. Profile design-intelligence/sites/plat-form.framer.ai.md; spec specs/platform.md; data/platform-*-2026-10-18.csv; screenshots platform-*.webp. Reuse premium-saas-dark as baseline, no new skin.
