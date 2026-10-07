# OrbAI - full-site distilled design intelligence

Source: https://orbai-template.framer.website/
Audit date: 2026-10-07
Coverage: 8/8 sitemap URLs

Audit scope: robots/sitemap discovery, Framer search-index parity, complete same-origin internal-link crawl, generated HTML/CSS for every public route, all 4 changelog detail pages, desktop and 390px mobile runtime checks, typography/tokens, media behavior, contact/privacy/changelog families, and utility /404 residue.

This is a whole-site profile, not a homepage-only read.

## Coverage manifest

Public sitemap routes:
- /
- /contact
- /privacy
- /changelog
- /changelog/introducing-orbai-1-0-7
- /changelog/introducing-orbai-1-0-6
- /changelog/introducing-orbai-1-0-5
- /changelog/introducing-orbai-1-0-4

That is:
- 4 primary/support routes;
- 4 changelog detail pages.

The Framer search index contains the same 8 route keys. The complete same-origin link graph found no additional public route outside this set.

Utility residue also audited:
- /404

## Landscape classification

Primary: template commodity, audited.
Secondary: clean product / agency conversion marketing.

OrbAI identifies itself as "Orbai – AI Agency Template" and the metadata describes a premium Framer template for AI automation agencies. The hero includes a "Get Template" action, and the site is hosted on Framer with platform/editor chrome.

Use OrbAI as:
- a clean light B2B/service marketing baseline;
- a compact commercial-site architecture reference;
- an example of one-page conversion storytelling plus satellite trust/support routes;
- an example of pricing followed by comparison;
- a lower-capability scaffold for AI/service marketing.

Do not use it as proof that the named clients, team members, project metrics, privacy copy, pricing, release history, or competitive claims are real.

## Source-confirmed platform

- generator: Framer 3db8496;
- robots.txt points to /sitemap.xml;
- sitemap contains 8 public URLs;
- Framer search index contains the same 8 route keys;
- /llms.txt is absent;
- /sitemap-index.xml resolves to the site 404 experience;
- generated responsive branches use 1200px, 810px, and <=809px ranges;
- page runtime uses Framer Motion modules rather than a site-specific GSAP/ScrollTrigger stack;
- no WebGL/Three/Spline runtime was found in the main site bundle.

## Source-confirmed typography

Visible/loaded primary roles:
- Satoshi;
- Inter.

Observed role split:
- Inter: giant ORB AI identity wordmark/display;
- Satoshi: section headings, pricing, narrative, card copy, article/changelog headings;
- standard body/UI copy remains in restrained sans roles.

Desktop:
- ORB AI identity: around 100px / 120px;
- major section heading: around 56px / 67.2px;
- statement heading: around 36px / 50.4px;
- project/pricing labels and subheads: roughly 24-44px.

Mobile 390px:
- ORB AI identity: around 40px / 48px;
- major section heading: around 36px / 43.2px;
- smaller editorial/changelog headings: roughly 20-24px.

Transfer the role contrast, not the exact Satoshi + Inter pairing.

## Source-confirmed color/material tokens

Shared generated tokens include:
- #f5f5f5 light neutral shell/surfaces;
- #fff white;
- #000 primary ink;
- #04070d near-black deep accent;
- #d5dbe6 cool gray;
- #814fff purple brand accent;
- translucent white/black surface variants;
- #f0f8ffe6 pale glass/light-blue tint.

Observed material grammar:
- light neutral global shell;
- 16-20px rounded content cards;
- restrained borders/shadows rather than heavy glass everywhere;
- one saturated purple accent family;
- dark/ambient media reused at identity-bearing boundaries.

Do not copy #814fff as a default "AI" accent.

## Hero and ambient media

The home hero is a full-viewport 900px-class stage on desktop.

Observed:
- fixed top navigation;
- eyebrow "AI AUTOMATION FOR BUSINESSES";
- logo;
- giant ORB AI identity;
- concise promise;
- primary "Get Template" and secondary "See Our Services" actions;
- one large ambient MP4 cropped beyond the viewport.

Media source:
- aMPvRVYHFQxBoB0v2qyJln83jI.mp4

Desktop hero media:
- approximately 1777x1185 rendered inside a 1424x900 clipped hero;
- autoplay + loop + muted + playsInline in the active desktop variant.

The same media asset is reused as a large footer/background visual bookend.

At 390px the video element remains oversized and clipped by the viewport-safe section. The mobile document stays 390px wide with no document-level horizontal overflow.

