# PlatForm / Platform® — Complete Framer Website Design Intelligence

Source: https://plat-form.framer.ai/ . Audit: **2026-10-18**. This is a **dark AI infrastructure, automation, SaaS/service Framer template** presented as Platform B.V., Netherlands, including marketing, CMS Labs articles, a FrameAuth-shaped customer journey, legal policies and an embedded **template creator purchase promotion ("Buy for $129")**. These are template source assertions and UI fixtures; do not transfer the Dutch address, uptime, project outcomes, customers, team, GDPR compliance, security assurances, subscription prices or active accounts as verified business facts.

## Exhaustive 19-Route Census

Official `/sitemap.xml` returns HTTP 200 and lists **19 URLs; 19/19 HTTP 200**. Page-family inventory:

- **Homepage `/` (1)** — an extremely long single landing page: Hero, product proof, Work, Services, Process, Smart Analytics, Pricing, FAQ, Team, Testimonials, Labs and contact; many nav labels target homepage fragments (`/#work`, `/#pricing`, etc.), **not separate routes**.
- **Services `/services` (1)** — modular digital infrastructure and AI capabilities, including Neural Network (learning engine), automation, infrastructure, scaling, observability and security. Distinct service-detail content; no independent `/contact` or `/pricing`.
- **Labs archive `/labs` (1) and EIGHT deep CMS article routes**:
  `/labs/adaptive-ai-smarter-decision-making-in-digital-products`;
  `/labs/ethical-ai-systems-for-scalable-products`;
  `/labs/zero-latency-infrastructure-for-real-time-ai`;
  `/labs/automated-infrastructure-observability-made-simple`;
  `/labs/ai-powered-process-automation-for-small-teams`;
  `/labs/the-evolution-of-self-learning-systems-in-modern-tech`;
  `/labs/designing-human-ai-collaboration-in-saas`;
  `/labs/predictive-scaling-beyond-traditional-auto-scaling`.
- **Auth paths (4)**: `/sign-up`, `/sign-in`, `/otp`, `/account`; marketing routes have explicit sign-up links. UI reads **"Powered by FrameAuth"** and offers Google/GitHub and email-like inputs, but OAuth, OTP delivery/verification, session gating and account changes were **not tested**. All four routes are HTTP 200 even without a logged-in session; this does not establish security or backend behavior.
- **Legal and data (4)**: `/terms-of-service`, `/privacy-policy`, `/data-protection`, `/gdpr-compliance`. Legal copy is live template content, not independently audited for correctness. Homepage and legal pages have generic SEO title `Platform® — Modular Landing Page` instead of unique canonical route-specific titles; CMS articles have article-specific titles.
- **Supplementary / negative route probes (12)** all **HTTP 404**: linked **`/404`** and linked broken **`/labs/:LGnOksssn`** (likely unbound Framer CMS route), plus `/pricing`, `/about`, `/contact`, `/projects`, `/blog`, `/dashboard`, `/login`, `/signup`, `/does-not-exist-20261018` and `/labs/this-article-does-not-exist`. Do not invent these as valid pages or silently replace explicit path names.

HTTP route inventory `data/platform-route-inventory-2026-10-18.csv` includes **31** rows (19 official + 12 supplementary) and canonical/title/meta/H1/HTML/media counts. `data/platform-internal-links-2026-10-18.csv` records **224 source-to-internal-target link pairs**. This is a complete official-sitemap + linked-path scope, not every possible unindexed Framer preview path.

## Desktop/mobile design observation

Chromium rendered **21 routes** (all 19 official + the 2 explicitly linked broken routes), at **1440×900** and **390×844** = **42 successful browser states**. All sampled `documentElement.scrollWidth - innerWidth` values were **0**, but document-level overflow cannot prove sticky internal panels are unclipped. Evidence `data/platform-rendered-states-2026-10-18.csv`.

