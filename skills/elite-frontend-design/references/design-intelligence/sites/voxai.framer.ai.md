# VoxAI - full-site distilled design intelligence

Source: https://voxai.framer.ai/
Audit date: 2026-10-07
Coverage: 36/36 sitemap URLs + /404 utility route

VoxAI is a dark AI/SaaS Framer template whose strongest transferable value is the full-site commercial system rather than one isolated homepage composition. The audit covers the complete sitemap, the indexed 404 utility surface, route-family structure, rendered desktop/mobile behavior, Framer search-index content, runtime media, typography, conversion grammar, and CMS binding integrity.

## Evidence confidence

- **Observed**: rendered desktop/mobile layout, visible content, route lengths, no-overflow checks, media presence, typography and computed colors.
- **Source-confirmed**: sitemap/search-index route inventory, Framer generator/build metadata, search-index CMS text, loaded fonts/assets, canonical URLs.
- **Inferred**: higher-level commercial/narrative intent derived from repeated route patterns.

## Source and runtime evidence

- Generator: Framer a050651.
- robots.txt points to /sitemap.xml.
- Sitemap exposes 36 public URLs.
- Framer search index is searchIndex-d5gy8ZmcXxvL.json.
- /404 exists in the search index and navigation even though it is not in the sitemap.
- Published source snapshot exposed an Oct 4, 2026 timestamp.
- Main shell background is #030014.
- Blue product accent observed around #0f63b8.
- Pink expressive accent observed around #f73e9e.
- Desktop main composition uses a centered 1200px content width.
- Home hero is approximately 800px high.
- Route-page desktop H1: Cal Sans, 64px, 76.8px line height.
- Representative mobile route H1: 36px, 43.2px line height.
- Active font families include Cal Sans, Inter Display, Inter, Poppins; Fragment Mono is source-loaded for utility/technical treatment.
- Home media includes y1kjVqQmzBxCWoHALMC2UwTOFPU.mp4 and 8qsenQIIXYW3mI4IYIYBv9PMtkU.mp4.
- Representative mobile routes at 390x844 showed no document-level horizontal overflow.

## Full route inventory

### Core/index routes - 7

1. /
2. /about
3. /pricing
4. /integrations
5. /contact
6. /blog
7. /case-study

### Case-study detail pages - 6

1. /case-study/automating-24-7-identity
2. /case-study/scaling-voice-checkout
3. /case-study/capturing-100-of-after-hours-emergency-service-calls
4. /case-study/streamlining-enterprise-onboarding-and-technical-voice-triage
5. /case-study/transforming-unstructured-voice
6. /case-study/automating-driver-check

### Legal routes - 2

1. /legal/terms-of-service
2. /legal/privacy-policy

### Blog detail pages - 8

1. /blog/bridging-design-development-2
2. /blog/bridging-design-development
3. /blog/the-end-of-blank
4. /blog/staying-in-flow-while-documenting-code
5. /blog/building-a-daily-writing-habit-without-typing-fatigue
6. /blog/cutting-follow-up-time-after-meetings-with-real-time-dictation
7. /blog/when-writing-becomes-easier-by-removing-the-keyboard
8. /blog/replacing-manual-status-updates-with-spoken-input

### Integration detail pages - 13

Canonical-looking records:
1. /integrations/posthog-voice-telemetry
2. /integrations/twilio-elastic-sip-trunking
3. /integrations/zapier-webhook-trigger
4. /integrations/stripe-voice-payment-processing
5. /integrations/hubspot-crm-voice-sync

Residue/copy records:
6. /integrations/posthog-voice-telemetry-copy
7. /integrations/posthog-voice-telemetry-copy-copy
8. /integrations/posthog-voice-telemetry-copy-copy-copy
9. /integrations/posthog-voice-telemetry-copy-copy-copy-copy
10. /integrations/posthog-voice-telemetry-c2
11. /integrations/hubspot-crm-voice-sync-copy
12. /integrations/twilio-elastic-sip-trunking-copy
13. /integrations/zapier-webhook-trigger-copy

This is 5 canonical integration records and 8 residue/copy integration routes.

