---
name: distilled-web-toolkit
description: "Searchable audited design recommendation toolkit distilled from 12 live references. Use for provenance-backed style, color, typography, component, route-system, proof, motion, responsive, interaction, performance, UX, and QA retrieval plus audited design-system synthesis."
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

- `data/sites.csv` ? 12 reference identities and archetypes.
- `data/live-audit-2026-10-07.csv` ? standardized live desktop/mobile snapshot.
- `data/patterns.csv` ? reusable audited patterns.
- `data/route-recipes.csv` ? route and route-family structures.
- `data/motion-recipes.csv` ? motion/media choreography patterns.
- `data/responsive-recipes.csv` ? responsive substitutions and transformations.
- `data/anti-patterns.csv` ? failure modes and residue to avoid.
- `data/design-profiles.csv` ? 12 audited style/product profiles with dials, fit, performance and accessibility watches.
- `data/color-systems.csv` ? semantic color-role strategies with transfer constraints.
- `data/typography-systems.csv` ? audited display/heading/body/utility type-role systems and responsive scales.
- `data/component-recipes.csv` ? Component Recipes with job, anatomy, interaction, responsive and accessibility contracts.
- `data/ux-guidelines.csv` ? site-derived UX rules expressed as do/don't guidance.
- `data/design-primitives-live-2026-10-07.csv` ? live desktop/mobile primitive ledger for the 12-site corpus.
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