This ambient media is a signature cue, not product evidence.
## Home route: commercial core

Desktop home is roughly 12.6k px tall and carries almost the entire buying narrative.

Observed section order:
1. hero / positioning;
2. founder/brand statement;
3. Why Choose Us;
4. All features in 1 tool;
5. Our AI-Driven Services;
6. Simple & Scalable process;
7. Proven Impact & Results;
8. What Our Clients Say;
9. Simple Price For All;
10. Precision vs Basic;
11. Team Behind Success;
12. Questions? Answers!;
13. shared identity/footer.

This exact order is template-specific. The transferable lesson is the progression from claim -> mechanism -> delivery -> proof -> offer -> objection handling -> trust -> conversion.

### Benefits/cards

Why Choose Us uses compact proof/benefit cards with:
- 20px radius;
- neutral #f5f5f5 surfaces;
- text + small visual evidence;
- cards around 384x360px in the inspected desktop state.

Examples include:
- Real-Time Analytics;
- AI-Driven Growth;
- before/after automation/cost visual;
- team sync;
- horizontally repeated capability labels.

These are conceptual marketing visuals, not evidence of a real product backend.

### Feature bento

"All features in 1 tool" uses an asymmetric 2x2 bento:
- wide card about 706x268px;
- narrow card about 470x268px;
- second row reverses the wide/narrow emphasis;
- 20px card radius.

Feature themes:
- Cutting-Edge AI;
- Automated Workflows;
- Insightful Analytics;
- AI-Powered Support.

Transfer:
- vary card span when idea/media weight differs;
- keep card height/radius rhythm stable;
- do not use bento only because "AI templates use bento";
- do not turn vague claims into fake product proof.

### Service bento

Our AI-Driven Services uses a second asymmetric system:
- 392px-class narrow service cards;
- 784px-class wide cards;
- around 374-382px height;
- 20px radius;
- text paired with relevant illustrative UI/concept media.

Service themes:
- AI Strategy Consulting;
- Content Generation;
- AI-Powered Chatbots;
- Automated Workflows.

This is stronger as an agency/service explanation pattern than as a software feature architecture.

### Process

Simple & Scalable exposes three delivery steps:
- 01 Workflow Assessment;
- 02 Deploy with Confidence;
- 03 Ongoing Support & Optimization.

The process section makes the invisible service engagement legible before the visitor reaches projects and pricing.

For service businesses, showing how work happens can reduce perceived execution risk.

### Projects / outcomes

Proven Impact & Results introduces a project/case-result section before testimonials and pricing.

Representative project:
- MedixCare — AI Triage Assistant for Healthcare;
- short problem/solution description;
- percentage-based outcome callouts.

Treat the exact project and numbers as template placeholder content. Transfer only the structure:
- named situation;
- short intervention;
- observable outcome;
- restrained amount of proof.

Never invent percentages to fill a layout.

### Testimonials and business metrics

What Our Clients Say combines:
- a large editorial testimonial statement;
- supporting testimonial cards;
- avatar/role identity;
- summary business metrics.

This is a template proof bundle. Use only when customer identities, quotes, and metrics are real or clearly marked as placeholders in a prototype.

### Pricing

Simple Price For All uses three plans:
- Starter;
- Pro with a "Popular" emphasis;
- Enterprise.

Desktop pricing cards:
- roughly 384px wide;
- 16px radius;
- neutral #f5f5f5;
- different card heights based on included capability count.

The plan hierarchy is conventional and easy for lower-capability execution.

### Pricing-to-Comparison Bridge

Pricing is followed immediately by "Precision vs Basic".

Observed structure:
- ORB AI column;
- Others column;
- symmetric capability rows;
- CTA on the ORB AI side.

This placement handles a natural post-price objection: "why choose this instead of a cheaper/generic alternative?"

Transfer the bridge, not the unverified claims.

Use:
plan -> included value -> defensible comparison -> objection resolution -> next action.

Avoid generic superiority rows such as "we are smarter/faster/better" unless measurable and supportable.

### Team and FAQ

After offer/differentiation, OrbAI adds:
- Team Behind Success;
- carousel/slider controls;
- team roles and social links;
- Questions? Answers! FAQ;
- direct support email;
- final identity/footer.

This makes human trust and objection handling the final conversion tail.

Again, exact team identities are template content and must not be reused.

## Commercial Core + Trust Satellites

