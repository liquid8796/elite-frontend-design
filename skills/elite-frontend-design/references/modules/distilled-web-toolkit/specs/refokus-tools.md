# Refokus Webflow Tools — Toolkit Spec

Source: https://www.webflow-tools.refokus.com/
Deep profile: `../../../design-intelligence/sites/webflow-tools.refokus.com.md`
Archetype: developer-tool
Primary skin anchor: `developer-infra`

## Live Snapshot — 2026-10-08
- 19/19 sitemap URLs: home + styleguide + 17 tool docs.
- Home ~1425x5488 desktop / ~390x4703 mobile.
- CMS Filters representative ~1425x4791 / ~390x5143.
- Dark #1C1C1C shell, white foreground, purple utility accent.
- Manrope + Consolas / IBM Plex Mono.
- No Three/GSAP signature runtime required.

## Route Grammar
Home: identity -> tool discovery/filtering -> how it works -> FAQ -> agency CTA.
Tool detail: promise -> copy script -> place -> configure -> publish staging -> verify -> demo/clonable -> agency CTA.
Styleguide: rationale -> classes -> component/child/modifier rules -> naming -> layout/hierarchy.

## Responsive
- 180px library display -> 64px;
- 80px docs H1 -> 36px;
- compact sticky context;
- zero outer mobile overflow.

## QA
All sitemap pages currently lack canonical and document language. Home also splits one visual hero across four H1 elements.

## Toolkit Patterns
`refokus-tools-copy-configure-verify`, `refokus-tools-public-styleguide`, `refokus-tools-sticky-context-band`.

## Do Not Transfer
Identity, exact tool code/names, exact purple palette, graphics or multi-H1 semantics.
