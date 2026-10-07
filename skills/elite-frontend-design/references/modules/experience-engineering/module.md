---
name: experience-engineering
description: High-ambition authored-world frontend engineering for scroll-stopping microsites, WebGL/Three.js experiences, mouse-reactive 3D worlds, cinematic narrative journeys and Awwwards-style launches. Combines renderer selection, story physics, GPU-first rendering, central experience direction, temporal staging, deterministic procedural systems, adaptive performance, multisensory cue design, resilience and key-state QA.
---

# Experience Engineering

Use this module when the brief is not merely "make a polished page" but asks for an **experience**:

- "most impressive";
- "scroll-stopping";
- immersive / cinematic / experiential;
- interactive 3D;
- mouse-reactive background/world;
- WebGL / shaders / particles;
- a narrative journey through time or space;
- an Awwwards-style launch where the visual system itself is the product;
- a signature moment such as explosion, transformation, reveal, world transition or final emotional payoff.

Do **not** use this module for normal dashboards, CRUD apps, ordinary marketing pages, or small motion polish. Those should stay on the lighter profiles.

The core principle:

> **Ambition in the brief must be matched by ambition in the rendering architecture, not by adding more CSS decoration.**

## 1. Prevent the Prototype Ceiling

For high-ambition work, a technically valid prototype is not the finish line.

Common prototype-ceiling symptoms:

- one giant JS component owns rendering, timeline, copy, audio and interaction;
- a modest point cloud plus bloom is treated as a complete "3D universe";
- large particle arrays are rewritten on the CPU every frame even though the transition is shader-friendly;
- random geometry changes on every reload, making QA inconsistent;
- scroll position is read directly inside many unrelated effects instead of through one normalized timeline;
- pointer motion only nudges the camera and does not affect the visual system itself;
- every chapter has the same visual treatment with different copy;
- the "signature event" is only a CSS flash;
- no performance tier, fallback, cleanup or reduced-motion architecture exists;
- there is no explicit visual/story spec before implementation.

If the user asked for "the most impressive" experience and the implementation still resembles a demo/tutorial architecture, stop and redesign the architecture before polishing.

## 2. Write the Experience Spec Before Coding

For a complex experiential prompt, a compact landing-page design contract is not enough.

Write an **Experience Spec** first with these fields:

### Intent
One sentence describing the emotional/narrative goal.

### Experience thesis
What should make someone stop scrolling and remember this experience?

### Story arc
List the ordered beats or chapters.

### World mechanics
For each beat, name the physical/visual logic that makes the world behave differently — collapse, orbit, flow, expansion, fracture, accumulation, turbulence, crystallization, diffusion, attraction, repulsion, or another domain-specific mechanism.

### Temporal direction
Define chapter weights/dwell, what must **hold** long enough to read, what transforms, what settles, and where the signature event peaks.

### Visual world
Palette, lighting, material, atmosphere, typography roles and image/render character.

### Rendering architecture
Choose DOM/CSS, timeline animation, pre-rendered scrubbed media, real-time WebGL, or a deliberate hybrid. State why.

### Interaction thesis
What do scroll, pointer, touch and optional sound each control?

### Signature event
Define the single highest-impact transformation/reveal and its synchronized layers.

### Performance budget
Desktop/mobile/reduced tiers, DPR cap, particle/object budgets, draw-call expectations, network/media expectations and hot-path rules.

### Quality feedback
Decide whether static tiers are enough or whether the runtime should monitor frame quality and adapt DPR/post-processing/detail live.

### Resilience
WebGL failure, reduced motion, mobile input, sound unavailable, hidden tab, resize/orientation.

### Progress domain
Define one authoritative mapping between user navigation/scroll and semantic story progress. State which source owns chapter boundaries and how DOM layout, renderer state, HUD, rail/navigation, audio cues and final-mode state derive from it or are explicitly calibrated to it.

Do not allow timeline weights, CSS section heights and `scrollY / maxScroll()` to become independent clocks.

### Spec-to-Implementation Traceability
For every material Experience Spec promise, name:
- the implementation owner/subsystem;
- the observable QA evidence;
- any deliberate fallback or reduced-quality behavior.

A flagship spec is not complete merely because the document sounds premium. Every promised behavior needs an implementation owner and a proof path.

### QA storyboard
Name the key states that must be inspected before signoff.

Do not start coding until this spec is coherent enough that two engineers would build approximately the same experience from it.

## 2A. Plan the Experience in Technical Slices

Do not implement an ambitious experience as one giant creative coding pass.

Turn the Experience Spec into an ordered technical plan whose subsystems can be verified independently.

A useful sequence for a real-time narrative experience is:

