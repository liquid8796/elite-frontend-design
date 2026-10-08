# Battlez — Whole-Site Design Intelligence

Source: https://battlez-template.framer.website/
Audited: 2026-10-08 through Chrome on the user's machine plus full sitemap HTTP census.
Confidence: 75/75 publicly sitemap-declared URLs requested. 74 returned HTTP 200; the intended /404 returned 404. Rendered desktop + 390x844 mobile for every major route family, multiple representative product types and news/category/detail variants; NOT a claim of 75 unique deep interaction tests.

## Full site topology

| Route family | URL count | Purpose |
| --- | ---: | --- |
| Home | 1 | game identity, product discovery and commercial path |
| Core + 404 | 6 | about-us, team, pricing, faq, contact-us, 404 |
| Store index | 1 | curated featured game shelf |
| Store detail | 53 | commerce product records, including unrelated demo fixtures |
| Game-category | 4 | racing, software, sale, new |
| News index | 1 | editorial archive |
| News detail | 6 | gaming editorial articles |
| News-category | 3 | guide, suggested, news |
| TOTAL | 75 | 74 HTTP 200 + /404 HTTP 404 |

Machine-readable census: ../modules/distilled-web-toolkit/data/battlez-route-inventory-2026-10-08.csv

The /404 URL returning 404 is deliberate error-route behavior, not a missing main route. Unlike Resend's /shop stale sitemap issue, this is not by itself a broken product page.

## Design DNA, facts separated from transfer rules

**Archetype:** dark game-commerce hybrid; existing `cinematic-game` skin is the brand/mood anchor, and `premium-ecommerce` contributes commerce ergonomics. It is NOT a studio/agency services website or single-title cinematic launch.

**Computed colors:** body #060914 (rgb 6,9,20); headings/light controls steel blue #9DC0E3 (rgb 157,192,227); body/secondary #D3E1EF (rgb 211,225,239); sample action gradients from #343D4D to #1D2330 with edge #4D5968. Rounded CTA radius 10px on sampled Add To Cart. Distill the restrained navy/light-blue hierarchy and controlled card accent, not exact pixels.

**Type:** visible rendered headings use Inter. Bricolage Grotesque Variable and DM Sans also load, but loaded does not imply applied. Home H1 ~90px desktop, 43px mobile; core route H1 ~100px desktop -> ~43px mobile; product/news detail H1 60px -> 45px; core H2 50px -> ~35px.

**Media/runtime:** at 1440 desktop, home ~1425x8321, 32 images, two videos, zero canvas. One video auto-plays silently in loop; supporting video is muted and looping. No observed WebGL/Three renderer. Framer runtime and Frameship cart/license integrations are present. Settled `document.getAnimations()` was zero in one moment (lifecycle-dependent; do not interpret as no motion).

**Shared shell:** sticky/floating navigation with About, Pricing, Store, News, contact CTA; shared footer includes Team. Brand mood continues through marketing, commerce and editorial, with related-item content holding buyer context.

## Homepage — campaign to marketplace bridge

Rendered ~1905x8310 at 1920-wide and ~1425x8321 at 1440-wide. Mobile 390x9441, zero page horizontal overflow.

Story order:
1. game-first identity and “View Marketplace” destination;
2. “why us” and About story;
3. premium offerings and Start Your Game continuation;
4. featured purchasable gaming cards with category, price, add-to-cart;
5. discover further games, final brand footer.

Transfer **Game Discovery -> Marketplace Bridge**: marketing world and real catalog directly connect. Do not replace product names/actions with generic trailers.

## Core family

About Us (~1905x6492 desktop, 390x9158 mobile): passionate gaming origin -> community ideals -> reason to choose -> latest gaming news.

Team (~1905x4640 / 390x7049): “Gaming community!” -> imagery/team/community -> FAQ continuation, with one video observed desktop.

Pricing (~1905x2988 / 390x4086): independent monthly membership funnel with 3 tiers (observed headings $9, $59, $19 — template fixtures, not verified commercial offerings). Keep subscription/membership promise separate from individual product/cart checkout. This is **Subscription + Product Dual Funnel**.

FAQ (~1905x1355 / 390x1898): compact dedicated FAQ route, not repetitive full-size landing.

