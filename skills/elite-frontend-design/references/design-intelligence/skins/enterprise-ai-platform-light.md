# Baseline Skin: Enterprise AI Platform Light

audited evidence anchor: ../sites/novaos.framer.website.md

This skin distills the whole-site NovaOS template audit into a coherent light enterprise-AI scaffold. It is deliberately safer than copying the template. Do not reuse NovaOS logos, exact blue, exact DM Sans/Geist pairing, mockup art, copy, leadership data, article content, or other site-specific assets.

## Use when

Use for:

- enterprise AI platforms;
- agent orchestration products;
- automation SaaS;
- workflow products;
- integration-heavy B2B software;
- products that need pricing, company, technical content, legal/security and enterprise forms in one coherent light system.

Prefer developer-infra.md when code/API proof is primary.
Prefer clean-product-light.md when the product is simpler and does not need enterprise route breadth.

## Deterministic Design Scaffold

Use one quiet light shell, one strong accent, believable operational product proof, and a full-site trust ecosystem.

The scaffold should make a lower-capability implementation feel coherent before bespoke art direction is added.

## Token Scaffold

- shell: soft neutral around #f5f5f2 to #fafafa;
- primary surface: white;
- ink: very dark neutral;
- muted: medium gray;
- border: pale neutral hairline;
- brand accent: one saturated color family; do not default to NovaOS blue;
- positive/warning/error remain semantic and separate from brand accent;
- display role: clean variable sans, regular-to-medium weight;
- utility/nav role: compact UI sans;
- body role: readable sans with restrained line length;
- headline scale desktop: roughly 44-64px depending on route;
- headline scale mobile: roughly 27-36px;
- standard card radius: 14-18px;
- proof viewport radius: 16-24px;
- pill radius: 999px for primary compact actions;
- section spacing desktop: 96-160px;
- section spacing mobile: 64-96px;
- default content max-width: 1180-1280px.

## Composition Grammar

### Home

1. compact navigation;
2. release/status pill when meaningful;
3. centered promise;
4. primary + secondary CTA;
5. integration/ecosystem context;
6. Operational Pipeline Storytelling;
7. focused product-proof surfaces;
8. use cases;
9. pricing preview or packaging;
10. FAQ/trust;
11. final conversion;
12. footer.

### Product-proof section

For each major proof:

- short claim;
- one sentence of context;
- one believable UI/system state;
- one visible input, state, or output;
- avoid decorative dashboards with meaningless numbers.

### Pricing

- 2-4 plans maximum unless the business model truly needs more;
- one emphasis state only when there is a recommended plan;
- capability comparison after plan summary;
- preserve readable capability relationships on mobile.

### Integrations

- real systems grouped or ordered intentionally;
- concise description of what the integration enables;
- avoid logo wallpaper without operational meaning.

### Company

- product/company thesis;
- evidence-backed metrics only;
- leadership/culture when relevant;
- connect company story back to product mission.

### Blog / technical content

- index prioritizes topic comprehension over visual novelty;
- article body becomes quieter and more editorial;
- related content follows the article, not interrupts it.

### Legal / security

- keep the same shell;
- use explicit headings and readable long-form structure;
- do not turn security/compliance claims into decorative badges without evidence.

### Careers

- benefits;
- role list;
- role detail;
- application;
- use real role requirements and compensation when available.

## Operational Pipeline Storytelling

When the product coordinates multiple AI/system layers, make the marketing story sequential.

Recommended abstract sequence:

**model/engine -> context/data -> agent/workspace -> tools/integrations -> workflow -> observable output**

Requirements:

- every stage has one job;
- adjacent stages connect causally;
- proof surfaces use believable states;
- the pipeline can be split across multiple sections;
- later routes should deepen the same model rather than contradict it.

Do not use pipeline storytelling for a single-purpose product that can be explained more directly.

## Proof Surface Cropping

On narrow screens, a complex product UI may be more legible at a larger internal scale than if the entire canvas is shrunk.

Contract:

- outer proof card stays within the viewport;
- inner proof surface may be wider;
- outer card uses overflow hidden/clip;
- choose a focal region intentionally;
- keep document-level horizontal overflow at zero;
- crop only marketing evidence, not required task controls;
- if interaction needs offscreen content, use an accessible pan/scroll/focus mechanism instead.

## Credibility Through Route Ecosystem

For enterprise products, trust is distributed.

Support the product claim through the routes that matter:

- integrations;
- pricing;
- company;
- technical blog/resources;
- security/privacy/legal;
- careers;
- contact/demo;
- FAQ/help.

Every route should reinforce the same product truth from a different angle.

Never fabricate compliance, customers, revenue, uptime, leadership metrics, benchmarks, or technical architecture to make the ecosystem look mature.

## Shared Conversion Tail

A repeatable close may contain:

1. route-relevant FAQ or objection handling;
2. one dark/high-contrast final CTA;
3. consistent footer.

Use the shared tail to create continuity, not to duplicate irrelevant content.

## Skin Lock

Lock:

- light neutral shell;
- white operational surfaces;
- one accent family;
- calm sans typography;
- 14-18px card family;
- pill primary actions;
- Operational Pipeline Storytelling;
- believable product proof;
- responsive proof behavior;
- enterprise route ecosystem;
- restrained motion;
- reusable conversion tail.

## Controlled Mutation

May mutate:

- brand accent;
- exact neutral warmth/coolness;
- font families;
- hero alignment;
- card radius within the family;
- proof media style;
- integration presentation;
- pricing structure;
- signature illustration/interaction;
- final CTA treatment.

Must mutate:

- NovaOS logo;
- exact #0082de blue;
- exact DM Sans + Geist pairing;
- exact product mockups;
- exact page copy;
- article/career/company/legal content;
- exact template demo bar and Framer-specific chrome.

## Responsive Contract

- desktop grids collapse cleanly to one column when needed;
- top-level mobile headings remain readable, not merely scaled proportionally;
- primary cards target viewport-safe width;
- forms retain full labels and touch-sized controls;
- job/detail sidebars stack into content order;
- pricing comparison becomes readable rather than tiny;
- use Proof Surface Cropping where product UI would otherwise become illegible;
- preserve no document-level horizontal overflow;
- mobile navigation reduces complexity;
- repeated CTA/footer remain available;
- preserve real information hierarchy, not desktop decorative spacing.

## Motion Language

- use subtle enter/reveal motion;
- no universal parallax;
- smooth scrolling is optional, not part of the visual identity;
- if smooth scrolling exists, honor reduced motion;
- pause it while menus/modals lock page scroll;
- product-proof motion should show system state, not merely float cards;
- CTA hover feedback stays fast and simple.

## Anti-Template Guard

Avoid shipping the recognizable commodity bundle unchanged:

- centered hero + blue gradient;
- white 16px cards everywhere;
- generic integration logo grid;
- three pricing tiers with a blue middle card;
- FAQ accordion;
- dark final CTA;
- pill buttons;
- generic dashboard mockups.

Any one of these can be fine. The risk comes from using the entire bundle without product-specific evidence or structural differentiation.

Require at least one strong differentiator in:

- proof mechanism;
- information model;
- typography;
- hero composition;
- interaction grammar;
- content architecture;
- responsive transformation.

Changing only accent color does not count.

## QA Rubric

Pass only if:

- product claims are paired with believable operational evidence;
- the operating chain is understandable from model/data through action/output;
- integrations describe useful work rather than show logos only;
- enterprise trust routes support the same product story;
- mobile proof remains legible;
- oversized proof is clipped intentionally with no document-level horizontal overflow;
- pricing/forms/job details reflow coherently;
- legal/security pages remain readable and truthful;
- article pages are calmer than marketing pages;
- repeated FAQ/CTA/footer content is relevant;
- reduced-motion users do not depend on appear/smooth-scroll behavior;
- the final result no longer reads as an off-the-shelf blue Framer AI template.
