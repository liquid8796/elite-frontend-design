# Cosmos implementation regression case study

Review dates: 2026-09-19, rerun QA 2026-09-20

Prompt under comparison:

> build the most impressive interactive scroll-stopping website (deploy to vercel) you can imagine. Make it a '10 billion years' journey: A 3D interactive background reacting to my mouse, moving through the cloud, the collapse, a galaxy, first light, the swelling, the fuel running out, a supernova boom, ending on the word 'you'.

This document compares three original local implementations of the same brief plus a rebuilt ChatGPT Web rerun using the hardened skill. It is a **skill-regression case study**, not a universal model benchmark.

## Deployed references reviewed

Observed on 2026-09-19:

- ChatGPT Web / earlier elite-skill result: historical local source; the same production URL was later overwritten by the rebuilt v3.6 rerun: `https://cosmos-gpt-56-sol-extra-high.vercel.app`
- Codex Ultra result: `https://cosmos-10-billion-years-gpt56sol.vercel.app`
- Claude Desktop / Opus 5 result: `https://cosmos-10-billion-years-opus5.vercel.app`

The local source comparison focuses on objective architecture/art-direction differences that can be encoded into the skill.

## A — ChatGPT Web / earlier elite-skill result

Project label:
`cosmos-gpt-5.6-sol-extra-high`

Observed source shape:
- Vite + Three.js;
- primary implementation concentrated in `src/main.js` and `src/style.css`;
- desktop main particle count around 7,600; mobile around 4,300;
- multiple particle target arrays interpolated on the CPU every animation frame;
- procedural composition uses ordinary runtime randomness;
- render loop, audio, timeline, pointer, UI and event wiring primarily live in one main module;
- bloom, procedural audio, responsive styling and reduced-motion handling exist;
- no comparable explicit experience-spec / implementation-plan / unit-test suite was found in the project root.

This is a real working experience, but its implementation resembles a strong creative-coding prototype more than an authored world system.

## B — Codex Ultra result

Project label:
`cosmos-10-billion-years-gpt56sol`

Observed source shape:
- Next.js + React + Three.js + custom GLSL;
- explicit experience design spec and implementation plan;
- separate modules for journey config/timeline, deterministic geometry, shaders, renderer lifecycle, procedural audio and semantic overlay;
- unit tests for timeline/cues, shaders, geometry, audio profiles and narrative contracts;
- desktop particle tier around 56,000; compact/low-power around 26,000; reduced-motion around 14,000;
- morph states uploaded as GPU attributes and interpolated in the vertex shader;
- deterministic seeded geometry;
- pointer gravity in the shader plus camera parallax;
- one hot render loop owns eased progress/pointer/energy;
- semantic framework UI published at low frequency rather than every frame;
- WebGL work pauses when hidden;
- explicit Three.js/resource cleanup;
- designed WebGL fallback;
- performance tier uses viewport, hardware concurrency and device memory;
- signature supernova combines particle burst, focal star, shockwave, camera shake, overlay flash and audio cue;
- final chapter removes competing HUD before `you.`.

B establishes an important baseline: **experience specification before implementation**, clean subsystem boundaries, GPU-first morphing, deterministic timelines, resilience and testable architecture.

## C — Claude Desktop / Opus 5 result

Project label:
`cosmos-10-billion-years-opus5`

Observed source shape:
- Next.js + React Three Fiber + Drei + Three.js + custom GLSL;
- Lenis for one smooth-scroll system;
- Zustand only for low-frequency semantic UI;
- runtime mutable state outside React for frame-rate data;
- custom modules for chapters, director, procedural particles, audio, runtime, world renderer, sky, camera rig, post FX, overlay, HUD, gate and flash;
- actual typography assets: Instrument Serif, Inter and JetBrains Mono;
- one primary `Points` system / draw call for the story;
- particle budget about 220,000 desktop, 110,000 low-core and 70,000 mobile/reduced;
- runtime PerformanceMonitor adapts DPR roughly between 0.85 and 1.75 and also exposes a post-FX quality factor.

### C's particle/world architecture

Instead of storing a full target-position buffer for all nine stages, the geometry stores a compact basis:

```text
cloud position
spiral-disc position
unit sphere direction
four random/identity values
local cloud density
```

The vertex shader analytically synthesizes the stage-specific state:
- void;
- cloud;
- collapse;
- galaxy;
- first light;
- swelling;
- fuel depletion;
- supernova;
- final remnant / you.

Examples of chapter mechanics in the shader/source:
- collapse spins up while contracting and flattening;
- galaxy rotation varies with radius;
- first light fills an interior body/corona rather than a hollow shell;
- fuel stage pulses while an inert core grows;
- supernova ejecta uses broken/fingered expansion rather than a smooth sphere.

This is **story physics**: motion rules encode the chapter's meaning instead of reusing one generic morph.

### C's procedural cloud

The molecular cloud is not a Gaussian blob with post-effect noise.

The source builds a 64³ ridged-multifractal density field, builds a cumulative density distribution, then importance-samples particle positions from the field.

Resulting principle:

```text
sample the spatial structure
instead of
uniformly place particles and smear them
```

