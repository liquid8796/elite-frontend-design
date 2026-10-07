---
name: scroll-world
description: Specialized scroll-cinematic workflow for continuous camera journeys, scroll-scrubbed pre-rendered video worlds, seamless scene chains, native mobile variants, reduced-motion fallbacks and seam-focused QA. Load only for immersive scroll storytelling where scroll should drive a coherent camera/world sequence.
---

# Scroll World

Use this module for experiences where the defining interaction is a **continuous scroll-driven visual journey**: a fly-through world, camera tour, product/environment voyage, connected diorama, architectural walkthrough, or pre-rendered cinematic that scrubs with scroll.

Do not load it for ordinary reveal-on-scroll, dashboard animation, simple parallax, or a few GSAP sections. Those belong to `motion-direction`.

The key idea is:

> **the camera/media owns the motion; scroll owns time.**

The page should not fake a complex continuous camera move by piling independent DOM animations on top of each other when a pre-rendered media chain would produce more coherent spatial motion.

## 1. Choose the Right Rendering Strategy

Before building, choose the mechanism that matches the experience.

### DOM / CSS / Motion / GSAP

Use when:
- the experience is mostly text, layout, masks, opacity, transforms and pinned sections;
- elements must remain semantic and interactive throughout the animation;
- the camera illusion is simple enough to construct from layers.

### Pre-rendered scroll-scrubbed media

Use when:
- the visual depends on a continuous 3D/cinematic camera move;
- scene-to-scene spatial continuity matters more than live scene interactivity;
- generated/rendered video can carry lighting, parallax, depth and complex geometry more reliably;
- a still fallback can preserve meaning under reduced motion.

### Real-time WebGL / Three.js

Use when:
- users must directly manipulate the 3D world;
- the camera/object state depends on live input or data;
- the performance budget and team/tooling justify a real-time renderer.

Do not choose WebGL simply because the result should look cinematic. A pre-rendered scrub chain is often cheaper, more deterministic and easier to art-direct.

## Ten Billion Years audited real-time anchor

Audited profile: `../../design-intelligence/sites/cosmos-10-billion-years-opus5.vercel.app.md`

Ten Billion Years demonstrates a real-time scroll-world variant where **scroll owns time but one live world owns the visual state**.

### Weighted Narrative Timeline

Instead of giving every chapter equal scroll distance, store a weight for each beat and normalize cumulative bounds. More important or slower beats receive more dwell.

A strong implementation contract is:

```text
chapter config
  -> normalized weighted bounds
  -> one progress value 0..1
  -> local chapter progress
  -> delayed/eased transform window
```

Hold the readable state long enough before morphing toward the next one. Continuous transformation with no dwell makes every chapter feel transitional and leaves no moment to land.

### Shared Progress Bus

Use one authoritative progress signal to coordinate:
- renderer stage/morph;
- camera/FOV;
- procedural background;
- DOM chapter visibility;
- HUD elapsed/progress state;
- chapter navigation;
- post-processing;
- continuous audio mix;
- sparse narrative cues;
- final/payoff mode.

Scroll velocity may exist as a secondary energy signal, but it must not become a second story clock.

### One world, analytic states

When many chapters share one procedural basis, avoid duplicating one complete scene/particle buffer per chapter if the stage can be synthesized analytically.

A compact basis can feed many shader states:
- one base position field;
- one alternate structural field;
- direction/identity/random attributes;
- local density or another meaningful scalar;
- stage uniforms;
- one primary draw call.

This is not mandatory for every experience. Use it when many states share enough physical structure that analytic synthesis reduces memory/upload cost and increases art-direction control.

### Two-layer renderer

A practical real-time scroll world can separate:
- a fullscreen procedural atmosphere/background;
- a foreground geometry/particle world.

This lets background nebula/stars/glow remain cheap and continuous while the foreground owns the semantically important morph.

### Adaptive Renderer Budget

Do not treat the launch-time device tier as the final performance decision.

Combine:
- initial DPR/detail cap;
- live frame-quality feedback;
- bounded DPR floor/ceiling;
- post-FX/detail quality factor;
- safe fallback when performance remains poor.

The Ten Billion Years audited implementation caps DPR around `1.75`, can fall toward `0.85`, and adjusts a separate quality factor. The exact numbers are reference evidence, not defaults.