1. **timeline/config** — chapter boundaries, progress model and replayable one-shot cue semantics;
2. **procedural geometry/data** — deterministic shape targets and reusable buffers;
3. **shaders/renderer** — visual morphing, pointer forces, focal objects, event geometry and lifecycle;
4. **audio** — optional pure control profile + disposable runtime engine;
5. **semantic overlay** — entry, narrative typography, progress/sound controls, final payoff;
6. **responsive/resilience** — mobile tier, reduced motion, WebGL fallback and visibility behavior;
7. **deployment + key-state QA**.

For each slice:
- define inputs/outputs;
- keep browser-independent logic pure when possible;
- implement it completely enough to integrate;
- run the relevant test/build/visual check before moving to the next slice.

This sequencing prevents a monolithic file from becoming the only place where story, renderer, audio and UI behavior can be understood.

## 2B. Test Architecture Contracts, Not Only DOM Output

High-ambition creative work still benefits from deterministic tests.

Useful contracts include:
- exact chapter-boundary resolution;
- normalized interpolation clamping;
- one-shot cue firing and re-arming after rewind;
- deterministic procedural geometry for a fixed seed;
- shader source contains the uniforms/attributes required by the architecture;
- audio profile loses/gains energy at intended narrative phases;
- semantic entry/final copy exists in the rendered document;
- cleanup/fallback functions are reachable;
- browser-level timeline/layout/navigation parity at representative chapter boundaries.

Do not try to unit-test whether the site is "beautiful." Test the architectural invariants that allow beauty and interaction to remain stable while iterating.

Visual quality is then verified through the QA storyboard in the browser.

## 2C. One Progress Domain and Timeline ↔ Layout Synchronization

A pure timeline can be mathematically correct while the integrated experience is wrong.

For any scroll/chapter-driven experience, define **one progress domain** that owns semantic story position. Keep these channels synchronized:

- visible narrative chapter;
- Experience Director / renderer stage;
- HUD/instrumentation;
- chapter rail or navigation;
- audio phase and one-shot cues;
- final/payoff mode;
- URL/deep-link state when present.

At a named chapter boundary, these channels must agree.

~~~text
visible narrative = chapter X
HUD              = chapter X
navigation       = chapter X
world/director   = chapter X
audio            = chapter X
~~~

If the HUD says chapter X while the visible narrative is still chapter Y, the experience has failed even if both subsystems pass their own unit tests.

### Choose one synchronization architecture

**A. Timeline drives layout**

Derive section lengths/anchors from the same normalized chapter config used by the director.

**B. Layout drives navigation anchors**

Measure actual rendered chapter geometry and map those anchors back into the director's semantic progress.

Either architecture can work. Do not independently combine:
- abstract chapter weights;
- CSS viewport-height multipliers;
- `scrollHeight - innerHeight`;
- sticky offsets;
- special-case final section heights;

without an explicit calibration layer.

### Navigation anchors are part of the contract

A chapter jump must land where the chapter is actually readable, not merely at the mathematical start of its abstract timeline segment.

For every named jump control test:

~~~text
activate chapter X
→ settle
→ visible copy = X
→ HUD = X
→ active navigation = X
→ world/director = X
~~~

Natural scroll and intentional jump navigation should converge on the same semantic state.

### Resize/orientation recalibration

If viewport changes alter scroll geometry, recompute the mapping immediately. Do not wait for the next user scroll event to repair stale story progress.

## 3. Rendering Architecture Gate

Choose the renderer based on the experience, not habit.

### DOM / CSS / Motion

Use when:
- hierarchy/copy/components are the main experience;
- motion is transforms, masks, fades, layout transitions or sticky storytelling;
- semantic interactivity must remain native DOM.

### GSAP / timeline-driven DOM

Use when:
- pinned sequences, scrubbed transforms, masks and coordinated section choreography are sufficient;
- the illusion does not require tens of thousands of independently moving elements or true 3D spatial interaction.

### Pre-rendered scroll-scrub media

Route to `scroll-world` when:
- the key value is a continuous cinematic camera journey;
- complex geometry/lighting is better rendered offline;
- scroll primarily controls time.

### Real-time WebGL / Three.js

Use when:
- the background/world must react continuously to pointer/touch;
- geometry/state must morph from scroll in real time;
- live shader effects are part of the art direction;
- user input changes spatial forces, particles, camera or material state;
- the experience needs runtime-generated visuals rather than a fixed film.

### Hybrid

Use intentionally when, for example:
- WebGL owns the world;
- semantic DOM owns narrative copy/controls;
- Web Audio owns sound;
- CSS owns grain/vignette/flash overlays.

Do not build the same concern in multiple systems without a reason.

## 4. Quality Floor for Real-Time WebGL Experiences

If the selected architecture is real-time WebGL and the visual is central, the renderer itself must carry the art direction.