### Utility surface outside sitemap

- /404

Full-site accounting therefore uses the sitemap as the canonical 36-route coverage set and tracks /404 separately as an indexed utility/template route.

## Executive DNA

The full system behaves as a commercial hub plus specialized proof satellites:

Home -> capability/workflow theater -> pricing -> integrations -> case-study proof -> blog/education -> contact -> legal trust

System-level characteristics:
- one dark chromatic shell across route families;
- one high-character display role plus quieter product/UI roles;
- operational micro-scenes instead of icon-only claims;
- short conversion routes after a dense home;
- consistent detail-page frames for CMS collections;
- repeated proof and CTA modules near conversion;
- mobile media reduction while preserving information order;
- visible template/CMS residue that must be quarantined from core Design DNA.

## Global composition

Desktop:
- fixed navigation around 66px;
- centered 1200px main canvas;
- home hero approximately 800px;
- large section-title blocks separated from operational/product surfaces;
- route pages use simpler centered heroes and shorter narrative stacks.

Mobile:
- fixed navigation around 60px;
- one-column flow;
- standard route H1 becomes 36px / 43.2px;
- home preserves an oversized centered VoxAI identity around 114px;
- multi-column proof grids stack vertically;
- expensive or secondary video is reduced before semantic content is removed.

## Typography

- Cal Sans: route/page display identity.
- Inter Display: secondary display and UI hierarchy.
- Inter: readable body/product copy.
- Poppins: selected component/UI treatment.
- Fragment Mono: source-loaded technical/utility role.

Transfer the role separation, not the literal font stack.

## Color + material

- shell: #030014;
- primary text: white;
- muted text: translucent white;
- product accent: approximately #0f63b8;
- expressive accent: approximately #f73e9e;
- semantic green/orange/red appears inside operational mock UI;
- translucent white borders/surfaces create hierarchy without turning every section into a card.

The dark shell is chromatic purple/navy rather than default black.

## Motion + rendering

VoxAI uses Framer DOM/media motion rather than a permanent custom WebGL renderer.

Observed richness comes from:
- animated operational UI cards;
- ticker/logo movement;
- lazy video surfaces;
- sliders/carousels;
- animated status lines;
- hover/action feedback;
- staggered product-like micro-scenes.

This reinforces Cinematic Without Heavy Rendering: perceived ambition can come from composition, media, product theater, and motion hierarchy without a continuous canvas world.
## Route-Family Density Ladder

Representative desktop heights at approximately 1905x889:
- Home: ~13,887px
- About: ~6,049px
- Pricing: ~3,575px
- Integrations index: ~6,524px
- Blog index: ~3,862px
- Blog detail: ~5,305px
- Case-study index: ~2,311px
- Case-study detail: ~4,356px
- Integration detail: ~2,997px
- Contact: ~2,292px
- Privacy: ~3,551px
- Terms: ~4,309px
- 404: ~1,493px

This forms a deliberate density ladder: home teaches broadly, indexes enable discovery, detail pages prove one object, pricing/contact compress decision-making, and legal/404 perform trust/recovery jobs without inheriting homepage-level spectacle.

## Home - operational product theater

The home is the densest route and acts as the system router.

Observed sequence:
1. identity/hero + version signal + primary/secondary CTA;
2. trusted-team/logo ticker;
3. How It Works;
4. Key Features;
5. The Solution;
6. stats;
7. VoxAi Power;
8. news/blog;
9. mobile assistant capabilities;
10. case-study previews;
11. more outcome stats;
12. primary CTA;
13. pricing;
14. integration ecosystem;
15. testimonials;
16. FAQ;
17. final CTA/newsletter/footer.

The strongest design move is the use of operational micro-scenes rather than only feature icons.

Examples:
- workflow bottleneck analysis;
- integrations list embedded in workflow context;
- changelog/update simulation;
- Count hours work -> Add to CRM -> Send invoice;
- role-based AI-agent roster;
- outreach methods across LinkedIn/email/messaging/calling/SMS;
- expense/data-analysis mock UI;
- mobile assistant feature surfaces.

