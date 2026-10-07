# NovaOS - full-site distilled design intelligence

Source: https://novaos.framer.website/
Audit date: 2026-10-06
Coverage: 23/23 sitemap URLs

Audit scope: robots.txt and sitemap discovery, Framer search index cross-check, every public page HTML, same-origin internal-link graph, all top-level route families, all 6 career detail pages, all 6 blog article pages, shared design tokens, Framer breakpoint branches, custom runtime scripts, desktop rendered checks, mobile 390x844 rendered checks, forms, accordions, product-proof surfaces, and document-level overflow behavior.

This is a full-site profile. It is not a homepage-only read.

## Coverage manifest

Top-level routes:
- /
- /pricing
- /company
- /blog
- /careers
- /integrations
- /contact
- /faq
- /book-a-demo
- /privacy-policy
- /terms

6 career detail pages:
- /careers/senior-runtime-engineer
- /careers/senior-guardrails-architect
- /careers/staff-product-designer
- /careers/enterprise-solutions-architect
- /careers/senior-frontend-engineer
- /careers/senior-optimization-engineer

6 blog article pages:
- /blog/designing-deterministic-guardrails
- /blog/zero-retention-knowledge-retrieval
- /blog/optimizing-token-economics
- /blog/why-most-ai-features-fail
- /blog/northstar-global-pr-triage
- /blog/ephemeral-state-machines

The Framer search index exposes the same 23 route keys, and the full internal-link graph did not reveal an additional public route outside the sitemap.

## Landscape classification

Primary: template commodity, audited.
Secondary: product precision / enterprise AI SaaS.

This site is explicitly presented as a Framer template through its visible demo bar, including a Get This Template action. That makes it useful as a coherent baseline and skin source, but not as evidence that its exact visual vocabulary is distinctive or proprietary to a real product.

Use it to learn consistency, route coverage, proof sequencing, responsive product-media treatment, forms, and enterprise trust scaffolding. Do not treat generic light-SaaS conventions as premium originality merely because the execution is polished.

## Executive DNA

NovaOS is a light enterprise-AI marketing system built around a simple proposition: AI becomes credible when the site shows the operational chain around it, not only a chat box.

Its transferable full-site system is:

- centered, restrained hero framing with one blue brand accent;
- soft off-white shell, white content surfaces, dark ink, muted neutral support colors;
- product proof shown as realistic operational surfaces rather than generic feature icons;
- a repeated architecture story: model selection, context assembly, agents, connected systems, workflows, and outcomes;
- consistent 16px-ish product/card surfaces with pill actions;
- route-specific bodies followed by reusable trust/conversion modules;
- enterprise credibility reinforced by integrations, company metrics, technical writing, legal/security pages, careers, forms, and pricing;
- mobile preserves product-proof readability by clipping oversized UI surfaces inside stable containers rather than shrinking every interface to fit;
- motion remains controlled: Framer appear effects plus Lenis smooth scrolling, both with reduced-motion awareness.

The highest-level lesson is not blue-on-white SaaS styling. It is: **show the operating system around the AI claim, and let the entire route ecosystem prove that the product can exist inside a serious company.**

## Evidence Confidence

### Source-confirmed platform and runtime

- Generator metadata: Framer 95da0c7.
- Every audited page loads the same Framer search index URL.
- Shared runtime loads Framer event tracking, the generated Framer main module, and Lenis 1.3.26.
- Custom Lenis initialization uses lerp: 0.085, smoothWheel: true, and autoRaf: true.
- Custom smooth-scroll code exits when prefers-reduced-motion: reduce matches.
- The Lenis integration observes html/body style/class mutations and pauses smoothing while overflow is locked, then resumes it after menus/overlays unlock the page.
- Framer optimized appear animations also check prefers-reduced-motion.
- Primary responsive branches are source-confirmed at:
  - desktop: min-width 1200px;
  - tablet: 810px through 1199.98px;
  - mobile: max-width 809.98px.
- robots.txt allows crawling and points to /sitemap.xml.
- /llms.txt is not provided.
- The public sitemap contains 23 URLs.
- The Framer search index contains the same 23 route keys.
- No additional public same-origin route was found through the complete internal-link graph.

### Source-confirmed visual tokens

Shared Framer color tokens include:

