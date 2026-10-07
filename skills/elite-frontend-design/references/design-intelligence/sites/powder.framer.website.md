# Powder - full-site distilled design intelligence

Source: https://powder.framer.website/
Audit date: 2026-10-07
Coverage: 21/21 sitemap URLs

Audit scope: robots.txt and sitemap discovery, Framer search-index cross-check, complete same-origin internal-link graph, HTML/DOM structure for every public route, all 10 blog detail pages, shared generated CSS/tokens, desktop runtime inspection, mobile 390px checks for home/pricing/get-started/blog/legal families, sticky/fixed behavior, form structure, and template residue classification.

This is a whole-site profile. It is not a homepage-only read.

## Coverage manifest

Top-level / utility routes:
- /
- /blog
- /about
- /changelog
- /get-started
- /pricing
- /terms-of-use
- /cookie-policy
- /privacy-policy
- /page
- /404

10 blog detail pages:
- /blog/how-ai-agents-are-replacing-tab-heavy-workflows
- /blog/building-trust-in-ai-outputs-why-source-attribution-matters
- /blog/from-support-tickets-to-resolved-issues-in-under-two-minutes
- /blog/the-architecture-behind-real-time-agent-memory
- /blog/5-prompts-every-sales-rep-should-save
- /blog/why-we-built-powder-as-a-conversation-first-platform
- /blog/connecting-your-stack-a-practical-integration-guide
- /blog/the-rise-of-agentic-workflows-in-enterprise-teams
- /blog/how-powder-handles-data-privacy-and-security
- /blog/reducing-onboarding-time-with-contextual-ai

The Framer search index exposes the same 21 route keys. A full same-origin internal-link crawl found no additional public route outside that set.

## Landscape classification

Primary: template commodity, audited.
Secondary: premium dark SaaS / AI agent product proof.

The page title and metadata explicitly describe Powder as an AI Agent & SaaS Website Template for Framer. The rendered site also exposes a fixed "Remix for free" control. Treat Powder as a high-quality template baseline, not as proof that its exact dark-card grammar is distinctive brand IP.

Use it to learn:
- how a dark SaaS template can keep one coherent product shell across a very long homepage;
- how to turn a chat/agent product from conversation into trusted action;
- how sticky product proof can own desktop narrative without being forced onto mobile;
- how CMS blog, changelog, pricing, legal, about, and conversion routes share one system;
- how to quarantine template-only residue instead of promoting it into product DNA.

## Executive DNA

Powder is a dark AI-agent marketing system built around one repeated promise: conversation should not stop at answers; it should produce sourced, actionable work.

Its strongest transferable system is:

- near-black shell with translucent charcoal layers and subtle warm/teal accents;
- large but not theatrical sans typography paired with mono utility/details;
- realistic conversation/workspace UI reused as the core proof language;
- a progression from shared context -> trusted answer -> action -> ongoing insight;
- desktop sticky capability storytelling inside one long proof chapter;
- integration, changelog, metrics, pricing, FAQ, testimonials, blog, and conversion routes reinforcing the same operational product story;
- restrained rounded surfaces and translucent borders instead of glow-heavy spectacle;
- mobile release of desktop sticky storytelling while preserving content order;
- template residue explicitly separated from the reusable system.

The lesson is not "make it black with dashboard cards." It is: **make the agent's journey from intent to sourced output to action inspectable, then keep the rest of the site aligned with that operating model.**

## Evidence Confidence

### Source-confirmed platform

- Generator metadata: Framer a050651.
- robots.txt allows crawling and points to /sitemap.xml.
- /sitemap.xml contains 21 URLs.
- Framer search index contains the same 21 route keys.
- /llms.txt is not provided.
- Standard primary Framer breakpoint branches appear at 810px and 1280px.
- /get-started and /404 additionally expose a 1024px branch in generated CSS.
- Every main content route uses the same generated Framer runtime family.

### Source-confirmed typography

Loaded/generated font families include:

- Inter Variable;
- Inter;
- Inter Display;
- Fragment Mono.

Observed role split:

- Inter / Inter Display carry marketing headlines and large metrics;
- Fragment Mono is available for compact technical/utility labeling;
- the system relies on weight, scale, opacity, and surface contrast more than on dramatic font pairing.

### Source-confirmed color/material tokens

Shared tokens include:

- base black #000;
- warm foreground #fff3f0;
- translucent white #ffffffa6;
- dark glass #0f0f0fd9;
- elevated dark #171717d9;
- deeper neutral #262626d9;
- hairline white #ffffff1a;
- stronger translucent rule #ffffff40;
- gradient endpoint #1b2228;
- muted gray #7a7a7a;
- muted rose #d39794;
- muted teal #177275.

The generated page shell also uses a #000912 dark fallback in its primary root surface.

This palette is cohesive, but the exact values are template identity and should not be copied literally.

## Observed desktop system

Audited at a 1440x900-class viewport.

Homepage:
- document is a very long narrative, roughly 17.6k px tall in the observed state;
- H1 "Solid AI agent that turns chats into outcomes" renders around 56px / 72.8px;
- major H2s render around 40px / 54px;
- oversized proof metrics such as "3.4 x" and "4.8M" render around 144px;
- page sections alternate black/transparent dark fields, with the final conversion section using a black-to-#1b2228 gradient;
- product/evidence cards commonly use 8px, 16px, and 24px radius layers with translucent white borders/overlays;
- a fixed top navigation remains present across the page;
- a fixed "Remix for free" template action is visible.

### Sticky Capability Stack

Runtime inspection confirmed three large desktop proof panels with:

- position: sticky;
- top: 120px;
- roughly 1080px width;
- roughly 628px height.

Observed sticky chapter labels include:
- Shared context;
- Instant action;
- Continuous insight.

The sticky sequence lets one viewport become a persistent stage while the meaning changes across scroll steps.

A separate FAQ category rail also uses sticky positioning around top: 120px.

This is an authored desktop storytelling mechanism, not a requirement for every breakpoint.

## Observed mobile system

Audited at 390px width across home, pricing, get-started, blog article, and legal families.

Across these checks:
- viewport/document width remains 390px;
- no document-level horizontal overflow was observed;
- homepage H1 becomes roughly 36px / 46.8px;
- top navigation condenses;
- desktop sticky product-proof panels are released rather than preserved as the same sticky 1080px stage;
- FAQ category navigation remains sticky;
- pricing becomes a long single-column 342px surface instead of a squeezed desktop comparison;
- get-started email form is about 342px wide and 56px high;
- blog and legal H1s use roughly 36px / 46.8px;
- article/legal H2s use roughly 32px / 43.2px;
- content order remains stable and readable.

The responsive lesson is to preserve the proof sequence while releasing geometry that depends on a wide viewport.

## Design DNA

### Composition

Powder uses one extremely long homepage as a product journey, then much shorter specialized routes.

Homepage rhythm:
- centered claim + conversation/workspace proof;
- unified platform framing;
- capability/proof chapter;
- question-to-progress workflow;
- integrations;
- changelog;
- outcome metrics;
- pricing;
- FAQ;
- testimonials;
- blog;
- final CTA.

The site repeatedly returns to product evidence rather than letting the middle of the page become abstract feature marketing.

### Typography

- medium-large Inter marketing display;
- slightly tighter tracking on major headlines;
- enormous numeric proof only where a metric deserves it;
- Fragment Mono reserved for technical/utility flavor instead of making all copy look like a terminal.

Transfer the role restraint, not the exact font stack.

### Material

- black / near-black base;
- layered charcoal glass surfaces;
- low-opacity white borders;
- warm off-white text;
- occasional muted rose and teal;
- modest radii rather than pillifying every large container;
- little dependence on heavy blur or neon glow.

This is useful as a dark SaaS baseline because hierarchy comes from layered luminance and border strength, not only a bright gradient.

## Conversation-to-Action Proof

Powder's core product story is stronger than a static chat mockup.

The repeated proof logic is:

**ask / intent -> contextual answer -> source / trust -> draft or action -> continuing work**

Evidence across the site includes:
- shared context;
- trusted answers with sources;
- tickets/replies/drafts/next steps;
- integration actions;
- persistent context and agent memory topics in the blog;
- source attribution and trust topics;
- changelog items such as source attribution, permissions, and workspace actions.

Transfer rules:
- show the user's intent, not only assistant text;
- show what context the system consulted when trust matters;
- show the artifact/action produced after the answer;
- make the next operational step visible;
- reuse the same product information model across marketing proofs;
- do not fabricate sources, integrations, actions, or autonomous behavior.

For agent products, a chat transcript is only the beginning of proof.

## Template Residue Quarantine

Full-site template audits often expose pages or controls that are technically public but should not teach the product's design system.

Powder includes:
- /404, an intentional error-state route;
- /page, a sparse metric/component-like route whose visible H1 values are "3.4 x" and "4.8M";
- the fixed "Remix for free" template control;
- template metadata that applies the same generic description across routes.

