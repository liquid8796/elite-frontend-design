# Tokenmeter - full-site distilled design intelligence

Source: https://tokenmeter.info/
Audit date: 2026-10-06
Coverage: 26/26 sitemap URLs

Audit scope: sitemap and robots discovery, llms.txt, all public page HTML, route-family structure, all 20 provider detail variants, shared CSS, provider-detail CSS, inline page styles/scripts, desktop-class and mobile-class rendered layout checks for every route family, and interactive table/directory behavior.

This is a whole-site profile. It is not based on the homepage alone.

## Coverage manifest

Core/reference routes:
- /
- /compare/
- /faq/
- /glossary/
- /methodology/
- /providers/

20 provider detail pages:
- /providers/anthropic/
- /providers/baseten/
- /providers/cerebras/
- /providers/cheapestinference/
- /providers/deepinfra/
- /providers/fireworks-ai/
- /providers/google-vertex/
- /providers/groq/
- /providers/hyperbolic/
- /providers/lepton-ai/
- /providers/mistral/
- /providers/modal/
- /providers/nebius/
- /providers/novita-ai/
- /providers/openai/
- /providers/openrouter/
- /providers/perplexity/
- /providers/replicate/
- /providers/sambanova/
- /providers/together-ai/

The 20 provider detail pages share one 8-section core template, with real data-driven variants: confidence level, OpenAI compatibility, per-token versus GPU-time pricing, reputation trend, compliance tags, and optional Reputation context/xref content.

## Executive DNA

Tokenmeter is a data-reference product whose visual credibility comes from consistency, legibility, visible uncertainty, and route-specific density rather than decorative spectacle.

Its reusable system is:

- an editorial/data-sheet shell shared across the full information architecture;
- a pale paper-like technical grid background with white square surfaces;
- one warm accent used for focus, ordering, hover, and key annotations;
- wide/heavy sans display type paired with mono labels, slugs, metadata, and numeric framing;
- the same dataset shown at multiple densities depending on route purpose;
- confidence labels and methodology links kept close to claims;
- dense tables preserved as dense tables inside internal horizontal scroll containers rather than crushed into unreadable mobile columns;
- static-first Astro pages with small local JavaScript for sorting/filtering instead of a large client application;
- human-facing pages mirrored by sitemap, robots.txt, llms.txt, canonical metadata, JSON-LD, and search-oriented structured surfaces.

The lesson is not "copy a beige grid with orange labels." It is: build a data product whose visual system communicates evidence quality as clearly as the data itself.

## Evidence Confidence

### Source-confirmed

- The generated HTML identifies Astro v7.0.7.
- Shared root tokens include background #fbfaf7, surface #fff, ink #0b0b0c, muted #6b6b66, hairline #e4e3dc, accent --accent:#e8590c, positive #1f7a3d, negative #c1121f, max width 1240px, and a responsive page pad.
- Typography loads Archivo Variable and JetBrains Mono Variable.
- Numeric rendering uses tabular numerals.
- The body background uses repeating 64px-style horizontal and vertical rules, creating a fixed technical-paper grid.
- Shared tiles use a 1px hairline border and border-radius 0.
- The site header is sticky, 56px high in source CSS, with a translucent background and restrained backdrop blur.
- The display role uses Archivo variable width/weight settings with uppercase treatment.
- Labels, badges, wordmark, tags, buttons, table headers, and metadata lean on the mono role.
- Global motion includes riseIn and explicitly handles prefers-reduced-motion.
- The comparison table keeps a min-width of 880px inside an overflow-x:auto container.
- Table headers are sortable buttons with aria-sort state; filter chips use aria-pressed.
- Directory category filtering is implemented with a small local module script that toggles card visibility and aria-pressed state.
- Provider-detail layout uses a 1.7fr / 1fr desktop grid and collapses to one column below 860px.
- Provider-detail strength/trade-off cells collapse below 520px; specification rows collapse below 480px.
- Glossary rows switch from two columns to one below 560px; FAQ answer indentation is removed below 480px.
- robots.txt explicitly allows general and major AI/LLM crawlers and points to sitemap-index.xml.
- llms.txt provides a machine-readable description, key pages, all indexed providers, confidence semantics, methodology notes, and sitemap/robots links.
- Homepage metadata includes Organization and WebSite JSON-LD plus a SearchAction target.
- Canonical, Open Graph, Twitter, favicon, and sitemap metadata are present in the generated page shell.