These micro-scenes turn abstract AI automation claims into something visitors can mentally simulate.

## About - trust satellite

Observed:
- H1 About VoxAi;
- Driving smarter growth through AI innovation;
- company numbers;
- team;
- testimonials;
- CTA/footer.

About does not repeat the full home product narrative. It exists to answer who/why/trust questions.

## Pricing - compressed decision route

Live rendered plans during audit:
- Starter: $99;
- Pro: $199;
- Enterprise: $599.

Sequence:
- pricing thesis;
- three plans;
- stats;
- testimonials;
- conversion CTA;
- newsletter/footer.

The page is intentionally much shorter than home. This is a good example of route-specific density.

Do not transfer the exact prices. Hidden/default/search-index variants exposed other values, so pricing data itself is not a trustworthy reusable fact.

## Integrations index - taxonomy before logo wall

H1: Connect VoxAi to Your Stack in Minutes.

Observed categories:
- Telephony;
- Payment;
- Data Platform;
- Customer Support & CX;
- CRM;
- Automation;
- Scheduling;
- Analytics & QA.

The catalog is useful because visitors can browse by job/category rather than scanning one undifferentiated logo cloud.

## Integration Detail as Implementation Proof

Representative live route: /integrations/twilio-elastic-sip-trunking.

Rendered information architecture:
1. tool logo / identity;
2. H1 Twilio Elastic SIP Trunking;
3. one-line job statement;
4. Introduction;
5. Features;
6. Installation;
7. operational metadata;
8. Setup Webhook action;
9. Contact Sales fallback;
10. Related Integrations;
11. final CTA/footer.

Metadata fields observed across canonical records include:
- setup time;
- difficulty;
- category;
- connection/type.

Canonical-looking records in the search index include PostHog, Twilio, Zapier, Stripe, and HubSpot CRM.

This is stronger than a logo wall because it can answer what the integration does, how it connects, how difficult setup is, and what the visitor should do next.

However the positive page grammar is undermined by content-binding errors described below. Transfer the architecture, not the literal data.

## Case-study family

Index H1: Explore our case studies.

Six detail routes use a consistent proof grammar:
- route identity / hero;
- client/industry/timeline metadata;
- Challenge;
- implementation/solution bullets;
- three quantitative outcomes;
- related cases;
- conversion CTA.

Unique metric sets found in the search index include:
- Identity: 84%, -75%, $62,000;
- After-hours emergency: +115%, <3 seconds, $180,000;
- Enterprise onboarding: -52%, 40 hrs/week, +28%;
- Voice checkout: 4.8 / 5.0, 6%, 120,000+;
- Unstructured voice analytics: -80%, 99.4%, 9x faster;
- Driver check-ins: 99.1%, 3.5 hrs/day, 92%.

These metrics are template/demo evidence and must not be reused as real-world claims.

## Blog family

Blog index H1: The VoxAi Blog: Voice AI News, Reviews & Tutorials.

The index separates featured content from the broader News & Update list.

Eight detail routes use a shared editorial frame:
- category/author/date;
- article title;
- long-form sections;
- related articles;
- newsletter/footer.

Important residue evidence:
- several voice-related titles share near-identical long-form bodies;
- two routes titled Bridging Design & Development contain materially different agency/branding-style copy;
- related-content metadata repeats generic/template text.

The editorial route family is useful structurally but its content corpus is not trustworthy product proof.

## Contact

H1: Have a Project in Mind?Let’s Talk.

Contact is a short conversion surface with form, FAQ, and global footer rather than another feature page.

## Legal

Privacy and Terms hydrate into long-form legal routes with document metadata.

Residue observed:
- references to the older voxaii.framer.website domain;
- placeholder legal variables in Terms such as currency/state/city-jurisdiction placeholders.

These are credibility defects and belong in Template Residue Quarantine.

## 404

The indexed utility route uses branded recovery:
- Oops! Page Not Found;
- explanation;
- Go Back Home;
- newsletter/global footer.

It is useful utility behavior but not a core product route.
## Route-Family Binding Integrity