Local density is retained as a particle attribute and affects visual intensity.

### C's temporal direction

The story uses weighted chapter lengths and a dedicated hold fraction before the chapter begins morphing into the next one.

Conceptually:

```text
ARRIVE
→ HOLD
→ TRANSFORM
→ SETTLE
```

The shader then adds a per-particle transition delay so the material pours into the new state instead of changing in lockstep.

This gives both macro pacing and micro temporal texture.

### C's Experience Director

`frameFor(progress)` is effectively a central director.

For the same normalized progress it coordinates:
- stage A/B and transition mix;
- particle size/brightness/colors/hot radius;
- camera position and FOV;
- bloom;
- chromatic aberration;
- sky nebula/glow/star/ring parameters;
- fullscreen flash;
- accent color;
- audio mix targets.

This makes every subsystem describe the same moment.

### C's input grammar

Inputs have different jobs:

```text
scroll      → story time
pointer     → camera + world-space particle push/swirl
tap/click   → travelling shockwave + low audio pulse
chapter rail→ intentional navigation
sound toggle→ audio layer
```

The pointer is unprojected through the active camera into world space so interaction radius scales with the actual camera/world relationship.

Touch tap is distinguished from drag using time/distance thresholds so ordinary scrolling does not accidentally trigger the shockwave.

### C's runtime architecture

One shared rAF/smooth-scroll loop owns:
- raw progress;
- progress velocity;
- secondary world damping;
- pointer damping;
- time;
- narrative audio cues;
- chapter semantic state;
- frame subscribers.

Overlay/HUD animation writes bounded style/text values directly to existing DOM nodes from that shared frame clock rather than re-rendering React at 60 fps.

React/Zustand remain responsible for semantic state such as started, active chapter, muted and ready.

### C's visual composition stack

The result uses several coordinated visual layers:
- the single large particle field;
- a full-screen custom sky shader with domain-warped nebula;
- several procedural star layers;
- central glow;
- supernova shock ring;
- dynamic bloom;
- dynamic chromatic aberration;
- vignette/tone mapping;
- DOM grain/flash;
- camera position/FOV/roll.

Post FX are directed by narrative state rather than left at one static intensity.

### C's sound architecture

The procedural score is richer than a single ambient oscillator bed.

It combines continuous layers:
- drone;
- sub;
- filtered pink-noise wind;
- harmonic pad;
- shimmer;
- generated reverb;

with sparse semantic one-shots:
- collapse;
- ignition;
- implosion;
- supernova detonation;
- arrival;
- interaction pulse;
- final heartbeat.

Chapter progress chooses the mix target; scroll velocity modulates a secondary energy dimension.

### C's narrative and typography

The entry thesis and chapter copy carry specific causal information rather than only poetic labels.

The visual roles are also distinct:
- Instrument Serif for narrative/display;
- Inter for readable body;
- JetBrains Mono for instrumentation/HUD.

The final `you.` arrives first; replay/context appears later as a coda instead of competing with the payoff immediately.

## GPU versus CPU morphing

A conceptually does:

```text
for every particle:
  interpolate XYZ in JavaScript
  mark position BufferAttribute dirty
every frame
```

B moves multiple morph targets to GPU attributes and blends them in the vertex shader.

C pushes the idea further for this specific story:

```text
upload a compact structural basis once
→ analytically derive many stage states in shader
→ apply per-particle transition phase
→ render a very large world in one primary draw call
```

There is no universal requirement to use C's analytic approach, but it provides a higher ceiling when many narrative states share a common procedural basis.

## Deterministic composition

A uses ordinary runtime randomness.

B uses seeded procedural target geometry.

C also uses seeded generation and derives cloud/disk/direction/identity buffers deterministically.

Determinism remains essential for:
- repeatable art direction;
- screenshot comparison;
- regression diagnosis;
- predictable tuning.

## Experience specification before implementation

B is strongest in explicit planning/testing:
- design spec;
- implementation plan;
- technical slices;
- unit-test contracts;
- designed WebGL fallback.

C is stronger in the authored visual-world implementation, but its package exposes build/typecheck rather than a comparable dedicated unit-test suite.

The skill should therefore **combine**:
- B's planning/test/resilience discipline;
- C's world authorship/physics/pacing/performance sophistication.

Do not regress one strength while adopting the other.

## Why C moves the visual ceiling further

The main new lessons beyond B are:

1. **Story physics** — every chapter has mechanics derived from meaning, not only a different target shape.
2. **Analytic state synthesis** — compact attributes can produce many states without N full morph buffers.
3. **Structured procedural sampling** — spatial fields are sampled from real density structure, producing voids/filaments/clusters.
4. **Experience Director** — camera, FOV, post-FX, sky, geometry, color and audio share one authored frame state.
5. **Temporal staging** — weighted dwell/hold plus per-particle stagger makes transitions land rather than constantly morph.
6. **Input grammar** — scroll, pointer, tap and sound each have a separate physical role.
7. **World-space pointer forces** — interaction remains spatially coherent as camera scale changes.
8. **Adaptive runtime quality** — performance feedback changes DPR/effect quality after launch, not only at initial device detection.
9. **Narrative specificity** — emotional payoff is earned through causal/domain-specific copy.
10. **Actual typography assets** — a deliberate font system improves perceived authorship.
11. **Dynamic post-FX** — bloom/chroma/FOV/flash become event/story channels, not permanent decoration.
12. **Continuous score + semantic cues** — sound itself has a narrative architecture.

