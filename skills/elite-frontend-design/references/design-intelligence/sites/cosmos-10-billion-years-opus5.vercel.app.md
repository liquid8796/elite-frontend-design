# Ten Billion Years (Opus 5) - full-site distilled design intelligence

Source: https://cosmos-10-billion-years-opus5.vercel.app/
Audit date: 2026-10-07
Coverage: 1/1 public route

This is a full experience audit of a deliberately single-route scroll world. Whole-site coverage means the complete entry gate, all 9 chapters, the fixed WebGL world, scroll timeline, pointer/touch input, HUD/navigation, procedural score, responsive behavior, reduced-motion mode, adaptive performance system, replay path, and final payoff.

## Prompt provenance

The user states that the page was generated from one creative prompt:

"build the most impressive interactive scroll-stopping website you can imagine. Make it a '10 billion years' journey: A 3D interactive background reacting to my mouse, moving through the cloud, the collapse, a galaxy, first light, the swelling, the fuel running out, a supernova boom, ending on the word 'you'"

Treat that prompt as intent/provenance supplied by the user, not as implementation evidence.

## Coverage evidence

Live audit found:
- one public route: /;
- no same-origin links to additional routes;
- /robots.txt -> 404;
- /sitemap.xml -> 404;
- /sitemap-index.xml -> 404;
- /llms.txt -> 404;
- one canvas;
- zero video elements;
- zero audio elements;
- 9 semantic chapter regions;
- one fixed entry gate;
- one fixed HUD/chapter-navigation system;
- one final replay action.

Desktop audited document after entry: roughly 9.1k px at an approximately 1920x889 viewport.

Mobile audited document after entry: roughly 8.7k px at 390x844 with no document-level horizontal overflow.

## What the prompt became

The strongest lesson is not the cosmic palette or particle effect. It is how a short prompt was compiled into a coherent authored system.

The prompt's nouns/events became states:
1. Before / void;
2. The Cloud;
3. The Collapse;
4. The Galaxy;
5. First Light;
6. The Swelling;
7. The Last Fuel / The Fuel Runs Out;
8. Supernova;
9. You.

The vague requirement "3D interactive background reacting to my mouse" became:
- one real-time WebGL world;
- a pointer-reactive camera;
- world-space particle push/swirl;
- click/tap shockwave response;
- procedural background parallax;
- touch-aware tap-vs-drag discrimination.

The vague requirement "scroll-stopping" became:
- an intentional entry gate;
- a 1029vh weighted scroll track;
- fixed semantic chapter overlays;
- one authored cross-channel director;
- high-energy event peaks;
- chapter navigation and elapsed-years instrumentation;
- optional procedural score;
- a delayed final word and coda.

This is the core Prompt-to-Experience Compile Contract.

## Entry gate

Observed live copy includes:
- TEN BILLION YEARS, IN NINE PARTS;
- Everything you are was somewhere else first.;
- Begin with sound;
- Continue in silence;
- headphone/lights-down hint.

Behavior:
- loading/readiness state initially replaces the sound CTA;
- sound is explicitly opt-in;
- silence is a complete first-class path;
- gate fades away after entry;
- narrative meaning does not depend on audio.

The gate is part of pacing, not merely an autoplay workaround.

## Fixed semantic overlay

The 9 chapter sections do not create normal document height themselves. They are fixed/absolute viewport overlays. A separate invisible scroll track owns vertical distance.

Each chapter:
- occupies the viewport;
- crossfades through opacity;
- translates vertically by a small amount;
- has eyebrow, display title, and narrative copy;
- alternates left/right alignment on desktop for middle chapters;
- centers the first and final chapters.

At <=860px, chapter copy becomes centered and bottom-biased while decorative HUD labels reduce.
At <=640px, the chapter rail is hidden.

## The 9 chapters

### 0. Before

Purpose:
- establish scale: 10,000,000,000 years;
- establish the thesis that the reader's atoms participated in the journey.

