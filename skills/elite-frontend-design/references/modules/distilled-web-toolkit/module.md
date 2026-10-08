---
name: distilled-web-toolkit
description: "Searchable audited design recommendation toolkit distilled from 17 live references. Use for provenance-backed style, color, typography, component, route-system, proof, motion, responsive, interaction, performance, UX, and QA retrieval plus audited design-system synthesis."
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

- `data/sites.csv` ? 17 reference identities and archetypes.
- `data/live-audit-2026-10-07.csv` ? standardized live desktop/mobile snapshot.
- `data/patterns.csv` ? reusable audited patterns.
- `data/route-recipes.csv` ? route and route-family structures.
- `data/motion-recipes.csv` ? motion/media choreography patterns.
- `data/responsive-recipes.csv` ? responsive substitutions and transformations.
- `data/anti-patterns.csv` ? failure modes and residue to avoid.
- `data/design-profiles.csv` ? 17 audited style/product profiles with dials, fit, performance and accessibility watches.
- `data/color-systems.csv` ? semantic color-role strategies with transfer constraints.
- `data/typography-systems.csv` ? audited display/heading/body/utility type-role systems and responsive scales.
- `data/component-recipes.csv` ? Component Recipes with job, anatomy, interaction, responsive and accessibility contracts.
- `data/ux-guidelines.csv` ? site-derived UX rules expressed as do/don't guidance.
- `data/design-primitives-live-2026-10-07.csv` ? live desktop/mobile primitive ledger for the 17-site corpus.
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