- primary blue: #0082de;
- light blue: #5bb8f5;
- dark ink: #161816;
- muted gray: #757677;
- secondary gray: #a7a9ac;
- white: #fff;
- soft background: #f7f7f7;
- alternate soft background: #f3f4f2;
- hairline neutral: #e4e7e2.

Loaded font families include:

- DM Sans Variable;
- DM Sans;
- Geist;
- Inter.

Observed role split:

- DM Sans Variable carries the major marketing/display headings;
- DM Sans carries article/legal subheadings and some editorial body roles;
- Geist appears in navigation/footer/template-demo controls and utility interface copy;
- Inter remains available as a Framer/system fallback.

### Observed desktop system

At a 1440x900-class viewport:

- homepage document height measured roughly 7.5k px;
- homepage H1 measured about 62px / 68px, centered, DM Sans Variable, weight 400, with negative tracking;
- most top-level route H1s measured about 46px / 52px;
- article/legal H3s measured about 30px / 36px;
- home begins with a subtle blue-to-transparent gradient rather than a full-page colored hero;
- main cards and product proof surfaces commonly use 16px radius;
- FAQ items use a smaller roughly 12px card radius;
- primary dark CTAs and white secondary CTAs use 999px pill geometry;
- pricing uses three roughly equal cards, with the Pro card taking the blue emphasis state;
- integrations uses a three-column grid of white 16px cards;
- careers benefits use the same three-column white-card grammar;
- demo/contact forms use large white card/form surfaces;
- article pages return to quieter editorial composition rather than forcing product cards into long-form content;
- legal pages retain the same shell but use clear numbered/sectioned content instead of decorative trust badges.

### Observed mobile system

Audited at 390x844 across home, pricing, integrations, contact, careers, one career detail page, one blog article, legal, and FAQ route families.

Across these rendered families:

- viewport width remained exactly 390px;
- no document-level horizontal overflow was observed;
- main top-level H1s reduce to about 27px / 32px;
- home H1 remains slightly larger at about 34px / 39px;
- desktop multi-column pricing, integrations, careers, and form layouts stack into one-column 350px-wide surfaces;
- pricing comparison content becomes a tall readable single-column comparison surface rather than a squeezed desktop table;
- contact and career application forms remain readable inside approximately 350px outer cards with about 302px form width;
- legal content becomes one long contained card rather than a fragile multi-column layout;
- FAQ maintains readable 21px / 27px question typography;
- job details reorder into role facts, role content, then application;
- the site keeps the same blue/ink/off-white identity instead of switching to an unrelated mobile template.

## Design DNA

### Composition

NovaOS combines a quiet global shell with contained product/evidence cards.

Repeated composition rules:

- centered top-level page titles;
- generous blank space before dense product proof;
- section copy first, operational UI proof second;
- card grids for comparable repeated entities;
- long-form pages use editorial flow rather than the card grid;
- conversion surfaces reappear at the end of route families;
- white cards sit on soft neutral backgrounds instead of heavy drop shadows.

The system has enough card containment to feel operational, but the best parts are not the cards themselves. The coherence comes from repeating the same hierarchy, type roles, accent semantics, and proof language across different route types.

### Typography

The typography system is restrained:

- display: DM Sans Variable, regular weight, tight/negative tracking, moderate scale;
- editorial subheads: DM Sans around 30px desktop;
- supporting UI/navigation: Geist or smaller DM Sans;
- copy avoids extremely tiny mono labels or decorative type contrast.

Transfer the calm role hierarchy. Do not copy the exact DM Sans + Geist pair as a default recipe.

### Color + material

The material system is deliberately low-noise:

- #f7f7f7 / #f3f4f2-like shell;
- white proof/cards/forms;
- #161816-like ink;
- one bright blue accent family;
- soft neutral dividers;
- little reliance on heavy shadow.

The blue Pro pricing card shows that the accent can temporarily own a whole surface when there is a real selection/emphasis reason. Most of the site remains neutral.

### Product evidence

Homepage proof is built from operational UI states such as:

- Choose a Model;
- Expansion context assembled;
- Revenue Agent;
- Executive Report;
- Connected Data;
- Expansion Opportunity Pipeline.

This is more convincing than a generic abstract feature illustration because each surface suggests a state in a real system.

The best transferable property is **role-specific evidence**: each proof surface demonstrates one part of the operating chain.

