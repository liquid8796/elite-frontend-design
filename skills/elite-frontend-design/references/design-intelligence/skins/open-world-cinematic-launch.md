# Baseline Skin: Open-World Cinematic Launch

audited evidence anchor: ../sites/rockstargames.com-vi.md

This skin distills transferable campaign mechanisms from the Rockstar Games VI audit. It does not authorize copying GTA/VI logos, exact ArtDeco typography, character art, shard art, pink/purple palette, trailer imagery, copy, or proprietary campaign assets.

## Use when

Use for open-world game launches, narrative entertainment campaigns, franchise reveal pages, or fictional-world launches that need cinematic art direction plus clear trailer, release, platform, edition, and conversion paths.

Prefer cinematic-game.md when the brief is not specifically a world-launch campaign.

## Deterministic Design Scaffold

Use World-Led Campaign Chapters with one global world grammar. Spend the most media/rendering ambition in the opening stage, then use user-invoked trailers and responsive static media for later chapters.

## Token Scaffold

- shell: deep world-derived neutral/chromatic dark, not default black;
- surface ladder: shell -> cinematic media -> 2-3 locally colored promo surfaces -> ordinary info/news surface;
- text: high-contrast light primary, softened secondary;
- action accent: one pale or bright contrast color reserved for conversion and selected state;
- display role: high-character campaign face; UI role: compact readable companion; body role: readable narrative face;
- headline scale: 56-84px desktop, 38-58px mobile depending on word length;
- tracking: wide only on short campaign statements;
- container: 1160-1360px for readable DOM; full-bleed media may escape it;
- section rhythm: 120-220px desktop, 72-128px mobile;
- promo radius: 12-28px desktop and tighter on mobile; pill only for compact actions.

## Composition Grammar

1. World Stage - signature art/canvas/image composition + title/release/platform context + primary CTA.
2. Trailer as User-Invoked Proof - one focused trailer chapter with explicit play choices.
3. Edition / Offer Chapter - at most 2-3 major offer surfaces with real differentiation.
4. Back-of-Box Chapter - one place/world statement plus concise conflict/tension copy.
5. World Exploration - music, people/places, media, factions, vehicles, or similar campaign pillars.
6. Update / News Chapter - current campaign updates after the core world is established.
7. Outro Conversion - community/signup/pre-order or platform reminder without inventing a second visual system.

Every chapter gets one dominant job. Avoid stacking trailer, lore, editions, screenshots, and purchase controls into one hero.

## Aspect-Ratio Art Direction

For the world stage and large campaign media:

- define focal subject and text-safe zones;
- prepare portrait, landscape, and ultra-wide compositions when one crop cannot serve all;
- route media by aspect ratio/orientation as well as width;
- preserve the same narrative subject even when the crop changes;
- test 390x844, 1280x800, 1440x1000, and an ultra-wide case when supported.

Do not use CSS object-position as the only rescue strategy for fundamentally incompatible art.

## World-Led Campaign Chapters

Lock a common world grammar across all chapters:

- typography roles;
- navigation/chrome;
- CTA semantics;
- media framing;
- transition intensity;
- world palette relationship.

Local chapters may own different colors or artwork. They may not invent a new design system each time.

## Trailer as User-Invoked Proof

- trailer/video playback starts from explicit user action unless ambient muted media is truly justified;
- provide poster/fallback media;
- avoid preloading full-resolution video before it is likely to be viewed;
- keep title, release state, and primary CTA legible without playback;
- trailer controls remain keyboard/touch accessible.

## Back-of-Box Chapter

After the first spectacle/conversion beats, insert one concise narrative bridge:

- where are we?
- who/what anchors the world?
- what tension or promise matters?
- why should the visitor explore deeper?

Keep this shorter than a lore page.

## Skin Lock

Lock:

- world-derived shell and palette relationship;
- high-character display vs readable UI/body roles;
- one conversion accent;
- chapter ownership;
- media cost ladder;
- explicit trailer interaction;
- aspect-ratio art-direction strategy;
- responsive world payload;
- navigation/accessibility basics.

Do not let later chapters drift into generic SaaS cards, random HUD chrome, or unrelated poster styles.

## Controlled Mutation

May mutate:

- fictional-world palette;
- display type genre;
- hero rendering mechanism;
- chapter order when the new campaign needs it;
- platform/release/edition information model;
- signature interaction;
- local chapter color worlds;
- media framing geometry.

Must mutate all proprietary art, logos, copy, exact colors, exact typography, trailer imagery, and branded shard/composition identity from the Rockstar reference.

## Responsive Contract

- preserve release/platform/primary CTA in the opening mobile experience;
- preserve one recognizable world-stage subject or lower-cost equivalent;
- use Responsive Fidelity Substitution for expensive canvas/3D/video;
- use Aspect-Ratio Art Direction for hero and large campaign media;
- stack offer cards without turning them into unreadable tiles;
- tighten radius/spacing before deleting world identity;
- maintain no unintended horizontal overflow;
- keep trailers user-invoked on touch devices;
- preserve user zoom and reduced-motion paths.

## Motion Language

- one major authored hero reveal/movement is enough;
- continuous world-stage motion runs only while relevant;
- chapter entrances stay quieter than the hero;
- trailer playback is content, not decoration;
- avoid universal parallax and identical fade-up motion;
- use theme transitions only when they communicate chapter progression.

## Anti-Template Guard

Avoid:

- generic neon sci-fi HUD overlays unrelated to the world;
- default black + purple game gradients;
- autoplay full-screen trailers that make copy/actions unreadable;
- every chapter becoming a poster card;
- random glitch/noise effects as shorthand for game;
- copying GTA-style Art Deco, pink CTA, shard silhouettes, crime/map iconography, or logo geometry;
- disabling user zoom to preserve composition.

If the page still reads as GTA-inspired after replacing content, the skin was applied too literally.

## QA Rubric

Pass only if:

- first viewport communicates world identity, release/status, and primary action without playback;
- each chapter has one clear job;
- Trailer as User-Invoked Proof works by keyboard and touch;
- Back-of-Box Chapter bridges cleanly into deeper world content;
- portrait/landscape/ultra-wide crops preserve focal subject and safe text zones;
- mobile retains world identity with no horizontal overflow;
- hidden/offscreen heavy media is not consuming unnecessary runtime/bandwidth when avoidable;
- local chapter colors still feel part of one world;
- CTA contrast survives bright/dark artwork;
- reduced-motion/fallback paths remain usable;
- final result belongs to the new franchise/world and does not reproduce Rockstar proprietary identity.