A strong baseline usually includes several layers, not one particle system:

1. **primary field/system** — particles, geometry or instanced objects that encode the narrative transformation;
2. **background depth** — far stars, atmospheric field, parallax layer or environmental depth;
3. **hero/focal object** — star, product, portal, planet, architectural object or other semantic center;
4. **material/shader identity** — custom shader behavior or material logic that makes the world specific to this brief;
5. **event geometry/effect** — shockwave, burst, fracture, transformation, trail, ripple, field distortion or other signature event;
6. **atmosphere/compositing** — restrained glow, vignette, fog, grain, color cadence, nebulae or overlays;
7. **semantic overlay** — copy and controls outside the renderer where possible.

Built-in Three.js materials are useful, but a visually ambitious WebGL brief should not rely on stock material defaults as its complete visual language.

## 4A. Authored World Systems — Story Physics

A premium narrative world should not be a generic particle field wearing different colors.

For each chapter, derive motion from the **meaning of the chapter**.

Examples:

- collapse → attraction, compression, spin-up, flattening;
- orbit/galaxy → radius-dependent rotation and arm drift;
- ignition → inward pressure becoming outward radiance;
- depletion → unstable pulsing, contraction, loss of high-frequency motion/light;
- explosion → directional ejecta, broken shell/fingers, shock fronts;
- product assembly → parts attract, align, lock and become one;
- logistics → routing, convergence, handoff and flow;
- finance → accumulation, branching, risk diffusion or compounding;
- biology → growth, division, migration, signaling.

The exact mechanics need not be scientifically literal. They should be **causally legible** and specific to the story.

Ask:

> If I removed the chapter title, would the motion itself still suggest what is happening?

If every chapter can be implemented as `mix(shapeA, shapeB)` plus a palette change, the world is probably under-authored.

### Visual physics over decorative adjectives

Prefer:
- behavior rules;
- forces;
- scale relationships;
- spatial constraints;
- stage-specific turbulence;
- differentiated time scales.

over vague prompts such as:
- "make it epic";
- "add more glow";
- "make particles cinematic".

The best creative-code art direction is often encoded as mechanics.

## 5. GPU-First Morphing

For large particle/vertex systems, prefer moving predictable continuous work to the GPU.

### Strong pattern

Generate reusable shape/morph targets once:

```text
aCloud
aCollapse / aSphere
aGalaxy
aBurst
aSeed
...
```

Upload them as geometry attributes.

Then drive transformations with uniforms:

```text
uProgress
uTime
uPointer
uReducedMotion
uPixelRatio
```

and interpolate/morph in the vertex shader.

Benefits:
- much larger particle counts;
- lower JS hot-path cost;
- smoother scroll/pointer response;
- more room for layered visual effects.

### Avoid

Do not mutate tens of thousands of vertex positions from JavaScript every animation frame when the transformation is expressible as shader interpolation.

CPU-side updates are acceptable when:
- the count is genuinely small;
- data comes from live application state;
- the transformation cannot reasonably be expressed in the shader;
- profiling proves it is not the limiting factor.

Architecture should be decided by the required visual density and interaction quality, not by which code is quickest to type.

## 5A. Analytic State Synthesis and Draw-Call Budget

Pre-baking a complete position array for every chapter is simple, but it can become memory-heavy and visually rigid when the story has many states.

When the stages share structure, consider a compact basis:

```text
base/cloud position
disc/flow position
unit direction
seed/random attributes
local density / identity
```

Then derive many stage positions analytically in the shader.

For example:

```text
stagePosition(stage, baseAttributes, time, narrativeParameters)
```

This can support many visually distinct chapters without uploading a full N×3 target buffer for each one.

For large homogeneous particle systems:
- prefer one or a few `Points` / instanced draw calls;
- avoid thousands of individual mesh objects;
- derive variation from attributes/seeds in shaders;
- reuse geometry across the story;
- keep stage-specific logic branchable and bounded.

Do not chase a one-draw-call slogan when multiple materials/depth passes are genuinely needed. The goal is to spend draw calls on visible value.

### Per-element phase creates flow

A globally uniform morph can look synthetic even when the geometry is sophisticated.

Use a per-particle/per-instance seed to offset the local transition window:

```text
localMix = smoothstep(delay, delay + width, globalMix)
```

so matter/objects **flow into the next state** instead of changing simultaneously.

Stagger should preserve the overall story timing; do not make the transition so scattered that the chapter never resolves.

## 5B. Sample Structure, Do Not Merely Smear It

When the brief calls for clouds, smoke-like fields, terrain distributions, crowds, constellations or other spatially structured phenomena, the **sampling strategy** strongly affects quality.

A Gaussian blob plus noise often reads as a fuzzy demo.