## Operational Pipeline Storytelling

For complex AI/infrastructure products, tell the product story as an operational pipeline rather than a flat list of capabilities.

A useful abstract chain is:

**model choice -> context/data -> agent/workspace -> connected tools -> multi-step workflow -> observable business output**

NovaOS repeatedly reinforces this logic across homepage product surfaces, integrations, pricing/capability framing, technical blog topics, and enterprise deployment copy.

Transfer rules:

- give each stage one clear responsibility;
- show inputs and outputs, not only internal intelligence;
- connect the marketing explanation to believable UI or system evidence;
- let later routes deepen the same pipeline instead of inventing unrelated product stories;
- do not force this pattern onto simple single-purpose products.

## Proof Surface Cropping

On mobile, some homepage product-proof surfaces remain materially wider than the 390px viewport: observed proof layers around 448px and 539px were nested inside roughly 350px containers with overflow hidden/clip and 16-24px radius.

The document itself still had no document-level horizontal overflow.

This is a deliberate alternative to miniaturizing complex product UI until the text and structure become meaningless.

Transfer rules:

- preserve readable product-UI scale when shrinking would destroy the proof;
- choose the most important focal region for the crop;
- clip inside a clearly bounded proof viewport;
- keep the page body horizontally stable;
- do not hide critical actions/content outside the crop;
- for interactive demos, provide pan/scroll/focus affordances if the offscreen content is necessary.

Proof Surface Cropping is best for marketing evidence, not for task UI where users need the whole interface.

## Credibility Through Route Ecosystem

Enterprise trust is distributed across the entire site, not concentrated in one testimonial block.

NovaOS reinforces the core product promise through:

- /integrations: proof that the product fits real systems of record;
- /pricing: operational limits and packaging;
- /company: company thesis, leadership, and platform metrics;
- /blog plus 6 technical articles: architecture-level competence;
- /privacy-policy and /terms: security, deployment, retention, compliance, SLA and ownership language;
- /careers plus 6 role pages: evidence of the disciplines the company claims to build;
- /contact and /book-a-demo: enterprise buying paths;
- /faq: repeated objection handling.

Transfer rule: when the product asks for enterprise trust, design the route ecosystem so adjacent pages independently support the same operational claim.

Do not fabricate compliance, company metrics, technical depth, customer results, or legal guarantees merely to make the route ecosystem look mature.
## Route-Family Map

### Home

Primary job: turn an abstract autonomous-AI promise into an operating-system story.

Observed sequence:

- release/update pill;
- centered hero with Start Free + Book Demo;
- integration/logo context;
- model/context/action product proof;
- workspace/data/workflow proof;
- use-case section;
- pricing preview;
- FAQ;
- final dark CTA;
- footer.

The transferable lesson is staged proof escalation: promise first, then increasingly concrete operational evidence.

### Pricing

Primary job: packaging and capability comparison.

Observed:

- centered pricing thesis;
- Starter / Pro / Business cards;
- Pro highlighted in blue;
- a deeper capability-comparison surface;
- FAQ;
- final CTA.

Mobile stacks the three plan cards and converts capability comparison into a tall readable card rather than compressing a wide comparison into illegibility.

### Company

Primary job: make the company itself support product credibility.

Observed:

- operating-layer thesis;
- longer future-of-work statement;
- platform metrics;
- use-case/proof content;
- leadership;
- FAQ;
- final CTA.

Company content is not treated as an unrelated culture page; it repeats the product's operational thesis.

### Blog index

Primary job: technical authority and content discovery.

Observed:

- centered editorial H1;
- six article entries;
- architecture/engineering-heavy topics;
- final conversion tail.

The article topics deliberately align with the product's risk/cost/privacy/runtime claims.

### Careers index

Primary job: company credibility + recruiting.

Observed:

- recruiting thesis;
- six benefit cards;
- open positions;
- final conversion tail.

The roles themselves reinforce the product architecture: runtime, guardrails, product design, enterprise solutions, frontend, optimization.

### Integrations

Primary job: prove the product belongs inside a real company stack.

Observed cards include:

- Google Drive;
- Notion;
- Slack;
- GitHub;
- Salesforce;
- HubSpot;
- Jira;
- Microsoft Teams;
- Linear.

