# Superior — Complete-Site SaaS/Startup Framer Template Distillation

Source: https://superior-template.framer.website/
Audit: **2026-10-18**. Direct **Jarvis MCP Chrome extension on the user's Windows machine** was connected (Chrome Win32NT browser selected). The **user's own Chrome**, not only a headless substitute, was used for live home DOM/screenshot, desktop representatives of Pricing, Integrations index/detail, Blog, Careers index/job, Hero v2, Book a Demo, Download and Contact and mobile homepage inspection at 430x844. For exhaustive two-breakpoint coverage, an **additional isolated Chromium** rendered all sitemap URLs at 1440x900 and 390x844. Do not conflate these two methods. This is a publicly available **commercial Framer template**, not independently verified SaaS operations/customer results/hiring status.

## Entire 48-route sitemap, linked pages and QA evidence

`https://superior-template.framer.website/sitemap.xml` HTTP200 includes **48 URLs**. **47 return HTTP200**. **`/404` is explicitly in the sitemap but returns HTTP404**, and can also appear in nav/footer; do not call the sitemap 48/48 HTTP200. Eleven extra non-sitemap negative routes (`/about-us`, `/services`, `/features`, `/login`, `/sign-up`, `/dashboard`, `/contact-us`, a fabricated path and nonexistent integration/blog/career details) all HTTP404. CSV `data/superior-route-inventory-2026-10-18.csv` = **59 rows** (48 declared + 11 extra). `data/superior-internal-links-2026-10-18.csv` = **966** unique source-target pairs, far beyond a homepage-only inventory. Each deep route was independently checked by HTTP and in the browser.

Full sitemap families:
- `/` homepage (1).
- **Three independently published full-length hero variants** `/heroes/hero-v2`, `/heroes/hero-v3`, `/heroes/hero-v4`. These are **complete alternative landing pages**, not just image assets or three slotted heroes.
- `/integrations` archive + **15 detail pages**: `core`, `orbit`, `pulse`, `flow`, `prism`, `fusion`, `elevate`, `scale`, `bridge`, `atlas`, `nova`, `vertex`, `luminous`, `cloud`, `osaka`. All **15/15** detail URLs are linked from archive. Marketing labels/partner names do **not** establish a working API integration.
- `/blog` archive + **10 deep articles** (11 total blog routes) concerning design simplicity, code collaboration, platform performance, customer support, transparency, product roadmaps, marketing storytelling, data analytics, automation, and subscription launch mistakes. **Only 7 distinct detail hrefs observed on the initial Blog archive state**, even though ten URLs are live: inspect pagination/filters/related and ensure 10/10 discoverable before adapting.
- `/careers` archive + **6 job details**: Senior Backend Engineer, Data Engineer, Mobile Engineer, Principal Product Designer, Product Designer, Mobile Designer; **6/6** reachable by archive links; sample job's `Apply now` goes `../contact`. They represent demo jobs unless an employer verifies current openings.
- `/legal/terms-of-service`, `/legal/privacy-policy` (2).
- Other standalone: `/about`, `/pricing`, `/contact`, `/book-a-demo`, `/download`, `/changelog`, `/waitlist`, `/404` (8).

**98 isolated Chromium route/viewport states** cover all 48 published URLs **plus one negative invalid URL** at **1440×900 and 390×844**. Of 98, **94 HTTP200 and 4 HTTP404** (sitemap /404 and invalid path at both widths); **zero positive outer overflow, zero JS page errors** in sampled navigation. CSV `data/superior-rendered-states-2026-10-18.csv`. All variants, detail families, legal and forms are represented in this file. Browser evidence 9 WebP screenshots `design-intelligence/sites/superior-*.webp`: home desktop/mobile, pricing, integrations, Orbit detail, blog, careers, demo, full alternate hero v2. **20 bounded UI probes** `data/superior-interaction-probes-2026-10-18.csv`; tests did not submit real emails, book actual meetings, purchase plans or apply for jobs.