Preserve semantic story state when quality drops. Reduce particles/post-FX/resolution before removing narrative chapters, copy, navigation, or required controls.

### Procedural score as a state layer

When sound materially improves the journey, treat it like another authored state channel rather than a background MP3 pasted onto the experience.

Useful architecture:
- explicit sound opt-in;
- continuous synthesized/looped bed;
- stage-dependent mix targets;
- sparse semantic one-shots at important events;
- mute control;
- silence path with full narrative meaning.

Sound must remain optional. Core understanding and navigation cannot depend on hearing it.

## Ten Billion Years audited real-time anchor

Audited profile: `../../design-intelligence/sites/cosmos-10-billion-years-opus5.vercel.app.md`

Ten Billion Years demonstrates a real-time scroll-world variant where **scroll owns time but one live world owns the visual state**.

### Weighted Narrative Timeline

Store a weight for each narrative beat and normalize cumulative bounds instead of giving every chapter equal scroll distance.

```text
chapter config -> normalized weighted bounds -> progress 0..1 -> local chapter progress -> delayed/eased transform window
```

Hold readable states long enough before morphing toward the next one. Continuous transformation with no dwell makes every chapter feel transitional.

### Shared Progress Bus

Use one authoritative progress signal to coordinate renderer stage/morph, camera/FOV, procedural background, DOM chapter visibility, HUD, navigation, post-processing, audio mix, sparse cues, and final/payoff mode.

Scroll velocity may be a secondary energy signal, but it must not become a second story clock.

### One world, analytic states

When many chapters share one procedural basis, avoid duplicating one full geometry scene or target buffer per chapter if stage state can be synthesized analytically in the shader.

A compact basis can include base position, alternate structure, direction/identity/random attributes, local density, and stage uniforms. Use this only when the shared basis is real and improves memory/draw cost or authorship.

### Two-layer renderer

A useful real-time scroll world can separate a fullscreen procedural atmosphere/background from a foreground geometry/particle world. Background nebula/stars/glow remain cheap and continuous while the foreground owns the semantically important morph.

### Adaptive Renderer Budget

Combine initial DPR/detail caps with live frame-quality feedback, a bounded DPR floor/ceiling, a post-FX/detail quality factor, and a safe fallback.

The Ten Billion Years audited implementation caps DPR around `1.75`, can fall toward `0.85`, and exposes a separate quality factor. Treat those numbers as reference evidence, not defaults.

Reduce particles/post-FX/resolution before removing chapters, copy, navigation, or required controls.

### Procedural score as a state layer

When sound materially improves the journey, treat it like another authored state channel rather than a background MP3. Use explicit opt-in, continuous synthesized/looped layers, chapter-dependent mix targets, sparse semantic one-shots, a mute control, and a complete silence path.

Sound must remain optional; core understanding and navigation cannot depend on hearing it.

## 2. Define the Journey Before Assets

Write the narrative as ordered beats.

For each scene/beat capture:
- id / label;
- subject: what exists in the scene;
- focal point: what the camera moves toward;
- purpose: what this beat explains, proves or makes the visitor feel;
- headline/body/CTA if copy appears here;
- expected dwell importance;
- transition destination.

A useful cinematic journey usually has a small number of strong beats rather than many weak ones. Each beat should advance the story, not just show another pretty environment.

Also define:

- **brand/world style** — palette, light, material, texture and rendering character;
- **camera grammar** — how the camera behaves within scenes and at handoffs;
- **desktop composition**;
- **mobile strategy**;
- **reduced-motion story**;
- **generation/render budget** when external rendering costs money.

If an external generation pipeline incurs credits or pay-per-render cost, estimate the run before spending and obtain approval for that spend. Previsualization is preferable to discovering the journey is wrong after final-quality renders.

## 3. Lock the World Style

Cohesion comes from repeated art-direction constraints.

Across every generated/rendered scene preserve:
- the same palette;
- the same light direction/temperature;
- the same material/render character;
- the same camera-family assumptions;
- the same level of detail;
- the same aspect strategy per target device;
- the same rendering/model family when practical.

When prompts generate the world, keep the **shared style preamble semantically identical** across scenes. Only the scene subject/focal content should change.