Desktop uses a three-column card grid; mobile stacks 350px cards.

### Contact

Primary job: general enterprise inquiry.

Observed form fields:

- name;
- work email;
- company;
- topic;
- message.

The form lives in a large white card and is followed by FAQ + final CTA.

### FAQ

Primary job: central objection handling.

Observed accordion items include execution tokens, data/model training, token quota overage, private-cloud/self-hosting, and plan changes.

The same FAQ component is reused across multiple route families, so the dedicated FAQ page also acts as a central canonical support surface.

### Book a Demo

Primary job: high-intent enterprise conversion.

Observed form fields include:

- name;
- email;
- company;
- job title;
- company size;
- country;
- deployment/context note.

A companion card explains what happens during the 30-minute session.

### Privacy Policy + Terms

Primary job: operational/legal trust.

Privacy topics include:

- zero model training;
- encryption;
- tenant isolation/private VPC;
- SOC 2 / GDPR / HIPAA;
- data retention/export/deletion;
- security contact.

Terms topics include:

- MSA/acceptance;
- platform license/acceptable use;
- IP/output ownership;
- token/subscription billing;
- SLA/support;
- liability/governing law.

These pages retain the same type/color/card shell rather than becoming unstyled legal dumps.

### Career detail template

All 6 career detail pages were checked.

Stable structure includes:

- role title;
- location + employment type;
- Role Details;
- Role Overview;
- Responsibilities;
- Requirements;
- Compensation & Benefits;
- Apply Now form;
- shared final CTA/footer.

Observed application fields include full name, email, profile URL, optional Why NOVA, and hidden role/context fields.

Mobile stacks role facts, role content, and application in one readable flow.

### Blog article template

All 6 blog article pages were checked.

Stable structure includes:

- article title;
- intro/metadata area;
- long-form article body;
- three major editorial subheads;
- occasional callout/quote;
- Read More Articles;
- related article cards;
- shared final CTA/footer.

This is deliberately quieter than the homepage/product surfaces.

## Shared Conversion Tail

Across many commercial/marketing routes, the page-specific body eventually hands off to a reusable trust/conversion tail:

1. FAQ or objection handling when relevant;
2. dark final CTA: Put AI to work across your entire company;
3. consistent footer navigation.

Transfer this only when the repeated tail answers genuine shared objections. Reusing a conversion tail is valuable because it lets route bodies specialize while preserving a consistent close.

Do not repeat identical FAQ/CTA modules mechanically on every route when the route's job or audience requires a different conclusion.

## Responsive Behavior

### Breakpoint ownership

Source-confirmed Framer breakpoints use three broad branches:

- desktop >= 1200px;
- tablet 810-1199.98px;
- mobile <= 809.98px.

The generated HTML can contain multiple SSR variant branches, which explains repeated headings in source extraction. Audit the visible rendered branch before interpreting duplicate source text as duplicate content.

### Mobile composition behavior

Observed at 390x844:

- global page width stays 390px;
- no document-level horizontal overflow;
- navigation condenses to logo/home/start-free level rather than preserving full desktop nav;
- most 3-column grids become single-column;
- primary cards become about 350px wide;
- forms become about 302px wide inside 350px shells;
- top-level headings reduce to roughly 27px / 32px;
- home gets a larger 34px / 39px headline;
- product proof may preserve an oversized internal canvas and crop it;
- content order remains recognizable;
- CTA and footer remain available.

### Responsive proof rule

The site uses two different mobile strategies depending on content type:

- **reflow** for pricing cards, integration cards, careers benefits, forms, legal content, and job details;
- **crop/contain** for product UI evidence where scaling would destroy legibility.

This is a useful reminder that one responsive mechanism should not own every component.

## Motion + Scroll

### Framer appear effects

Framer's optimized appear pipeline is present and checks reduced-motion preferences.

Use the transferable rule:

- entrance motion should help initial hierarchy;
- it must not be required to reveal essential content;
- reduced-motion should receive the settled state.

### Lenis lifecycle

Source-confirmed custom integration:

- Lenis 1.3.26;
- lerp: 0.085;
- smoothWheel: true;
- autoRaf: true;
- disabled when prefers-reduced-motion: reduce;
- paused when html/body overflow is locked;
- resumed after the lock clears via MutationObserver.

