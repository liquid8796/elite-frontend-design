# Nouva — complete public-site design intelligence

Source: https://nouva-template.framer.website/
Audit: 2026-10-08; complete sitemap HTTP census and actual connected Chrome desktop/mobile route inspection.
Coverage: 8/8 sitemap URLs HTTP 200 plus linked /404 at HTTP 404. 9 routed surfaces rendered at 1920x889 and 390x844. Marketing sections, pricing state and scroll-dependent statistics were inspected. External FrameAuth identity service was NOT authenticated against, and contact/auth forms were not submitted.
Archetype: dark-ai-productivity-saas. Skin anchor: premium-saas-dark. The current design repository has 13 baseline skins; no new baseline required.

## Complete public route topology

| Route | HTTP | Desktop document | Mobile document | Job |
| --- | --- | --- | --- | --- |
| / | 200 | ~1905x11075 | 390x15559 | product thesis, workflow proof, pricing, objections and lead CTA |
| /contact | 200 | ~1905x1554 | 390x1913 | lead capture/support contact form |
| /sign-up | 200 | ~1905x1044 | 390x1301 | passwordless-style registration email UI |
| /sign-in | 200 | ~1905x1069 | 390x1326 | sign-in email UI |
| /otp | 200 | ~1905x1044 | 390x1326 | OTP code entry UI |
| /account | 200 | ~1905x1240 | 390x1523 | account/profile edit form UI |
| /legal/terms-of-service | 200 | ~1905x2702 | 390x3552 | readable long-form terms |
| /legal/privacy-policy | 200 | ~1905x2680 | 390x3607 | readable long-form privacy |
| /404 | 404 | ~1905x1226 | 390x1453 | authored error/recovery page; linked in footer, not in sitemap |

The eight sitemap entries are not eight distinct marketing landings. On homepage, #hero, #benefits, #features, #pricing and #faq are section anchors, not separate routes. This distinction prevents manufactured route counts. The authored 404 correctly returns 404, not a broken page. Full dated route inventory is in modules/distilled-web-toolkit/data/nouva-route-inventory-2026-10-08.csv.

## Design DNA — observed, not a copied skin

- Background body: rgb(8,12,18) = #080C12 (near-black blue).
- Raised sections/cards: rgb(14,19,29) = #0E131D, nested surfaces ~#0F1520 and #121926.
- Display/heading text: rgb(250,250,250) = #FAFAFA; body white or gray rgb(153,160,176) = #99A0B0.
- White primary CTA with ~12px radius; dark foreground is implemented inside its children.
- Visible type roles: Onest for display, body, section titles and inputs; Inter also loaded.
- H1 desktop ~60px, mobile ~46px; H2 48px -> 38px, feature H3 36px desktop, legal H2 28px -> 23px.
- One dark shell, quiet whites/grays, dense rounded bento cards rather than neon heavy-glass ornament.
- Home desktop 22 image nodes, 0 video and 0 canvas; mobile 16 images, 0 video/canvas in sampled render.
- Framer runtime with sticky sections and animated counters; no observed WebGL/Three or independently authored cinematic shader scene.
- Sticky/fixed stages on homepage; don't assume a fixed nav/content stack is automatically safe at mobile.

## Homepage — long-form product-to-lead system

At 1920x889 the document was ~1905x11075; at 390x844 it grew to 390x15559 without outer horizontal overflow.

Observed section sequence:
1. Hero: "Words that work. Every single time." / AI content writing, tracking and team output; "Try for free" leads to /contact.
2. Benefits/problem: modern team output thesis plus scroll-triggered counters.
3. Three task/goal/time benefits: "Track your output", "Stay ahead of goals", "See where time goes".
4. Feature triad: growth/analytics, one brief to many formats, reduced workflow effort, with concrete product screenshots.
5. Team/platform expansion and more use cases: "One platform, endless possibilities".
6. Differentiation/competitive positioning: "Everything else falls short."
7. Testimonial proof: "Teams who never looked back"; template social proof and numeric claims are not independently substantiated.
8. Pricing: monthly/yearly switch visual + Starter/Pro/Teams plan cards and feature comparison.
9. FAQ: six buyer questions about ChatGPT, adaptation, volume, workflows, cancellation and privacy.
10. Final CTA / footer: product promise and direct contact, account/login, legal and social links.

This is **Problem -> Workflow -> Proof -> Plan -> Objection -> Lead**. The product promise is not demonstrated as a live editor; visible screenshots/mock UI provide task-specific proof. Transfer task anatomy, not fake metrics or screenshots.

### Scroll-triggered metric reveal

The benefit area initially showed duplicate numeric states 0%, 0.0x. After scrolling that section into the viewport and waiting ~1.3s, visible text yielded 47%, 46%, 3.2x, 3.1x, 68%, 66%. This indicates animation transitions and/or layered animated nodes, not a truthful live calculation.