## Skill changes derived from this case

The root router should continue to send strong ambition signals to `experience-engineering`.

The implementation contract now requires or strongly considers:

1. Experience Spec before coding;
2. technical-slice implementation plan;
3. rendering architecture appropriate to the visible promise;
4. world mechanics / story physics for chaptered experiences;
5. GPU-first large-system work when appropriate;
6. analytic stage synthesis when it reduces memory/draw cost and increases expressiveness;
7. structured procedural sampling when the subject needs spatial hierarchy;
8. deterministic procedural art;
9. normalized timeline plus central Experience Director;
10. weighted hold/transform/settle pacing;
11. per-element phase/stagger when organic flow matters;
12. one hot animation-loop owner;
13. low-frequency semantic framework state and shared frame subscribers for presentation;
14. separate progress and velocity/energy signals;
15. deliberate input grammar and world-space interaction;
16. dynamic narrative post-FX;
17. continuous audio bed + sparse semantic cues when sound is justified;
18. static device tiers plus runtime quality feedback for expensive scenes;
19. actual typography/art-direction assets for flagship work where practical;
20. narrative truth/specificity before vague poetic filler;
21. fallback/reduced-motion/cleanup;
22. key-state visual QA;
23. architectural tests where pure contracts are available;
24. one authoritative/calibrated progress domain across layout and semantic story state;
25. browser-level timeline/layout/navigation parity;
26. cross-channel state QA across narrative, HUD, navigation, world and chrome;
27. responsive accessibility snapshots after breakpoint presentation changes;
28. clean-context reruns after synthetic diagnostic probes.

## D — Rebuilt ChatGPT Web result with Elite v3.6

The ChatGPT Web project was rebuilt using the hardened skill and the production URL was reviewed again. The current production deployment at the earlier ChatGPT Web URL now represents this rebuilt run; the original implementation remains historical source evidence, not the current live page.

The rebuild materially raised the implementation ceiling:
- explicit `EXPERIENCE.md`;
- pure journey/frame state;
- deterministic seeded geometry;
- GPU analytic stage synthesis;
- roughly 150k / 80k / 40k particle tiers;
- world-space pointer interaction;
- tap-vs-drag impulse behavior;
- continuous audio bed plus supernova transient;
- adaptive DPR;
- reduced-motion path;
- automatic WebGL fallback;
- semantic HUD/rail/final payoff structure.

Live QA verified:
- Supernova before/peak/after behavior and cue re-arming after rewind;
- mobile 390×844 layout with no horizontal overflow;
- final HUD/rail becoming hidden/inert once final mode actually arrives;
- reduced-motion production rendering;
- automatic WebGL-failure fallback;
- clean real-input runtime health aside from a minor favicon 404.

The rerun also exposed a new integration ceiling.

### Timeline/layout desynchronization

The journey director used abstract chapter weights and `scrollY / maxScroll()`, while rendered DOM sections used `weight × vh` geometry plus a different final-section multiplier.

As a result:
- clicking the `SUPERNOVA` rail item could set the HUD/active rail to Supernova while much of the viewport still showed `THE FUEL RUNS OUT`;
- clicking `YOU` could mark chapter VIII while Supernova copy remained visible and final chrome had not yet entered final mode.

The pure timeline unit tests remained green because the bug lived **between** the timeline and rendered layout.

Permanent regression rule:

~~~text
HUD says chapter X
while visible narrative says chapter Y
= failure
~~~

This case is why v3.7 adds One Progress Domain, Timeline ↔ Layout Synchronization, Navigation Parity QA and Cross-channel State QA.

### Responsive accessibility regression

Desktop exposed the sound toggle as `button "sound off"`, but mobile CSS changed `.sound__label` to `display: none` while the icon bars were `aria-hidden`.

At 390px the accessibility tree therefore exposed an unnamed `button`, even though `aria-pressed` still toggled correctly.

Permanent lesson:

> Responsive presentation changes require a second accessibility-semantic check; desktop accessibility does not prove mobile accessibility.

## What should NOT be copied blindly

Do not turn every creative website into:
- 220k particles;
- React Three Fiber;
- Lenis;
- Web Audio;
- scientific simulation;
- Instrument Serif;
- a density field;
- a cosmic aesthetic.

The regression lesson is:

> choose an architecture that can deliver the promised experience, then author the world deeply enough that its mechanics, pacing, interaction and content all express the brief.

For another brief, the right result may instead be:
- image-first frontend;
- pre-rendered `scroll-world`;
- GSAP DOM choreography;
- instanced 3D objects;
- shaders without particles;
- video + semantic DOM;
- a much simpler interface.

The skill should prevent **under-building and under-authoring**, not force one technology.
