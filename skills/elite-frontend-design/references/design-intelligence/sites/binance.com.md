# Binance — Multi-System Exchange, Research, Market, Trading and Editorial Distillation

Source: https://www.binance.com/en · Audited: **2026-10-20**.
Method: **Jarvis MCP browser extension attached to the user's Chromium-compatible Windows browser**; instance is advertised to MCP as `Chrome` (user identifies it as Cốc Cốc). All listed representative pages were **actually opened in the connected browser**. Do not misattribute these inspections to isolated Playwright. Market data, active-product availability and geographic restrictions are time-specific. **The browser had an authenticated state**, so account balances, identifiers, settings, order history, trade execution, KYC, security or payments were deliberately not collected or tested.

## Scope: comprehensive route taxonomy, not millions of visited pages

The root `/sitemap.xml` returned **HTTP403 AccessDenied**, but the public `/robots.txt` enumerated **15 independent sitemap index families**: Trade, Blog, Nft, SupportAndAnnouncement, Futures, Earn, Loan, Market, Default, Fiat, Crypto, Square, Academy_New, Muses and Growth. All **15 HTTP200** indexes were parsed and comprise **852 locale-shard references**. Only the **20 en-specific shards** were recursively fetched, declaring **50,624 URL rows**, across **2,708 mechanically grouped path prefixes**. The entire English declaration inventory is compressed in `data/binance-english-sitemap-inventory-2026-10-20.csv.gz` (not 50,624 HTTP validations); 15-index census, 20-shard counts and grouped routes are in adjacent CSVs. **220 URL rows** triggered a deliberately coarse suspicious-path heuristic; examples included double-escaped fragments, .php/.sqlite and contrived parameter payloads. These may be crawler-polluted endpoints; **do not follow, trust or turn these into product recipes**. Non-English page-by-page inventories, dynamic private flows and external Binance subdomains are NOT exhaustively enumerated or rendered.

English URL declarations per index:
- Growth 17,904; Default 12,211; Muses 3,202; Blog 2,939; Crypto 2,903; Nft 2,609; Futures 2,490; Square 2,186; Trade 1,376; Academy_New 1,230; Earn 502; Fiat 476; Loan 265; SupportAndAnnouncement 193; Market 138.
- The size includes **symbol/asset/time/option variants and CMS details**, not 50,624 fundamentally different designs. Source route records alone do not establish existence, current 200 status, discoverability or genuine UI interaction.

## Direct desktop Chrome-MCP route-family observations

Observed at Windows Chromium desktop (~1875/1910px width), generally in **English + VND** localization. Product route `/en`: exchange nav with Buy Crypto / Markets / Trade / Futures / Earn / Square / Institutional / AI / More, authenticated Deposit instead of Sign Up, hero/market watchlist/news/social proof/SAFU/app distribution/FAQ/footer; personalization differs from logged-out landing.

- **Markets** `/en/markets/overview`, `/en/markets/trading_data`: market stats, asset ticker cards, categories Spot/Futures/TradFi/Alpha, top gainer/new listing/volume rankings, coin-name search, advanced filters and dense table. Desktop outer scroll width exceeded client width in sampled markets states; the overflow may include responsive chart/table infrastructure or overlays — **QA watch**, not automatically a visually broken page.
- **Spot** `/en/trade/BTC_USDT?type=spot`: different, extremely dense **#0B0E11** canvas, live order book rows, side-by-side buy/sell tickets, quantity inputs/ranges, trading fee affordance, live market announcements and chart region. Clicking Buy/Sell or placing orders **was not tested**.
- **Futures** `/en/futures/home`: separate futures secondary navigation, contract ticker lists/market cards, multiple trading CTA, risk-appropriate product hierarchy. Futures wallet/perpetual contract execution not tested.
- **Crypto purchases** `/en/crypto/convert?source=ocbs`: VND → USDT quote form, From/To controls, currency selector and quote; `/en/how-to-buy/bitcoin`: personalized asset guide + buy widget + trust and education sections. Neither purchase, quote acceptance nor payment was submitted.
- **Price detail** `/en/price/bitcoin`: price headline, chart with time ranges (1D / 7D / 1M / 3M / 1Y / YTD), market stats, analysis/news/FAQ tab deck, buy widget, exchange data; market figures are live and must not become hardcoded design evidence.
- **Earn** `/en/earn`: dedicated hero, APR/product catalog, Search coins, HODLer airdrop/earn onboarding, product cards and FAQ; values may vary by asset, risk, and locale.
- **Loans** `/en/loan`: overview, product differentiation Lite/Flexible, explanation of collateral, FAQ, account state panel; no borrowing action.
- **Launchpool** `/en/launchpool`: upcoming/completed projects, subscription CTA, token metrics; no subscription or deposits.
- **Auto-Invest** `/en/auto-invest` **redirected** to `/en/convert/USDT/BNB?activeTab=recurring`. Actual recurring configuration includes frequency/plan name/max trigger count/limit price; do not equate old marketing route with standalone app.
- **Square** `/en/square` and `/en/square/news/all`: **community app shell** distinct from main marketing nav — Discover/Following/News/Stocks, social posting, trending/sidebar sentiment, recommendation cards, author metadata. The authenticated shell showed profile data; no private state transcribed and no post created.
- **AI product marketing** `/en/AI-overview`: distinct product campaign for Binance Intelligence, use-case narrative, CTAs and FAQ; marketing statements **not proof of usable AI capabilities**.
- **NFT** `/en/nft/home` **redirected to `/en/nft/closed`**, displaying the notice that Binance NFT platform is no longer available, with support handoff. Do not describe indexed NFT product/collection URLs as active commerce.
- **Institutional** `/en/institutional`: encountered `We're sorry, but something went wrong` with home fallback. Do not infer rendered service features.
- **Academy** `/en/academy` and `/en/academy/articles/what-is-bitcoin`: separate educational nav Articles/Courses/Learn & Earn/Partnership/Developer Academy, strong editorial categories, reading time, level, updated date, key takeaways, accessible article heading/long-form structure.
- **Blog** `/en/blog`: different marketing editorial archive, featured long-form stories, category and search, load-more. Keep distinct from Academy, Square and Support content.
- **Support** `/en/support/faq` and `/en/support/announcement`: topic-category search, support journey by account/trade/earn/security and live announcement categories, separate from Binance Blog.
- **Company** `/en/about` and `/en/careers`: editorial mission, metrics, trust/security/culture/job discovery; proof and hiring data vary by date and must be validated before reuse.
- **Legal** `/en/legal/home` redirects to `/en/about-legal/home`, showing long categorized regulatory and legal documents without a semantic H1 in sampled DOM. `/en/terms` had the main site chrome/footer but no meaningful visible terms body in sampled initial render (potential loading/region/gating), **not evidence of complete legal text**.
- Additional surfaced families from sitemap, not deeply browser-opened: futures derivatives/options, stocks, Convert pair permutations, FAQ detail, announcement detail, support notices, referral/campaign, fiat rails, token unlock, lending detail, marketplace NFTs (closed), locale variants, and thousands of CMS records.

