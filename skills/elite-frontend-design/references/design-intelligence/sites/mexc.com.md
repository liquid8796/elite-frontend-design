# MEXC — Full-System Public Website Distillation (2026-10-20)

Source: https://www.mexc.com/ • User machine **Cốc Cốc** connected via **Jarvis Agent Browser extension**, recognized as **Chrome** in Jarvis MCP. Audit focused on public navigation and safe UI states; the browser was already signed in, so NO account identifiers, assets, order history, wallet balances, tokens, authentication or transactions were collected or exercised.

## Evidence tiers and exact coverage

**Index census:** `robots.txt` points to a valid HTTP200 `/sitemap.xml`, which lists **34 top-level sitemap indexes**. **33** return XML sitemap indexes, while `/mx-activity/sitemap-index.xml` returned **404**. Indexes include exchange; price, prediction, tokenomics, info, analysis; price converter; how-to-buy; market insights; memecoin; markets; pre-market; crypto pulse/glossary; stocks and stocks/how-to-buy; tools; compare; links; futures; futures activity; buy-crypto; DEX; support; learn; generic sitemap; official verify; API docs; launchpad; token airdrop; MX; SUN assessment; launchpool.

**Declared URLs:** The 33 accessible indexes link to multi-language child sitemaps. We fetched **53 first-level language-neutral URL sets**, yielding **77,737 URL declaration rows and 10,547 mechanically grouped prefixes**. The initial traversal selected 55 first-level no-locale children; 2 of these are themselves nested indexes (`/price-converter/sitemap.xml` and `/tools/sitemap.xml`). The nested indexes enumerate **1,475 additional child XML locations** (1,474 converter instrument files and one crypto tax calculator sitemap). Of these, a bounded **12 nested files** were actually fetched as examples with **1,785 further declarations** (possible overlap; no deduplicated site-wide page count is claimed). **Do not claim all 1,475 nested XML files were downloaded.** The complete nested *index manifest* is preserved; detailed content of the un-fetched converter shards and every language-specific site version remains outside the completed census. The original 77,737 declarations are not 77,737 pages opened, HTTP-tested or user journeys validated.

**Files:** `data/mexc-sitemap-index-2026-10-20.csv`, `mexc-default-sitemap-shards-2026-10-20.csv`, `mexc-default-sitemap-declarations-2026-10-20.csv.gz`, `mexc-route-families-2026-10-20.csv`, `mexc-sitemap-errors-2026-10-20.csv`, `mexc-nested-sitemap-manifest-2026-10-20.csv`, `mexc-nested-sitemap-sample-2026-10-20.csv`, `mexc-nested-declaration-sample-2026-10-20.csv.gz`. Reproducible bounded collector: `scripts/audit_mexc_sitemaps.py`. A URL declaration is a route hypothesis, not an authenticated function claim.

## Connected browser: directly verified desktop surface families

At ~1875–1910px desktop viewport on user's Cốc Cốc, Jarvis MCP navigated the original domain and inspected document title/heading, links, input controls, CSS and redirects:

| Page family | Observed real route(s) | Observed UI / information architecture |
| --- | --- | --- |
| Global home | `/` | Buy Crypto, Markets, Spot, Futures, Earn, Event Center, Rewards Hub, More; hero "Your 0-Fee Gateway to Infinite Opportunities"; large announcements ticker, rankings, promo rails, official trust links; signed-in Deposit/Wallets/Orders are present but their content was NOT accessed |
| Market overview | `/markets/crypto/futures/usdt-m` | Markets H1; Hot Tokens/Futures/Newest, Favorites, Crypto, Stocks and TradFi tabs; asset list and category changes |
| Spot terminal | `/exchange/BTC_USDT` | Pair ticker, chart, bid/ask depth, price/amount/total fields, order ticket surfaces, fee/market context; no trade execution |
| Futures terminal | `/futures/BTC_USDT` | Contract/mark price headline, perpetual contract/leverage display, more intense dense order controls; no leverage/order adjustments, no trades |
| Copy trading | `/futures/copyTrade/home` | Trader Match, AI Traders, Top/All Traders, feed, competitions and trader search; performance claims and automation not verified |
| Buy / payments | `/buy-crypto` | Fiat purchase range/input, selection, onboarding tutorial and asset pages; payment not attempted |
| Convert | `/convert` | From/To inputs, conversion figures and FAQ; no quote acceptance/order placed |
| Earn | `/staking` → **`/earn`** | Product catalog, search token, match-my-assets, onboarding, FAQs and earn tutorials; APRs are transient marketing claims, not guaranteed yields |
| MEXC AI | `/mexc-ai` | "Intelligence for Every Opportunity" landing with Discover / Understand / Trade and CTA; tool/model capability not verified |
| DEX | `/dex` → `/dex/onchain/sol/CARDSccUMFKoPRZxt5vt3ksUbxEFEcnZ3H2pd3dKxYjp` | A selected Solana token onchain trade terminal, contract-address input, asset/order history tabs; no wallet signing/swapping |
| Launchpad | `/launchpad` | Ongoing/ended listing, fundraising metrics and FAQ; no subscription attempted |
| Token airdrop | `/token-airdrop` | Ongoing/ended campaign cards, reward amount and countdown; reward figures not preserved as timeless truth |
| MX | `/mx` | Token holder benefits, fee discount, reward and insights marketing |
| Rewards/event | `/rewards-hub`, `/event-center/futures` | Reward-center eligibility/terms and multi-campaign cards; no reward claims |
| Asset price | `/price/BTC` | Coin price/history/timeframe/market stats, additional analysis and conversion inputs |
| Forecast | `/price-prediction/BTC` | Predictive 2026–2050 projections, short-term vs long-term forecast and percentage input; **not evidence of prediction accuracy** |
| How to buy | `/how-to-buy/bitcoin` → `/how-to-buy/BITCOIN` | SEO/canonical case redirect; sampled destination initially lacked substantive heading and switched to white body, likely hydration/region/fallback; do not infer complete content |
| Market intelligence | `/market-insights` | News-driven sentiment, thematic updates, trending macro/headline cards |
| Pre-market | `/pre-market` | Available vs past token tabs, search, workflow explanation and FAQ; actual settlement not verified |
| Crypto Pulse | `/crypto-pulse` | Long-form topical news/content feed with editorial headlines |
| Memecoin | `/memecoin` | Memecoin listings and DEX-like token/contract search; no onchain action |
| Stocks | `/stocks` | US equities-themed overview, market summary, top stocks, further discovery; region eligibility not verified |
| Learn | `/learn` | Distinct editorial shell: search, beginner guides, featured articles, hot topics, curated content |
| Support | `/support` | Help center, self services, FAQ, support search; do not send private account information |
| Announcements | `/announcements`, `/en-US/announcements/all` → `/announcements/all` | Verified official operational notifications / listing / delisting / fees; separate from news/social chatter |
| API developer | `/mexc-api` | API developer landing; no API secrets read or generated |
| Official verification | `/official-verify` | Full-query official-channel verification form; no input of personal identifiers |
| About | `/about` | Brand mission/leadership/trust and corporate design |
| Fees | `/fee` | Pair search, fees breakdown, trading fee overview; snapshots must be revalidated |

