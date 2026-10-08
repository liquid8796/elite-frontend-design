# Fizens — Full-Site Design Intelligence

Source: https://fizens.framer.ai/
Audit: 2026-10-08. Complete sitemap URL census plus representative desktop/mobile Chrome, CMS detail and form audit.

## Full-Site Coverage

**43/43 sitemap URLs HTTP 200.** Route families:
- home (1), core landing/utility routes (9): features, about, integration, download, contact, changelog, pricing, articles, overview;
- legal (2): term-and-conditions, privacy-policy;
- integration detail (9): Chainly, Syncnest, Relaylink, Connectzen, Integryhub, Taskio, Flownet, Databridge, Zapsync;
- team-member profiles (8);
- career detail pages (4): bussiness-analyst, marketing-manager, ios-developer, product-designer;
- financial/insurance editorial article details (10).

Four sampled paths outside the declared sitemap (/404, /jobs, /team-member and random unknown path) correctly returned 404. No /jobs index exists even though job detail routes do. Full 47-row dated URL/status/title/canonical census: modules/distilled-web-toolkit/data/fizens-route-inventory-2026-10-08.csv.

Chrome rendered 17 representative desktop 1440x900 and 15 representative 390x844 mobile states across every page family (including 404 and legal desktop). Root scrollWidth never exceeded viewport width in tested states. **This is 43/43 URL response validation and 32 representative rendered states; not 43 deep individual E2E tests.** Forms were not submitted, no payment made, apps not installed, and no actual finance data/API integration was authorized.

## Visual DNA

**Archetype**: light financial-product SaaS template with multi-route support/people/editorial/partner/finance documentation. Existing baseline `clean-product-light` is best anchor, optionally product-screenshot/comparison patterns from other SaaS sources. Do not create a redundant finance skin from one template.

**Observed CSS:** white #FFFFFF body; main dark ink #171717; supporting #4B5563; confident financial blue #0040C1 (rgb 0,64,193) for selected headings and CTAs. Primary H1/H2 rendered with Poppins, ~64px at 1440px desktop -> **36px at 390px mobile**. Geist, Instrument Sans and Inter also loaded in runtime but are not proof that hero uses them. Article H2 ~36px desktop -> 24px mobile, H3 ~24px ->18px. Vertical rhythm, subtle surface/price cards, dashboard and finance app screenshot motifs.

**Runtime:** homepage sample desktop 1440x14316, 98 image nodes, zero canvas/video, one visible newsletter form. Connected browser at larger 1875px viewport observed 194 images; mobile sample 390x19177 measured 243 images. These counts vary with Framer responsive/lazy media rendering. **About has 4 videos**, so video exists in the whole site even though not home. Fixed creator/Framer chrome and sticky content modules exist. No observed custom WebGL/3D engine.

**Global shell:** nav Home / Features / About / Pricing / Blog / All Pages / Contact and Get Started Free; footer includes Download, Integration, Changelog, person/job examples, policy links, publisher credits and marketplace. Template vendor badge, Framer promotion and "Get the template" checkout are not end-user fintech conversion.

## Route Grammar: Financial confidence through visible tools

### Home (~1440x14316 / 390x19177)
"Start Managing Your Finance With Our Tool" display thesis uses **three separate visible H1 fragments**, each 64px desktop -> 36px mobile. Long homepage flow:
- financial control promise + screenshots/visual proof;
- "Explore Our Standout Features";
- "Experience The Future of Finance", with time, anxiety, planning and security promises;
- "See Your Wealth Grow" / product analytics story;
- "How Fizens Can Help You" benefit scenarios;
- testimonial proof, then $0/$20/$40 tri-tier pricing;
- professional articles/news and FAQ;
- final financial-freedom CTA and app/download links.

Transfer **Financial Confidence -> Dashboard Evidence**, not unaudited security/performance/returns claims.

### Features (~1440x8373 / 390x11642)
Standalone feature/benefit chapter system: headline, product visuals, detail cards and repeated lead CTA. Shows a full product capability route rather than a homepage section only.

### About (~1440x7364 / 390x10240)
"The Fizens Journey": mission, brand/team and trust narrative; 4 videos in desktop/mobile inspection. Positioning and media proof are not independently verified customer testimonials.

### Pricing (~1440x4339 / 390x5797)
Three plan amounts $0, $20, $40 and "Compare Plans" feature matrix. Price numbers themselves use H1 tags in addition to page H1: implement semantic page heading with prices as content. This is a **Plan Compare -> Contact Continuation**, not tested subscription checkout. Header Get Started Free leads to /pricing, and home Get Started Now actions lead to /contact.

### Contact (~1440x1860 / 390x2574)
Actual contact form: **five required visible fields** (first name, last name, email, phone, message), alongside global newsletter. Correct visible input types email and tel. Nonvisible auxiliary fields in forms must not be counted as real user questions. Submission/status not tested.