State evidence:
- weight 1.00;
- accent #8fa6e8;
- camera near [0, 0, 62];
- low bloom/glow.

### I. The Cloud

Narrative:
- cold hydrogen cloud;
- enormous, sparse, patient;
- nothing yet requires it to become a star.

State evidence:
- weight 1.05;
- accent #7fb2ff;
- camera roughly [0, 22, 232];
- stronger nebula field.

### II. The Collapse

Narrative:
- external shock breaks equilibrium;
- gravity begins winning.

Story physics:
- cloud contracts;
- angular momentum increases spin;
- material flattens toward a disk;
- turbulence remains.

State evidence:
- weight 1.05;
- purple/magenta transition;
- camera roughly [0, 26, 88].

### III. The Galaxy

Narrative:
- collapse produces a galaxy;
- the story searches for one ordinary star.

Story physics:
- particles use a spiral-disc basis;
- angular speed changes with radius.

State evidence:
- weight 1.15;
- gold/cool-blue combination;
- camera roughly [0, 178, 102].

### IV. First Light

Narrative:
- core reaches fusion temperature;
- mass becomes light.

Story physics:
- filled luminous body/corona rather than a hollow shell;
- early flash/glow peak marks ignition.

State evidence:
- weight 1.00;
- bloom around 1.3;
- camera roughly [0, 2, 38].

### V. The Swelling

Narrative:
- long stable burn;
- hydrogen thins;
- core contracts and envelope expands.

State evidence:
- weight 1.00;
- orange/red thermal palette;
- camera roughly [0, 7, 88].

### VI. The Last Fuel

Narrative:
- helium -> carbon -> oxygen -> neon -> silicon -> iron;
- each burning stage gets shorter;
- iron ends the energy-producing chain.

Story physics:
- pulsing/hotter internal state;
- growing inert-core implication.

State evidence:
- weight 1.00;
- deep red/orange palette;
- camera roughly [0, 6, 95].
### VII. Supernova

Narrative:
- catastrophic core collapse;
- rebound/explosion;
- heavy elements form and are thrown outward.

State evidence:
- weight 1.20;
- highest bloom class around 1.5;
- camera roughly [0, 14, 205];
- white-hot accent;
- FOV kick;
- fullscreen flash;
- chromatic pulse;
- shock ring;
- foreground ejecta;
- semantic audio detonation.

This is the single highest-intensity Event Peak on Continuous Timeline.

### VIII. You

Narrative:
- debris cools and reassembles;
- calcium in bones, iron in blood, oxygen in breath;
- 10 billion years terminate in the reader.

Composition:
- chapter text clears room for the final word;
- giant italic gradient word: you.;
- replay/context appears later as coda;
- final note explains that elements heavier than helium were assembled inside a star.

State evidence:
- weight 1.35, the longest chapter;
- warm #ffc98a accent;
- calmer bloom/glow;
- camera roughly [0, 0, 42].

## Weighted Narrative Timeline

Source-confirmed weights:
- Before: 1.00;
- Cloud: 1.05;
- Collapse: 1.05;
- Galaxy: 1.15;
- First Light: 1.00;
- Swelling: 1.00;
- Fuel: 1.00;
- Supernova: 1.20;
- You: 1.35.

Sum: 9.8.

Source computes scroll distance as 105 * sum(weights), producing a 1029vh track.

Normalized cumulative bounds define each chapter.

Within a chapter, the world holds its current state before beginning the morph to the next state. The transition window starts after roughly 42% local progress and uses a smooth high-order easing curve.

This produces:

ARRIVE -> HOLD -> TRANSFORM -> SETTLE

instead of continuous never-ending morph.

## Narrative Parameter Matrix

Each chapter is represented by one coordinated object containing both meaning and rendering direction.

Observed/source-confirmed fields include:
- id;
- weight;
- label;
- eyebrow;
- title;
- body;
- accent;
- base/hot/spark colors;
- spark amount;
- hot radius;
- particle size;
- brightness;
- camera position;
- bloom;
- nebula intensity;
- glow;
- glow tightness;
- procedural audio mix parameters.