Do not mix render providers or model families mid-chain casually. Even when boundary position matches, different grain, color, motion or lighting character can create a visible perceptual seam.

## 4. Continuity Contract — Position AND Velocity

A seamless chain requires two kinds of continuity.

### Position continuity

The first frame after a seam must match the actual last rendered frame before it.

When chaining generated video:

- use the **actual rendered boundary frame**, not the original scene still or an approximate recreation;
- extract the boundary from the completed clip;
- feed that rendered boundary into the next leg/connector when the generation system supports it.

A source still can match the same scene semantically while differing enough in pose, lighting or props to produce a visible pop.

### Velocity continuity

Matching pixels are not enough.

If one clip ends moving forward and the next begins by pulling backward, the seam can look like a rewind even when the boundary frame is identical.

Define a **handoff motion contract**:
- each leg settles into a known direction/speed near its final moment;
- the next leg begins by continuing that direction/speed;
- expressive orbits/cranes/lateral moves can happen inside a leg, but the handoff itself remains predictable.

Remember that scrubbed experiences are reversible: visitors can scroll backward. A seam that only feels continuous in the forward direction is still broken. Check the handoff grammar in both directions.

Think of the seam as both:

```text
position(t_end) ≈ position(t_next_start)
velocity(t_end) ≈ velocity(t_next_start)
```

## 5. Pick a Chain Architecture Deliberately

### Architecture A — continuous forward chain

Best for:
- grounded/photoreal environments;
- architecture/hospitality;
- first-person or steadicam walkthroughs;
- journeys that should feel like one uninterrupted take.

Pattern:

```text
scene 1 leg
  last rendered frame
      ↓
scene 2 leg
  last rendered frame
      ↓
scene 3 leg
...
```

The next leg starts from the previous leg's actual final frame.

Avoid forcing every leg toward a wide end frame if that causes a backward camera pull. Let scene content evolve under the forward-motion handoff contract.

This architecture can be sequential to render, but its seam logic is simple and physically coherent.

### Architecture B — scene dive + world connector

Best for:
- isometric worlds;
- miniature/diorama systems;
- map-like journeys;
- stylized worlds where pulling out to travel between islands/locations is part of the visual language.

Pattern:

```text
dive into scene A
→ connector pulls out / travels
→ dive into scene B
→ connector
→ scene C
```

The reversal from dive-in to pull-out is intentional here. Do not use this architecture for a realistic walkthrough unless that rewind-like rhythm is deliberately wanted.

### Locked-angle variant

For calm isometric/systematic motion, hold one camera angle and let the world travel beneath it. Check angle drift at the end of every generated leg before chaining the next.

## 6. Crossfade Is Insurance, Not a Fix

A short seam crossfade can hide:
- codec softness;
- tiny render drift;
- small exposure/grain differences.

It cannot hide:
- a different composition;
- missing/changed props;
- a camera teleport;
- a large geometry mismatch.

Never substitute crossfade for actual-frame handoff.

## 7. Previsualize Before Expensive Final Rendering

If generation is slow or billed:

1. build the complete story/scene chain at a cheap draft resolution/model/tier that preserves the same continuity mechanism;
2. inspect journey pacing, scene order, camera grammar and seams;
3. revise the story while changes are cheap;
4. render final-quality assets only after the chain itself works.

The important property of a previz model is not beauty. It must preserve the same **handoff capability** used by the final chain.

If a renderer cannot condition the next clip on the required start/end frame, it is not suitable for a seamless chain even if its standalone clips look better.

Provider/model APIs change. Inspect the current schema/capabilities before a paid batch instead of trusting an old command line or model name.

## 8. Media Asset Budget

For a scene-chain architecture with N scenes:

- scene still/poster assets: roughly N;
- scene motion clips: roughly N;
- connector clips for architecture B: roughly N-1;
- motion chain total for B: roughly `2N - 1`;
- a native mobile motion chain can roughly double the video generation work.

Treat these as planning counts, not a provider-specific pricing formula.

Keep all boundary frames, posters and source assets until QA is complete.

## 9. Encode for Scrubbing, Not Normal Playback

Scroll-scrubbed video has different needs from autoplay video.

### Seekability

`video.currentTime` must seek reliably.