**Metric Reveal with Stable Meaning**: lazy/scroll counters should retain a readable static target and label, respect reduced-motion and not show confusing 0% placeholders to non-motion users. Treat all values as marketing template claims, not audited business outcomes.

### Commercial routing reality

Header "Sign In" goes to /sign-in. Nearly every homepage marketing/pricing CTA ("Try Nouva", "Try for free", all "Get started" plan cards) goes to **/contact**, not a checkout, real product editor or /sign-up. Preserve this distinction as **Contact-First SaaS Conversion**, rather than claiming users can start using the app from marketing CTA.

Pricing visually advertises Starter $0, Pro $19 user/mo, Teams $29 user/mo and a "Yearly 20% OFF" switch. In one browser click on the switch wrapper, displayed amounts and its "Inactive" state did not change. This is a **suspected nonfunctional billing switch**, requiring browser/keyboard verification before reuse; we did not assert backend billing or annual plan economics.

## Contact route — qualified lead form

/contact renders one explicit form with seven input/control nodes:
- First name, Last name, Email — required;
- Company — optional;
- Subject select — required;
- Message textarea — required;
- Newsletter checkbox — optional.

Contact is an actual form surface (not a dummy mailto-only CTA). Content and status of form submissions were not tested. The conversion path is an enquiry/contact funnel despite marketing copy saying "Try for free"; either align CTA language or provide a genuine signup path.

## Passwordless account UI family (FrameAuth)

- /sign-up: one form with email text input and submit, secondary Sign In link.
- /sign-in: equivalent email form with Sign Up link.
- /otp: code input and submit.
- /account: name/email inputs and submit.
- All appear in the same Nouva brand shell and include the external "Powered by FrameAuth" link at https://dub.frameauth.com/hello.

This is **Branded Authentication Shell Continuity** (marketing identity -> email form -> code verification -> profile) and **Small-State Auth Route Grammar**. The UI structure is visible; no identity backend, signed-in guard, OTP delivery, recovery or session security was verified. Public navigability of /account alone does NOT prove an authorization vulnerability.

Observed auth fields are generic type="text" rather than purpose-specific input types, and required flags were absent in the sampled DOM; production apps should use appropriate email/one-time-code semantics, autocomplete hints and proper labeled accessible submit actions. Do not copy the auth provider's scripts or infer its backend from template markup.

## Legal, error and global utilities

- /legal/terms-of-service and /legal/privacy-policy are dedicated, sectioned long-form routes using Onest and smaller H2 roles, with contact mailto links. Legal copy must be reviewed by actual owner/counsel before publication; it is not a product feature recipe.
- /404 returns HTTP 404 and retains branded recovery/navigation rather than a bare server error. Its footer link should be treated as template QA/preview affordance, not necessary consumer navigation.
- Footer shows creator credit, external template licensing ("Get Template"), X/Twitter creator profile and generic LinkedIn/Instagram destinations. These are template provenance/placeholder chrome, not trustworthy social validation.
- Contact and homepage share the same generic document title "Nouva — AI Content Template for Framer", as does /404; auth and legal routes are more specific. Route-specific metadata should distinguish contact from home, and production copy should remove "Template for Framer".

## Responsive contracts

All 9 representative routes at 390x844 had root document width 390 and zero positive horizontal overflow:
- marketing normal document scroll grows from ~11075px to ~15559px;
- contact 1554 -> 1913;
- signup 1044 -> 1301;
- signin 1069 -> 1326;
- otp 1044 -> 1326;
- account 1240 -> 1523;
- legal 2702/2680 -> 3552/3607;
- 404 1226 -> 1453.

Display scale 60px -> ~46px; section scale 48px -> ~38px. Pricing cards, FAQ, and marketing proof stack into tall but readable mobile flow. The global shell remains; mobile visible navigation depends on responsive variant and footer links.

## Transfer rules / anti-patterns

Promote:
1. Problem -> Workflow -> Proof -> Plan -> Objection -> Lead.
2. Contact-First SaaS Conversion Routing.
3. Branded Authentication Shell Continuity.
4. Scroll-Triggered Metric Reveal (with stable non-motion values).
5. Dark Onest Bento Task Proof.
6. Workflow Triad -> Expandable Capability Proof.
7. Legal/Recovery Support Routes with Real Status.

Do NOT transfer:
- exact Nouva/creator/FrameAuth logos or copy, exact colors/fonts, metrics, testimonials, template screenshots or pricing as real offers;
- Framer builder badges, template-purchase links and placeholder social pages;
- email/OTP implementation without auth security review;
- a monthly/yearly switch without confirmed functionality;
- duplicate generic contact page title.

Audit boundary: HTTP/HTML census of all public routes and Chrome rendered desktop/mobile routes; no paid checkout, authentication, form submission or multi-user production workflow was exercised.