The computed body surface is near-black **rgb(22,23,25) = #161719**. Display type is **Inter Display** (with declared `Inter Display Placeholder` fallback); body computed `sans-serif`. Orange/coral emphasis and CTA/action details contrast against dark digital-technical surfaces; no exact accent hex confirmed by computed sample. The homepage uses oversized display headlines with a vivid accent applied to selected words, small technical annotations, abstract glimmering orbital/neural graphics, product tiles, chart/mock telemetry and dark panels with meaningful spacing. **Homepage H1 ~100px desktop →54px mobile**, service page H1 ~70px desktop; homepage H2 about 28px in sampled first H2. Framer's variant duplication means H1 counts differ by breakpoint and content family (0,1,2,3,4 sampled); notably **`/labs` has visual H2 with no semantic H1**, and all four auth pages had **no H1** in the sampled DOM. Services lacks H1 in the 390px sample despite H1 on desktop — accessibility heading/variant boundary.

Home DOM at 1440px **68 `img` nodes, 4 `video` nodes, 2 `canvas` nodes**. At 390px **60 img, 2 video, 2 canvas**, no evidence those counts map one-to-one to downloaded media files or that canvases mean GPU 3D. Home scroll heights **21,423px desktop** and **28,097px phone**. Homepage includes template vendor popup; screenshot captures after 2s load `design-intelligence/sites/platform-home-1440.webp`, `platform-home-390.webp`, `platform-services-1440.webp`, `platform-labs-1440.webp`, `platform-sign-up-1440.webp`. First frames taken at DOMContentLoaded can still show entry-animation blank areas; final evidence frames were captured after longer settling. Screenshots are snapshots, not proof of motion FPS or network bytes.

## Deep route-family structure and UX

### Landing / : dense modular infrastructure narrative

Desktop first fold reads **"You innovate, we automate."**, followed by `— The smarter way to build, run, and scale your business.`, a demo CTA, neural-network latest release and animated/visual technical stage. Hero glimmer/particle aesthetic is dark cinematic, not a generic pastel SaaS template. Below: Work / Featured Product **Neural Core**, `Platform Suite Neural-Powered Infrastructure`, product lineup `8/8` (marketed count, **no eight deep product routes in sitemap**), Services, Process, Smart Analytics, tiered Pricing, FAQ, Team, Testimonials, Labs previews and long contact/footer.

Home pricing offers **Studio $49**, **Scale $89**, **Supreme $249** on initial visible text; each describes Monthly/Yearly, `You save 16%`, plan features, `Select Plan` and seats. Example Studio: Smart Deployment, Basic Monitoring, Core Security, Email Support, 5 seats, Basic Analytics, Standard API. Scale lists all Studio features + AI optimization, advanced monitoring, enhanced security, 24/7 support, auto-scaling, full analytics, priority API. Supreme markets enterprise features. These are **Framer template prices**, not a verified live billing service. A `Plan Switch` is clickable but first click did **not** change the captured price text, so billing-switch functional correctness remains unconfirmed. No payment or subscription created.

A homepage `#contact` lead-capture form appears with visible required **Your Name, Your Email, Your Company** (from one captured form) plus an atypical second form (newsletter: required Name and Your Email) and many hidden `name` fields as spam traps/instrumentation. In the newsletter source one field `name="Emaiil"` is misspelled, versus `Email` on another form. Form delivery and handling were not tested. Template vendor component repeatedly displays **"New Template!", "Buy Template", "Buy for $129"**, which must be removed/reassigned when deploying an actual client brand.

### Services /services

Uses a focused hero: `Our Services` -> "Flexible solutions for building modern digital infrastructure" -> "Modular, flexible solutions for modern digital infrastructure", then distinct service/technical narratives. Source first named capability **Neural Network**, a self-learning intelligence core; other content discusses AI-driven optimization, automation, deployment/scaling and operational support. Services page has **no checkout/auth of its own**. Preserve distinction between capability messaging and genuine technical/product proof.

### Labs /labs and 8 articles

Visual Labs index uses editorial hero `Platform Labs®` and concise description of insights on AI, automation and infrastructure. **Archive initially exposes SEVEN unique CMS article hrefs**, and clicking **Load More exposes all EIGHT**, with final newly visible `/labs/ethical-ai-systems-for-scalable-products`. This was verified by a corrected relative-link-compatible browser probe, not inferred from `Load More` label. Article pages have authored cover/metadata, titles, long explanatory body and `More Articles` recirculation. Some article pages have multiple H1 nodes because CMS/Framer responsive duplicates and the **More Articles H1**. Ensure one accessible document H1 and lower-level related-content heading in production.

