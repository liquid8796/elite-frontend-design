# Nouva — Distilled Toolkit Spec

Source: https://nouva-template.framer.website/
Deep profile: `../../../design-intelligence/sites/nouva-template.framer.website.md`
Archetype: dark-ai-productivity-saas
Skin: `premium-saas-dark`. No new baseline skin.

## Route census — 2026-10-08

Sitemap: 8/8 HTTP 200: home, contact, sign-up, sign-in, otp, account, terms, privacy. Footer also links authored /404 with actual HTTP 404. See `data/nouva-route-inventory-2026-10-08.csv`. All nine route surfaces rendered at desktop and 390px mobile, with zero outer mobile overflow. Forms/auth/paid workflows not submitted.

## Visual grammar

Dark navy #080C12 shell, raised #0E131D and #121926 product cards, white #FAFAFA headings, gray #99A0B0 utilities; high-contrast white rounded CTA. Onest carries visible heading/body; Inter loaded. H1 ~60px -> 46px, H2 ~48px -> 38px. 0 home video, 0 canvas; static product screenshots and Framer sticky stages, plus scroll count animation. No evidence for Three/WebGL.

## Whole-site route grammar

Home: identity/promise -> problem + animated evidence -> output/goals/time triad -> screenshots and workflow proof -> teams/integrations -> differentiation -> testimonials -> tier pricing -> FAQ -> last CTA.

Contact: explicit required first/last/email/subject/message + optional company/newsletter; qualifies a lead, not immediate use of an editor.

Auth: branded passwordless email sign-up/sign-in -> code-entry /otp -> account profile (name/email) with FrameAuth external attribution. Backend security and delivery not verified.

Legal: long-form sectioned Terms and Privacy with real document metadata and owner-contact continuation.

404: branded recovery route returns 404; not in sitemap.

## Recommended patterns

`nouva-product-lead-spine`; `nouva-contact-first-conversion`; `nouva-auth-brand-continuity`; `nouva-scroll-metric-reveal`; `nouva-workflow-proof-triad`; `nouva-dark-task-bento`; `nouva-utility-route-parity`.

## UX / QA constraints

- Marketing/pricing CTA all go /contact; adjust “try free” expectation to match conversion behavior.
- Price switch Monthly/Yearly 20% off did not change price or switch state in one sampled wrapper click: verify functionality, ARIA switch state, keyboard interaction and unit/proration before production.
- Metrics initially show 0%/0.0x, then transition in-view; preserve reduced-motion end states and trustworthy labeling.
- Contact/home/404 share one generic "AI Content Template for Framer" page title; use route-specific titles.
- Input semantics: email/OTP currently text-type in observed auth UI; verify suitable keyboard hints/labels and secure flows.
- All metrics, testimonials, tier pricing, imagery, links and legal policies are template fixtures requiring replacement and review.

## Do not imitate

Do not claim verified team productivity, signup/payment processing, OTP delivery or account protection based only on rendered UI; do not clone vendor artwork/fonts, mock product screens or preview badges.