### Observed across route families

Desktop-class audit:
- shared header height remains visually constant across all route families;
- the homepage uses the largest display scale, while reference/tool pages use a smaller shared display scale and provider details use an intermediate detail-title scale;
- the page shell remains low-decoration and border-led even when content density increases;
- comparison and methodology tables retain explicit table geometry instead of being converted to decorative cards;
- provider detail pages keep main evidence/spec content in the larger left region and price/reputation/compliance/comparison context in a narrower aside;
- directory uses a repeatable card grid rather than the dense comparison table because its job is scanning providers, not comparing every metric simultaneously.

Mobile-class audit:
- route families collapse major grids to one column;
- comparison/methodology tables retain their minimum information width inside an internal horizontal scroller;
- the document shell itself does not inherit the table width;
- directory cards become a single-column stream;
- provider-detail two-column layout becomes one column;
- glossary term-definition rows and provider specification rows stack;
- the same typography roles, border grammar, accent semantics, badges, and evidence hierarchy survive.

## Whole-Site Route Family Map

### Home

Purpose: orientation + extractable facts + compact comparison.

Pattern:
- eyebrow/source status;
- oversized thesis headline;
- dateline and dataset scope;
- numbered TL;DR facts;
- direct actions to comparison and methodology;
- compact 20-row comparison table.

The homepage does not try to introduce every route. It gives enough evidence to establish usefulness and then hands off to denser route families.

### Compare

Purpose: high-density side-by-side decision support.

Pattern:
- concise route intro;
- filters grouped by category, OpenAI compatibility, and compliance;
- visible result count;
- sortable 20-row table;
- sticky table header on larger viewports;
- explicit no-results state.

This route accepts horizontal density because comparison is its primary job.

### Directory

Purpose: scanning and discovery.

Pattern:
- category chip filter;
- auto-fill provider card grid;
- each card combines name/slug, category/confidence metadata, four key metrics, and one-line editorial summary;
- subtle staggered riseIn motion;
- hover changes border/name emphasis rather than adding large transforms.

This route is deliberately less dense than Compare even though it uses the same dataset.

### Methodology

Purpose: make trust mechanics inspectable.

Pattern:
- prose explaining source model;
- Confidence as Interface through high/medium/seed legend cards;
- separate explanations for pricing, latency/throughput, reputation, and neutrality;
- per-provider confidence table;
- same mono/border/table grammar as comparison pages.

Methodology is not hidden legal copy. It is a first-class product surface.

### Glossary

Purpose: resolve domain vocabulary without leaving the system.

Pattern:
- sectioned term-definition rows;
- stronger term column + quieter explanation column;
- target rows can receive accent-tint focus;
- mobile stacks term and definition.

### FAQ

Purpose: answer trust and operational questions with minimal interaction.

Pattern:
- numbered question rows;
- answers are always visible rather than hidden behind accordion chrome;
- orange numeric index provides orientation;
- on narrow screens, answer indentation is removed rather than shrinking type.

### Provider detail template

Purpose: turn one row/card into a trustworthy reference profile.

Core structure:
- breadcrumbs;
- category + provider title + slug/headquarters/founded line;
- confidence badge + external provider action;
- Key facts;
- Specification;
- Strengths & trade-offs;
- Pricing;
- Reputation index;
- optional Reputation context/xref;
- Compliance;
- Compare with;
- Related providers.

All 20 provider detail pages were checked structurally. They share the same core template, with content-driven variants instead of bespoke page designs.
## Design DNA

### Composition

Tokenmeter uses a strict information architecture but varies density by route role.

- global max-width shell around 1240px;
- strong 2px black section/panel rules mark major boundaries;
- 1px hairlines divide repeated facts, terms, cards, and rows;
- square surfaces avoid soft-card visual noise;
- whitespace is measured and functional, not luxurious;
- important lists use counters or compact metadata rather than decorative iconography.

The visual hierarchy is generated by weight, width, rule thickness, spacing, and data density more than by large color blocks.

### Typography

Observed/source-confirmed roles:

- Archivo Variable: product/editorial sans;
- display role: wide, heavy, uppercase Archivo treatment;
- body role: normal-width Archivo for prose and explanations;
- JetBrains Mono Variable: labels, slugs, badges, tags, buttons, filters, table headers, metadata, and compact numeric framing;
- tabular numerals preserve metric alignment.

Transfer the role separation, not the exact fonts.

### Color + Material