## Genuine visual hierarchy and design system

The whole site uses a **near-white / white canvas**: computed body background **rgb(255,255,255) = #FFFFFF**. Display and body identity **Inter / Inter Placeholder**, sharply structured black-gray text and extremely restrained light-gray panels, fine borders and soft elevated application mockups. Tiny green **NEW** release/announcement pill and growth micro-metrics provide selective accent, while primary CTA is mostly black. This is **not** a dark AI/neon cyberpunk SaaS style. Visual styling: friendly premium startup/professional product UX, clean SaaS surfaces, serif-free typography, modular bright page templates, roomy central hero, compact primary navigation with Pages menu, pill-shaped black/outline CTAs and a large realistic **dashboard app mockup** beneath hero.

The homepage H1 is "The most powerful business platform." at **64px / 1440px** and **36px / 390px**, bold Inter; sampled user's real Chrome at 430px also calculated 36px. Desktop home document height **17,063px**, mobile **20,275px**, with **45 img / 0 video / 1 canvas** nodes at desktop, **39 img / 0 video / 1 canvas** at 390px. Counts are **DOM nodes not downloaded images, GPU performance or assets created**. Full alternate hero v3 has **2 H1 nodes on desktop** due to duplicated responsive/layout variants while one H1 mobile; many integration details and waitlist have **zero semantic H1**, even though visual title exists. Legal and FAQ are not independent design systems.

## Route-family UX dissection

**Homepage**: logo + Pages navigation, About, Pricing, Integrations, Blog, Book a Demo; announcement `NEW Announcing API 2.0`; center-aligned product manifesto; Get Started / Learn More; screenshot-like dashboard featuring revenue/customers/projects; social trust proof; sections **Powering teamwork to simplify workflows**, **Dynamic planner that keeps you ahead**, **Analytics that power smarter decisions**, **Features designed to empower your workflow**, **Suited for every scenario**, **Everything you need to grow, in one place**, **Explore our most powerful features**, **Integrates with your favorite tools**, **Trusted by the best in your industry**, **The latest insights**, **In case you missed anything**, and **Start your trial today**. Some featured claims, quotes and chart numbers are template mock data, not actual business results. Separate from vendor's "Get template" / Framer sales CTA.

**Hero variants**: all three `/heroes/hero-v2/v3/v4` are full independent pages sharing the Superior SaaS brand but differing section composition. v2 includes a hero/workflow, planner/analytics, pricing and getting-started story; v3 is shorter and has source duplicated desktop H1; v4 is broader with core feature scenario/product blocks. Do not mistake variants for one navigation subcomponent. Treat page length, supporting proof cadence, and section ownership separately.

**Pricing /pricing**: "Choose a plan that's right for you", comparison matrix **Compare plans**, multiple plan offer cards, expert contact/CTA, testimonial and FAQ. Source had no semantic button found among sampled `button/input/[role=switch]` controls at page load; do not claim tested real billing toggles/checkout. Deep packages, payment provider, subscription live backend unverified.

**Integrations /integrations**: clean searchable/filterable-looking catalog with categories **Popular, Collaboration, Automations, Engineering** and **15 detail pages**. A `Search Icon` exists and can be clicked; bounded probe did **not** establish a working search input/filter, so mark it **unverified**. Integration detail e.g. Orbit has icon/label/value "Link tasks between project management tools for seamless collaboration and tracking", category label, long explanatory text and CTA/footer; **no real H1** in the sampled `/integrations/orbit` DOM. Distinguish CMS visual title from correct article-like semantic H1; replace fixture partner claims with approved provider docs and verified deep link.

**Blog /blog**: editorial index "Blog", category/covers, newsletter "Enter your email" and search icon. **Seven of ten CMS detail hrefs** initially linked from archive in bounded probe. Actual search filter and load/pagination impact unverified; do not claim it can reach all 10 from archive without a follow-up navigation proof. Article details have **one H1** and share-on-X / LinkedIn / Pinterest affordances, cover/metadata/narrative and related content CTA; no social API success verified. Source generic document title **Superior - Startup & SaaS Template** also appears on legal and many others; customize unique route metadata in production.