The transferable lesson is lifecycle ownership, not the exact lerp value.

If smooth scrolling is introduced:

- honor reduced motion;
- coordinate with menu/modal scroll locks;
- do not run two competing scroll owners;
- stop/resume predictably;
- verify keyboard, anchor, and browser-navigation behavior.

## Template Commodity Lessons

Because NovaOS exposes a Get This Template demo action, treat these as commodity patterns unless the new product gives them product-specific meaning:

- centered SaaS hero;
- blue accent on a white/off-white shell;
- rounded white feature cards;
- pill CTAs;
- integration-logo/card grid;
- three-tier pricing;
- FAQ accordion;
- dark end-of-page CTA.

These patterns are not bad. They are familiar and often usable. But simply recoloring them does not create distinctive art direction.

Use the Template Archetype Firewall:

- preserve the coherent scaffold when execution capability is limited;
- require at least one structural differentiator in proof mechanism, content model, typography, composition, or interaction;
- prefer real product evidence over a decorative dashboard skin.

## Cross-Site Synthesis

Compared with audited Resend:

- both are developer/technical products that use product evidence to support claims;
- Resend leans on code/API proof;
- NovaOS leans on operational UI, integrations, workflows, and enterprise route breadth;
- both benefit from responsive fidelity rather than decorative effects.

Compared with audited Tokenmeter:

- Tokenmeter builds credibility through data provenance and confidence;
- NovaOS builds credibility through operational specificity and route ecosystem breadth;
- both show that trust can be a site architecture problem rather than a testimonial-section problem.

Compared with Refokus:

- Refokus concentrates identity into a signature immersive stage;
- NovaOS distributes confidence across many conventional product/trust surfaces;
- these are different excellence modes and should not be blended indiscriminately.

## Adopt / Adapt / Avoid

| Pattern | Decision | Why |
|---|---|---|
| Operational Pipeline Storytelling | Adopt for complex AI/infrastructure products | Makes abstract autonomy understandable as a sequence of responsibilities. |
| Proof Surface Cropping | Adopt selectively for mobile marketing evidence | Preserves UI legibility without destabilizing the document. |
| Credibility Through Route Ecosystem | Adopt for enterprise products | Trust is stronger when adjacent routes reinforce the same claim. |
| Shared Conversion Tail | Adapt | Useful for coherent route endings; can become repetitive if applied blindly. |
| Reduced-motion-aware Lenis lifecycle | Adapt | Good runtime discipline if smooth scrolling is justified at all. |
| 16px white cards + blue accent + pill CTAs | Adapt heavily | Coherent but highly template-common. |
| Three-tier pricing with colored middle plan | Adapt only when packaging supports it | Familiar hierarchy, not a universal requirement. |
| Exact NovaOS color tokens, fonts, mockups, copy, leadership metrics | Avoid | Template/site identity and content-specific evidence. |

## Best-Fit Briefs

- enterprise AI platforms;
- agent orchestration products;
- automation SaaS;
- workflow platforms;
- B2B products with integrations, pricing, security/legal and technical content;
- product sites where lower-capability execution needs a coherent light-SaaS scaffold.

## Weak-Fit Briefs

- luxury/editorial brands;
- entertainment/game launches;
- image-led consumer products;
- highly transactional ecommerce;
- products without believable operational UI proof;
- developer APIs where code is a much stronger proof mechanism than product dashboards.

## Regression Questions

- Was every public sitemap route accounted for?
- Were all CMS detail templates checked, not sampled once and assumed?
- Does the homepage explain the operating chain rather than only listing AI features?
- Do product proof surfaces show believable state and outputs?
- On mobile, is complex proof cropped/contained intentionally rather than miniaturized?
- Is there no document-level horizontal overflow?
- Do pricing, integrations, company, blog, legal/security, careers and forms reinforce the same enterprise claim?
- Is the site-specific body allowed to vary while navigation, FAQ/CTA/footer and visual tokens stay coherent?
- Is smooth scrolling disabled for reduced-motion users and paused under scroll locks?
- Are template-common patterns being used as scaffold rather than mistaken for originality?
- If the exact blue, fonts, card radius, mockup content and copy disappear, does the new site still have a product-specific proof mechanism?

Pass only when the result uses NovaOS as a coherent baseline teacher without shipping a blue Framer-template clone.