The key lesson is not the exact values. Camera, particles, background, color, post-FX, typography/HUD accent, and sound all describe the same chapter.

## Shared Progress Bus

One normalized story progress value feeds the experience director.

It coordinates:
- stage A and B;
- stage interpolation mix;
- particle parameters;
- background shader parameters;
- camera position;
- FOV;
- bloom/chromatic behavior;
- flash;
- accent color;
- chapter text visibility;
- active HUD chapter;
- elapsed-year counter;
- chapter rail fill;
- continuous audio mix;
- sparse semantic event cues;
- final payoff state.

Scroll velocity exists separately as an energy/modulation signal, not a competing chapter clock.

## Smooth-scroll runtime

Source-confirmed:
- Lenis 1.3.25;
- auto RAF disabled so the experience owns one frame loop;
- normal scroll smoothing around 0.085;
- stronger/direct response in reduced motion;
- wheel multiplier 1;
- touch multiplier about 1.6;
- progress, pointer, audio cues, semantic chapter, and frame subscribers share one requestAnimationFrame owner;
- frame delta is bounded.

## Renderer architecture

Live/source-confirmed stack:
- Next.js;
- React;
- React Three Fiber;
- three.js r185;
- custom GLSL;
- one fixed full-viewport canvas;
- semantic DOM overlays above the canvas.

Canvas configuration includes:
- perspective camera around FOV 55;
- near 0.1 / far 3000;
- frameloop always;
- antialias false;
- alpha false;
- stencil false;
- high-performance power preference;
- preserveDrawingBuffer false;
- NoToneMapping in the authored canvas configuration.

## One primary particle world

The experience does not mount nine separate 3D scenes.

One primary Points system carries the story.

Geometry stores a compact structural basis:
- molecular-cloud positions;
- spiral-disc positions;
- unit directions;
- per-particle random/identity values;
- local density.

Custom vertex shader functions analytically synthesize multiple stages from that basis.

Benefits:
- fewer full morph buffers;
- one coherent material identity;
- very high particle count with low draw-call complexity;
- particle identity persists through the story;
- continuity feels physical rather than like scene replacement.

## Existing local-source benchmark particle tiers

The plugin's pre-existing Opus 5 source benchmark records approximately:
- 220,000 particles for desktop/high tier;
- 110,000 for lower-core tier;
- 70,000 for mobile/reduced tier.

These values come from the existing local source review of the same Opus 5 deployment lineage, not DOM inspection alone.

Do not copy these counts as universal targets.

## Story physics

Different chapters do not merely morph toward arbitrary shapes.

The shader encodes meaning-specific mechanics:
- collapse contracts, spins up, and flattens;
- galaxy rotation depends on radius;
- first light creates a luminous body/corona;
- swelling changes envelope scale;
- fuel intensifies/pulses internal structure;
- supernova creates broken/fingered ejecta rather than a clean sphere;
- the final state settles toward the semantic coda.

This is why the world feels authored instead of like one generic particle morph with different colors.

## Procedural background layer

A separate fullscreen shader supplies atmosphere.

Source-confirmed mechanisms:
- procedural nebula;
- three-octave FBM/value-noise style field;
- multiple hashed sparse star layers;
- star twinkle;
- central chapter-dependent glow;
- supernova shock ring;
- vignette;
- fine procedural grain;
- pointer-offset parallax.

No external video is required for the space field.

## Post-processing as narrative state

Bloom, chromatic aberration, FOV, and flash are not constant decoration.

Supernova increases:
- flash;
- bloom;
- chromatic aberration;
- FOV;
- ring intensity.

First Light gets a smaller ignition flash/glow peak.

Post-FX therefore functions as an event channel.

## Event Peaks on Continuous Timeline

Most of the journey is continuous interpolation.