When structure matters, consider:
- scalar density fields;
- multi-octave/ridged noise;
- signed distance fields;
- vector fields;
- masks/importance maps;
- blue-noise or Poisson sampling;
- domain-specific distributions.

Then sample particles/instances **from the structure** rather than placing them uniformly and trying to hide the distribution with post effects.

A useful general pattern:

```text
build density/importance field
→ normalize meaningful occupied range
→ sample locations proportional to density
→ preserve local density as an attribute
→ use density for color/brightness/behavior
```

This produces real voids, filaments, clusters and hierarchy.

Use this technique only when it improves the visual subject. A button explosion does not need a 64³ density field.

## 6. Deterministic Procedural Geometry

For procedural experiences, use seeded generation where practical.

Determinism makes:
- screenshots comparable;
- visual QA repeatable;
- regressions diagnosable;
- mobile/desktop tuning easier;
- the same composition survive reloads.

Randomness can still animate or vary detail, but core composition should not unexpectedly become better or worse on refresh.

Treat the seed as part of the art direction when the composition matters.

## 7. Narrative Timeline as a Pure Model

Do not scatter chapter boundaries across CSS, DOM, audio and WebGL code.

Define one timeline/config model:

```text
chapter
start
end
time label
kicker
title
accent
visual cues
audio cues
```

Then expose pure helpers such as:

```text
resolveFrame(progress)
chapterProgress
cue controller
```

The timeline should not require browser APIs to test.

Scroll produces a normalized progress value; the renderer, UI and audio consume that normalized state.

This separation prevents the visual system from becoming a collection of unrelated scroll handlers.

## 7A. Add an Experience Director

A timeline tells you **where** the visitor is. A director tells every subsystem **how the world should read at that point**.

For high-ambition experiences, derive one shared `FrameState` / director output from normalized progress.

A director may contain:

```text
stage A / stage B / mix
camera position + FOV
particle/material parameters
palette / hot color / accent
bloom / chromatic aberration / vignette intensity
sky / fog / atmosphere
glow / shock ring / flash
pointer-force parameters
audio mix targets
semantic accent / chapter identity
```

Then renderer, camera, sky, post-FX, audio and overlay read the **same authored state**.

Conceptually:

```text
progress
   ↓
timeline
   ↓
Experience Director
 ┌───────┬───────┬────────┬───────┬───────┐
 GPU   camera    sky     postFX   audio   DOM
```

Benefits:
- transitions stay synchronized;
- chapter tuning is centralized;
- one edit can retime/recolor/reframe a beat coherently;
- consumers cannot silently invent conflicting interpolation.

Keep the director allocation-light. Reuse state/scratch objects in hot paths when appropriate.

### Post-FX should be directed, not permanently "on"

Bloom, chromatic aberration, shake, flash, distortion and vignette are narrative channels.

A restrained baseline plus short authored spikes is usually stronger than running every effect at maximum throughout the experience.

For example:
- quiet chapter → low bloom/chroma;
- ignition → brief exposure/bloom hit;
- failure/depletion → reduced saturation/energy;
- explosion → bloom + chroma + FOV/shake spike;
- final state → effects settle and visual noise recedes.

## 7B. Temporal Staging — Hold → Transform → Settle

Continuous scroll does not require continuous transformation.

If every pixel of scroll is morphing the world, the visitor never gets a stable moment to perceive what they reached.

For each chapter define:
- **arrival**;
- **hold/dwell**;
- **transformation window**;
- **settle/handoff**.

A useful chapter mapping can reserve an initial fraction for hold, then map the remaining range to a smootherstep transformation.

Example:

```text
chapter local progress
0.00 -------- 0.42 ---------------- 1.00
      HOLD          TRANSFORM
```

The exact fraction is art direction, not a constant.

Important beats may also receive larger scroll weights.

The principle:

> Let a scene become readable before asking it to become the next scene.

Combine macro pacing with per-element stagger carefully:
- chapter hold creates comprehension;
- per-element delay creates organic transition;
- final settle creates a clean next state.

## 8. One Hot-Path Animation Loop

High-end experiences should have one clear real-time owner.

Preferred pattern:

1. scroll/pointer events update **targets only**;
2. one `requestAnimationFrame` loop eases target values;
3. the loop updates renderer uniforms/camera/effects;
4. React/framework state is published only at low frequency when semantic UI actually changes;
5. audio receives bounded/throttled control values.

Do not:
- set React state every animation frame;
- allocate new large objects in hot paths;
- attach multiple independent scroll loops that compete;
- make layout reads/writes bounce across several subsystems each frame.

For React:
- refs own hot mutable values;
- state owns semantic UI;
- Three.js resources live outside React render cycles.

