---
name: reference-first
description: Evidence-first workflow for screenshots, mockups, generated concepts, live references and UI videos. Extracts a buildable design specification, preserves fidelity, and defines how to compare the rendered implementation against the reference.
---

# Reference First

Use whenever the task includes a visual target or asks to recreate an existing interface.

## Principle

Reference work is not "inspired by" unless the user says so. When the task is faithful recreation, visible evidence becomes the design specification.

Do not make the reference a background image or slice it into fake UI pieces.

## Intake

Record what evidence exists:

- screenshot/image;
- multiple responsive screenshots;
- live URL;
- video/screen recording;
- design file/export;
- existing code;
- brand assets;
- generated concept image.

Note the viewport dimensions when known.

## Evidence Hierarchy

Use the strongest evidence available for each question:

1. user requirements and exact supplied copy;
2. structured design/source data that describes real layout or behavior;
3. the actual rendered branch for the target route/state/viewport;
4. screenshots or video from that real state;
5. reasoned visual inference only for details the evidence does not reveal.

When HTML/CSS/JS or a structured design source exists, do not guess interaction or component structure from pixels alone. When a structured source is too large, first inspect its high-level map/metadata, then fetch only the relevant child regions or source branches.

For an existing application, confirm the code path that actually renders at the target viewport. A mobile fallback, feature-flagged branch, loading branch or alternate route shell must not be mistaken for the desktop/active target.

## Static Reference Extraction

Extract:

### Geometry
- viewport;
- outer gutters;
- max-width/container;
- column count/ratios;
- alignment anchors;
- section heights;
- repeated spacing intervals;
- component dimensions.

### Typography
- family class/character;
- heading/body/UI roles;
- approximate size ratios;
- weight/width;
- line height;
- line length;
- letter spacing;
- case conventions.

### Visual tokens
- backgrounds/surfaces;
- text hierarchy;
- borders;
- radii;
- shadows;
- accent/state colors;
- icon treatment.

### Components
- repeated families;
- state variants;
- navigation;
- forms/controls;
- tables/lists/cards;
- media frames.

### Assets
- image crop/aspect ratio;
- logos/marks;
- illustration/render style;
- textures/backgrounds.

Classify assets by purpose before implementation:

- **identity** — logos, marks, brand fonts and durable brand imagery that must remain exact;
- **content** — product photos, illustrations, posters or media that must appear in the final UI;
- **reference** — screenshots, competitor examples and mood material used only to guide design;
- **UI glyphs/icons** — interaction symbols whose metaphor, stroke/fill style, optical weight and state treatment matter.

Do not silently substitute identity assets or UI icons with "close enough" generic replacements when the real asset is available.

## Video / Interaction Extraction

Treat video as a timeline.

For each meaningful segment capture:

- initial state;
- user or scroll trigger;
- element entering/leaving;
- spatial direction;
- timing relationship;
- easing character;
- pin/sticky behavior;
- scrubbed vs triggered motion;
- final state.

Translate this into behavior, not frame-by-frame imitation.

## Buildable Reference Spec

Before coding, summarize:

1. page regions in order;
2. container/grid rules;
3. type scale;
4. color/surface tokens;
5. repeated component families;
6. signature media treatment;
7. interaction/motion behaviors;
8. responsive behavior visible in evidence;
9. unknowns that require best-effort inference.

## Fidelity Priority

When implementation trade-offs occur, preserve in this order:

1. information architecture and visible content;
2. overall composition/container geometry;
3. typography scale and wrapping;
4. major spacing rhythm;
5. color/surface relationships;
6. component proportions;
7. assets/crops;
8. small decorative details.

Accessibility and actual interaction correctness may require controlled deviations. Keep them visually compatible with the reference.

### Accepted-reference lock

Once a reference or concept is explicitly accepted, do not "improve" it from taste alone. Lock and record:

- exact visible copy that must remain;
- first-viewport composition and section/state order;
- container model and major geometry;
- background/surface colors, including whether a background is true white, off-white, tinted or dark;
- typography proportions and control/chrome text treatment;
- image crop, mask, tint/overlay and edge-treatment behavior;
- component families and their variants;
- icon/glyph inventory: metaphor, outline vs filled style, optical weight, size, color, alignment and state;
- density and spacing rhythm.

If the accepted hero image has no tint, do not add one. If its background is white, do not warm it to cream. If the design is open/cardless, do not introduce floating cards merely because they are convenient.

Record any necessary deviation caused by accessibility, missing assets, browser behavior or a concrete implementation constraint.

### Section/state detail references

For multi-section pages or dense app screens, readability of the evidence outranks compactness.

- Use a coordinated fresh reference for a major section/state/detail when the overview makes text, control anatomy, spacing or assets too small to inspect.
- For dashboards/tools, detail references may cover tables, inspectors, sidebars, modals, charts, toolbars, forms and selected/loading/error states.
- Do not crop or zoom a tiny part of an old overview and treat it as authoritative. Create or obtain a fresh detail view that preserves the same design system.
- Across all detail references, preserve one brand world: palette, typography, component geometry, media treatment, density and spacing logic.
- During implementation, compare one section or contiguous viewport at a time when that produces more reliable fidelity than judging only a giant page overview.

