# Echoes of Mars — Toolkit Spec

Source: https://ready-material-053719.framer.app/
Deep profile: `../../../design-intelligence/sites/ready-material-053719.framer.app.md`
Archetype: cinematic-game
Primary skin anchor: `cinematic-game`

## Live Snapshot — 2026-10-07
- 1/1 sitemap URL: `/`; no hidden content route families.
- Generic Framer 404 returns real HTTP 404 and is not in sitemap.
- Framer c9b3949.
- Complete campaign: hero -> trailer -> premise -> world -> story -> gameplay -> systems -> footage -> character -> sound -> release -> press -> final wishlist.
- Desktop 1440x900: document ~1425x18690, 47 images, 0 video, 0 canvas.
- Mobile 390x844: document 390x17608, zero outer overflow, 47 images, 0 video/canvas.
- Saira Variable display/narrative + Datatype Variable telemetry.
- Warm black/bone/rust world-derived palette.

## Composition Grammar
Use one long single-title campaign only when every chapter has a distinct proof or decision job. The late conversion is earned by world, gameplay and media proof rather than repeated generic feature sections.

## Signature Interaction — Pinned Sector Survey
Desktop uses one sticky viewport and ~5320px world track to survey six sectors and finish with one summary state. Horizontal movement is justified by spatial exploration, not novelty.

Mobile/reduced motion must release sticky ownership and restore vertical flow while preserving every place fact.

## Telemetry as Narrative UI
Coordinates, mission/sector IDs, UTC, archive dates, figure/build/platform labels and uncertainty can sustain world identity when each field provides real context. Do not use random terminal noise as decoration.

## Recovered Footage Proof
Treat screenshots as evidence with truthful source/location/build/platform context. Never fabricate capture provenance.

## Mechanics Survey Rows
A small set of mechanics can use indexed full-width rows instead of a card grid. Hover media is enhancement only; text remains visible. Replace pointer-specific instructions on coarse pointers and use correct heading semantics.

## Responsive Contract
- preserve chapter order, field-report grammar, primary action and all sector facts;
- H1 observed 190 -> 56px; H2 70 -> 33px; large mechanic/gameplay words 126 -> 46px;
- desktop horizontal survey -> mobile vertical stack;
- retain no document-level horizontal overflow;
- keep cinematic meaning complete with still imagery.

## QA / Residue
Release blockers in the live demo include:
- home `html lang` empty;
- multiple mechanic titles authored as H1;
- `HOVER TO SURVEY` copy surviving on touch/mobile;
- wishlist/trailer/social actions leading only to platform roots;
- soundtrack/press/legal using example.com;
- anonymous press quotes;
- generic Framer 404 and badge.

## Toolkit Patterns
`echoes-telemetry-narrative-ui`, `echoes-pinned-sector-survey`, `echoes-recovered-footage-proof`, `echoes-numbered-field-report`, `echoes-mechanics-survey-rows`.

## Do Not Transfer
Echoes of Mars identity/lore, exact art/assets, Saira/Datatype as mandatory fonts, exact rust palette, fictional claims/press quotes/build/platform data, placeholder URLs, Framer chrome, repeated-H1 semantics or pointer-only instructions.

## Re-Audit Delta — 2026-10-08

Sitemap still declares only home /; 13 authored chapters unchanged. Generic /404 and invalid routes return HTTP 404.

Three measured responsive modes: <=809px normal vertical survey with viewport-relative track; 810–1199px sticky 4280px horizontal track, world height 3600px; >=1200px sticky 5320px track, world height 3780px. Both boundaries verified at adjacent widths, and zero outer document overflow observed.

At 1440px actual world scroll transform goes ~0 -> -1019.76 -> -2038.96 -> -3312.97 -> -3880px. Crucially, at prefers-reduced-motion: reduce the source STILL uses sticky world viewport and travels to -3880px. Previously documented reduced-motion vertical presentation is RECOMMENDED implementation behavior, not observed in the live template. Implement a static, accessible six-sector sequence for reduced motion.

Chrome headless validated desktop/tablet/mobile (Chrome extension disconnected) while preserving date-bound source observations. Data: data/echoes-survey-breakpoints-2026-10-08.csv; full details in original deep profile. Content, placeholders, semantic QA and 47-image/no-video/no-canvas findings otherwise unchanged.