### Shared frame subscribers

If overlay/HUD elements need to move at frame rate, they may subscribe to the same shared animation clock and write bounded style/text changes directly to existing DOM nodes.

This can be cleaner than:
- publishing progress to React 60 times/sec;
- creating separate requestAnimationFrame loops for each overlay.

Keep React/state for semantic changes such as:
- active chapter;
- started/muted/ready;
- fallback state.

Use direct per-frame DOM writes only for presentation values that genuinely need frame synchronization.

### Input smoothing and world inertia are separate

A smooth-scroll engine can improve wheel/touch input, but the **world may still need its own damping**.

Useful separation:

```text
raw wheel/touch
→ one smooth-scroll engine
→ normalized page progress
→ secondary world damping
→ director/render progress
```

This slight trailing inertia can make a fast flick feel like continuous camera/world motion rather than a jump cut.

Do not stack multiple smooth-scroll libraries. One input scroller plus deliberate renderer damping is enough.

## 9. Scroll Progress and Scroll Energy Are Different Signals

Narrative position and interaction intensity are not the same thing.

Use:
- **progress** — where the visitor is in the story;
- **scroll energy/velocity** — how energetically they are moving.

Progress can drive:
- chapter/state;
- morph target;
- palette;
- focal object;
- copy.

Energy can modulate:
- turbulence;
- audio intensity;
- secondary trails;
- transient distortion;
- subtle camera response.

Do not let scroll velocity accidentally change which story chapter the user is in.

## 10. Pointer Interaction Must Reach the World

For a prompt that explicitly asks the 3D background to react to the mouse, pointer response should be more than a generic camera offset.

Possible bounded reactions:
- local gravity/repulsion field;
- particle curl/turbulence near pointer;
- material highlight/fresnel response;
- camera parallax;
- field rotation;
- lens/ripple distortion;
- attraction of a focal cluster.

Keep it bounded and eased.

Good interaction feels like the world notices the pointer.

Bad interaction feels like the entire canvas is loosely attached to the cursor.

On coarse-pointer/touch devices, use a deliberate fallback:
- autonomous drift;
- touch location influence;
- device orientation only with explicit permission and a real benefit.

## 10A. Design an Input Grammar

Different inputs should have distinct jobs.

For example:

```text
scroll / wheel → narrative time
pointer move   → local field + camera parallax
tap / click    → impulse / shockwave / pulse
sound control  → audio layer
chapter rail   → intentional navigation
```

This makes the experience feel interactive rather than merely reactive.

### Prefer world-space pointer interaction when camera scale changes

Normalized device coordinates are useful input, but if the camera travels or zooms substantially, a fixed NDC-radius force can feel inconsistent.

When appropriate:
1. unproject the pointer through the active camera;
2. intersect/project it onto the relevant world plane/volume;
3. scale the interaction radius/force from camera distance or world scale;
4. feed that world-space point to the shader.

The result is an interaction footprint that remains perceptually consistent as the camera moves.

### Touch: distinguish tap from drag

Do not trigger a click/tap effect on every `pointerdown` if the same gesture may become a scroll.

For touch/coarse input:
- record down time/position;
- wait for pointer-up;
- reject long gestures;
- reject movement beyond a small threshold;
- ignore taps on buttons/links;
- only then fire the world impulse.

This prevents scroll gestures from accidentally exploding the scene.

## 11. Design Chapter-Specific Visual States

Each chapter should change more than text.

For every beat define a **scene state**:

| Dimension | Ask |
|---|---|
| Geometry | What shape/system does the world become? |
| Scale/depth | Does it collapse, expand, disperse, orbit, recede? |
| Palette/light | What color/energy state communicates this beat? |
| Camera | Where is the viewer and how stable is the camera? |
| Pointer response | Stronger, weaker, attractive, repulsive, locked? |
| Atmosphere | Fog, field, glow, grain, nebula, silence? |
| Typography | Left/right/center, display mode, copy amount? |
| Audio | What harmonic/energy state exists? |
| Transition | What physically connects this state to the next? |

A chaptered experience should feel like one evolving system, not eight slides with the same background.

## 12. Signature Event Must Be Multilayered

If the brief contains a signature event such as a supernova, impact, reveal or transformation, synchronize multiple channels.

Example layers:
- geometry burst/morph;
- focal-object scale/material shift;
- shockwave/ring;
- palette/lighting change;
- camera impulse/shake;
- compositing flash/glow;
- sound transient/bass/noise;
- UI/copy timing.

Not every event needs every layer, but a major moment should not depend on one CSS animation.

Use a cue controller so one-shot events:
- fire once when crossing the threshold;
- do not stack repeatedly while staying beyond the threshold;
- can re-arm after the visitor rewinds far enough when reverse-scroll replay is meaningful.