The 8 editorial topics are AI decisioning, ethical scaling, zero-latency infrastructure, automated observability, small-team AI process automation, self-learning systems, human-AI collaboration and predictive autoscaling. These are source publication topics, not proof each claimed technical system is shipped.

### Auth: /sign-up, /sign-in, /otp, /account

All four have consistent split/shell with bottom repeated site template vendor/footer. `/sign-up`: "Create your account with us"; `/sign-in`: "Enter back into your account"; `/otp`: "Enter the code sent to your email", a `Code` text input and reset/forgot CTA; `/account`: Name/Email profile inputs. Sign-up and sign-in show Google/GitHub buttons and brand **FrameAuth**. Auth primary forms are method POST in source HTML; sampled email and code fields have `required=false` / no H1, yielding misleading `form.checkValidity()===true` for blank values; do not assume production auth is secure, complete, or accessible. No user credentials supplied and no real submit performed.

### Legal, provenance, SEO and CTA QA

Four independent legal pages are reachable and self-canonical, but most share a generic `Platform® — Modular Landing Page` document title. The frontend footer identifies **Platform B.V.**, `hello@platform.nl`, `Westerdoksdijk 500, 1013 BX — Amsterdam, Netherlands` and a 2021–2026 copyright. They are **template content**, not independently verified legal company registration, email delivery or compliance. Site nav/footer exposes `404` as a clickable page (HTTP404), and at least one `/labs/:LGnOksssn` placeholder link resolves 404; remove broken CMS placeholders in an actual implementation.

The source's headline stats (e.g. `200+ Enterprise Clients`, `Uptime`, `Performance`), Neural Core release and product lineup, testimonials and named team members are **unverified marketing fixtures**. Framer template upsell `$129` belongs to the template publisher's storefront, not Platform subscription plans. Quality gates: content evidence, canonical route titles, no linked 404 nav item, required validation, real OAuth/OTP session flow and billing state behavior.

## Interaction audit and confidence boundary

`data/platform-interaction-probes-2026-10-18.csv`: **18 bounded probes**, covering homepage heading/CTA/section anchors, pricing control anatomy and inconclusive plan switch, Services content, Labs initial hrefs and the corrected 7→8 Load More delta, an article's headings and related links, four FrameAuth page forms/fields/providers, two legal pages and mobile nav controls. One early Labs probe used an incorrect relative-href-only CSS selector and produced an empty set; a subsequent independent relative-aware probe corrected it, preserving that test limitation in evidence.

**High confidence:** 19 sitemap URL HTTP200, 12 extra URL HTTP404, 224 internal href pairs, 42 error-free dual viewport state extractions with zero outer document overflow, dark #161719 and Inter Display computed styles, 7→8 Labs Load More, /sign-up/sign-in/otp/account document structure and visible FrameAuth branding. **Limited/unverified:** exact canvas implementation and animation fps, successful OAuth/OTP/account actions, charging/yearly price switch, lead/newsletter delivery, customer logos/metrics/claims, independent GDPR compliance and true media transfer/performance.

## Patterns worth reusing

**Infra product showroom + trustworthy systems documentation:** communicate automation with tangible product UX/telemetry, not fake uptime/live metrics.
**All-sections homepage, few deep pages:** navigation anchor names ≠ sitemap route names.
**Expandable editorial collection:** 7 featured articles and 8th on Load More, with CMS href parity check.
**Studio/Scale/Supreme subscription cards:** tiers/show rates and explicit interval controls, but real billing logic requires actual price state and checkout proof.
**Provider login with owned backend:** Google/GitHub/Email + OTP/account are one identity lifecycle; HTML forms and trademarked FrameAuth badge alone are insufficient.
**Source identity firewall:** separate Platform NL business copy and Framer creator's $129 template purchase offer.
**Responsive variant semantic QA:** Framer can hide visible headings yet leave duplicate H1s in DOM; test the accessibility tree per breakpoint.
**Broken link and title audit:** /404 and CMS placeholder must not ship as normal nav; legal page titles/route semantics must be unique.

This profile is a **complete official website route-family distillation**, not a claim that sample prices, AI infrastructure or security services genuinely operate.
