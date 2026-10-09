# Arpeggio — Entire-Website Toolkit Spec

Source: https://arpeggio.framer.website/
Deep profile: ../../../design-intelligence/sites/arpeggio.framer.website.md
Archetype: editorial-agency-membership.
Baseline skin: **creative-agency-editorial**; reuse it, do not add a duplicate skin.

## Whole-Route Census and Evidence

**22/22 sitemap-declared HTTP 200:** home, about, contact, Work index + **7 case studies**, Journal index + **7 article details**, three legal pages. Additional **8 path probes HTTP 404** including deliberately linked /404 and missing /pricing. Pricing/Membership lives at homepage **#pricing**, not /pricing. Dated route/link/interaction CSV under data/arpeggio-*-2026-10-09.csv: 30 HTTP rows and **10 interaction probes**. Browser audited all 22 real routes and /404 in both 1440x900 and 390x844 Chromium, **46 states with zero positive document overflow**.

## Art Direction

White rgb(255,255,255), dark editorial Inter Display, restrained orange/red accents, tight typographic scale and high-contrast image/photo workbench, layered visual manifesto and real portfolio/story chapters. About/Journal/Contact H1 130px desktop ->48px phone; case H1 84px ->42px; work list H1 56px ->48px. Home opens with smaller subscription thesis H1, then larger expressive manifesto. Desktop home has 0 canvas, 115 image nodes and 2 video nodes; more mobile media DOM nodes are responsive duplication **not confirmed network loads**.

## Route Job Matrix

- Home: membership value -> signature editorial stage -> selected work/reel -> awards/metrics -> Branding/Digital/Development lanes -> benefits -> Core/Pro plan switch within #pricing -> FAQ/testimonials -> contact.
- About: agency philosophy -> process/principles -> recognition -> proof example -> consult.
- Work archive: 7 visual project records, Search Projects field and category filter -> project detail. Search/category state correctness needs QA.
- Work detail: hero -> client/date/tech/discipline -> Overview -> Challenge -> Solution -> Results -> Reflection -> Credits -> related work/contact. Seven records with unique CMS content.
- Journal archive: 7 topic articles, authors/dates, Search Articles field -> details/newsletter. Search behavior not confirmed correct.
- Journal detail: author/date -> opening thesis -> long editorial sections -> takeaways/related stories.
- Contact: service/budget selector before name/email/message -> Calendly/WhatsApp/direct email -> FAQ/newsletter. Submission not tested.
- Legal: distinct Terms, Privacy and Disclaimer.
- 404: actual HTTP 404; not a legitimate marketing destination.
- Vendor boundary: Framer template $129 creator promotion, Monodrift cross-sell, placeholder agency stats/socials not part of an authentic future client's conversion.

## Reusable Patterns

arpeggio-editorial-proof; arpeggio-case-argument; arpeggio-portfolio-result-contract; arpeggio-membership-pricing; arpeggio-qualified-contact; arpeggio-time-presence; arpeggio-vendor-firewall; arpeggio-mobile-recomposition; arpeggio-template-content-integrity.

## Interaction and QA Limits

Work search produced some href-set change but did not conclusively isolate the requested project; later category sample inconsistent. Journal search had no change in sampled href subset. Clicking Pro did not prove the price changed. Mobile menu click did not prove focus management. External agency plan CTA reaches a Polar URL; contact shortcuts reach Calendly/WhatsApp home and mailto. No payment, send, booking or award/client truth verified.

Transfer editable mechanisms and responsive geometry, never the source agency persona, fictional client results, real people's identity, proprietary photos or creator's marketplace links.
