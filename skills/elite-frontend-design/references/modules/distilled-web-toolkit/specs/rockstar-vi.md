# Rockstar Games VI ? Toolkit Spec

Source: https://www.rockstargames.com/VI
Deep profile: `../../../design-intelligence/sites/rockstargames.com-vi.md`
Archetype: cinematic-launch
Primary skin anchor: `open-world-cinematic-launch`

## Live Snapshot ? 2026-10-07
- Campaign route has no public `/sitemap.xml` inventory at this path.
- Desktop document ~1440x11870; mobile ~390x10578; zero outer overflow.
- Runtime: 3 canvas elements, 2 videos, 33 images, ~10 fixed/sticky elements.
- Custom ArtDeco family remains a strong branded typography signal.

## Composition Grammar
- Hero -> trailer -> story/world chapters -> exploration/media/news -> back-of-box summary -> conversion/outro.
- Each chapter has one campaign job.

## Media / Motion
- Use aspect-ratio art direction and user-invoked trailer proof.
- Escalate media cost from still to motion/video/renderer only when it improves world storytelling.

## Responsive Contract
- Preserve minimum world payload: logo/key art/focal crop + core action.
- Re-author crop/asset by aspect ratio rather than center-crop everything.

## Toolkit Patterns
`rockstar-aspect-art`, `rockstar-world-chapters`, `rockstar-trailer-proof`, `rockstar-back-of-box`, `rockstar-media-cost-ladder`, `rockstar-world-payload`, `rockstar-chapter-contrast`.

## Do Not Transfer
Rockstar/GTA identity, custom fonts, logos, characters, exact campaign art, copy, release details, or proprietary trailer assets.
