# Arpeggio — Whole-Site Design Intelligence

Source: https://arpeggio.framer.website/
Template listing: https://www.framer.com/marketplace/templates/arpeggio/
Audit: 2026-10-09. **This is a Framer digital-agency/portfolio/membership template, not independently verified operating-agency evidence.**

## Entire Website Census

**22/22 sitemap URLs HTTP 200:** home (1), About (1), Contact (1), Work index (1), **7 Work case details**, Journal index (1), **7 Journal article details**, and **3 legal routes** (Terms, Privacy, Disclaimer). **Eight extra public path probes HTTP 404:** /404, random missing path, /pricing, /services, /tutorial, /style-guide, non-existent Work and Journal details. /404 is deliberately linked in demo navigation; **Membership Pricing lives in homepage #pricing**, not /pricing.

Dated evidence in modules/distilled-web-toolkit/data/arpeggio-*-2026-10-09.csv: **30 HTTP route rows**, same-host link graph, **46 rendered Chromium states** (all 22 declared routes plus 404, each at desktop 1440x900 and phone 390x844), **10 limited interaction probes**. All 46 rendered states showed no positive outer document overflow. Census does not verify actual service delivery, form submission or purchases.

## Design DNA

White computed background rgb(255,255,255), dark editorial type, restrained orange/red graphic punctuation, Inter Display as large heading face, light thin separators, image-led asymmetry, sticky navigation and service/work chapter rhythm. About/Journal/Contact H1 **130px desktop →48px mobile**; case H1 **84px→42px**; work listing **56px→48px**. Home uses smaller (~27px) subscription H1 and a later much larger manifesto heading, showing that text hierarchy matters more than a blanket H1 size rule. Docs and product-world WebGL are not part of this template.

Homepage is long: ~21,722px desktop and 25,809px mobile. At sampled desktop DOM 115 image nodes, two video nodes and **zero canvas**. At phone a far higher count of image/video nodes was observed, plausibly due to responsive Framer duplication, not evidence of 759 downloaded pictures. Do not infer network cost or runtime FPS from static node counts. Navigation includes social/clock/location context for a Milan-based agency persona.

## Complete Route Roles

1. **Homepage**: subscription promise -> huge editorial design manifesto -> showcased projects/reel -> award and agency performance claims -> Branding/Digital/Development service lanes -> why-us editorial benefit grid -> two-tier Core/Pro membership pricing and FAQ -> testimonials -> consult/contact/footer. Example Core plan $5,499/mo, two-month minimum, one project queue and first mockup within 72hrs appear as **template fixture marketing claims**, not a validated fulfillment contract.
2. **About**: agency principles, strategic method, process/working relationship, named award/result metrics, client example, team/talent narrative, consult CTA.
3. **Work archive**: seven case studies with hero image, project name, client, date and discipline; visible Search Projects field and category select with Branding, UI/UX, Motion Design, Digital Campaign, Product Design, Web Design, Mobile App, Industrial Design, 3D Design and Framer Development.
4. **Seven case details**: Boreal VR Headset, Stride Apex, Velocity Motors, Hoekstra Lens, Frost Tracker, Vespa Stories and Mercato Diretto. Dedicated hero + client/project type/release/timeline/tech -> Overview -> Challenge -> Solution -> Performance Results -> Final Thoughts -> Credits -> related works/contact. Live Site links may point through framer.link/demo; claims and clients not authenticated.
5. **Journal archive**: seven articles and searchable editorials with author/date/intro and newsletter route. Subjects include micro-interactions, subscription design, animation, sustainable design, typography, AI-assisted design and design systems.
6. **Seven Journal details**: article-specific image/title/byline/date, explanatory long-form chapters, quotes, takeaways/related reading. Claim statistics unverified.
7. **Contact**: scope-first project form (visible Service dropdown with Full Stack Website, UI Design, Framer Development and Brand Identity; Budget dropdown with under €10k, €10–20k, €20–50k and €50k+), followed by required sender fields and message; distinct CTA handoffs to Calendly, WhatsApp and mailto, plus FAQs and newsletter. No form submitted.
8. **Three legal routes**: actual Terms/Privacy/Disclaimer documents.
9. **Linked /404**: actual HTTP 404, demo-only sitemap-excluded route.
10. **Vendor/template layer**: official listing identifies Arpeggio as template by Tamas Bodo, template sales at $129, cross-promotion for Monodrift and other Framer templates. This business differs from fictional agency membership and project awards. Socials point to generic provider homepages in samples; mailto hejj@... versus hey@... differs between surfaces. Do not clone vendor sales, partner/ARR stats, dummy links or testimonials.

## Direct Interaction Observations

The ten bounded probes include Work search, work category, missing query, Journal search, Contact form anatomy, outbound contact links, homepage membership selector, case-study headings and mobile nav click. Work href subset changed after typing Boreal, but it was not narrowed to one project and later filter state was inconsistent. Search Articles did not change captured article href subset in one probe. A Pro Plan click was dispatched but did not conclusively show a changed plan price. Mobile menu clicked but abbreviated snapshot did not establish focus-trap/overlay state. **Do not promote these as confirmed fully working features**; require a deterministic search/filters/empty-state QA test.

The visible Contact external targets are Calendly home, WhatsApp home, and direct mail; provider booking and email delivery were not executed. Homepage membership select-plan points to an external Polar checkout URL, but owner/payment behavior was not established.

## Distilled Mechanisms

**Editorial Manifesto Anchored by Proof**: one memorable huge typographic stage followed by detailed service, case evidence and action routes.

**Case Study as an Evidence Argument**: client/period/tech metadata + problem -> intervention -> result -> attribution, not just photo galleries. All actual outcome metrics must be verified.

**Portfolio Taxonomy with Result Contract**: search/category controls must change *visible* cards, expose clear/no-result and keyboard paths; mere field existence is insufficient.

**Homepage Membership Commercial Loop**: price/plan/queue/turnaround terms adjacent to case credibility and concrete consult/checkout, not fictitious /pricing route.

**Budget-First Qualified Contact**: request service and budget before contact, preserve selection from work/pricing CTA to form, offer alternate clear channel with valid destinations.

**Agency Presence as Detail, Not Navigation Tax**: local clock/location/social rail express personality but cannot hide primary case/contact actions.

**Template Vendor Firewall**: agency persona/award claims and publisher template sales are separate; never transfer branded art, logos, metrics, fake case studies or vendor checkout.

**Mobile Editorial Recomposition**: 130→48px title and 84→42px case headings, aligned image crop and readable long project chapters; monitor responsive DOM duplication.

## QA/Confidence

All declared route HTTP status and 46 DOM-computed dual-viewport page states are directly observed. Zero positive outer overflow. Actual search filtering outcomes, newsletter/contact send, pricing checkout, calendar booking, social identity, external client live sites, results/awards, real business registration, revenue and responsive media network load are NOT independently verified.
