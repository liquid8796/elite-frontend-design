# Spector — Whole-Site Design Intelligence

Reference: https://spector.framer.website/
Audit date: 2026-10-09. Spector is a **Framer creative agency template**, not independently verified production evidence for the named agency, studio personnel, awards, clients or business metrics.

## Complete Site Inventory — 19/19

Official sitemap: **19/19 HTTP 200**. Home (1); About and Contact (2); **/projects archive + six project details (7)**; **/lab archive + five editorial article details (6)**; three standalone legal pages (/privacy-policy, /terms-of-service, /disclaimer). **10 supplementary routes HTTP 404**, including linked /404, an unintended /instagram.com destination, /pricing, /services, /blog, /work, /shop, missing project/article and nonsense URL. Actual homepage offers **#pricing**; there is no /pricing route. Public robots.txt explicitly allows crawling.

Evidence stored in modules/distilled-web-toolkit/data/spector-*-2026-10-09.csv: route census **29 URLs** (19 officially declared and 10 supplementary invalid), internal link graph, **40 Chromium rendered states** (all declared pages plus linked /404 at 1440x900 and 390x844), and **11 bounded interaction probes**. All 40 rendered states: **0 positive outer document horizontal overflow**. These checks do not prove payment, real company identity, actual newsletter delivery, or marketing statements.

## Art Direction and Design Tokens

A high-contrast, black-on-white editorial system with extremely oversized **Plus Jakarta Sans / Plus Jakarta Sans Variable** typography, kinetic number/counter strips, mixed Latin/Japanese graphic texture, campaign stills and restrained neutral/warm visual accents. Computed body white rgb(255,255,255), body generic sans-serif while display heads Plus Jakarta Sans. Home initial H1 **48px desktop and phone** ("Design Agency") but the dramatic manifesto is elsewhere as display text: **"OUR BRANDS JUST REFUSE TO BLEND IN"**. About prominent H1 **120px desktop →42px phone**, projects archive case title **120px→32px**, project detail **180px→42px**. Lab index dramatic "THE LAB" H1 computed ~279px both desktop/phone; lab details misuse a very large "MORE LABS" as H1 (~215px) while the actual article title is H3. Do not copy semantic mistakes.

Homepage is ~22,958px tall desktop and 26,918px mobile. Desktop home DOM 57 img, 1 video and **8 canvas elements**; mobile 140 img, 2 video and **10 canvas elements**. Rendered canvas confirms a media/graphics surface, **not actual WebGL implementation or FPS**. About page also has 3/2 canvas per breakpoint. Constrain animation and media costs with fallback poster, reduced-motion and device sampling rather than mandating WebGL. No positive 390px outer overflow detected, but oversized inline Lab display on phone may be clipped inside contained sections.

## Whole Route Family Jobs

1. **Home**: small studio location (35 Mercer Street, Soho/New York) and bilingual identity -> giant "brands refuse to blend in" thesis -> selected case frames -> client identity 3D carousel/sector claims -> services Brand Identity, Product Design, Web Systems, Development, Content & Messaging, Motion & Interaction -> awards/recognition examples -> count metrics -> showreel -> discovery/process steps -> testimonials -> #pricing bundled Focus etc -> client invitation -> agency team/contact and newsletter. Distinct language: fewer-project capacity, strategy+making under one roof, client evidence before contact.
2. **/about**: studio position -> work principles/partnership -> years/project/retention/industry numbers -> 3D client carousel -> rigorous discovery strategy and process -> illustrated team/personnel -> client story -> CTA. Studio member names and prior employment are template illustration until verified.
3. **/projects**: featured immersive image-led project tiles. **Only four visible detailed links**: Sous La Lumière, The Wendrich GT922, Thermal Dynamics, Rituel Noir Collection. Sitemap provides **six** details; two others are discoverable via related projects from detail pages, not from the top-level archive. Preserve all six in toolkit rather than assuming archive is exhaustive.
4. **Six /projects/<slug> cases**: Sous La Lumière (fashion editorial), The Wendrich GT922 (auto/performance), Thermal Dynamics (winter wear), Rituel Noir (cosmetics), The Human Interface (technology/product), The Secret Keeper (editorial/story). Project-specific campaign hero -> short proposition -> client/year -> Industry / Role / Deliverables / Timeframe -> Challenge -> Solution -> illustrated assets -> invitation -> Next/More projects. Some "VIEW PROJECT" outbound claims not verified; do not fabricate completed client work.
5. **/lab**: "THE LAB" dramatic editorial masthead, 4 initially linked article summaries with date/byline/media, newsletter/footer. Sitemap has **5** article details: last is discoverable from related articles, not archive listing.
6. **Five /lab/<slug> stories**: Why Most Brand Systems Collapse After Launch, Interfaces Should Feel Guided Not Operated, Designing for Attention, The Cost of Over-Explaining, Why Time Disappears During Good Work. Each has true title/byline/reading-time top content, editorial long read, images/captions, social share controls and "MORE LABS"/next-story references. Semantic QA: actual article title renders as H3 and related "MORE LABS" as H1; implement corrected headings instead of repeating source.
7. **/contact**: short "LET'S CONNECT" premise -> native select required Budget (Under $15K, $15–40K, $40–80K, $80K+) -> required Name, Email, Message -> Submit -> Terms link -> social shortcuts and capacity disclaimer. Native blank validation rejects missing Budget/Name/Email/Message; back-end submission NOT attempted. Contact X, LinkedIn, Instagram, Facebook and WhatsApp shortcuts point to **generic platform homepages**, not owner profiles. No independent appointment provider workflow.
8. **Legal three routes**: dated and independently linkable Privacy Policy, Terms of Service, Disclaimer. General template policy claims require client-specific legal review; 200 responses do not validate compliance.
9. **/404**: intentionally linked footer utility, returns HTTP 404, no indexed standalone marketing route; don't ship footer 404 links in production.

