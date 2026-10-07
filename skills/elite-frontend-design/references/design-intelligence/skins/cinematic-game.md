# Baseline Skin: Cinematic Game

Generic game / entertainment marketing baseline.

Audited evidence anchor: `../sites/ready-material-053719.framer.app.md` (Echoes of Mars). Use its field-report telemetry, pinned sector survey, still-image campaign pacing, recovered-footage proof, and mobile vertical substitution as mechanism evidence only.

This skin is for game-adjacent and entertainment marketing that needs strong genre identity, world-aware art direction, and cinematic pacing without assuming either a full studio/service information architecture or a flagship franchise launch campaign.

Use game-studio.md when the organization sells game-development capabilities and needs services, cases, team, about, editorial, and contact as a coherent proof ecosystem.

Use open-world-cinematic-launch.md when one specific game/franchise launch needs campaign chapters, trailer/media orchestration, launch conversion, and world-led art direction.

## Use when

Use for:
- game/entertainment marketing pages;
- publisher or campaign microsites;
- game community/event pages;
- soundtrack, DLC, update, season, or expansion marketing;
- entertainment brands with still-art-led identity;
- compact game experiences that do not need studio-service route depth;
- lower-capability execution that needs a disciplined cinematic baseline.

Avoid making this the primary skin for:
- game studios selling services -> use game-studio.md;
- flagship/open-world launch campaigns -> use open-world-cinematic-launch.md;
- dense product dashboards;
- developer/API products.

## Deterministic Design Scaffold

Start with the Game/Experiential Audit Lens.

Choose the lowest-cost medium that can carry the identity:
1. authored still imagery and crop;
2. typography + contrast + spatial composition;
3. light CSS/Framer motion;
4. bounded video/media;
5. heavy renderer only when continuous world/camera state actually matters.

A cinematic result comes from authored hierarchy and pacing, not from effect count.

## Token Scaffold

- world-derived dark or neutral shell;
- high-contrast readable primary text;
- one dominant world/faction accent;
- optional secondary signal accent;
- display type with clear genre character;
- quiet body/UI sans;
- optional compact metadata/mono role;
- media radius 0-12px by default;
- content width roughly 1120-1320px;
- section spacing roughly 96-160px desktop;
- mobile spacing roughly 64-112px;
- route/display headings roughly 52-88px desktop, 36-56px mobile;
- body roughly 15-18px;
- chrome, brackets, ticks, badges, and HUD cues remain subordinate to art/content.

## Composition Grammar

### Hero

Use:
- one dominant world/game identity;
- clear title;
- optional eyebrow/status/platform metadata;
- one primary action;
- optional secondary action;
- one strong image/media field.

Do not bury title/CTA under decorative HUD chrome.

### World / feature chapters

Each chapter should have one job:
- introduce a place/faction/feature;
- show a gameplay or narrative promise;
- reveal a character or mechanic;
- prove a content update;
- move the visitor toward the next decision.

Prefer varied editorial composition over repeated equal cards.

### Media / proof

Use:
- still art;
- screenshots;
- trailers;
- bounded clips;
- platform/store availability;
- release/status facts;
- community or event proof when real.

Decorative art is not proof of gameplay/system capability.

### Conversion

Keep actions explicit:
- wishlist;
- buy/preorder;
- watch trailer;
- learn more;
- join community;
- download;
- read patch/update details.

Do not make users discover core actions through hover-only or drag-only interaction.

## Cinematic Without Heavy Rendering

A premium game feel can come from:
- still art with authored crop;
- display typography;
- high-contrast color;
- restrained HUD metadata;
- sticky or overlapping sections;
- selective scale shifts;
- editorial pacing;
- lightweight motion.

Earn WebGL/3D/video complexity rather than using it as a genre shortcut.

## Media Ownership

Every expensive medium needs an owner and purpose.

Use video when:
- motion itself communicates content;
- trailer/story beat is important;
- a still cannot carry the evidence.

Use canvas/WebGL when:
- continuous state/camera/material change is part of the experience;
- interaction benefits from spatial continuity;
- performance/fallback work is justified.

Otherwise prefer still-image composition.

## Navigation / Input Grammar

Keep primary navigation conventional.

Optional game-flavored input:
- keyboard shortcuts;
- carousel controls;
- chapter jumps;
- cursor treatments;
- hover reveals.

Rules:
- never require a pointer-specific trick for core navigation;
- maintain visible focus;
- preserve accessible labels;
- do not hide route escape paths inside world chrome.

## Skin Lock

Lock:
- world/chrome hierarchy;
- type-role separation;
- accent semantics;
- media framing;
- metadata grammar;
- spacing rhythm;
- motion ownership;
- core action hierarchy;
- responsive identity priorities.

## Controlled Mutation

May mutate:
- accent;
- shell temperature;
- typography families;
- hero alignment;
- world/character artwork;
- chapter composition;
- media tier;
- one signature interaction;
- HUD grammar intensity;
- light vs dark subchapter treatment.

Must not default to:
- acid-lime gaming palette;
- Oswald/condensed all-caps everywhere;
- fake player counts/awards;
- fake platform badges;
- fake launcher/download controls;
- generic glitch overlays;
- copied franchise artwork.

## Responsive Contract

Preserve:
- world identity;
- title hierarchy;
- project/game art treatment;
- primary actions;
- chapter order;
- one identity-bearing media/scroll cue.

Adapt:
- display scale;
- crop;
- chapter geometry;
- sticky behavior;
- metadata density;
- navigation;
- media cost.

Required:
- no unintended document-level horizontal overflow;
- touch-safe controls;
- readable text over art;
- reduced-motion fallback;
- no pointer-only core paths.

## Motion Language

Priority:
1. navigation/input feedback;
2. state/chapter transitions;
3. one signature reveal or media transition;
4. local ambient motion;
5. decorative motion last.

Avoid:
- universal parallax;
- random glitch;
- constant scale/pulse;
- fake HUD animation everywhere;
- autoplay media without purpose;
- motion competing with readable content.

## Anti-Template Guard

High-risk generic gaming bundle:
- charcoal shell;
- neon green/purple accent;
- condensed all-caps display;
- giant character still;
- bracket labels;
- fake HUD;
- glow borders;
- sticky screenshots;
- fake player numbers;
- generic "download launcher" CTA.

Require meaningful differentiation in at least one:
- world/faction art direction;
- chapter model;
- interaction grammar;
- typography system;
- media choreography;
- proof mechanism;
- conversion model;
- responsive transformation.

Changing only logo, accent, and character image does not count.

## QA Rubric

Pass only if:
- the Game/Experiential Audit Lens has been applied;
- world identity is clear without overwhelming usability;
- HUD/chrome remains subordinate;
- media complexity is earned;
- Cinematic Without Heavy Rendering remains a valid low-cost path;
- core actions are conventional and accessible;
- motion has explicit ownership;
- mobile preserves identity without accidental overflow;
- reduced-motion users keep the full informational path;
- proof claims are real;
- the result does not collapse into a generic neon gaming template.

