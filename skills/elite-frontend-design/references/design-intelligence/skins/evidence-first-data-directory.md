# Baseline Skin: Evidence-First Data Directory

audited evidence anchor: ../sites/tokenmeter.info.md

This skin distills the whole-site system grammar of Tokenmeter into a reusable baseline for directories, comparison engines, benchmarks, catalogs, and technical reference products. It does not authorize copying Tokenmeter's exact wordmark, orange value, fonts, grid spacing, provider data, editorial scores, or copy.

## Use when

Use for products whose main value is helping people scan, compare, verify, and inspect structured records across multiple routes.

Typical fits:
- provider/model/API directories;
- benchmark/comparison sites;
- pricing and performance references;
- compliance/certification directories;
- technical catalogs;
- evidence-driven data journalism utilities.

Prefer a marketing skin when persuasion or imagery is the primary job rather than structured evidence.

## Deterministic Design Scaffold

Build one shared evidence grammar first, then project the same data at different densities across route families.

Required route roles when relevant:
- orientation/home;
- directory/list;
- compare;
- detail;
- methodology/provenance;
- glossary;
- FAQ/help.

Not every product needs all seven, but each route should have one clear information job.

## Token Scaffold

- page shell: warm neutral or cool neutral paper-like background;
- primary surface: white/light neutral;
- ink: near-black;
- muted: medium neutral with accessible contrast;
- hairline: quiet 1px divider;
- accent: one warm or cool brand accent, used sparingly;
- semantic positive/negative colors remain separate from brand accent;
- body: variable or highly legible sans;
- metadata/data role: mono or numeric-focused companion;
- use tabular numerals for aligned metrics;
- max content width: roughly 1180-1280px;
- page padding: responsive clamp;
- default radius: 0-6px; avoid soft SaaS-card inflation;
- panel rule: 1px hairline with occasional 2px high-authority divider;
- motion: 120-360ms state changes; entrance motion optional and subtle.

Optional brand texture:
- faint technical grid, dotted paper, or ruled background;
- it must never compete with table/grid readability.

## Composition Grammar

### Home
- source/status eyebrow;
- strong product thesis;
- dataset freshness/scope line;
- 3-6 extractable facts;
- primary action to compare/browse;
- compact data preview.

### Directory
- clear category/filter controls;
- repeatable record cards;
- 3-5 high-value metrics per card;
- one-line summary;
- medium information density.

### Compare
- grouped filters;
- visible result count;
- sortable column headers;
- one dense comparison table;
- no-results state;
- methodology link near the data.

### Detail
- breadcrumbs;
- entity category/title/slug;
- confidence/source status;
- key facts;
- specification;
- strengths/trade-offs or equivalent interpretation;
- primary metrics;
- related/comparison links;
- main/aside hierarchy on large screens.

### Methodology
- confidence/provenance legend;
- sourcing explanation;
- metric definitions;
- editorial/computed-score caveats;
- per-record confidence when relevant.

### Glossary
- term + definition rows;
- anchorable terms;
- scan-friendly two-column layout on large screens;
- one-column stack on small screens.

### FAQ
- numbered or clearly indexed questions;
- concise always-visible answers by default;
- avoid accordion interaction unless answer volume genuinely requires it.

## Confidence as Interface

If data quality varies, confidence must be visible as part of the UI.

Use:
- consistent confidence vocabulary;
- small badges or labels near records;
- clear methodology definitions;
- source/freshness links;
- per-record caveats only when they materially differ.

Do not hide uncertainty in footer legal copy while rendering values with false precision.

## Route-Family Density Ladder

Use the same underlying data model at different densities:

- Home: low-medium density orientation;
- Directory: medium density scanning;
- Compare: highest density;
- Detail: one-record depth;
- Methodology: trust/provenance;
- Glossary/FAQ: cognitive support.

Do not force the same card component onto all route families.

## Contain Horizontal Density, Don't Crush It

For real comparison tables:

- set a minimum table width based on readable columns;
- place the table in its own horizontal scroll container;
- keep the page/document itself stable;
- preserve meaningful column labels and sort controls;
- avoid turning every row into a mobile card unless comparison is no longer the task;
- allow sticky headers where useful;
- ensure touch scrolling is obvious and usable.

## Human + Machine Surface Parity

For public reference products, the machine-readable product should match the visible product.

When appropriate, maintain:
- sitemap;
- robots policy;
- llms.txt or equivalent AI-readable summary;
- canonical metadata;
- Open Graph/Twitter metadata;
- structured data;
- search action metadata;
- consistent route names and data caveats.

Machine-readable surfaces must not omit important confidence/freshness caveats.

## Skin Lock

Lock:

- one shared evidence grammar;
- one display/body/data typography role system;
- square/low-radius surface language;
- one restrained brand accent;
- confidence semantics;
- tabular numeric treatment;
- route-family density roles;
- dense-table containment;
- provenance/methodology access;
- accessible filter/sort state;
- responsive collapse rules.

## Controlled Mutation

May mutate:

- light versus dark shell;
- exact accent;
- font families;
- background texture;
- route names;
- card metric count;
- main/aside ratio;
- whether comparison uses table or matrix when the data model demands it;
- density within the stated route role;
- brand-specific visual signature.

Must mutate:
- Tokenmeter wordmark;
- exact orange;
- exact 64px grid;
- exact fonts;
- exact provider card content;
- editorial reputation concept if the new product cannot support it.

## Responsive Contract

- collapse layout grids before shrinking data below readable size;
- directory grids become fewer columns, usually one at narrow widths;
- detail main/aside becomes one column;
- glossary/specification rows stack;
- confidence badges and tags wrap;
- preserve filters and state;
- dense tables keep internal horizontal scroll;
- document body must not inherit table overflow;
- maintain readable metric labels and tabular numbers;
- preserve provenance/confidence on mobile;
- reduced-motion users should not depend on entrance animation to understand state.

## Motion Language

- state change beats spectacle;
- filter/sort feedback should be immediate;
- row/card entrance animation, if used, is short and staggered lightly;
- hover may adjust border, tint, or text color;
- avoid large translate/scale motion on evidence surfaces;
- respect reduced motion globally.

## Anti-Template Guard

Avoid:

- generic glassmorphism on every card;
- huge gradient hero unrelated to the dataset;
- dark-terminal styling merely because the subject is technical;
- hiding source/confidence details behind tooltips only;
- compressing tables into unreadable eight-column mobile layouts;
- converting every route into the same bento grid;
- using mono everywhere;
- using a warm accent on every border, icon, and metric;
- decorative charts with no additional decision value.

## QA Rubric

Pass only if:

- each route family has one clear data task;
- the same data means the same thing across home, list, compare, detail, and methodology;
- confidence/freshness is visible wherever it materially qualifies a claim;
- dense tables remain readable and scroll internally on narrow screens;
- the outer document has no unintended horizontal overflow;
- numeric alignment is stable;
- filters/sorts expose state accessibly;
- directory/detail layouts collapse coherently;
- glossary/help pages retain the same visual system;
- machine-readable surfaces align with the visible information architecture when included;
- reduced-motion users lose no information;
- the final product does not visibly reproduce Tokenmeter's exact brand identity.
