# Spector — Whole Website Toolkit Spec

Source: https://spector.framer.website/
Profile: ../../../design-intelligence/sites/spector.framer.website.md
Archetype: experimental-editorial-agency
Reuse existing **creative-agency-editorial** baseline; no overlapping new skin.

## Exhaustive Audit Evidence

**19/19 official sitemap URLs HTTP 200** — home, About, Contact, Projects archive + six project cases, Lab archive + five editorial reads, three legal pages. **10 additional probes HTTP 404**, notably footer-linked /404 and unintended relative /instagram.com. **29-row route inventory**, complete same-host link graph, **40 Chromium states** (all sitemap URLs plus 404 on 1440x900 and 390x844, no outer overflow), **11 bounded probes** under data/spector-*-2026-10-09.csv. Full-site means every published detail including those hidden by short archives, not just the homepage.

## Visual Structure

White computed body #FFFFFF and strong near-black **Plus Jakarta Sans** giant editorial typography with restrained warm/neutral photography and occasional Japanese microcopy. The small home H1 "Design Agency" is 48px but a separate huge manifesto carries weight. About title H1 120px desktop ->42px phone; project case H1 180px ->42px; project archive feature 120px ->32px. Homepage DOM has 8 canvas + 1 video desktop, 10 canvas + 2 videos mobile; not proof of specific render tech. Lab index and Lab-detail decorative H1s remain huge at phone: contained clipping and heading semantics require correction.

## Route / Job System

- Home: location/specialty -> large "brands refuse to blend in" manifesto -> curated projects -> 3D client/sector carousel -> six service disciplines -> selected award/metrics -> showreel -> process/timing -> social proof -> #pricing project package tiers -> contact invite.
- About: agency focus -> self-limiting project commitments -> operating numbers -> carousel -> discovery process -> people -> client story -> consult CTA.
- Projects archive: **4 selected project links** displayed vs **6 indexed project details**. Treat "selected" as curated only if there is a discoverable All Projects directory.
- Six project details: media hero + year/client, Industry/Role/Deliverables/Timeframe -> Challenge -> Solution -> media chapters -> next/related/All Projects; unique story each. Source metrics illustrative.
- Lab archive: **4 displayed articles vs 5 published**; metadata/date/author and linkable article preview, newsletter.
- Five Lab details: byline/date/reading time -> long essay/images/captions -> share -> next/related. Source has article H3 but decorative related-section H1; implement actual title H1.
- Contact: required Budget, Name, Email, Message -> native validity/Terms -> submit and channel options. Do not infer successful server submission.
- Legal: Privacy/Terms/Disclaimer as real standalone pages.
- /404 is demo-only actual HTTP 404.

## Components and Motion Behaviors

1. Editorial kinetic manifesto with single clear project/contact route.
2. Canvas/3D client carousel with item-of-six semantics and next/previous, keyboard and reduced-motion escape; exact selection transition unverified.
3. Six discipline service roster with reason/benefit/outcomes; don't assert untested tabs or accordion.
4. Project proof card and case progression with dated industry/role/deliverables.
5. Animated recognition/stats rail, always backed by provenance.
6. Lab article with correct heading hierarchy, next/related article link and social share.
7. Scope-based plan/pricing section on home #pricing, not /pricing standalone route.
8. Budget-first contact with owner-controlled destinations, native field validity and terms disclosure.

## Critical Anti-Patterns / Release QA

- All **19 pages** contain invalid relative `instagram.com` link -> local /instagram.com HTTP 404; validate external scheme/host.
- /projects exposes only 4/6 real detail URLs; /lab only 4/5. Mark curated view explicitly and expose a full archive or pagination.
- Contact `h1` absent; article title is H3 while "MORE LABS" is H1. SEO titles for project pages are nonunique; fix semantic outline/title.
- Project teaser captions repeatedly use the same "Soft form, deliberate gaze"; sample assets/copy cannot be reused as project-specific proof.
- Footer demo /404, Framerpod creator link, X creator username, shared framer.link destination and generic network homepages are template residue.
- Studio claims awards, employees and clients without independently verified truth. Use real business proofs.
- Home canvas count is **not** evidence of WebGL; test actual performance, nonblocking fallbacks and reduced motion.
- Carousel arrow probe observed no reliable item state change in sampled labels: don't claim verified functional transition.

## Transfer Rule

Transfer visual mechanics, route architecture, content/proof boundaries and responsive scale, **never** branded mock work, publisher assets, phantom metrics or creator's store identity.