The most important negative lesson from the full-site audit is that a polished detail template does not guarantee a trustworthy route family.

### Case-study binding drift

Several case-study routes have unique document titles, unique challenge/solution bodies, and unique metrics, but the visible/search-index hero identity repeatedly falls back to:

Automating 24/7 Identity Verification and Fraud Triage with Voice AI

and a shared VaultPay-style summary.

This means the route slug/title/metrics can describe one case while the H1/summary describes another.

### Integration binding drift

The live Twilio Elastic SIP Trunking route correctly identifies Twilio in the H1, but its Introduction, Features, and Installation instructions describe HubSpot CRM behavior such as contact creation, transcript sync, pipeline automation, CRM OAuth, and field mapping.

Several copy routes also expose:
- Tool Name;
- tool.com;
- copy / copy-copy suffixes;
- mismatched category/type combinations;
- reused PostHog or HubSpot descriptions.

### Blog duplication

Multiple article titles map to near-identical voice-vs-typing bodies. The two Bridging Design & Development routes also demonstrate template content drift.

### Legal residue

Old-domain references and unresolved jurisdiction/currency placeholders remain public.

### SSR / hydration inconsistency

Programmatic fetches of some dynamic routes initially exposed minimal/default shells, while live browser navigation hydrated them into complete detail pages. Initial/server output and hydrated identity should therefore both be part of route-family QA.

These failures motivate the reusable Route-Family Binding Integrity rule:

URL/slug + canonical + title/description + H1 + summary + media + metadata + body + metrics + related items + CTA must resolve to the same CMS record unless a field is intentionally global.

A whole-site audit should use duplicate-content canaries and complete route inventories rather than assuming one representative detail proves the family.

## Template Residue Quarantine

VoxAI contains useful template grammar and obvious unfinished artifacts at the same time.

Quarantine rather than promote:
- Get Template / Buy For $129 template-vendor chrome;
- Framer editor/remix surface;
- integration copy/copy-copy routes;
- Tool Name / tool.com placeholders;
- duplicated article bodies;
- incorrect common case-study H1/summary;
- wrong connector installation text;
- old-domain legal references;
- unresolved legal placeholders;
- repeated generic footer copy unrelated to voice AI.

Full-site distillation means complete accounting plus selective weighting.

## Responsive Fidelity Substitution

Representative mobile audit at 390x844 covered:
- Home;
- Pricing;
- Integrations;
- blog detail;
- case-study detail;
- Contact.

All representative routes had no document-level horizontal overflow.

Observed mobile transformations:
- fixed navigation compresses to roughly 60px;
- standard route H1s become 36px / 43.2px and center;
- home retains an oversized centered VoxAI identity around 114px;
- product/proof grids become vertical;
- desktop video/product-media surfaces are reduced or omitted;
- semantic section order and conversion actions remain.

This is Responsive Fidelity Substitution: the expensive mechanism changes, but the route still performs the same narrative/commercial job.

## Commercial Core + Trust Satellites

VoxAI reinforces a useful full-site architecture:

- Home carries the heaviest teaching and demonstration burden.
- Pricing compresses package selection.
- Integrations converts ecosystem claims into setup proof.
- Case studies convert capability into outcome narratives.
- Blog supports education/discovery.
- About supports organization trust.
- Contact supports high-intent conversion.
- Legal supports risk/trust.
- 404 supports recovery.

Do not force every trust satellite to repeat the home feature stack.

## Operational Pipeline Storytelling

The home repeatedly communicates AI value as a sequence of operational states rather than abstract benefits.

Transferable examples:
- detect bottleneck -> analyze workflow;
- connect existing tools -> automate handoff;
- receive/update status -> continue operation;
- trigger task -> sync CRM -> send invoice;
- find lead -> choose outreach channel -> act;
- collect interaction data -> expose analysis.

Use operational pipelines when the product promise is automation/orchestration. They make causality visible.

## Credibility Through Route Ecosystem

Strong AI/SaaS credibility can be distributed across the route ecosystem:
- product/capability proof on home;
- concrete connector/setup proof in integrations;
- packaging clarity in pricing;
- outcome grammar in cases;
- education in blog;
- legal/trust surfaces.