## 13. Typography Is Part of the Cinematography

Experiential sites often benefit from two textual roles:

- **narrative display** — emotional, editorial, expressive;
- **instrumentation/meta** — time, coordinates, progress, sound state, technical labels.

Use typography to distinguish those roles.

Do not automatically use:
- giant all-caps sans for every chapter;
- generic website hero copy;
- nav/footer/CTA patterns when the experience is meant to feel like a film.

If the brief ends on one word such as `you.`, remove competing HUD/chrome before the payoff. The final frame deserves a designed silence.

Copy should be sparse enough that visitors can read it without pausing the visual story.

### Use actual type assets for flagship work

For a flagship experiential piece, do not rely on a generic fallback stack when an intentional font pairing is feasible.

A strong pattern is:
- expressive display/serif or distinctive grotesk for narrative statements;
- neutral sans for readable body copy;
- mono/technical face for instrumentation/time/progress.

Load the actual fonts through the repository's normal asset/font system. Preserve performance and licensing constraints.

Typography can materially separate an authored experience from a competent technical demo.

## 13A. Narrative Truth Before Poetry

High-end narrative copy should be **specific enough to earn the emotion**.

Avoid a sequence made only of vague lines such as:

```text
matter awakens
light remembers
everything becomes everything
```

unless abstraction is the explicit art direction.

Prefer a causal spine:

```text
what happened
→ why it changed
→ what that means
→ why the visitor should care
```

Domain truth can be scientific, product-specific, cultural, mechanical, spatial or fictional-world logic.

For the experience spec, write one sentence per chapter answering:

> What new fact or causal transformation does this beat contribute?

Then compress that truth into readable on-screen copy.

This produces emotional payoff through accumulated meaning rather than decorative profundity.

For fact-based subjects, verify important claims when freshness/accuracy matters.

### Payoff first, utility later

The final frame may be intentionally empty except for the payoff.

If replay/CTA/context is useful, reveal it **after** the payoff has had time to land rather than competing with it immediately.

## 14. Sound Can Multiply the Experience

Audio is optional, but when the brief is cinematic it can materially increase perceived quality.

If using audio:
- require an explicit user gesture before audible playback;
- keep the experience complete when muted;
- use Web Audio or properly licensed/local assets;
- treat audio as another timeline consumer;
- map chapter state and optional scroll energy to bounded audio parameters;
- create one-shot event cues for signature moments;
- provide a persistent accessible mute/sound control;
- suspend/pause expensive audio work when the document is hidden;
- dispose the graph on teardown.

Do not block the visual experience if audio initialization fails.

### Continuous bed + sparse semantic cues

A sophisticated score often works best as two systems:

1. **continuous bed** — drone/noise/pad/shimmer/sub layers whose target mix is interpolated by the Experience Director;
2. **semantic one-shots** — a small set of cues fired at meaningful causal moments.

Possible one-shots:
- collapse swell;
- ignition bell/chord;
- impact;
- implosion;
- detonation;
- arrival;
- final heartbeat/motif.

Scroll velocity may modulate a secondary parameter such as shimmer, wind or distortion, while chapter progress controls the actual harmonic state.

Use motifs sparingly. The visitor should feel progression, not a sound-effect checklist.

## 15. Performance Tiering Is Part of the Design

Do not build desktop spectacle and hope mobile survives.

Choose deterministic performance tiers using signals such as:
- viewport size;
- `deviceMemory` when available;
- `hardwareConcurrency`;
- reduced-motion preference.

Examples of tiered parameters:
- particle/object count;
- geometry detail;
- DPR cap;
- antialiasing;
- postprocessing;
- secondary atmosphere layers.

Rules:
- cap DPR instead of blindly rendering at devicePixelRatio 3–4;
- reuse buffers/geometries/materials;
- avoid per-frame allocation;
- avoid unnecessary postprocessing if shader/material composition already produces the look;
- pause rendering when the document is hidden;
- do not run decorative effects at full cost on low-power devices.

For greenfield high-end WebGL, define the performance budget in the spec before implementation.

## 15A. Adaptive Runtime Quality

Static device tiers are only the starting point.

A device that looks powerful on paper can still miss the target frame rate because of:
- thermal throttling;
- browser/GPU differences;
- high refresh rate;
- expensive postprocessing;
- embedded/webview constraints.

For demanding experiences, consider a lightweight runtime performance monitor.

It can adapt, within bounded quality ranges:
- DPR;
- post-processing quality/radius;
- secondary atmosphere layers;
- shadow/reflection resolution;
- nonessential effect density.

Prefer reducing **resolution/effects** before changing the core narrative composition mid-session.

A useful principle:

> preserve the world, lower the rendering cost.