## Verified design language

Desktop main shell: computed body **rgb(24,26,32) = #181A20**; foreground **rgb(234,236,239) = #EAECEF** (use RGB as ground truth). CTA sampled on About: **rgb(252,213,53) = #FCD535**, foreground **rgb(32,38,48) = #202630**. Main font **BinanceNova / Arial / sans-serif**. About page H1 `48px`, font-weight `600`, standard body `16px / 400`, nav/Deposit button `14px / 500`. Trading view more compressed and darker; Square and Academy have their own shell/component grammar. Yellow is **status/CTA priority**, not a universal background fill. No external site should inherit Binance trademarks or exact BinanceNova font as a matter of default.

Visual hierarchy: dark surface layers and hairline edges, muted secondary figures, conditional positive/negative change color, dense tab/filter/search interface, spatially distinct real-time data modules; public trust/governance content contrasts with dark operational trading. Do not copy market-price screenshot data to another product or misrepresent a chart prediction as financial performance proof.

## True mobile Chrome observations

Actual `resize_window(390,844)` produced **innerWidth=390**, `documentElement.clientWidth=390`. `/en`, `/en/markets/overview`, `/en/price/bitcoin`, `/en/earn`, `/en/blog` and `/en/academy` were navigated on a phone-size window. All sampled documents reported outer scroll width **390** (no positive outer overflow in bounded probe). Mobile nav collapsed, homepage became **app-like account/quick-actions** variant under existing signed-in state, and hero H1 about **32px/40px**; Earn H1 **28px**, Blog H1 **24px**, Academy H1 **28px**, Bitcoin price H1 **14px** (latter is a utility title, not a hero). Desktop About H1 **48px**, so **do not** assume one typography breakpoint across routes. The first Markets mobile reading lacked its H1 immediately after navigation; could be hydration race, not a stable missing heading. No device-GPU or 60fps claims.

## Transfer-ready, site-scoped lessons

1. **One brand → multiple application shells**: conversion marketing, operational exchange, derivatives, discovery table, educational CMS, social community and regulatory resources must be composed with distinct densities and navigation ownership.
2. **Dense market information architecture**: pair summary → chart/order book → execution controls → secondary account/risk, with persistently visible symbol, units, positive/negative change and data freshness.
3. **Market discovery route system**: overview, categories, filter/search, ranking and asset detail link with direct deep routes, without making authentication a prerequisite for basic discovery.
4. **Money-onboarding separation**: fiat purchase/conversion, trading, Earn, margin/futures, and loans have different eligibility and danger, requiring different form validation, disclosure and confirmation contracts.
5. **Education is not promotion**: Academy article details, Blog editorial, Square social, announcement/FAQ support and governance documents are separate content families.
6. **Responsive task prioritization**: mobile removes desktop mega-nav and restructures data into narrower task-first cards. Do not merely scale down a desktop exchange DOM.
7. **Route/state degradation**: explicit NFT closure, Auto-Invest redirect, institutional error; distinguish valid redirects/error states from missing site features.
8. **Sitemap hygiene**: all locales and 50,624 English sitemap declarations are a **coverage map only**; inspect crawl pollution and classification before transferring patterns.

## Exclusions and safety boundary

No automation of trades, simulated buy/sell clicks, account provisioning, KYC, deposits, wallets, security or private account inspection. No claim of all 50,624 pages rendered or tested. Sitemaps, finance metrics and availability can evolve. All design intelligence follows provenance and accessibility rules, not Binance-specific commercial financial recommendations.