Treat these as **template residue / utility evidence**, not core product DNA unless the brief specifically needs the same kind of route.

Quarantine process:
1. include the route in coverage so the audit is complete;
2. classify its role;
3. note reusable utility behavior if relevant;
4. exclude placeholder/demo/editor chrome from the main Design DNA;
5. do not promote isolated component pages into the site-wide composition grammar.

This prevents "whole-site distillation" from becoming "copy every public artifact."
## Route-Family Map

### Home

Purpose: long-form product persuasion.

Key chapters:
- agent outcome thesis;
- conversation/workspace proof;
- unified platform;
- one-agent capability framing;
- sticky capability stack;
- question-to-progress workflow;
- integration ecosystem;
- changelog preview;
- outcome metrics;
- pricing preview;
- FAQ;
- testimonial/social proof;
- blog/content;
- final conversion.

The page is long, but it repeatedly changes proof mode rather than repeating generic feature cards.

### About

Purpose: company/team credibility.

Observed:
- trust-centered company thesis;
- team/role framing;
- people/team surfaces;
- operating principles;
- open-position conversion;
- shared final CTA.

The page uses the same layered dark material system rather than becoming a separate corporate microsite.

### Blog index + 10 blog detail pages

The blog index is a CMS discovery surface.

All 10 article detail routes were checked structurally. They share one editorial template with:
- large article title;
- topic/date/hero context;
- long-form article body;
- H2/H3 hierarchy;
- related-post section;
- shared final conversion.

Article topics intentionally reinforce product claims such as:
- agentic workflows;
- source attribution;
- support resolution;
- persistent memory;
- sales workflows;
- conversation-first UI;
- integration design;
- enterprise adoption;
- privacy/security;
- onboarding.

This makes content strategy part of product proof rather than an unrelated SEO layer.

### Changelog

Purpose: make product evolution visible.

Observed entries include:
- Saved answers and collections;
- Source attribution v2;
- Team permissions and roles;
- Workspace actions.

The changelog supports the same trust/action story as the homepage and blog.

### Pricing

Purpose: package the product without leaving the dark product world.

Observed:
- plan summary;
- Starter / Basic / Pro comparison;
- deeper plan comparison;
- embedded/reused product workspace proof;
- shared conversion tail.

Desktop uses multi-column plan geometry; mobile becomes one tall readable comparison surface.

### Get Started

Purpose: low-friction conversion.

Observed:
- "Get a demo";
- one visible work-email input + submit action;
- hidden anti-spam/context inputs generated by the form system;
- same dark shell and footer.

Mobile keeps the visible form around 342px wide with a 56px control height.

### Legal

Routes:
- /terms-of-use
- /cookie-policy
- /privacy-policy

All retain the same dark system and long-form typography.

Mobile legal pages keep:
- roughly 36px / 46.8px H1;
- roughly 32px / 43.2px H2;
- single-column reading flow;
- no document-level horizontal overflow.

### /404

Intentional utility route with the message:
"No workflow found for this route."

Keep as an example of on-brand error-state writing, but do not promote it into the primary product narrative.

### /page

Sparse component-like route exposing the large metrics:
- 3.4 x
- 4.8M

This is a strong example of why complete coverage and Template Residue Quarantine must coexist: a route can be public and indexable without deserving equal weight in the site's design DNA.

## Sticky Capability Stack

Desktop behavior:
- large product-proof panels share one visual stage;
- each panel is position: sticky at top: 120px;
- the scroll progression swaps semantic emphasis without moving the entire shell out of view;
- repeated geometry reduces cognitive reset between capability steps.

Responsive behavior:
- at 390px the large desktop sticky proof panels are no longer present as the same sticky stage;
- content remains in the document flow;
- document width stays stable;
- the narrative survives even though the desktop mechanism is released.

Transfer rules:
- use sticky stacking when sequential comparison benefits from a persistent stage;
- each sticky step must meaningfully change state/content;
- reserve enough vertical distance for reading;
- release sticky behavior on narrow screens when viewport height/width makes the stage oppressive;
- do not use sticky stacks merely to make ordinary cards feel cinematic.

## Responsive Contract

Source-confirmed primary breakpoints:
- mobile: max-width 809.98px;
- tablet: min-width 810px;
- large desktop: min-width 1280px.

Some utility/conversion routes also expose a 1024px branch.