Contact (~1905x2707 / 390x4169): direct form with first/last name, email, phone, message, then benefit narrative. Both first and last name input nodes reuse name `Name` in sampled DOM; clarify labels for assistive technology.

404: publicly declared recovery route responds HTTP 404.

## Store/catalog family — 53 detail routes, not six cards only

Store index ~1905x3293 / 390x4924, presenting approximately six gaming cards in sampled rendered index. Four distinct category destinations (/game-category/sale, software, racing, new) exist.

Representative category /game-category/racing (~1905x1431 / 390x2173) and software (~1905x1898) show category title + subset of game cards with price and Add To Cart, not only a filter toggle.

All 53 /store/* URLs use a common detail grammar:
`image -> title -> price -> quantity -> Add To Cart -> category links -> long description -> related games -> marketplace continuation`.

Live examples:
- Mystic Mayhem Game: ~1905x2482 desktop, ~390x3629 mobile, quantity default 1, displayed $39.99, Racing/New category, lore content and related games.
- Gift Card: uses the same commerce shell.
- Dinosaur Raincoat: ~390x2793; obviously unrelated toy/apparel fixture within “game library”.
- Zenith Air: ~390x4456; drone with longer prose, still same shell.
- Leather Basketball: ~390x2898; sports fixture, same “Related games” label.

This supports **CMS Commerce Shell Reuse** and **Product Purchase + Lore**, but also reveals a serious **Cross-Vertical CMS Fixture Leak**: toy, cosmetics, nail care, home goods, drones and sports inventory is being published under a gaming promise. Do NOT promote the data as gaming taxonomy. Variation in detail length comes from available product copy; avoid padding unrelated records to match a cinematic game landing.

**Cart semantics:** a sampled product Add To Cart is an `a` without `href`, with `tabindex=0`; in the Chrome accessibility tree cart actions are sometimes generic rather than buttons. Frameship cart localStorage key `frameship_cart_id` exists. The Quantity input has accessible label `Quantity`. Keyboard activation, cart drawer and checkout outcome were not verified; treat this as a QA gate, not a recommended control implementation.

## News/editorial family

News index (~1905x2668 / 390x4809): six story cards, category label, Learn More, long-form destination.

News detail sample /news/behind-the-scenes-how-a-hit-game-is-created (~1905x4622 / 390x6625): story H1 60px desktop / 45px mobile -> image, sectioned article (H2 50px, H3 36px), details anchor, more gaming news continuation.

News categories Guide/Suggested/News are separate shareable archive routes. Sample /news-category/guide ~1905x1446 / 390x1825.

Transfer **Genre Editorial -> Discovery Loop** (news as community/interest proof), but don't invent actual title/product links without evidence.

## Responsive and motion contracts

Observed 390x844 states had zero document-level horizontal overflow across homepage, about, team, pricing, FAQ, contact, store, several product types, category, news index/detail and category. Major displays shrink ~90–100px to 43px; detail headings 60px to 45px; normal stacked long-form scroll replaces wide compositions. Product quantity and related purchase controls remain in normal flow. Collapsed mobile nav observed.

Video supports atmosphere, not an unverified WebGL world. Preserve meaningful still/poster fallback and reduced-motion user preference; defer out-of-view playback.

## Site quality and do-not-transfer

**All 75 sitemap pages have the same server HTML title:** `Battlez - Gaming Framer Template`, even though canonical URLs point to their respective routes. Production SEO requires unique product/article/category page titles. Server HTML contains repeated H1 markup for hidden Framer variants; rendered representative routes displayed one visible H1 — do not conflate static duplicates with visible multiple headings. Check accessibility tree route-by-route.

Preview-specific Framer “Create a free website” badge, Frameship “BUY LICENCE” link, designer attribution, placeholder social links and brand media are template chrome, not commercial product design.

**Transferable recipe set**
- Game Discovery -> Marketplace Bridge
- Subscription + Product Dual Funnel
- Category-as-Commerce Landing
- Game Purchase + Lore Product Detail
- Genre Editorial -> Related Content
- CMS Boundary Enforcement / Cross-Vertical Fixture Quarantine
- Unified Genre Commerce Shell

Adopt route jobs and mechanics; avoid proprietary artwork, names, exact fonts/colors, sample goods, licenses, cart scripts or incomplete semantics.