**Careers /careers**: "Build your future with us" -> "Why join us" -> "Open roles" then six CMS job cards. Deep job documents include job title, role specifics and apply CTA: `/careers/senior-backend-engineer` links Apply now to `../contact`. No recruitment backend or current vacancy verified.

**Contact /contact**: heading "Contact our sales team" and multi-region office narrative. Browser real Chrome verified form fields `Name` (optional), `Email` (required), `Company` (optional), `Message` (optional) plus hidden honeypot fields; native blank form check invalid. Form action points to current site, **no successful send tested**.

**Demo /book-a-demo**: heading "Book a demo", field `Name` (required), `Email` (required), `Company`, native dropdown for professional role (Designer/Engineer/Marketer/Investor etc), team size (1–10, 10–25, 25–50, 50+), country selector and CTA. Native blank form invalid; **no verified booking calendar/provider**.

**Waitlist /waitlist**: sparse full-height email field `Enter your email` and Join waitlist button, but source input `required=false` and blank native `checkValidity()===true`. This is a **production conversion/accessibility weakness** requiring required state/server validation and confirmed opt-in.

**Download /download**: "Download our apps" and platform distribution CTAs. Do not assert operating system apps or working installer URLs if source only contains marketing mock calls-to-action.
**Changelog /changelog**: release timeline entries (sample `v1.0.2 Jan 16, 2025` / Custom Dashboard). Treat dates/release items as source fixtures, not active roadmap.
**About /about**: product/company positioning, values, social proof/team, storytelling and trial CTA. Trust claims must be verified.
**Legal**: two stable legal paths; title reused generic template product name; legal owner must approve.
**/404**: intentionally sitemap-indexed but HTTP404. Keep as error UI, not main indexed content or conversion path.

## Verification caveats / transfer boundaries

- **47/48 official HTTP200**; don't misstate 48/48.
- **96 official screenshot states + 2 negative states**, no outer overflow (doesn't prove device-level visual QA inside all panels); **20 bounded probes**; Chrome MCP direct on Windows + independent Chromium verified separately.
- Stronger real browser proof for Homepage, Pricing, Integrations index/detail, Blog, Careers index/job, Hero v2, Contact, Demo and Download; no claim manual eyes inspected all 48 individually when batch probes rendered full coverage.
- Template look is **white minimalist Inter**, not black/neon AI; use `premium-saas-light` if present, otherwise a matching existing SaaS skin, never invent a new skin only for look.
- Search icon probe opens/clicks but not conclusively filtered; Blog archive 7/10; no successful contact/demo/waitlist submission; job and product data are illustrative; some H1 absent/duplicated; pricing commercial claims and Framer marketplace promotion separate.
- Images/video: UI design generation guidance supports original **dashboard illustration** only if it represents a fictional product clearly; never substitute generated screenshot as proof that an actual running app exists.

## Portable pattern inventory

1. Hero announcement pill → 64/36 Inter thesis → paired CTA → primary app mockup fold.
2. Modular Product Story: teamwork → planner → data analytics → features → scenarios → more feature details.
3. Full-page hero variants with shared design tokens and separate route maps.
4. Integration index/15-details family with typed taxonomy and links, no fake connectivity.
5. Editorial 10-story archive with 7 initial entries and clear reveal/discoverability checks.
6. Six-job careers with independent case-like job details and explicit apply handoff.
7. Pricing plans + genuine comparison matrix as two content depths.
8. Contact vs qualification-heavy demo vs waitlist: three distinct lead flows with correct required-field contracts.
9. Desktop/mobile responsive type hierarchy and clean product panel cropping.
10. Broken/fixture SEO & semantic heading checks; preserve real review provenance.

Transfer **structure and verified interaction contracts**, not site branding, exact stock imagery, vendor Framer upsell, fictional KPI or legal copy.