Preferred production options:
- serve media with correct HTTP range support;
- or, for short/bounded clips, fetch into Blob/object URLs so media is locally seekable.

Blob loading is robust for small segmented experiences but consumes memory. For long/high-bitrate experiences, prefer proper range-serving and bounded preloading.

### Encoding

General guidance:
- preserve useful native resolution; do not upscale a lower-resolution render;
- remove audio when it is not used;
- use fast-start metadata;
- use a relatively short GOP so seeks do not decode a long run of intermediate frames;
- avoid all-intra encoding by default: it can multiply file size without enough benefit;
- keep encoding settings consistent across segments.

Phone variants usually benefit from:
- lower resolution than desktop;
- a tighter GOP;
- lower bitrate/quality appropriate to the device;
- the same visual source/continuity rules as desktop.

Inspect source resolution before encoding instead of assuming every renderer outputs the requested size.

## 10. Scroll → Time Mapping

The core runtime loop should map scroll position to media time.

Conceptually:

```text
section scroll progress 0..1
        ↓
optional monotone pacing remap
        ↓
target video time 0..duration
        ↓
smoothed/coalesced seek
```

### Per-scene pacing

Important scenes can receive more scroll distance; transit scenes can be brisk.

Prefer **expressive motion inside the rendered clip** and restraint in the scroll-time remap. Clip motion + aggressive easing compound and can make the experience feel over-directed or hard to control.

A `linger`/dwell remap may slow the middle of a scene so copy peaks while the camera settles.

Any time-remap used for a chained segment must preserve the boundaries:

```text
f(0) = 0
f(1) = 1
```

Never change seam frames through easing.

### Runtime update

- read scroll on passive events;
- schedule visual/time updates through `requestAnimationFrame`;
- do not write `currentTime` for tiny changes;
- on constrained decoders, do not issue another seek while `video.seeking` is still true;
- when the decoder becomes free, jump toward the latest target rather than replaying stale queued seeks.

Scroll input can outrun video decoding. Seek coalescing is a correctness feature, not just an optimization.

## 11. Poster and Floating-Scene Treatment

Stills are more than placeholders: they are the startup frame, reduced-motion surface and lazy-load fallback.

When a generated still has a flat background:
- simplest path: match the page background to the still background so no rectangle is visible;
- if the scene should float transparently, use a **border-connected background knockout** rather than deleting every pixel near the background color. A flood fill from the image border preserves interior walls/objects that legitimately share the background hue;
- soften the alpha boundary slightly and retain meaningful contact shadow;
- keep the original solid-background still when it is required as a video-generation start frame.

Do not feed a transparent knockout into a video generator that expects a complete start frame unless the renderer explicitly supports that workflow.

## 12. Load Only What Is Near

Do not eagerly decode every cinematic clip.

Use a small active window:
- current segment;
- previous/next segment;
- optionally one extra neighbor for fast scroll.

Keep still/poster imagery visible while a video segment is not ready.

The poster should match the video's first visible frame closely enough that the handoff from still → video does not flash.

## 13. Mobile Is a Separate Composition Problem

A desktop cinematic squeezed into portrait is usually not a true mobile version.

For high-quality mobile output:
- render or design a native portrait chain;
- preserve the same story/world/style, but recompose framing for 9:16;
- derive mobile boundary frames from the mobile chain itself;
- generate/encode the complete mobile chain consistently rather than mixing portrait segments with cropped desktop segments;
- make the mobile poster match the mobile video's first frame.

A center-cropped landscape encode is an explicit fallback, not an equivalent mobile art direction. If used, state that limitation.

### Mobile scrub hardening

On touch/mobile:
- coalesce seeks aggressively;
- reduce per-frame decorative effects competing with video decoding;
- keep the poster visible until a real video frame paints;
- muted `playsinline` video may need a user-gesture prime on iOS before seeking paints reliably;
- account for safe-area insets;
- do not rebuild scroll geometry for browser URL-bar height-only resizes;
- do recompute on real width/orientation changes;
- use finger-sized navigation/control hit areas.

## 14. Reduced Motion Is a Different Rendering Mode

Under `prefers-reduced-motion`:

- do not load/decode cinematic video unless functionality truly needs it;
- present the scene stills/posters;
- switch between story beats without camera travel;
- remove particles/parallax/scrub motion;
- keep copy, navigation, CTA and narrative order complete.

Reduced motion is not "same flight but faster."

## 15. Runtime Lifecycle Is Mandatory

When adapting a scrub engine into React/Vue/Svelte or any routed application, provide teardown.

Track and clean up:
- scroll/resize/orientation/pointer/touch listeners;
- requestAnimationFrame loops;
- pending fetches with AbortController where practical;
- object URLs created from Blob media via `URL.revokeObjectURL`;
- observers/timers;
- video references and large in-memory blobs;
- framework-specific effects/components.

A cinematic route that leaks videos/object URLs on every navigation is not production-ready.

## 16. Seam-Focused QA

For every seam:

1. navigate/scroll to just before the transition;
2. capture evidence;
3. move just after the transition;
4. capture evidence;
5. compare composition, camera direction, important props and exposure.

Judge continuity primarily by visible composition and motion, not a single pixel metric. Generated video can show texture/detail shimmer while still having a visually correct seam.

Optional pixel metrics are supporting diagnostics, not the acceptance criterion.

Also verify:
- media becomes seekable;
- `currentTime` actually tracks the intended scroll band;
- no segment remains frozen at frame 0;
- copy reaches peak visibility during the intended scene, not on the seam;
- route/nav state follows the nearest story beat;
- console/network show no missing clips.

## 17. Mobile QA

For an explicit mobile cinematic, test:

- portrait viewport;
- landscape/rotation;
- fast flick scrolling;
- slower scroll through each seam;
- CPU-constrained or low-end simulation when available;
- the mobile media variant is actually served;
- native portrait dimensions when native portrait was promised;
- poster → first video frame has no landscape/portrait flash;
- iOS/Safari first-paint behavior when available;
- URL-bar collapse does not jump the page;
- safe-area clearance;
- reduced-motion fallback.

For a desktop-only cinematic, still perform a phone sanity check: useful poster content, readable copy and no overlap.

## 18. Common Failure Diagnosis

### Visible pop at a seam
Likely cause:
- next segment did not start from the actual rendered boundary frame.

Fix:
- extract the real neighboring frame and regenerate/rebuild the handoff.

### Rewind/stutter despite matching frames
Likely cause:
- velocity reversed across the seam.

Fix:
- use a continuous-forward architecture or change the handoff grammar so both sides share direction.

### Video appears frozen at frame zero
Likely cause:
- seeking is unavailable/unreliable or seeks are piling up.

Fix:
- verify range/Blob seekability;
- coalesce seeks;
- use a tighter GOP/lighter mobile asset where necessary.

### Black/blank first video frame on iOS
Likely cause:
- poster hidden before a real frame paints or the muted inline video has never been primed by user gesture.

Fix:
- retain the poster until video paint;
- preserve `muted` + `playsinline`;
- prime after the first touch/pointer gesture.

### Mobile page jumps as browser chrome collapses
Likely cause:
- full layout recomputation on every height-only resize.

Fix:
- relayout on meaningful width/orientation changes, not touch URL-bar height noise.

### Portrait view loses the focal subject
Likely cause:
- desktop chain was simply cropped.

Fix:
- use native portrait composition when quality matters; a crop is only a declared fallback.

## 19. Relationship to Other Modules

Typical profile:

```text
elite-core
+ scroll-world
+ visual-qa
```

Add `reference-first` when recreating a known scroll experience from video/site evidence.

Usually do **not** also load all of `motion-direction` for the same task. `scroll-world` already owns the specialized scroll/camera/media pipeline. Load `motion-direction` only if the page also has a separate motion system outside the cinematic world.

## 20. Source-Specific Notes

This local module is inspired by `oso95/scroll-world`, but intentionally removes hard dependencies on:
- Monid;
- Higgsfield;
- any single video/image model;
- a clay/isometric art direction;
- fixed vendor pricing or dated model flags.

The durable ideas are the story/scene pipeline, frame handoff, position + velocity continuity, architecture choice, scroll-scrub runtime, mobile/reduced-motion handling, and seam QA.

Provider capabilities, model names, pricing and schemas are volatile. Verify them at execution time when an external renderer is actually used.