Sparse source-confirmed threshold events punctuate major beats:
- collapse near early Collapse;
- ignition near early First Light;
- implosion late in Fuel;
- boom near the start of Supernova;
- arrival near the beginning of You.

Triggers include cooldown/replay logic rather than naive every-frame firing.

Event peaks synchronize visuals and sound while underlying chapter progress remains reversible.
## Input grammar

Source-confirmed jobs:

scroll -> story time
pointer -> camera parallax + world-space particle push/swirl
tap/click -> travelling shockwave + low audio pulse
chapter rail -> intentional chapter navigation
sound toggle -> procedural score layer
Begin again -> authored replay to the start

Pointer values are smoothed before use.

The pointer is projected through the active camera/world relationship so interaction radius scales with world depth rather than being a fixed screen-space gimmick.

Tap is separated from drag/scroll using time and movement thresholds; buttons/links are excluded from shock triggering.

## Procedural Web Audio score

There are zero HTML audio elements because the score is generated in-browser.

Source-confirmed audio engine starts from AudioContext with an interactive latency hint.

Continuous layers include:
- drone;
- sub oscillator;
- filtered pink-noise wind;
- harmonic pad;
- shimmer;
- generated convolution reverb.

Signal chain includes limiting/compression and gradual master fade-in.

Chapter configuration supplies different audio mix targets.

Sparse semantic sound events include:
- collapse noise sweep;
- ignition bell/noise event;
- implosion pitch/noise event;
- supernova boom with bed ducking and transients;
- arrival cue;
- click/tap pulse;
- final heartbeat.

This is Web Audio as narrative state, not background music pasted under the page.

## Adaptive Renderer Budget

Source-confirmed live architecture:
- initial DPR capped around 1.75;
- runtime performance monitoring;
- DPR can fall toward roughly 0.85;
- separate effect/quality factor;
- high-performance WebGL preference;
- antialias disabled;
- one primary particle draw system;
- analytic shader-state synthesis;
- cheap trigonometric turbulence favored over expensive noise in per-particle hot paths.

Performance degradation should reduce resolution/effect/detail before reducing semantic story coverage.

## Responsive behavior

CSS breakpoints observed:
- max-width 860px;
- max-width 640px;
- max-width 520px;
- prefers-reduced-motion: reduce.

At <=860px:
- chapter text becomes centered;
- text shifts toward a bottom-readable composition;
- secondary HUD labels disappear;
- scroll cue disappears.

At <=640px:
- chapter rail is hidden entirely.

At 390x844 live audit after entry:
- document width: 390px;
- canvas CSS size: 390x844;
- canvas internal size in the inspected state: 390x844;
- chapter rail: display none;
- active semantic opening chapter remains readable;
- no document-level horizontal overflow.

Mobile preserves the world rather than replacing it with a generic static article.

## Reduced-motion contract

Source/CSS confirms prefers-reduced-motion support.

Reduced mode:
- strongly reduces world motion;
- disables particle pointer force/swirl;
- reduces camera parallax;
- disables fullscreen flash;
- disables HUD/gate/cue decorative CSS animations;
- collapses transitions to near-instant;
- uses a reduced particle/runtime tier according to the existing source benchmark;
- keeps all narrative copy and controls.

Reduced motion is a different rendering mode, not the same ride at higher speed.

## Typography roles

Existing source benchmark and loaded implementation identify:
- Instrument Serif -> narrative/display;
- Inter -> body/readability;
- JetBrains Mono -> HUD/instrumentation/meta.

This triad is effective because roles are semantic:
- serif = cosmic/editorial time scale;
- sans = clear causal narrative;
- mono = measured/technical instrumentation.

Transfer the role separation, not the exact fonts.

## Base material / UI system

CSS root evidence:
- near-black #04050b background;
- off-white #f4f6ff primary ink;
- soft/faint translucent white text roles;
- chapter accent changes with story state;
- responsive padding clamps;
- one calm ease curve.