## Image-First Concepting

When image generation is available and useful for a brand-new design:

- generate a complete enough target to guide implementation, not just a hero;
- for long pages, prefer readable section-level references over one tiny tall image;
- keep concepts internally consistent;
- extract tokens and layout rules from the selected concept;
- build real semantic components;
- render at the same viewport and compare.

Do not make external image APIs a hard dependency of this skill.

### Explicit image-first approval workflow

Use this stricter branch when the user asks to see/approve a design before code or asks for image-first/pixel-matching work:

1. Inspect the existing project, content constraints, assets and target viewport first.
2. Save generated concepts as versioned references such as `design-previews/<page>/reference-v01.png`; never overwrite a previous version.
3. Generate or edit one concept at a time.
4. Show the actual preview and stop before implementation until the user explicitly approves, requests a targeted revision, or asks for a redo.
5. For a targeted revision, describe two blocks: `Preserve` and `Change`. Change only the requested design variables.
6. For a redo, return to a materially different direction instead of feeding the rejected image back as the visual source.
7. Never infer approval from silence or unrelated feedback.
8. After approval, the approved version is the visual source of truth at its reference viewport.
9. Do not commit preview assets unless requested.

For ordinary frontend tasks, do not force this approval gate. Use it only when the task calls for image-first concept approval.

### Design-first prompt contract

When generating a visual concept, prompt like a design system rather than a vague wish. Cover:

- GOAL — artifact, audience and success criteria;
- FORMAT — viewport/aspect and safe margins;
- LAYOUT — grid, placement and hierarchy;
- TYPE SYSTEM — family character, weights, leading and tracking;
- COLOR + MATERIAL — base, text, one dominant accent, surface/texture treatment;
- IMAGERY / UI STYLE — photo/3D/UI treatment;
- COPY — exact must-preserve text;
- CONSTRAINTS — the few variables currently locked;
- NEGATIVE CONSTRAINTS — unwanted text, marks, effects or generic patterns.

Prefer variants over rerolls. Once the structure is promising, change only 1–2 variables per revision so the reason a design improved or regressed stays legible.

## Video-to-Spec Workflow

When the evidence is a local video or screen recording:

1. Inspect duration, dimensions and frame rate when tooling such as `ffprobe` is available.
2. Extract representative frames when tooling such as `ffmpeg` is available. Favor timeline beats and transition moments over arbitrary uniform thumbnails.
3. Analyze in layers:
   - story and section order;
   - layout and sticky regions;
   - motion triggers, easing, scrub/pin/parallax/masks;
   - typography, color, surfaces and media treatment;
   - likely implementation mechanism;
   - accessibility, reduced-motion and mobile behavior.
4. Create an asset map: existing assets, URLs, local files, generated media needs, masks/posters/sprites when relevant.
5. Produce a builder-ready specification detailed enough to reproduce the interaction without repeatedly rewatching the source.
6. Name concrete mechanisms when evidence supports them: sticky, pinned timeline, scroll scrub, video `currentTime`, transform, mask, shader, carousel physics, pointer field, and so on.

Do not call a screenshot pan or slideshow evidence of a live website interaction.

## Source-Available Interaction Extraction

If HTML/CSS/JS for the reference exists, inspect source behavior before guessing from screenshots.

Search for useful interaction clues such as:

- `pointermove`, `mousemove`;
- `ScrollTrigger`, sticky/pin/parallax;
- `requestAnimationFrame`;
- canvas/WebGL/Three.js;
- hover/focus/active handlers;
- IntersectionObserver / Web Animations;
- masks, clip paths, filters, carousels and smooth-scroll engines.

Treat working source behavior as stronger evidence than visual inference. Extract reusable interaction concepts rather than copying source implementation blindly.

## Reliable Full-Page Evidence

Native one-shot full-page screenshots can fail on lazy-loaded, reveal-heavy, WebGL or scroll-animated pages.

When full-page evidence looks blank, sparse, clipped, or disagrees with a working scroll video:

1. open the real page;
2. warm it by scrolling top → bottom once;
3. return to the top;
4. scroll in viewport-sized or slightly overlapping steps;
5. wait for lazy/reveal content to settle at each stop;
6. capture each settled viewport;
7. stitch the captures vertically when tooling allows;
8. derive section crops from that stitched full-page evidence.

Reject a full-page candidate that contains large unexplained blank bands, misses lower sections, or materially disagrees with the live page/video.

## Reference Comparison Loop

Use visual-qa.

At the reference viewport:

1. capture implementation screenshot;
2. compare silhouette/composition;
3. compare text wrapping and scale;
4. compare major gaps;
5. compare color/surfaces;
6. compare image crop and component geometry;
7. fix the largest difference first;
8. repeat.

Do not chase one-pixel details while the page silhouette is still wrong.
