# MEXC — Exchange, Market Discovery, Yield & Content UI Spec

Audit: 2026-10-20, via Jarvis MCP connected to user's Cốc Cốc (exposed as Chrome). Source https://www.mexc.com/. Full provenance and limitations: `../../../design-intelligence/sites/mexc.com.md`.

## Source census — exact scope

34 primary sitemap groups; 33 primary index responses HTTP200, one MX activity index HTTP404. 53 first-level language-neutral URL sets enumerated 77,737 *declared* URLs / 10,547 mechanical prefixes. Two nested indexes expand to 1,475 named child XMLs, with only 12 representative child XMLs fetched (1,785 URL declarations sampled, possible overlap). No assertion of all paths, all locales, all nested shards or all interactions validated. The UI spec transfers mechanisms, not MEXC brand.

## Art direction

High-density exchange dashboard with very dark operational surfaces, bright blue primary actions, restrained grey secondary labels, tabular prices, economical dividers, information-heavy left-to-right workflow; for landing/editorial use larger 56px desktop and ~32px mobile headline modules on the same brand framework. Observed MEXCSans, near-black body `#000000`, foreground `#F2F4F6`, sampled CTA `#1463FF`; choose a legitimately licensed brand palette and font rather than cloning.

## Canonical navigation/route shells

| Shell | Representative observed paths | Primary navigation |
| --- | --- | --- |
| Marketing/home | `/`, `/about`, `/fee` | Product mega-menu -> primary value proposition -> rankings/content -> deposits/fees/support |
| Market scanner | `/markets/crypto/futures/usdt-m`, `/price/BTC` | Explore/rank/filter -> instrument detail -> trade handoff |
| Spot terminal | `/exchange/BTC_USDT` | Symbol -> quote, chart, order book -> explicit buy/sell ticket |
| Futures terminal | `/futures/BTC_USDT` | Contract, leverage/risk -> chart/depth -> trade intent and review |
| Follow/automation | `/futures/copyTrade/home`, `/mexc-ai` | Trader listings and signals -> inspect risk -> guarded action; AI screen is marketing/curation |
| CEX purchase | `/buy-crypto`, `/convert` | From/To or fiat asset -> quote/fees/rate expiry -> explicit user confirmation |
| Yield | `/staking` → `/earn`, `/launchpad`, `/token-airdrop` | Eligible asset/status -> APR/rewards and conditions -> enrollment with disclosure |
| DEX/onchain | `/dex` -> token-specific Solana trading terminal | Chain+contract identification -> quote/slippage/gas -> wallet signature boundary |
| Early assets | `/pre-market`, `/memecoin`, `/stocks` | Category/ranking + asset type and eligibility -> detail |
| Insights/prediction | `/market-insights`, `/crypto-pulse`, `/price-prediction/BTC` | News/forecast -> explicit provenance, assumptions and date -> asset detail |
| Learn/help | `/learn`, `/support`, `/announcements/all` | Separate pedagogy vs help vs official notices; scoped search |
| Trust/developers | `/official-verify`, `/mexc-api`, `/about`, `/fee` | Anti-fraud verification, API/docs links, legal and pricing surfaces |

## Reusable component system

- Exchange mega navigation and account-state-aware header, without emitting data about signed-in user.
- Symbol/ticker selector with instrument domain and quote units, multiple market sort/filter states, chart pane with timeframe and stale signal, orderbook bids/asks and spread.
- Trade ticket with order side/market-or-limit/quantity/total/fee/error/review state, never automatic execution on tab changes.
- Futures contract header with leverage, mark price and risk indicator, per-product local state rather than a reused Spot wallet assumption.
- Fiat buy/convert quote widget with timed rates, confirm/cancel flow.
- Earn catalog, risk/term cards, eligibility badges; launchpad/airdrop countdown status, ended labels.
- DEX chain-and-contract selector, gas/slippage/approval review and signature boundary; CEX balance must not be implied.
- Editorial card + article detail and public notices, categorized Help Search, Official Verify checker.
- Reusable failure/loading/stale/retired/region-restricted/unauthenticated states.

## Interaction QA and responsive contract

For representative source pages a true 390×844 Cốc Cốc window reported JS `innerWidth=390`, `documentElement.clientWidth=390` and `scrollWidth=390`: home, Markets, BTC price, Learn, Support and Earn. **Zero positive outer document overflow in those six only.** Do not assume the hidden DOM's internal tables, mobile trade ticket or carousels are QA-verified. Desktop Learn H1 56px/700, mobile 32px; mobile BTC price title 24px. Reorder high-priority task cards and use single-active-pane navigation in terminal. Focus/keyboard, contrast, screen-reader market delta, reduced motion, hover and confirmation require tests in the new implementation.

All rates, availability, APRs, predictions, rewards and claimed AI results must be clearly labelled/dated if shown. Never place orders, trade, create API credentials, process payment or connect a wallet as part of a screenshot-based site audit.