Avoid continuously oscillating quality. Use hysteresis, slow adjustments or a library/runtime monitor that already handles this well.

If runtime quality falls back, QA that fallback state too.

## 16. Failure and Reduced-Motion Architecture

### WebGL failure

Provide a designed fallback that still communicates:
- the full story;
- chapter transitions;
- final payoff;
- controls/copy.

Do not leave a black canvas with console warning as the fallback.

### Reduced motion

Reduced motion should:
- preserve narrative state;
- reduce camera movement, explosive travel and constant drift;
- use restrained morph/crossfade;
- keep major copy and final reveal intact.

It should not simply disable every visual and leave the experience empty.

### Hidden tab

Stop or suspend:
- animation loop;
- audio modulation;
- expensive timers.

Resume cleanly when visible.

## 17. Lifecycle and Resource Cleanup

Production WebGL is not complete without teardown.

Dispose/remove:
- animation frame;
- scroll/pointer/resize/visibility listeners;
- WebGL context listeners;
- geometries;
- materials;
- textures;
- render targets/composers;
- audio nodes/context where owned;
- timers;
- observers;
- Blob URLs/media when used.

A route that leaks a renderer on each navigation is not premium frontend engineering.

## 18. Do Not Let Framework Choice Dilute the Experience

Next.js/React/Vite/vanilla are implementation shells, not the source of quality.

The architecture can be excellent in any suitable stack.

When using React/Next:
- dynamically load browser-only heavy visual code when appropriate;
- keep SSR/semantic overlay separate from WebGL lifecycle;
- do not push renderer state through React every frame.

When using vanilla:
- modularize timeline/render/audio/input even without framework components;
- do not put the entire experience into one giant file merely because there is no framework.

High-end work needs conceptual boundaries even if the runtime is simple.

## 19. Implementation Complexity Must Match the Brief

When the user says:
- "the most impressive you can imagine";
- "10/10";
- "Awwwards";
- "scroll-stopping";
- "3D interactive";
- "cinematic";

do not optimize for the shortest implementation.

This does **not** mean add complexity blindly.

It means:
- spend complexity on the renderer and signature interactions that produce visible value;
- keep UI chrome simple;
- avoid unnecessary libraries;
- build one coherent visual system deeply instead of many shallow gimmicks.

A 500-line sophisticated renderer can be justified.
Five decorative React component libraries usually are not.

## 20. Build a QA Storyboard Before Signoff

For a chaptered experience, name key visual states before testing.

Example:

```text
00 entry / prelude
01 cloud
02 collapse
03 galaxy
04 first light
05 swelling
06 depletion
07 supernova peak
08 final "you"
```

At minimum inspect:
- entry viewport;
- 2–3 representative middle states;
- signature event before / peak / after;
- final state;
- mobile;
- reduced motion;
- fallback when practical;
- representative chapter navigation parity;
- cross-channel state agreement at the signature event and final payoff.

### Navigation Parity QA

For chaptered experiences, verify at least representative chapter jumps and always the signature event/final payoff.

Test both:
- natural scrolling into the state;
- intentional navigation/rail jump into the same state.

After settle, compare:
- visible chapter copy;
- HUD/status;
- active navigation item;
- renderer/director semantic stage;
- final chrome visibility;
- audio/cue state when observable.

A jump is not correct merely because the active rail item changed.

### Cross-channel State QA

At each key storyboard state, record a compact parity matrix:

| Channel | Expected |
|---|---|
| Narrative copy | chapter/state X |
| HUD/status | X |
| Navigation | X |
| Renderer/world | X |
| Audio | X when applicable |
| Chrome/final mode | expected visibility |
| URL/deep link | X when applicable |

The rows must describe one coherent moment.

### Spec-to-Implementation QA Trace

For QA-3 experiential work, map each material Experience Spec promise to:
- implementation owner;
- evidence state;
- result: verified / partial / blocked.

Missing implementation or missing evidence is not silently treated as complete.

### Temporal QA — inspect motion, not only keyframes

Screenshots prove composition. They do not prove pacing.

For at least one representative chapter transition, observe the full motion sequence:

```text
arrival
→ hold/dwell
→ transformation
→ settle
```

Verify:
- the hold is long enough to read/perceive the state;
- the transition begins intentionally rather than immediately on entry;
- per-element stagger reads as flow rather than random desynchronization;
- the next state resolves cleanly before its own important copy/event;
- fast scroll does not collapse the journey into hard jump cuts;
- slow scroll does not expose awkward dead frames or endless in-between states.

For the final payoff:
- verify the payoff appears before replay/utility/coda;
- verify later utility does not visually dilute the first reveal.

### Input-grammar QA