The important caveat from VoxAI is that route breadth only increases credibility when content bindings are correct. More routes with wrong records reduce trust faster than a smaller accurate site.

## Design DNA summary

### Composition
- deep, long-form commercial home;
- centered route heroes;
- 1200px desktop shell;
- product mock UI used as content, not merely decoration;
- short specialized conversion/trust routes;
- consistent global nav/footer.

### Typography
- expressive rounded display identity via Cal Sans;
- quieter Inter-family product copy;
- occasional technical/utility role;
- strong scale reduction on mobile while home identity stays exceptional.

### Color + material
- purple-black chromatic shell;
- white/translucent-white hierarchy;
- blue primary product energy;
- pink secondary accent;
- semantic colors confined to operational UI.

### Media
- illustration/image-heavy hero;
- lazy bounded videos;
- DOM product theater;
- no need for a persistent WebGL canvas.

### Motion
- Framer motion around product scenes;
- ticker/carousel behavior;
- animated status/process lines;
- restrained enough that content remains the main narrative.

### Narrative + proof
- claim -> operational mechanism -> capability -> ecosystem -> outcomes -> package -> testimonial -> CTA;
- integration and case families are the main off-home proof systems.

### Responsive
- preserve commercial order and brand scale hierarchy;
- remove/reduce desktop media before removing meaning;
- stack complex cards/details;
- zero representative horizontal overflow at 390x844.

## What to adopt

- dense home paired with shorter specialized routes;
- operational micro-scenes for automation products;
- taxonomy-led integration discovery;
- Integration Detail as Implementation Proof;
- route-family density ladder;
- Commercial Core + Trust Satellites;
- Responsive Fidelity Substitution;
- one chromatic shell across a large route ecosystem;
- separate capability, integration, case, education, pricing, contact, and trust jobs.

## What to adapt

- exact number of route families;
- home depth;
- dark vs light shell;
- hero scale;
- media/video density;
- integration metadata schema;
- case-study metrics/proof structure;
- blog/editorial cadence;
- mobile media reductions.

## What to avoid

- cargo-culting the purple/blue/pink AI palette;
- using fake operational UI when real product proof is available;
- copying Cal Sans/Inter as a default AI stack;
- exposing template-vendor purchase chrome in a finished product;
- public copy/copy-copy CMS records;
- placeholder integration domains or technical metadata;
- duplicated articles under different titles;
- unique case metrics under a shared wrong H1;
- connector pages whose setup instructions belong to another tool;
- legal pages with old domains or unresolved variables;
- assuming one detail page proves a dynamic route family.

## Best-fit reference use

Strong fit:
- AI/SaaS marketing systems;
- voice/automation products;
- products with many integrations;
- products that need both case-study and editorial ecosystems;
- Framer templates that need route-family cleanup before production;
- dark product sites seeking richness without heavy 3D.

Weak fit:
- minimal single-feature utilities;
- documentation-first developer products where code proof should dominate;
- luxury/editorial brands;
- transaction-first ecommerce;
- experiences whose identity genuinely depends on one authored WebGL world.

## Regression questions

- Was the complete 36/36 sitemap audited, not only home?
- Was /404 accounted for separately as an indexed utility route?
- Are all 6 case-study detail pages represented?
- Are all 8 blog detail pages represented?
- Are all 13 integration detail pages represented?
- Are the 5 canonical integration records separated from 8 residue/copy routes?
- Do route-family fields resolve to the same underlying record?
- Does a duplicate-content canary detect suspiciously reused bodies/heroes?
- Are SSR/default and hydrated identities consistent?
- Are integration setup instructions specific to the named connector?
- Are case-study hero, body and metrics describing the same case?
- Are legal placeholders and old domains removed before production?
- Does mobile preserve route purpose while reducing media cost?
- Is there no document-level horizontal overflow at 390x844?
- Does the final design transfer the system rather than cloning VoxAI's exact visual skin?

Pass only when the reference is treated as a full route ecosystem with both its strengths and its CMS/template failure modes.
