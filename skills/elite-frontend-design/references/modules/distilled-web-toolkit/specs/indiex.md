# Indiex — Toolkit Spec

Source: https://indiex.framer.ai/
Deep profile: `../../../design-intelligence/sites/indiex.framer.ai.md`
Archetype: game-studio
Primary skin anchor: `game-studio`

## Live Snapshot — 2026-10-07
- Sitemap: 2 URLs: `/` and `/404`; the 404 route correctly returns HTTP 404.
- Framer befeeaf.
- Homepage is a 15-section one-page system with public anchors for about, service, games, testimonials, FAQ, team and contact.
- Desktop 1440x900 -> document about 1425x11401; mobile 390x844 -> 390x17793; no document-level horizontal overflow on mobile.
- Desktop: 141 images, 2 video, 0 canvas, 4 settled runtime animations.
- Mobile: 70 images in the rendered variant, 2 video elements, 0 canvas, 0 settled runtime animations.
- Type roles: Oswald + Inter / Inter Display.
- Main palette role: deep navy shell + one acid-green action/HUD accent.
- Featured-game selector is sticky on desktop and releases on mobile.

## Composition Grammar
- identity/hero -> studio credibility -> media reset -> capabilities -> game proof -> character/world gallery -> testimonials -> FAQ -> team -> contact -> final trust -> footer.
- This is a compact studio conversion spine, not a substitute for deep case/service routes when those are needed.
- The strongest late-funnel sequence is proof -> objection handling -> people proof -> contact.

## Media / Motion
- Start from authored still/game art and poster-first video surfaces.
- Video is deferred (`preload=none`) and was not observed playing during the audit.
- Keep media meaning complete without playback; add explicit accessible controls when video matters.
- Do not add WebGL merely to signal “gaming”.

## Interaction
- The game selector is a useful stable-selector + proof-panel pattern.
- Production implementation must use real button/tab semantics and expose selected state instead of focusable DIV controls.
- FAQ belongs in the funnel, but use semantic accordion buttons with `aria-expanded` and `aria-controls`.

## Responsive Contract
- Preserve the section order and one condensed-display identity cue.
- Release sticky selector ownership on narrow screens.
- Step down type roles rather than flattening them: observed H1 96->48, H2 48->32, H3 32->24.
- Drop nonessential motion/media variants before cutting semantic content.
- Keep outer document overflow at zero.

## Template Residue Firewall
Indiex is unusually valuable as a negative QA reference. The live site visibly mixes:
- Indiex, Nexira and ThemeForest identity;
- game-studio content with gym/fitness FAQ and fitness copy;
- `info@onepage.com` with `info@nexira.com`;
- service cards that link back to `./`;
- placeholder GET-to-self forms;
- generic vendor/social/contact residue.

Run one identity/content-integrity invariant across hero, body, metrics, FAQ, team, contact, forms, footer, meta/OG and 404 before release.

## Toolkit Patterns
`indiex-one-page-studio-spine`, `indiex-sticky-game-selector`, `indiex-poster-first-interlude`, `indiex-late-funnel-sequence`, `indiex-anchor-commercial-core`, `indiex-content-integrity-firewall`.

## Do Not Transfer
Exact game art, Indiex/Nexira/ThemeForest identity, fake metrics/testimonials/team data, gym/fitness copy, placeholder contacts/forms, Reddevs/Framer residue, exact acid-green/navy palette pairing, or DIV-based pseudo-tab/accordion semantics.