## Navigation, Trust, and QA Findings

All **19 official pages include a relative href "instagram.com"** resolving to **https://spector.framer.website/instagram.com** and returning HTTP 404; this is separate from absolute instagram links on contact/footer. Critical off-domain link validation rule. Footer contains creator-specific X handle and **Framerpod** "Framer template" credit; YouTube/LinkedIn/Instagram footer links share the same framer.link target. These are template-vendor residue, not a future real agency's accounts. Generic X/LinkedIn/Instagram/Facebook/WhatsApp contact destinations cannot be assumed to contact Spector.

Six project case URLs but only four links on /projects archive; five Lab detail URLs but only four initially linked on /lab archive. Require archive-to-detail sitemap parity or an explicit curated selection with a full index link. Project teaser captions repeat **"Soft form, deliberate gaze"** across visibly different work, indicating placeholder editorial residue. Most pages use the undifferentiated "Spector | Digital Creative Agency" document title; consider unique SEO titles for case pages. Contact has **no H1** in observed DOM; homepage/about and projects archive can have multiple H1s; Lab article uses "MORE LABS" H1 instead of article title. Prioritize correct accessible page heading landmarks rather than art direction alone.

The home "3D Carousel" announces item count and keyboard keys. Clicking a Next button did **not conclusively change** extracted selection/live text, so accessible intention is observed, not fully verified transition mechanics. Service controls are linked/tile-like with no role=tab confirmed. Pricing presents scope-based package levels (not Arpeggio's subscription queue): do not infer annual recurring billing. Cases share explicit industry/role/deliverables/timeframe. Long-form editorial link previews, social share buttons and newsletter form exist; no share/submit/payment executed. Homepage and About use multiple canvas nodes; no real FPS/WebGL profiling.

## Promotable Pattern Principles

**Editorial Brand Manifesto with Scoped Proof** — a giant public promise balanced by selected work, service capabilities, awards, concrete case metadata and clear invitation.

**Motion/Canvas as Evidence Staging** — 3D client carousel, counter ribbons, moving media and a single showreel should have a content job, keyboard controls, reduced-motion/static fallback and bounded runtime budget.

**Case Archive vs Hidden Detail Parity** — independent sitemap enumeration matters. Make curated four-project teasers and full six-project directory clearly distinguishable, with semantic previous/next/related entry points.

**Lab Editorial Semantic Integrity** — article title as H1, proper subhead hierarchy, editorial metadata, captions/alt text and discoverability for all five stories.

**Scope-Based Package Pricing** — tier price/what's included + project timelines and consult, avoid "unlimited subscription" copy or invented standalone /pricing path.

**Budget-First Contact Validation** — budget qualification, required sender and message fields, service intent carry-over, privacy/terms link, verified service-provider links and correctly surfaced errors.

**Provenance-Linked Awards and Numeric Claims** — template brand clients, employee names, award claims and retention metrics are not usable business proof without evidence.

**Off-Domain Link and Publisher Firewall** — fix relative social URLs, remove Framerpod/creator handle/demo target, replace generic platform homepages with real profiles, avoid 404 in primary/footer menu.

**Large-Type Mobile Recomposition** — shrink 120/180px title roles to 32–42px; explicitly manage giant lab headings; avoid multiple H1, clipping and excess canvas/media duplication.

## Limits

Audit directly observed 19 sitemap HTTP 200, ten supplementary HTTP 404, 40 rendered device states and eleven public UI probes. It did not validate backend form delivery, real client ownership, awards, creators, employee identity, payments, 3D framework/WebGL identity, network media bytes or animation frame rate. Transfer principle/structure only; do not clone publisher artwork, client imagery, brand text or names.
