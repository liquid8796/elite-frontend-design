# Superior — Full SaaS/Startup Framer Site, 48-Route Design Toolkit Specification

Source: https://superior-template.framer.website/
Deep intelligence: `../../../design-intelligence/sites/superior-template.framer.website.md`
Archetype: `white-modular-saas-product-platform`.
Reuse skin **`clean-product-light`** (do not create new skin).
Audit: 2026-10-18; source web inspection used **Jarvis MCP attached to actual user-machine Chrome browser** for homepage, mobile and representative route-family pages; separate Chromium used for exhaustive dual-viewport rendering. No real submissions made.

## Census and proof boundaries

**48 sitemap paths; 47 HTTP200 and one intentionally returning HTTP404 (`/404`)**, plus 11 non-sitemap negative paths all HTTP404. Families: Home (1), three full-page alternate heroes, Integrations archive and **15 details**, Blog archive and **10 details**, Careers archive and **6 details**, About (1), Pricing (1), Contact (1), Book a Demo (1), Download (1), Changelog (1), Waitlist (1), Legal terms/privacy (2), explicit /404 (1).

**966 internal link pairs** and **59 HTTP census entries**. Rendered **98 Chromium 1440x900/390x844 states** (48 site + one negative path × 2) with zero positive outer overflow and zero runtime errors; **20 bounded interaction probes**; **9 WebP screenshots**. Evidence `data/superior-{route-inventory,internal-links,rendered-states,interaction-probes}-2026-10-18.csv`. Browser-MCP observations are distinguished from software isolated browser renders.

## Main visual recipe

Pure **#FFFFFF body canvas**, near-black Inter display, gentle neutral light surfaces, understated green NEW announcement tag, restrained borders and rounded CTA pills. Homepage H1 64px desktop (1440) →36px mobile (390), centered thesis **"The most powerful business platform."**, CTA Get Started / Learn More and giant app dashboard proof mockup immediately below fold. Site home ~17,063px desktop, ~20,275px mobile, **45 img/0 video/1 canvas desktop; 39 img/0 video/1 canvas phone**. DOM nodes are not downloaded bytes or 3D performance evidence. Prefer real supplied app screenshots over fabricated, generated metrics.

## Complete page-family component sequence

- **Home /**: tiny topbar Pages, About, Pricing, Integrations, Blog, Book a Demo → NEW Announcing API 2.0 → large centered platform manifesto → Get Started/Learn More → application dashboard with revenue/projects → trust logos → teamwork → planner → analytics → features → scenarios → deeper product detail → integration partners → customer testimonials → latest blog → FAQ and full trial CTA.
- **Three /heroes/hero-v2/v3/v4**: actual full landing variants sharing design tokens and some content yet materially different section sequences. Template could expose pages as demos or conditionally deploy one primary home. v3 contains duplicate desktop H1; never ship multiple accessible top-level headings because of breakpoint copies.
- **/integrations**: categorized 15-tile app/provider directory (Popular, Collaboration, Automations, Engineering) → all **15/15** detail links → typed icon/name/synopsis. Search Icon was clickable; no verified result subset or input appeared in bounded test. Avoid asserting search works.
- **15 /integrations/<slug>**: provider icon/title/category/explanation/CTA and crosslink, e.g. Orbit collaboration task linking. Many source detail routes **lack semantic H1** despite visually present headings. This is a marketing integration catalog, not proof any external API is connected.
- **/blog**: newsletter signup, search icon, visual editorial CMS. **7/10** sitemap article URLs exposed in initial archive state. Content should be fully discoverable via explicit pagination/search/related; don't claim index directly links ten. Article detail: strong H1, cover/byline/category/date, story body, social share affordances, related follow-up and trial footer.
- **/careers**: Build your future with us -> Why join us -> Open roles -> six CMS role detail hrefs (6/6). Career detail: job/office/experience, skills, responsibilities, `Apply now → /contact`. Role listings and business hiring data are demo until current owner confirms.
- **/pricing**: product offer tiers, "Choose a plan that's right for you", Compare plans feature matrix, testimonials, expert contact CTA and trial. The source rendered no native button/switch among sampled pricing elements, so no verified billing interval or payment backend.
- **/contact**: "Contact our sales team" -> offices -> input Name optional, Email required, Company optional, Message optional + honeypots -> Submit. Native form blank invalid, actual delivery not tested.
- **/book-a-demo**: name/email required, company, role dropdown (Designer/Engineer/Marketer/Investor), team size dropdown (1–10/10–25/25–50/50+), location/country, Book a demo. Native blank invalid; calendar/provider unavailable as proof.
- **/waitlist**: minimal full-height email field and Join waitlist; email **required=false** and blank native validity **true**. Must repair before real leads.
- **/download**: Download our apps CTAs/product distribution context; actual installers not verified.
- **/changelog**: dated release notes and update subscription (example v1.0.2 Jan 16, 2025), no proof latest release.
- **/about**: company/team/values/credibility story and contact/trial end stage.
- **/legal/terms-of-service**, **/legal/privacy-policy**: template legal policy and general title metadata; legal owner review needed.
- **/404**: expected 404 status in sitemap, not a working product page.

## Transferrable implementation rules

1. Build homepage app-mockup section anchored to legible display hierarchy; no decorative gradient as replacement for actual product proof.
2. Preserve **48-route** sitemap depth; three hero variants are full pages, not a single variant toggle.
3. Keep Integration catalog links all fifteen details and test taxonomy/search behavior independently.
4. Ensure Blog ten article permalinks all have a path from editorial index, even if seven initially displayed.
5. Keep six job details independently reachable and link Apply to real application destination, not blindly /contact.
6. Separate Contact, Demo Qualification and Waitlist flows with distinct required fields and real consent/server feedback.
7. Verify all template/customer claims, apps/download buttons, release notes, privacy and job vacancies before production.
8. Correct 0 H1 on integration details/waitlist and v3 duplicated desktop H1; preserve responsive 64px→36px hero scale.
9. **User's operational rule**: for future distillations connect **Jarvis MCP to the user's Chrome** as the first browser-inspection pathway (unless unavailable/unauthorized, in which case clearly state so); supplement it with exhaustive isolated Chromium/Playwright where beneficial. Separate Chrome-direct results from headless test ledger and preserve independent evidence. Browser extension session/tab cleanup required.
10. Site source is a commercial Framer template; creator "Get template" and example customer/product charts are vendor/demo context, not direct customer account data.

**Production QA**: all sitemap route-family jobs, desktop/mobile full-site screenshot states, correct headings and full internal graph, user-machine Chrome inspection, form validation, no fake subscription/hiring/delivery assertions.
