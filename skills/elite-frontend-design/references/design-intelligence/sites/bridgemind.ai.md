# BridgeMind — Full-Site Design Intelligence

Source: https://www.bridgemind.ai/
Companion docs: https://docs.bridgemind.ai/docs
Audited: 2026-10-09. Public website and all official sitemap routes, not merely the home page.

## Full-Site Route Coverage

**153/153 official sitemap URLs returned HTTP 200.** Main-site sitemap contains **143 routes**: home (1); product/pricing/BridgeVoice/BridgeVerse (4); Learn and blog archives (2), blog articles (8); changelog index (1) and **120 individual changelog details**; developer resource page (1); contact, Discord, merch, giveaway (4); legal terms/privacy (2). Companion docs sitemap adds **10 routes**: /docs; getting started, Agent, Code, Chat, dictation, skills/plugins, routines, macOS and Windows.

12 separately tested alias/auth/invalid paths yielded 7 HTTP 200 and 5 HTTP 404. Public non-sitemap /login, /signup, /api; /signin -> /login, /download -> homepage #download, docs root -> /docs. /404, /faq, /account, /checkout and one random nonexistent path return 404. The /faq probe is not proof of broken site FAQ: BridgeVoice uses an on-page FAQ section.

Evidence files: modules/distilled-web-toolkit/data/bridgemind-route-inventory-2026-10-09.csv (165 route rows); bridgemind-internal-links-2026-10-09.csv (same-ecosystem link graph); bridgemind-rendered-states-2026-10-09.csv (46 representative rendered desktop/mobile states); bridgemind-interaction-probes-2026-10-09.csv (13 bounded actions).

**23 representative route types at 1440×900 and 390×844, 46 rendered states total, zero positive outer document overflow** in sampled Chromium. This does not equate to interactive testing of 153 routes. The isolated Chromium browser was given publicly fetched HTML because direct headless navigation encountered a challenge and the connected Chrome extension was unavailable.

## Design DNA

Dark, intentional developer-product system: computed background rgb(13,14,17), white text, Sora display headings and Inter body/utility; real-looking terminal/agent panes create visual depth rather than generic blue glow. Homepage/product H1 84px/600 desktop -> 44.04px phone; pricing/blog/release H1 56px -> 36.44px. Documentation uses a separate rgb(10,10,10) shell and Inter H1 30px/800.

At the sampled homepage state, 2 canvas elements desktop and 1 mobile, 65 image elements. Do not label this WebGL without verifying rendering. BridgeVerse marketing tells its 3D native-app story with explanatory still images; no live 3D marketing renderer was verified.

## Complete Route Jobs

1. Homepage /: Agent Super App premise -> simulated Agent/Code/Thread workbench, notification and voice assistant -> BYO coding tool support -> community/livestream process evidence -> suite products -> three pricing plans -> FAQ/installer/legal actions.
2. /product: Agent owns delegated routines/approvals, Code owns folder/terminal/browser panes, Thread owns read-first conversational sessions; practical task evidence instead of empty feature cards.
3. /pricing: Basic $20, Pro $50, Ultra $100 monthly and advertised annual equivalents $16/$40/$80; credits and tier features differentiated, explicit own-provider subscription/API billing. Checkout and account state not verified.
4. /bridgevoice: no-mic simulator of Home/History/Dictionary/Shortcuts/Settings; Try sample, engine/shortcut UI, model download sizes, privacy paths for local Parakeet/Whisper/Distil vs cloud provider, searchable language matrix, FAQ and download. Sample states no microphone access, upload or actual model download.
5. /bridgeverse: one workspace floor per tower, agent desk/status, opened terminal and room assistant told through screenshots; links to installers/plans. Marketing stills are not automatically an interactive browser game.
6. /learn, /blog and eight articles: evergreen workflows, model release reporting, dates, reading metadata and source links. Provider release claims are external and must not be cloned as verified product results.
7. /changelog and 120 details: product rail (BridgeMind, BridgeVoice, older BridgeSpace/BridgeAgent), platform/date/version facets, individual deep-linked historical updates. These are 120 version entries, not 120 unique layouts.
8. /developers and /api: machine-discoverable product identity with read-only site-info and OpenAPI/llms resources distinguished from privileged application API. No authenticated endpoint was invoked.
9. /contact, /discord, /merch, /giveaway: contact, builder community, hoodie product and properly ended campaign state. Payment/order behavior not tested.
10. /terms and /privacy: long-form legal and service scope.
11. /login and /signup, not sitemap-declared: branded Google/Apple/email views, recovery, newsletter choice, signup anti-abuse challenge. No sign-in, payment or CAPTCHA action attempted.
12. docs.bridgemind.ai, ten pages: installation, mode guides, dictation, plugins, routines, macOS/Windows and doc navigation, not merely a docs homepage.

## Verified Interaction Versus Inference

Homepage simulator: a dispatched **Thread** button swaps sample Code pane into a thread scene; **Agent** produces a distinct delegated-worker scene; **Explore** expands the demo. BridgeVoice **Try sample** displays Listening; **Dictionary** and **History** tabs change visible sample-panel content. These are front-end simulated states, not running agents, hardware audio, or account work.

Monthly/Annual period and platform changelog filters visibly exist; the abbreviated probes did not conclusively prove full resulting calculations or release subset. Mobile Open menu was dispatched but captured main-content excerpt cannot prove the menu overlay state. Do not promote these actions as verified complete workflows.

## Reusable Design Mechanisms

**Operational Simulator with Authority Boundary**: real-feeling but explicitly sample-data app proof, clear interactive preview/real app CTA separation.

**Mode Contract, Not Three Feature Cards**: one product shell with different work units and proofs for Agent, Code and Thread.

**Proof Modality by Capability**: bounded workbench for coding, no-microphone voice sample for dictation, still sequence for native spatial world, factual deep-linked history for releases and task-first docs for adoption.

**Local/Hosted Speech Trust Ledger**: on-device audio vs hosted requests, model size, supported languages, enhanced transcript credit/privacy boundary next to selection.

**Cross-Host Capability Claim Invariant**: marketing, downloads, docs and release notes should share a dated supported-platform truth. Marketing/downloads say Mac, Windows and Linux; docs home calls Windows in development and Linux unsupported, a specific dated inconsistency in public copy.

**Product-Family Version Ledger**: product/platform/date navigation, stable update detail routes, long-form mobile readability rather than a chronological blob.

**BYO Provider Billing Boundary**: app credits do not automatically pay for third-party AI subscriptions or API usage.

**Builder Community as Process Proof**: connect real implementation records, livestreams, release logs and learning content. Do not import claims of revenue or membership into another brand without evidence.

## Responsive and Risk Contract

All 46 sampled states fit document width. Preserve readable pane proof at 390px; H1 scales 84->44px on home and 56->36px for editorial, rather than miniaturizing all UI. Changelog is roughly 15,961px desktop and 24,090px phone; vertical density step-down is acceptable.

Test selected mode keyboard/ARIA state, simulator sample labelling, voice status announcements, reduced-motion, documentation/support claims, plan selection and end-to-end authenticated route separately. Strong evidence is limited to HTTP census, computed render DOM and specific clicks. No claims of actual backend agent runs, installer compatibility, live microphone transcription, transactions, payment/OAuth success or live BridgeVerse rendering.