DOM grain uses a tiny fixed SVG turbulence texture with low opacity/mix-blend overlay.

HUD contains:
- title/active chapter top-left;
- sound control top-right;
- elapsed-year counter bottom-left;
- vertical chapter rail right;
- initial scroll cue bottom-center.

HUD is instrumentation, not a content card system.

## Final payoff discipline

The final word you. is deliberately delayed.

The coda/replay UI appears later than the word itself.

This protects the emotional peak from interface competition.

Useful general rule:

payoff first -> explanation/replay second

Do not place a CTA, share row, footer, or navigation cluster on top of the exact frame intended to land emotionally.

## Live reference scope

This standalone Opus 5 live design profile documents:
- current live-site coverage;
- current runtime/source corroboration;
- transferable design intelligence;
- scroll-world routing anchor;
- prompt -> experience mapping.

Do not delete the benchmark; it remains model/implementation-comparison evidence.

## What to adopt

Adopt when the brief warrants it:
- Prompt-to-Experience Compile Contract;
- weighted chapter timing;
- Narrative Parameter Matrix;
- Shared Progress Bus;
- one live world instead of unrelated chapter scenes;
- story physics;
- sparse Event Peaks on Continuous Timeline;
- explicit input grammar;
- semantic DOM over a renderer;
- procedural score as optional state layer;
- adaptive renderer quality;
- payoff-first final staging;
- full reduced-motion narrative.

## What to adapt

Adapt to the actual brief:
- particle system vs meshes/volumes/video;
- number of chapters;
- world mechanics;
- typography role families;
- audio depth;
- HUD density;
- pointer-force intensity;
- chapter rail visibility;
- post-FX intensity;
- DPR/particle budgets.

## What to avoid

Do not cargo-cult:
- 220k particles;
- cosmic nebula;
- one canvas merely because the reference uses one;
- Web Audio on ordinary marketing pages;
- 1029vh scroll length;
- Instrument Serif + JetBrains Mono;
- blue/purple/orange cosmic palette;
- bloom/chromatic effects everywhere;
- a supernova-like explosion unrelated to the story;
- long intro gates without a sensory reason.

Do not interpret "most impressive" as "maximum effect count." The experience works because one narrative model coordinates every effect.

## Best-fit briefs

Strong fit:
- scientific/educational experiential stories;
- origin/evolution/time journeys;
- space/cosmic topics;
- process transformations;
- museum/exhibition microsites;
- flagship interactive essays;
- high-ambition product/world narratives where one state can transform continuously;
- AI-generated creative briefs with explicit ordered stages and a strong final payoff.

Weak fit:
- dashboards;
- ecommerce catalogs;
- transactional SaaS;
- documentation;
- ordinary portfolios;
- sites whose audience cannot tolerate heavy GPU work;
- stories that need random route exploration rather than one authored temporal arc.

## Regression questions

- Is coverage correctly treated as 1/1 public route plus the complete 9-chapter runtime?
- Did all 9 chapters remain present and semantically ordered?
- Does chapter weighting produce a deliberate dwell hierarchy?
- Does one authoritative progress domain own semantic story time?
- Do visible copy, HUD, navigation, renderer, audio, and final mode agree at chapter boundaries?
- Does pointer movement affect world materiality/camera instead of only cursor decoration?
- Are click/tap impulses protected from normal scrolling and task controls?
- Does the renderer use a coherent world basis rather than nine unrelated scenes?
- Do story mechanics differ by chapter meaning?
- Are major flashes/booms sparse event peaks rather than constant decoration?
- Is sound opt-in and optional?
- Does adaptive quality preserve narrative semantics?
- Does 390x844 stay free of document-level overflow?
- Does reduced motion keep the complete story?
- Does the final you. land before replay/context competes with it?
- Could the experience still be explained as one authored system rather than a pile of effects?

Pass only when the result transfers the authored system and prompt-compilation reasoning, not the literal cosmic skin.
