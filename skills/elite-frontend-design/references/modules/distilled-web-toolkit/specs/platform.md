# PlatForm / Platform® — Whole-Site Framer AI Infrastructure Toolkit Spec

Source: https://plat-form.framer.ai/
Deep audited profile: `../../../design-intelligence/sites/plat-form.framer.ai.md`
Archetype: **dark-modular-ai-infrastructure-platform**.
Baseline skin: **premium-saas-dark**, without introducing a near-identical 14th skin.

## Scope and provenance

Full official sitemap: **19/19 HTTP 200** = homepage (1), Services (1), Labs index (1) + eight Labs CMS essays, four FrameAuth-style auth pages, four legal/data policy pages. **Twelve additional probes** all HTTP404, including two **linked** broken paths `/404` and `/labs/:LGnOksssn`. Internal link graph **224** unique source→target pairs. **42 Chromium rendered states** (all 19 official + two broken linked routes at 1440x900 and 390x844), zero positive outer document overflow. **18 bounded interaction probes** including corrected Labs Load More parity 7→8 and inconclusive pricing switch; no user credentials or real submissions used.

Datasets under `data/platform-{route-inventory,internal-links,rendered-states,interaction-probes}-2026-10-18.csv`. Actual browser viewport snapshots in `design-intelligence/sites/platform-{home-1440,home-390,services-1440,labs-1440,sign-up-1440}.webp`.

All claimed customers, legal registration, compliance, uptime/product KPI, awards, team, subscription prices and vendor template commerce represent **sample source copy** and must not become verified production facts. Source footer `Platform B.V.`, Netherlands address, `hello@platform.nl`, and Framer `Buy Template $129` are separate demo identity vs creator storefront layers.

## Source visual DNA

Body `#161719` computed (rgb 22/23/25), **Inter Display** for display text with fallback, dark technical product canvases and vivid coral/orange accent on actionable verbs/buttons. Home H1 ~100px at 1440 → 54px at 390; services H1 ~70px desktop, not present in sampled phone DOM. Motion-rich dark neural/technical hero with speckles, orange CTA and a narrow release pointer; application/telemetry cards, contrasting dark modular sections, data proof and charts, process/proof/offer alternation. Homepage **21,423px desktop, 28,097px mobile**, **68 img + 4 video + 2 canvas desktop**, **60 img + 2 video + 2 canvas mobile** (DOM nodes, not confirmed media fetch/GPU draw budget). Preserve empty space/semantic hierarchy rather than reproducing an indiscriminate cinematic effect on every card.

## Complete route recipes

1. **Home /**: wordmark/minimal header → "You innovate, we automate" and oversize build/run/scale manifesto → See Platform in action / Book a Demo → Neural Core/Neural Network featured → Our Work and claimed 8/8 lineup → Our Services → Our Process → Smart Analytics → Pricing and Studio $49 / Scale $89 / Supreme $249 sample tier cards (Monthly/Yearly, seats, plans) → FAQ → Meet the Team → Testimonials → Platform Labs related stories → Home contact form → company/footer legal and newsletter. Most header section links are homepage `/#section`, **not deep routes**.
2. **Services /services**: focused modular infrastructure hero → Neural Network/AI optimization/automation/scaling/operational capabilities → contact CTA → footer/legal. Distinct route, not /services/* CMS.
3. **Labs /labs**: Labs editorial intro → article cards (7 initial) → functional **Load More** displays the eighth ethical-AI article → related CTA/newsletter/footer. Test source relative links `./labs/*`, not root-only selectors.
4. **Labs detail /labs/<slug>**: eight subjects (adaptive AI, ethics, latency, observability, small teams, learning systems, collaboration, predictive scaling); byline/date/hero → narrative/media → More Articles → contact/newsletter/footer. Source CMS H1 can be duplicated by related heading and responsive variants: replace with one logical article H1 and lower-level related heading.
5. **Sign-up /sign-up**: FrameAuth-styled "Create your account with us" → Google/GitHub buttons and email method → sign-in crosslink. Real provider handshake unverified.
6. **Sign-in /sign-in**: matching FrameAuth "Enter back into your account" → identity input / providers → sign-up crosslink → OTP handoff only once real auth flow is implemented.
7. **OTP /otp**: "Enter the code sent to your email" + Code text input and reset link. Blank sampled code input `required=false`; add explicit validation, expiry, resend/rate-limit, error state, backend verification when production.
8. **Account /account**: Name/Email profile form accessible without verified session; treat session enforcement as **not demonstrated** and never as confirmed account management.
9. **Four legal**: `/terms-of-service`, `/privacy-policy`, `/data-protection`, `/gdpr-compliance`, each should have title, owner-approved effective/modified dates and policy scope; source generic SEO title is weak.
10. **Homepage pricing anchor**: Studio/Scale/Supreme subscriptions, cost displayed on sample states, monthly/yearly controls, plan-seats content, Sales handoff; a Plan Switch click did not alter sampled text. Do not assert checkout/payment/annual calculation work.

## Component and interaction templates

Dark/amber hero, technical release ticker/card, product lineup feature tiles, process/service case tiles, smart analytics monitor UI, three tier cards with real state, Labs Load More archive, article context/related cards, FrameAuth provider panels/OTP/account forms, visible consent lead/newsletter forms, legal/footer publisher separation.

**QA hard gates:** one semantic H1 per route and breakpoint; repair Labs/auth missing headings and CMS article duplicate H1s; distinguish CTA anchor/route destinations; remove nav links to actual 404 and `/labs/:LGnOksssn`; ensure sample forms don't expose typo `Emaiil` and all real user input validation; prevent UI-only auth security theater and demonstrate complete OAuth/OTP/session state before claiming functioning accounts; keep real billing/interval rates and annual savings approved; replace fictitious client/KPI/security/compliance claims; move template seller $129 promotion out of end-client frontend.

## Transfer use

Promote **site-wide information architecture and mechanisms**, not brand/trademark/client data or unverifiable credentials. Choose existing premium-saas-dark for baseline skin; motion level must remain bounded. For true technical credibility connect the visualization to real product state/data, using deterministic demo data explicitly labeled as sample. Respect reduced motion, responsive headings, mobile performance and accessible forms. The source is a **marketing/template showcase**, not a certified production AI orchestration platform.
