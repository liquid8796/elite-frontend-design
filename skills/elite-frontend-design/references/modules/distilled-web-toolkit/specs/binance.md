# Binance — Multi-Shell Financial Exchange Design Specification

Reference https://www.binance.com/en · Audit 2026-10-20 · Full evidence: `../../../design-intelligence/sites/binance.com.md`.
Archetype: `crypto-financial-exchange`; use existing `premium-saas-dark` skin only as a structural starting point. It is **not a copied Binance skin**.

## Census and limitations

15 official `robots.txt` index URLs (852 all-locale child sitemap references). 20 English child XML files yielded **50,624 sitemap-declared URL rows** and 2,708 mechanically computed route prefix groups. The archive `data/binance-english-sitemap-inventory-2026-10-20.csv.gz` is complete for those English shard declarations, **not** a claim all links return 200 or that every localized/private/subdomain route is audited. 220 rows triggered a coarse malformed-URL heuristic. Public browser directly inspected more than twenty concrete route instances across market/trade/earn/loan/futures/conversion/price/academy/support/blog/square/legal/about/AI/retired/redirect surfaces; approximately six routes were also visited at 390px in a Chrome-labelled Jarvis MCP Cốc Cốc session. Browser authentication was present; no private account data is retained.

## Design tokens grounded in observed public UI

- Dark `#181A20` body for most product shells; `#0B0E11` spot terminal; `rgb(234,236,239)` foreground; text/data-muted and secondary background have separately controlled roles.
- Yellow `#FCD535` sampled CTA fill and `#202630` sampled CTA foreground. Treat exact palettes as non-transferable brand material.
- `BinanceNova` family observed, but must substitute the new product's licensed type. Desktop About H1 48px/600, body 16px/400, yellow CTA 14–16px/500. Mobile brand hero ~32px/40; Earn 28px, Blog 24px, Academy 28px; price detail H1 14px utility. Scales differ by shell and job.
- Density dial 9/10 in trading/data, 5–6/10 in marketing/editorial. Motion limited to data/feedback, not ornament.

## Route/system contracts

| Shell | Route examples | Component/interaction contract |
| --- | --- | --- |
| Global marketing | `/en`, `/en/about` | global navigation → market/trust/app education → safe product CTAs; signed-in/out hero differs |
| Market discovery | `/en/markets/overview`, `/en/markets/trading_data` | search/categorize/rank → selected asset → detail and trade; retain units and time |
| Asset detail | `/en/price/bitcoin` | quote summary → timeframe chart → analysis/news/FAQ → optional buy |
| Spot terminal | `/en/trade/BTC_USDT` | instrument → chart + order book → explicit buy/sell ticket → review, NEVER implicit execution |
| Derivatives | `/en/futures/home` | futures nav, contract cards and risk-hand-off |
| Purchase/convert | `/en/crypto/convert`, `/en/how-to-buy/bitcoin` | fiat/crypto From/To → rates/fees → deliberate confirmation |
| Yield and loan | `/en/earn`, `/en/loan`, `/en/launchpool` | product search → risk-qualified offers → eligibility/terms → explicit action |
| Auto-Invest | `/en/auto-invest` | redirect to recurring `/en/convert/USDT/BNB?activeTab=recurring`; preserve chosen state |
| Education | `/en/academy`, `/en/academy/articles/what-is-bitcoin` | article topic/level/update time/TOC/heading/order |
| Editorial/community | `/en/blog`, `/en/square`, `/en/square/news/all` | distinct editorial archive vs social stream; explicit author/time |
| Help/governance | `/en/support/faq`, `/en/support/announcement`, `/en/about-legal/home` | topical search and official notices, separate from social |
| Retired/error | `/en/nft/closed`, `/en/institutional` | NFT retirement notice/support; institutional unavailable in sample; no fictitious active UI |

## Component grammar and responsive ownership

Provide four navigation families (exchange marketing; market terminal/derivatives; Academy education; Square community). Keep search and market filters independent of account-sensitive trade state. Use typed components for asset/quote, numerical table, rich chart, order ticket, conversion quote, APR product, article/FAQ, social feed, legal category and closure notice. Use prefixed symbols, consistent currency, accessible chart alt/summary and tabular numerals. Loading/errors/stale quotes/cancel/review must be explicit.

At mobile real browser 390x844, homepage quick-actions replaced desktop marketing chrome under signed-in state. Observed no positive **outer document** horizontal overflow on home, markets, price, earn, blog, academy. Preserve one task per viewport: stack market overview, tabs/drawer for chart vs depth vs buy/sell, explicit close and keyboard focus. No GPU benchmark or successful money movement was observed.

## Acceptance checks for reuse

- No fake live data; timestamps/data source/stale states, numerical signs and units always shown.
- Price movement not color-only; action focus visible; high-density text legible.
- Disclosure and confirmation required for transaction/lending/derivatives; never imitate Binance APIs without authorization.
- Each indexed URL declaration goes through separate canonical/status/live DOM validation before treated as usable UI.
- Retired feature stays retired, and error states have navigation/support exits.
- Production source must use the new product's own brand/trademarks/fonts, never Binance account details, market balance or original copyrighted artwork.