OrbAI uses one main commercial page plus a small route ecosystem.

Navigation from support routes points back into home anchors:
- ./#features
- ./#pricing
- ./#services
- ./#projects

Independent satellites:
- /contact
- /privacy
- /changelog

This architecture is useful when:
- the offer can be explained in one coherent scroll;
- services/features/pricing/projects are sections, not standalone information domains;
- legal, contact, and release history deserve separate routes;
- route proliferation would add duplication rather than clarity.

The commercial core owns persuasion. Satellite routes deepen trust/support without repeating the sales page.
## Contact route

Purpose: focused lead capture plus last-mile objection handling.

Desktop:
- document roughly 2.6k px;
- Reach Us At Anytime at about 56px;
- primary form around 520x564px;
- FAQ after the form;
- shared footer/ambient media.

Visible fields:
- Name;
- Email;
- Subject of interest;
- More info;
- Send Your Message.

Generated hidden anti-spam/context fields are also present.

Mobile 390px:
- form width about 354px;
- major heading about 36px;
- no document-level horizontal overflow;
- FAQ and footer remain in normal reading order.

Transfer:
- contact should reduce decision complexity;
- preserve clear labels, input purpose, touch targets, success/error behavior;
- do not expose placeholder names/emails as real contact identity.

## Privacy route

Purpose: legal/trust satellite.

Observed content:
- Privacy Policy;
- last-updated date;
- sections for information collected, use, sharing, cookies, choices, security, children, changes, contact;
- same global shell/nav/footer as marketing routes.

Desktop:
- roughly 2.8k px document;
- 56px top heading;
- readable long-form body.

Mobile:
- heading about 36px;
- last-updated subhead about 20px;
- 390px document width with no overflow.

Transfer the readable legal-shell continuity, not the literal privacy text. Legal content must come from the actual business/legal requirements.

## Changelog index

Purpose: update/release-history satellite.

Observed:
- label "OUR SAYINGS";
- "Fresh Takes & Updates";
- four CMS entries;
- category;
- date;
- version title;
- short summary.

Entries:
- Introducing OrbAI 1.0.7 — Nov 28, 2024;
- Introducing OrbAI 1.0.6 — Nov 28, 2023;
- Introducing OrbAI 1.0.5 — Nov 28, 2022;
- Introducing OrbAI 1.0.4 — Nov 28, 2021.

The staggered yearly dates/content are template data. Do not reuse as real release history.

## 4 changelog detail pages

All 4 changelog detail pages were inspected structurally as one CMS family.

Representative 1.0.7 structure:
- category + date;
- version title;
- summary;
- What's New?;
- Other updates;
- Fixes;
- adjacent/previous release handoff;
- shared footer.

Representative content mentions integrations, live data sync, notification limits, dashboard UI, mobile layout fixes, hover-state fixes, animation smoothness, and data-sync bugs.

Transfer:
- release details should separate new capability, secondary improvements, and fixes;
- navigation between releases can help continuity;
- changelog is a credibility surface only when releases are real and dated truthfully.

Do not fabricate a changelog merely to make a young product look mature.

## Utility /404

/404 is not one of the 8 sitemap routes, but was audited under Template Residue Quarantine.

Observed:
- shared global nav;
- 404 marker;
- "Whoa!";
- "That didn’t work out.";
- short explanation;
- "Go Back Home" recovery action;
- no ambient footer video.

At 390px the route remains exactly viewport width with no document overflow.

The reusable lesson is recovery clarity, not the exact playful copy.

## Responsive behavior

Primary generated breakpoints:
- >= 1200px;
- 810px-1199px;
- <= 809px.

Observed 390px transformations:
- ORB AI identity around 100px desktop -> 40px mobile;
- major 56px sections -> about 36px;
- 44px pricing/process numerals -> about 28px;
- 36px narrative statements -> about 24px;
- multi-column cards stack vertically;
- pricing tiers become sequential;
- comparison columns become separate readable blocks;
- contact form fits about 354px inside a 390px document;
- legal and changelog routes remain single-column readable;
- footer media stays clipped inside the viewport-safe shell;
- no document-level horizontal overflow was observed on home/contact/privacy/changelog/detail/404 at 390px.

The key rule is to preserve semantic sequence and proof hierarchy before preserving desktop card geometry.

## Motion and interaction