### Integration hub + 9 detail pages
/integration (~1440x2006 / 390x4944): named partner directory and per-partner routes.
/integration/chainly (~1440x3658 / 390x6138): visible "Connect with Chainly" story, integration benefits and general contact/CTA. All nine details were in the complete sitemap HTTP census. **These are partner compatibility descriptions, not proof that working OAuth connection, institution authorization, data sync or connected-state UX exists.**

Transfer **Ecosystem Directory -> Scoped Compatibility Detail** with real connection/permission states implemented separately.

### Download (~1440x2218 / 390x3951)
A small multi-app destination list with Finora, Credexa and Investa product cards. Generic homepage App Store Vietnam and Google Play Games directory URLs were seen, NOT verified product-specific app store listings. Distill **App Portfolio -> Verified Install Destination**, not fictitious published finance apps.

### Editorial: /articles + 10 detail routes
/articles (~1440x2800 / 390x4834), with topical finance, investing, insurance and financial aid posts. Detail /articles/buy-low-sell-high (~1440x4584 / 390x6167): sectioned long-form article with H1/H2/H3, metadata and recommendation/reading continuation. **Education -> Financial Product Trust Loop** is transferable only with credible authored sources; don't treat template posts as personalized financial advice or regulated expertise.

### Team + jobs
8 profile details. Sample /team-member/sarah-jane (~1440x2085 / 390x3138) presents person role and bio in the common brand shell. People may be template placeholders.

**Important source defect:** all **4/4** /jobs/xxx routes have distinct slug and customized HTML titles, but visible H1 is always **"Product Designer"** (including /jobs/ios-developer, /jobs/marketing-manager and /jobs/bussiness-analyst). This is not correct CMS binding. /jobs index is 404. Sample /jobs/ios-developer (~1440x2899 / 390x3920). No verified application form was observed (only global newsletter). Transfer people/careers credibility taxonomy and strict slug/title/H1/body field alignment, not the faulty data.

### Changelog, legal, template overview, recovery
/changelog (~1440x2020 / 390x2379): standalone release chronology/updates destination.
/term-and-conditions (~1440x2662) and /privacy-policy (~1440x3292): distinct public policy routes, content subject to real product-owner legal review.
/overview (~1440x8215 / 390x10579): **Framer template marketplace all-pages index**, not a customer finance dashboard. Keep vendor template marketing separate from customer app navigation.
/404 returned actual HTTP 404 with branded shell.

## Responsive contract

At 390px tested every main route family with zero document-level horizontal overflow. Desktop -> mobile document heights:
home 14316 -> 19177; features 8373 -> 11642; about 7364 -> 10240; integration index 2006 -> 4944; integration detail 3658 -> 6138; pricing 4339 -> 5797; contact 1860 -> 2574; download 2218 -> 3951; articles 2800 -> 4834; article detail 4584 -> 6167; team detail 2085 -> 3138; job detail 2899 -> 3920; overview 8215 -> 10579. Heading scale 64px ->36px, articles 36px ->24px section heads. Card grids, comparison, brand/media and long-form descriptions become ordered mobile flow; document scroll is long but readable.

## Whole-site quality and non-transfer

1. **21 of 43 sitemap URLs** (home/core/legal plus all nine integration details) use the exact generic HTML title "Fizens - The Ultimate Finance SAAS Framer Template". All 43 declared URLs have self-addressed canonical. Generate route-specific SEO titles.
2. **Four job routes share Product Designer H1 despite distinct slug/title**, a direct template CMS mismatch. Require URL/metadata/visible job identity consistency.
3. Homepage hero and pricing cards produce **multiple visible H1s**; maintain typographic appearance with accessible heading hierarchy, not multiple main headings and price amount H1.
4. Many footer links sell/download the *Framer template* or point to generic social platform roots. Remove vendor/publisher chrome for a real financial business.
5. App store directory badges are not validated app listings, and integration descriptions aren't connected real integrations.
6. Security, returns and personal-finance results are marketing claims, not verified evidence. Financial/insurance editorial requires accuracy, attribution and suitable disclaimers before launch.
7. Newsletter/contact forms exist; don't assert successful delivery/CRM connection without testing.

## Template Vendor and End User Surface Firewall

Keep the marketplace /overview and publisher purchase interface separate from real finance SaaS conversion, product app installations and customer claims.

## Transferable mechanisms

- Financial Confidence -> Dashboard Evidence
- Integration Directory -> Partner Detail
- Multi-App Download Portfolio
- Three-Tier Pricing -> Comparison + Contact
- Finance Education -> Related Content
- Team/Career Proof with CMS Integrity
- Template Commerce Firewall (end-user vs vendor audience)

Do not transfer Fizens brand identity, exact fonts/asset/screenshots, fake partners/people/positions, financial promises or legal policy copy.

Auditable rendered-state data: data/fizens-rendered-states-2026-10-08.csv; four role H1 comparisons: data/fizens-career-title-audit-2026-10-08.csv.