The system uses a paper/data-sheet palette:

- warm near-white page;
- white surfaces;
- near-black structural ink;
- medium gray supporting copy;
- pale gray hairlines;
- one warm accent for focus and editorial annotation;
- green/red reserved for positive/negative semantics.

The accent is intentionally scarce. Most hierarchy comes from typography and rules.

### Motion

Motion is subordinate to information:

- table rows and provider cards use short staggered riseIn entrance motion;
- hover effects change tint, border, or text color;
- filter/sort interactions update state without large transition choreography;
- prefers-reduced-motion is explicitly handled globally.

Reusable lesson: data credibility benefits from calm state changes. Avoid turning sorting/filtering into spectacle.

### Interaction Grammar

The site uses conventional controls with visible state:

- sort buttons live inside table headers and expose aria-sort;
- chips expose aria-pressed;
- category filters hide/show existing data rather than introducing custom gesture grammar;
- links and hover states use the same warm accent;
- horizontal table scrolling is contained inside the table viewport;
- glossary target focus uses a background tint;
- FAQ stays expanded, prioritizing searchability and scanning over accordion theatrics.

### Confidence as Interface

Uncertainty is treated as product data, not a disclaimer.

Tokenmeter places confidence in multiple layers:

- data-confidence badges on provider surfaces;
- high / medium / seed semantics on Methodology;
- provider-specific confidence table;
- per-profile confidence badge;
- xref/Reputation context on some provider pages;
- repeated warnings that approximate figures are reference points rather than SLAs/quotes.

Transfer rule:

- if a metric has uncertainty, provenance, freshness, or editorial judgment, show that state near the value or record;
- define the confidence vocabulary once and reuse it;
- give users a path to methodology/source context;
- do not use visual precision to imply evidentiary precision.

### Route-Family Density Ladder

One dataset can require multiple presentations.

Tokenmeter forms a useful density ladder:

1. Home: headline + a few extracted facts + compact comparison.
2. Directory: medium-density scan cards.
3. Compare: maximum-density sortable/filterable table.
4. Provider detail: one-entity evidence profile with main/aside structure.
5. Methodology: trust model and confidence data.
6. Glossary: terminology reference.
7. FAQ: explanatory objections/questions.

Transfer rule: choose density by user task rather than forcing one component grammar across every route. Shared tokens and semantics should remain stable while the content container changes.

### Contain Horizontal Density, Don't Crush It

For genuinely comparative data, compressing eight columns into tiny mobile cells destroys usefulness.

Tokenmeter instead:

- gives comparison tables an explicit minimum width;
- places them in overflow-x:auto containers;
- keeps the outer page shell stable;
- collapses surrounding grids before shrinking critical metrics beyond readability;
- changes sticky-header behavior at narrow widths.

Transfer rule: dense tables may scroll horizontally internally. The page itself should not become horizontally unstable.

### Human + Machine Surface Parity

The human information architecture is mirrored in machine-readable surfaces:

- sitemap-index.xml -> sitemap-0.xml contains all 26 public URLs;
- robots.txt advertises the sitemap and explicitly permits crawlers;
- llms.txt describes the product, key routes, all 20 provider records, confidence semantics, and methodology caveats;
- page shell includes canonical, Open Graph, Twitter, favicon, JSON-LD, and SearchAction metadata;
- visible route names and machine-readable route descriptions align.

Transfer rule: for reference/catalog/documentation products, machine-readable surfaces should describe the same information model and trust caveats users see. Do not publish a rich human UI with stale or contradictory crawler/LLM metadata.

## Provider Detail Variants

All 20 provider pages were structurally checked.

Stable structure:
- 8 main sections per profile;
- shared detail CSS;
- shared main/aside responsive layout;
- shared pricing/reputation/compliance/compare/related primitives.

Content-driven variants observed:

- high, medium, and seed confidence;
- OpenAI-compatible versus native API language;
- improving versus stable reputation trend;
- optional Reputation context/xref panel on a subset of providers;
- per-token price versus Modal's GPU-time billing where blended price is shown as an em dash;
- varying compliance tag sets;
- varying related/compare targets.

This is a strong example of keeping template structure stable while allowing data truth to alter content and small surface states.

## Responsive Contract

Across the audited route families:

- preserve the sticky global shell and typography roles;
- collapse multi-column content grids before reducing legibility;
- keep cards full-width on narrow viewports;
- stack glossary and specification definition rows;
- stack strength/trade-off cells;
- remove unnecessary answer indentation in FAQ;
- preserve dense comparison data inside internal horizontal scrollers;
- retain filter/sort states and accessible names;
- keep badges/tags wrapping rather than shrinking into unreadable text;
- preserve confidence/provenance information on mobile.

Responsive success is not "everything fits without scrolling." It is "the document remains stable and each dense component owns its own necessary overflow."

## Technical Architecture Lessons

### 1. Static-first is a design advantage for reference products

Most route content is delivered as generated HTML. JavaScript is reserved for interactions that require it: table sorting/filtering and directory filtering.

Benefits:
- content is immediately inspectable;
- semantics remain available without a large client runtime;
- crawler/LLM surfaces align naturally with page content;
- interaction logic stays small and auditable.

### 2. Use one data model, multiple route projections

The same provider fields appear as:
- homepage comparison rows;
- full comparison table;
- directory cards;
- provider details;
- methodology confidence rows;
- llms.txt records.

This reduces semantic drift when implemented from one structured dataset.

### 3. Make confidence/provenance composable

Confidence appears as badges, legends, tables, context panels, and prose. The vocabulary is consistent even though the component changes.

### 4. Local JS should preserve native semantics

Sorting operates on real table rows. Filters use buttons and aria-pressed. No-results states remain in the DOM. This preserves accessibility and makes behavior easier to verify.

### 5. Reduced motion belongs in the shared shell

Because riseIn is reused across row/card surfaces, the reduced-motion policy is global rather than reimplemented by each page.

## What Not to Copy Literally

Avoid transferring:

- exact Tokenmeter name/wordmark;
- exact #e8590c accent;
- exact Archivo + JetBrains Mono pairing;
- exact 64px grid;
- exact provider dataset/copy/reputation weights;
- exact page order or labels if the new data model differs;
- the editorial reputation concept when the new product cannot justify such a score.

Transfer the information and trust grammar, not the brand identity.

## Adopt / Adapt / Avoid

| Pattern | Decision | Why |
|---|---|---|
| Confidence as Interface | Adopt for uncertain/editorial data products | Prevents false precision and makes trust inspectable. |
| Route-Family Density Ladder | Adopt for directories/catalogs/reference products | Different tasks need different projections of the same data. |
| Contain Horizontal Density, Don't Crush It | Adopt for real comparison tables | Preserves readability without destabilizing the document. |
| Human + Machine Surface Parity | Adopt for public reference/documentation sites | Improves search/LLM discoverability and information consistency. |
| Mono labels + tabular numeric role | Adapt | Strong for technical/data products; can feel overly terminal-like elsewhere. |
| Paper grid + square tiles | Adapt | Supports reference-sheet character but is brand-specific in intensity. |
| One warm editorial accent | Adapt | Useful for calm data hierarchy; choose a new brand-specific value. |
| Exact reputation scoring model or provider copy | Avoid | Product/data-specific. |

## Best-Fit Briefs

Use this profile for:

- comparison engines;
- directories and catalogs;
- benchmarks;
- price/performance reference sites;
- data journalism utilities;
- API/provider/model directories;
- compliance/certification reference products;
- knowledge bases where confidence/freshness matter.

## Weak-Fit Briefs

Do not let this profile dominate:

- emotional brand campaigns;
- luxury/editorial sites driven primarily by imagery;
- social/community products;
- entertainment launches;
- task-heavy dashboards where users already know the data domain;
- products without enough structured data to justify dense reference surfaces.

## Regression Questions

- Did the audit or implementation account for every public route, not only the homepage?
- Does one structured data model remain semantically consistent across list, compare, detail, methodology, and machine-readable surfaces?
- Is uncertainty visible near the claims it qualifies?
- Can users reach the methodology behind confidence/reputation values?
- Are dense tables preserved legibly inside internal scrollers?
- Does the outer document avoid unintended horizontal overflow?
- Do mobile routes preserve confidence, provenance, and comparison capability?
- Are mono, accent color, and grid texture supporting information rather than becoming decorative tech clichés?
- Do filters/sorts expose accessible state?
- Does reduced motion disable nonessential entrance animation?
- Do sitemap, llms.txt, robots, structured metadata, and visible routes describe the same product?
- After replacing the name, exact colors, fonts, dataset, and copy, does the resulting design still make sense for the new reference product?

Pass only when the new product feels evidence-first, coherent across route families, and trustworthy without looking like a Tokenmeter clone.