Observed:
- Framer Motion runtime;
- fixed desktop navigation;
- compact/mobile nav variant;
- carousel controls for team;
- FAQ disclosure controls;
- hover/button motion;
- autoplay ambient hero media on desktop;
- same media reused near footer;
- mobile uses a non-autoplay rendered video variant in inspected DOM state.

No evidence supports a custom WebGL/3D stack.

Use motion for:
- navigation feedback;
- state disclosure;
- card/CTA affordance;
- controlled ambient identity.

Do not imply "AI sophistication" through unnecessary continuous motion.

## Template residue quarantine

Template/vendor-specific material includes:
- "Orbai – AI Agency Template";
- "Get Template";
- Framer editor/free-site chrome;
- placeholder team identities;
- placeholder client names/testimonials;
- sample project MedixCare;
- sample outcome percentages;
- sample pricing;
- sample changelog history;
- generic competitor claims;
- generic privacy copy.

Keep these in audit coverage but exclude them from transferable product truth.

## Cross-site synthesis

Compared with NovaOS:
- NovaOS is broad enterprise AI platform storytelling with multiple operational/trust routes;
- OrbAI is a compact service/agency marketing system;
- NovaOS benefits from Operational Pipeline Storytelling and route ecosystem depth;
- OrbAI benefits from Commercial Core + Trust Satellites and a simpler conversion ladder;
- do not force OrbAI’s small-site architecture onto an enterprise product.

Compared with Powder:
- Powder is dark agent/workspace SaaS with conversation-to-action proof and sticky capability storytelling;
- OrbAI is light agency/service marketing with conventional cards, process, projects, pricing, team, and FAQ;
- both are template commodity references, but they teach different baseline execution modes.

Compared with Nudge Folio:
- Nudge isolates creative experimentation in a playground;
- OrbAI stays commercially conventional across all routes;
- OrbAI is better as a lower-risk clean conversion scaffold; Nudge is better for personality-led portfolios.

## Adopt / Adapt / Avoid

| Pattern | Decision | Why |
|---|---|---|
| Commercial Core + Trust Satellites | Adopt for focused service/product sites | Prevents needless route sprawl while keeping trust/support material inspectable. |
| Pricing-to-Comparison Bridge | Adopt when comparison claims are defensible | Handles post-price differentiation at the right moment. |
| Process before projects/pricing | Adapt for services | Makes delivery risk understandable before asking for purchase. |
| Asymmetric feature/service bento | Adapt | Useful when idea weight differs; avoid generic AI-template repetition. |
| Ambient media bookend | Adapt cautiously | Creates identity continuity but is decoration, not proof. |
| Three-tier pricing | Adapt | Familiar and easy to scan, but only when business model truly has tiers. |
| Changelog satellite | Adapt when real releases exist | Can show continuity and accountability. |
| Exact purple accent / Satoshi + Inter pairing | Avoid | Template-specific skin. |
| Placeholder clients, metrics, team, pricing, releases | Avoid | Not transferable truth. |
| Generic "Us vs Others" superiority claims | Avoid | Must be evidence-backed. |

## Best-fit briefs

Use this profile for:
- AI automation agencies;
- consulting/service firms;
- focused B2B productized services;
- simple SaaS/product marketing that fits one main commercial page;
- lower-capability implementation needing an explicit light conversion scaffold;
- teams that need contact/privacy/changelog satellites without enterprise route sprawl.

## Weak-fit briefs

Do not let this profile dominate:
- complex enterprise platforms;
- developer/API tools where code proof is primary;
- product dashboards;
- ecommerce catalogs;
- editorial/portfolio work;
- high-ambition immersive campaigns;
- regulated products requiring deep legal/security/compliance route systems.

## Regression questions

- Was coverage verified as 8/8 sitemap URLs?
- Were all 4 changelog detail pages accounted for?
- Was /404 audited but quarantined from public-route count?
- Does home remain the commercial core rather than duplicating the same story across satellites?
- Do satellite nav links return users to meaningful home anchors?
- Are benefits/features/services/process/projects/pricing/comparison clearly distinguished?
- Does Pricing-to-Comparison Bridge use defensible criteria?
- Are project metrics, clients, team, pricing, release history, and legal copy truthful?
- Does mobile preserve sequence while stacking card systems cleanly?
- Does every 390px family audit avoid document-level overflow?
- Are exact OrbAI fonts, purple accent, ambient video, copy, and vendor chrome excluded from clone transfer?

Pass only when OrbAI functions as an audited clean-product/service template teacher, not a source of fictional product truth.