Other sitemap groups (tokenomics, analysis/info, stock purchase guides, converter per asset, nested tools, glossary, compare, affiliate links, generic sitemap, SUN, regional market variants) were **catalogued structurally** but not separately opened for each dynamic record. Global nav exposed additional partner/app/ventures/security/legal workflows; no private route visited.

## Style primitives and hierarchy (real CSS inspection)

- Homepage/Learn/common shell sampled body `rgb(0,0,0)`, primary foreground `rgb(242,244,246)=#F2F4F6`.
- Strong primary action blue `rgb(20,99,255)=#1463FF` with white text. Subdued functional text around `rgb(135,144,159)`.
- Global type family `MEXCSans` with system sans fallback, body around 14px and white/light typography; dark chart-first trading interface, unlike Binance's yellow. These visual tokens are **observed brand materials and should not be copied by default**. About, markets and crypto buy funnels use different arrangements/densities.
- Sampled Learn H1 on desktop **56px, weight 700**; mobile **32px**. Mobile Support/Earn H1 also **32px**; BTC price page H1 **24px**. Route-specific typography scales, not one site-wide H1 rule.
- Operational surfaces (Spot, Futures) have high information density, tightly grouped quote/volume/time controls, compact tabs and numeric chart; marketing/editorial surfaces use larger copy and category panels.
- No direct animation timing/FPS benchmark. Any suggested market-ticker, chart refresh or countdown motion recipes are **derived implementation guidance**, not measured source animation coefficients.

## Genuine 390×844 Cốc Cốc/mobile observations

MCP window was set to 390×844 and **confirmed JS innerWidth=390/clientWidth=390** on `/`, `/markets/crypto/futures/usdt-m`, `/price/BTC`, `/learn`, `/support`, `/earn`. In these six sampled routes, document scrollWidth = 390 and **no positive outer-document horizontal overflow** was measured. This does not certify all internal carousels or tables; no physical mobile device/FPS study was performed. Public Learn desktop and phone-size cropped screenshots are retained. Nav and content stack adapt by route; mobile should prioritize selected symbol, account-safe actions and compact browse/filter before secondary widgets.

## Transfer-ready implementation mechanisms

1. Independent shells: conversion-facing homepage, market explorer, spot/futures/DEX terminals, Earn, content/help and event/campaign collection must have distinct navigation density and state ownership.
2. Unified symbol search with separate instruments (CEX spot pair, perpetual derivative, token contract, equities concept). Same characters **must not automatically mean same product**.
3. Numeric console: price, amount, total, bid/ask, chart timeframe, depth, spread and precision; never imply a preview is an executed order. Clear explicit confirmation and risk.
4. Quote and card conversion workflows separate from advanced trading; fee preview and rates expiry, failure, stale data and locale.
5. Yield/rewards/Launchpad campaigns are date- and eligibility-sensitive; keep status labels, dates, risk disclosure, paused and ended states.
6. User-directed content channels: Learn vs market-insights vs crypto pulse vs official announcements vs support with authorship, timestamps and topical search.
7. DEX security boundary: onchain token address, chain and slippage/gas/signature affordances are not CEX balances; do not depict fake successful blockchain settlement.
8. Stable mobile tasks and reduced motion: markets/spot/futures cannot be reduced to tiny desktop columns; scope and aria-label icon-only controls.
9. SEO taxonomy accuracy: 34 families and thousands of symbol variants, including 1,475 deeper child-sitemap references, are **not 34 unique apps** and not a substitute for state-level tests.
10. Trust and anti-scam affordances: official-verify, support, API documentation and fee/legal pages are first-class user trust destinations.

## Exclusion / integrity

No orders, payment, deposits, withdrawals, trading bots, copy-trade activation, wallet connection, account, security, KYC, or personal data were tested or saved. Finance data/rates/campaign numbers are transient and **not** facts to hardcode. Original logos, proprietary MEXCSans, marketing text and third-party artworks should not be reproduced as a default style. Full every-page interaction QA, all nested converter sitemap leaves and non-default locales remain outside verified scope.
