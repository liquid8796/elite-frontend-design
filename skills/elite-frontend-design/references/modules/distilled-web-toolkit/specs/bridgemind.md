# BridgeMind — Whole-Site Toolkit Spec

Source: https://www.bridgemind.ai/
Deep profile: ../../../design-intelligence/sites/bridgemind.ai.md
Archetype: developer-agent-workspace; existing skin developer-infra (no new skin).

## Coverage
143/143 main website sitemap + 10/10 companion documentation sitemap URLs HTTP 200. Main coverage contains 120 changelog details, 8 blog details, four core product/plan routes, learning/archives, company/community/merch/ended campaign, developer and legal. Twelve extra auth/redirect/invalid probes yield seven 200 and five 404. Full 165-row inventory, link graph, 46 rendered representative 1440px/390px states and 13 UI probes live under data/bridgemind-*-2026-10-09.csv. All sampled mobile states have no outer overflow. Public HTML replay into Chromium was used because Chrome extension unavailable.

## Visual and Flow
Dark rgb(13,14,17), white, Sora 84px home H1->44px phone and Inter body. Editorial H1 56->36.44px; docs separate Inter 30px and dark shell. Operational simulator, task-shaped terminals, voice no-mic demo, 3D product stills and versioned content instead of generic card bento.

Homepage: thesis -> Agent/Code/Thread read-only simulator -> voice -> developer community -> suite/plans -> installers.
Product: distinct Agent/Code/Thread jobs and practical screen proof -> price/download.
Pricing: Basic/Pro/Ultra app credits and BYO outside model spend -> authentication.
BridgeVoice: sample dictation -> local/cloud model paths -> language search -> privacy FAQ -> installer.
BridgeVerse: workspace tower -> agent desk -> live-terminal claim *inside native product* -> still walkthrough -> installer.
Learn/blog: guide directory -> dated release/evergreen details -> primary citations.
Changelog: product navigation -> platform/date/version list -> 120 deep links.
Docs: getting started -> three modes -> dictation/plugins/routines -> OS setup.
Auth: login/signup out of sitemap; no sign-in attempted.
Utility: contact, Discord, merch, ended giveaway, developer discovery, legal, actual 404.

## Observed UI and Boundaries
Agent/Thread buttons visibly swap simulated app scenes and Explore expands it. Voice sample Listening and tab content changes verified. No real AI agents/microphone. Pricing toggle and release platform filters not conclusively asserted from limited probes. Marketing says macOS/Windows/Linux but docs index retains Windows-development/Linux-unsupported text. /download redirects home #download; /signin to /login; /faq standalone 404, while BridgeVoice has in-page FAQ.

Transfer honest workflow simulators, mode-specific proof, local/cloud data privacy disclosure, cross-host OS parity and stable release deep links. Never copy source branding, UI screenshot pixels, claims or invented account/work result.
