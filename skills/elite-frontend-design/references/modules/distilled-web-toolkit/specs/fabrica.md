# Fabrica — Entire Website Toolkit Implementation Spec

Source: https://fabrica.framer.media/
Deep profile: ../../../design-intelligence/sites/fabrica.framer.media.md
Archetype: dark-digital-agency-portfolio
Baseline skin: **creative-agency-editorial**, with dark tokens; no redundant skin.

## Exact Site and Evidence Coverage

Official sitemap **20/20 HTTP 200**: Home, Studio, Projects archive + **6 case details**, Blog archive + **7 article details**, Contact, two legal routes. **10 supplemental probes HTTP 404** (including /404, /about, /pricing, /services and unknown details); the site's Studio substitutes for About, and Pricing exists on homepage rather than a separate route. Toolkit evidence: data/fabrica-route-inventory-2026-10-11.csv **30 route rows**, data/fabrica-internal-links-2026-10-11.csv site graph, data/fabrica-rendered-states-2026-10-11.csv **42 Chromium 1440x900/390x844 page states, 0 positive outer overflow**, data/fabrica-interaction-probes-2026-10-11.csv **11 probes**. No form submitted or purchase executed.

## Visual / Motion Identity

Deep charcoal #121212, white/intermediate gray typographic hierarchy, **Inter**. Standard inner-page H1 ~148px desktop ->64px phone; homepage premise H1 ~22->18px while a huge H2 ~144->62px. Rich project cards with preview media, team photography, grayscale/dark graphics, 4 service image rows, client logo/metric grids and occasional videos. Homepage two video DOM nodes, 64 images, **zero canvas**; browser DOM count not transfer-byte measurement. No verified WebGL. Preserve readable 390px composition and no outer overflow.

## Route System

- Home: agency pledge -> clients and **six** case cards -> results counter -> four capability categories with subservice lists -> four-step launch process -> showreel -> testimonials and outcome panels -> homepage **#pricing Per project / Monthly** + optional SEO addon -> team -> FAQ -> blog preview -> contact and newsletter.
- Studio: about/identity, multidisciplinary team/scale numbers, operational values and proof; no /about route.
- Projects archive: six project cards with title/year, **functional text Search… + native Category select**. Test search Boltshift **6->1**, category Web design **6->3**. Implement genuine clear/no-results and keyboard semantics.
- Project detail (6): specific hero/year/brief, problem, approach, media and outcome claims -> related next case/contact. Source title template suffix "My Framer Site"; verify client attribution and exact live-site URL.
- Blog archive: **all seven** articles linked by visible category/editorial cards.
- Blog detail (7): true H1, supporting paragraphs/H2, captioned images, context and related reading; isolate topic mismatches (Color Branding page unexpectedly has Speed/SEO headings).
- Contact: inviting oversized H1 + team lead persona -> **required Name and Email only** -> Terms/Privacy notice; not full project-brief form. Validate emptiness natively; no server/send proof.
- Legal Privacy and Terms: standalone, production law/business-identity verification.
- /404: correct status error handling, no published route.
- Vendor/creator shell: footer Framer and Anatolii Dmitrienko/TEMPLIFICA template shop and $129 template promo; don't install publisher marketing on genuine agency.

## Transfer Components and QA

1. Split small positioning thesis from huge editorial display; preserve document headings, especially /projects no H1.
2. Visual Project archive with search and category controls, real filtered list counts and empty/reset states.
3. Media-backed project case narrative with actual client/problem/solution/result evidence.
4. Capability lanes for 4 disciplines, with explicit deliverable taxonomy.
5. Provenance-bound metric/testimonial panels; never reproduce 56+, 4.9/5, 100 Pagespeed, 60% leads as verified numbers.
6. Responsive showcase with video poster/reduced motion, not mandatory WebGL.
7. Scope-focused Pricing, project/monthly affordances, marketing addon and genuine handoff. Selected tier change *not confirmed*; no /pricing page.
8. Studio team/culture and multi-step process sections; real staff credentials only.
9. Blog CMS topic integrity: title, H1, H2 body, image, metadata and citations agree.
10. Low friction contact and newsletter; verified email delivery and honest Terms/Privacy.

Do not clone source branding/assets, exact copy, creator store or unverified public metrics.
