# Battlez — Toolkit Spec

Source: https://battlez-template.framer.website/
Deep profile: `../../../design-intelligence/sites/battlez-template.framer.website.md`
Archetype: gaming-commerce
Skin: `cinematic-game` for dark genre marketing, `premium-ecommerce` as secondary conversion grammar. Do not establish a new skin without cross-site evidence.

## Complete topology and confidence (2026-10-08)

One sitemap contains **75 URLs**: home 1, core+404 6, store 1, store details 53, game categories 4, news 1, news details 6, news categories 3. All 75 HTTP-checked: 74 returned 200; /404 intentionally returned 404. Route inventory: `data/battlez-route-inventory-2026-10-08.csv`.

Chrome desktop/mobile audited representative routes from every family; 390x844 representatives had zero document-level overflow. Not 75 unique interaction tests.

## Visual/interaction recipe

Body #060914 navy-black; headline #9DC0E3, body text #D3E1EF. Heading is rendered Inter (other loaded fonts: Bricolage Grotesque, DM Sans). Marketing H1 ~90–100px desktop -> ~43px mobile. Detail H1 ~60px -> 45px. Rounded gradient cart/button surfaces, editorial spacing and large still art. Home 2 videos, zero canvas; avoid invented WebGL.

**Navigation:** unified sticky brand header -> About / Pricing / Store / News -> contact. Mobile nav collapses. Footer repeats meaningful route families.

**Homepage:** game identity -> brand thesis -> selected game cards/categories -> marketplace CTA.

**Store:** curated cards with game name/price, category route and Add To Cart.
**Game category:** category identity -> scoped cards -> cart/detail.
**Product detail:** product media -> title/price -> quantity/cart -> long description/lore -> category links -> related products.
**Pricing:** memberships separate from one-off cart sales.
**About/Team:** brand/community story + news/FAQ continuity.
**News:** archive -> category -> H1/image/body with proper section headings -> related stories.
**FAQ/Contact:** focused objection resolution and support message form.
**404:** valid 404 response and recovery navigation.

## Promoted patterns

`battlez-discovery-marketplace`; `battlez-dual-funnel`; `battlez-commerce-category-archive`; `battlez-game-detail-lore`; `battlez-genre-editorial`; `battlez-cms-fixture-quarantine`; `battlez-genre-commerce-shell`.

## Failure modes / QA

**75/75 distinct URLs currently share one document title**: `Battlez - Gaming Framer Template`. Must make title route-specific before launch. Canonicals are route-specific. 53 store-detail records contain non-game toys, cosmetics, furniture, sports goods and drones: do not mix generic demo fixture CMS with gaming inventory. The visible game store only surfaces a curated subset of records.

Product Add To Cart surfaced as an anchor without href (tabindex=0), with generic a11y role in Chrome tree. Replace with semantic button and verify keyboard/cart/checkout states; do not claim real payment succeeded. Contact name field labels need distinct first/last name semantics.

Framer preview badge, Frameship “BUY LICENCE”, placeholder social links, vendor credits and unrelated sample goods are non-transferable template residue.

## Responsive / media

General H1 90–100px -> ~43px; detail 60px -> 45px; body stacks vertically and 390px had zero outer overflow. Two homepage video assets are muted/looping. Use video only as bounded identity punctuation, with still/poster and reduced-motion fallback. No novel motion library or WebGL mechanism confirmed.