Observed rules:
- desktop navigation collapses on mobile;
- major headings reduce from 56px-class to 36px-class;
- wide plan grids become one column;
- long legal/editorial content stays single-column and readable;
- desktop sticky capability stage is released on mobile;
- FAQ sticky category rail can remain where the smaller geometry still fits;
- no document-level horizontal overflow was observed in the 390px audits.

The mobile identity comes from the dark material system, typography, conversation proof, and content order - not from preserving every desktop scroll trick.

## Motion and Interaction

Source metadata describes:
- scroll animations;
- FAQ accordion;
- testimonial marquee;
- integration showcase.

Rendered/runtime evidence confirms:
- fixed global navigation;
- desktop sticky narrative panels;
- sticky FAQ category navigation;
- fixed template controls;
- accordion-style FAQ content;
- Framer responsive SSR variants.

Use motion to maintain continuity between proof states, not to animate every dark card independently.

## Template Commodity Lessons

Powder is a useful teacher precisely because its market grammar is recognizable.

Commodity traits include:
- dark near-black shell;
- translucent card surfaces;
- centered hero;
- rounded product mockups;
- compact mono/utility accents;
- integration showcase;
- changelog;
- pricing;
- FAQ;
- testimonial marquee;
- blog;
- final CTA.

The Template Archetype Firewall still applies.

A new project using this skin must add product-specific differentiation in at least one structural layer:
- proof mechanism;
- product information model;
- typography role system;
- hero composition;
- interaction grammar;
- responsive transformation;
- content architecture.

A recolored Powder clone is not a successful use of the reference.

## Cross-Site Synthesis

Compared with NovaOS:
- both are audited Framer AI/SaaS templates;
- NovaOS teaches a light enterprise route ecosystem and operational pipeline;
- Powder teaches a dark conversation-first agent proof system and sticky desktop capability narrative;
- they should anchor different skin choices rather than be mixed into a gray average.

Compared with Resend:
- Resend uses code/API proof;
- Powder uses conversation/workspace proof;
- both demonstrate that technical trust improves when the visitor can inspect cause and outcome.

Compared with Tokenmeter:
- Tokenmeter exposes confidence/provenance directly as data UI;
- Powder uses source attribution and contextual answers inside the product story;
- both reinforce the rule that trust must be visible near evidence.

## Adopt / Adapt / Avoid

| Pattern | Decision | Why |
|---|---|---|
| Conversation-to-Action Proof | Adopt for agent/automation products | Shows value beyond a chatbot transcript. |
| Sticky Capability Stack | Adapt | Strong desktop narrative tool; release it where mobile geometry makes it costly. |
| Template Residue Quarantine | Adopt for template/full-site audits | Prevents utility/demo pages from polluting reusable DNA. |
| Dark layered luminance hierarchy | Adapt | Useful baseline, but exact palette is commodity/template identity. |
| Fragment Mono utility role | Adapt | Good for technical labeling; avoid terminal cosplay. |
| Changelog/blog as trust surfaces | Adopt when the product genuinely evolves and has technical depth | Makes product maturity inspectable. |
| Exact Powder copy, metrics, colors, mockups, testimonial content | Avoid | Site/template-specific identity and claims. |

## Best-Fit Briefs

Use this profile for:
- AI agent products;
- conversation-first automation tools;
- dark B2B SaaS;
- workflow products with sourced answers/actions;
- products that benefit from sticky sequential proof;
- lower-capability execution needing a coherent dark scaffold.

## Weak-Fit Briefs

Do not let this profile dominate:
- luxury/editorial brands;
- playful consumer apps;
- image-first commerce;
- game/cinematic launches;
- simple utilities that do not need a long trust narrative;
- developer APIs where authentic code is stronger proof than conversation UI.

## Regression Questions

- Was coverage really 21/21 sitemap URLs?
- Were all 10 blog detail pages checked as a family?
- Were /page and /404 included in coverage but quarantined from primary DNA?
- Does the new design prove an agent can move from conversation to sourced output/action?
- Are sources/context/actions real rather than decorative labels?
- If using a Sticky Capability Stack, does each step change meaning and does mobile release the geometry cleanly?
- Does the mobile document stay free of unintended horizontal overflow?
- Does the dark hierarchy use luminance/borders/material restraint rather than generic neon glow?
- Is Fragment Mono used as a role rather than everywhere?
- Do changelog/blog/legal/about/pricing surfaces reinforce the same product truth?
- Would the result still feel product-specific after removing the exact Powder colors, copy, logo, metrics, and mockups?

Pass only when Powder functions as an audited dark-SaaS template teacher, not as a clone target.