Exercise each input that has a distinct promised role:
- scroll/wheel → narrative progress;
- pointer move → local world response;
- tap/click → separate world impulse when implemented;
- chapter/navigation control → deliberate jump;
- sound toggle → audio only, without breaking visual state.

For pointer interaction, test at more than one camera scale when the camera moves significantly.

For touch:
- verify dragging/scrolling does not trigger the tap impulse;
- verify a short intentional tap still does.

For scroll threshold events:
- cross forward;
- remain beyond threshold;
- rewind;
- cross again when replay should be allowed.

### Performance-response QA

When adaptive quality exists:
- confirm quality can fall back without changing chapter semantics or composition;
- ensure resolution/effect reductions do not remove the signature interaction;
- avoid visible rapid quality oscillation.

Test pointer response at a meaningful state, not only at the entry screen.

Check console and runtime after the full journey, not only page load.

## 21. Experiential Quality Review

Before calling the experience finished, ask:

### Concept
- Does the experience have one unmistakable thesis?
- Does the final payoff justify the journey?

### Renderer
- Is the visual world richer than a tutorial demo?
- Does GPU work carry the high-density continuous motion where appropriate?
- Do chapters genuinely transform the world?

### Interaction
- Does the pointer affect the world itself?
- Does scroll feel like time/progression rather than section navigation?

### Narrative
- Can the story be understood with sparse copy?
- Does UI chrome disappear when drama requires silence?

### Performance
- Are desktop/mobile/reduced tiers intentional?
- Is the hot path outside framework rendering?
- Are resources cleaned up?

### QA
- Were actual key states rendered and inspected?
- Was at least one complete hold → transform → settle transition observed?
- Were the promised input roles tested independently?
- Was the signature moment tested across its threshold?
- Was adaptive quality/fallback observed when practical?
- Do natural scroll and intentional chapter navigation converge on the same semantic state?
- Do narrative, HUD, navigation, world and final chrome agree at representative chapter boundaries?
- Does the final state remain stable?

If several answers are "no", more styling is unlikely to fix the problem. Revisit the experience architecture.

### Cross-system synchronization regression

The rebuilt ChatGPT Web Cosmos run demonstrated a failure class worth keeping permanently:

- the pure journey/director timeline passed unit tests;
- renderer architecture, fallback and mobile layout were substantially improved;
- but chapter rail navigation used abstract timeline weights while rendered DOM sections used different viewport-height geometry;
- clicking SUPERNOVA could mark the HUD/rail as Supernova while much of the viewport still showed THE FUEL RUNS OUT;
- clicking YOU could mark chapter VIII while Supernova copy remained visible and final chrome had not yet entered final mode.

General lesson:

> A correct director plus a correct layout can still produce an incorrect experience if their progress domains are not synchronized.

The regression condition is explicit:

~~~text
HUD says chapter X
while visible narrative says chapter Y
= failure
~~~

This is why browser integration parity is required in addition to pure timeline tests.

## 22. Cosmos Regression Lessons

The local Cosmos benchmark in `references/benchmarks/cosmos-gpt56-case-study.md` exists to prevent regression toward a lower-ceiling implementation.

The main lessons combine engineering discipline with world authorship:

- design/spec first for ambitious experiences;
- world mechanics / story physics per narrative beat;
- GPU morphing over CPU per-particle morph loops when scale justifies it;
- analytic state synthesis when shared attributes can express many stages;
- structured procedural sampling when spatial hierarchy matters;
- deterministic procedural composition;
- pure/testable narrative timeline plus a central Experience Director;
- hold → transform → settle chapter pacing and per-element phase where useful;
- one animation-loop owner and shared frame clock;
- low-frequency semantic framework state;
- distinct input grammar with world-space interaction when needed;
- static tiers plus adaptive runtime quality;
- dynamic post-FX and synchronized signature events;
- isolated audio engine with continuous bed + sparse semantic cues;
- narrative specificity, real type assets and delayed final coda;
- full cleanup/fallback/reduced-motion behavior.

Do not cargo-cult the exact star aesthetic. Apply the architecture to the actual brief.

## 23. Relationship to Other Modules

Typical profile:

```text
elite-core
+ experience-engineering
+ frontend-qa
```

`frontend-qa` owns the overall functional/visual/accessibility/performance signoff and may use `visual-qa` as its rendered-evidence specialist.

Add `frontend-design` only when art direction needs extra ideation.

Add `motion-direction` only for a distinct DOM/GSAP choreography concern outside the real-time renderer.

Use `scroll-world` **instead** when the defining experience is a pre-rendered continuous camera film scrubbed by scroll.

Use `reference-first` when reproducing a known interactive experience from screenshots/video/source evidence.

Avoid loading all of them simultaneously unless the task genuinely contains those distinct systems.
