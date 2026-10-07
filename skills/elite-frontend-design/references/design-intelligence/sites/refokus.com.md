# Refokus - distilled design intelligence

Source: https://www.refokus.com/
Audit date: 2026-10-05
Audit surface: live homepage in the user's Chrome, desktop 1920?889 and mobile 390?844, accessibility tree, computed styles, runtime animation state, network-loaded experience assets, and readable client-side JavaScript.

This profile records reusable mechanisms, not a recipe for cloning Refokus. Do not copy its proprietary logo/model, copywriting, exact project artwork, exact palette, or branded type choices into unrelated work.

## Executive DNA

Refokus combines a **quiet shell** with a **one signature stage**: a technically ambitious WebGL hero carries the strongest identity, while later sections rely more on typography, proof, editorial grids, large media, and project-specific color worlds.

The site feels premium not because every section is animated equally, but because ambition is allocated asymmetrically:

- the hero owns live 3D, lighting, post-processing, pointer response, and optional sound;
- editorial narrative uses large type, blur/focus, opacity, and controlled whitespace;
- proof appears before the loudest portfolio showcase;
- case studies behave like editorial spreads instead of a generic card grid;
- each featured project can enter its own vivid project world while global chrome remains restrained;
- mobile preserves the identity-bearing hero and type contrast rather than replacing them with a generic mobile template.

## Evidence Confidence

### Source-confirmed

- Webflow owns the primary site shell/content structure.
- GSAP and ScrollTrigger are active at runtime; approximately sixty ScrollTrigger instances were present during the desktop audit.
- SplitText and CustomEase are bundled and used by the experience JavaScript.
- The hero uses Three.js-style WebGL architecture with `WebGLRenderer`, `GLTFLoader`, perspective camera, scene lights, and a loaded `model.glb`.
- Hero texture assets include environment, diffuse, and normal textures.
- Post-processing uses `EffectComposer` with render, FXAA, film, and output passes.
- Renderer pixel ratio is explicitly bounded to 1.5 instead of blindly following high-DPR hardware.
- Pointer coordinates are stored and interpolated before they affect the rendered world.
- The expensive hero render step is bounded by scroll relevance rather than running as the active visual engine through the full document.
- Optional audio is user-gated through a visible sound-enable interaction; Howler-compatible audio support is present.
- Section-aware navigation theming is driven from real section state through ScrollTrigger.

### Observed

- Desktop starts as a dark purple/navy immersive stage with sparse top chrome, a central 3D brand object, vertical light-like texture, and floating service language.
- The first long scroll transition changes from spectacle to narrative focus: prominent copy becomes readable while future lines remain dimmed/blurred.
- A restrained social-proof interval follows, using moving/stacked client logos and testimonial content rather than another major spectacle.
- A large serif manifesto establishes a thesis before portfolio projects.
- Portfolio work shifts into saturated, project-owned visual worlds with title, summary, capabilities, geography, and large media separated on an editorial grid.
- Menu/contact chrome stays compact and control-like; content itself is largely open rather than cardified.
- Mobile retains the live/signature visual character, the editorial display role, the global dark shell, and the narrative sequence without horizontal overflow.

### Inferred

- The design intentionally uses contrast between one expensive signature moment and calmer supporting sections to make the hero feel more valuable.
- Proof placement before portfolio spectacle is partly a trust-building strategy for an agency selling high-consideration creative work.
- Project-owned color worlds help demonstrate range while the dark global shell keeps the agency itself coherent.

## Design DNA

### Composition

**Desktop**

- Global chrome is nearly edge-to-edge: menu left, monogram centered, contact right.
- The hero spends a large vertical scroll budget rather than behaving like a conventional one-screen hero.
- Copy is not constantly centered; narrative text uses left/offset anchors and deliberately large empty fields.
- Later manifesto and project layouts use asymmetric editorial grids rather than a repeated component template.
- Large media is allowed to dominate project sections; metadata occupies small, precise columns.

**Reusable rule**

If a premium marketing site earns a long first chapter, the scroll distance must expose a changing idea?not merely extend a static hero. Use spatial or typographic state change to justify the extra height.

### Typography

Observed/source-visible roles:

- `Featuredeck` acts as an expressive editorial/display face.
- `Generalsans Variable` acts as the quieter product/UI/body face.
- Desktop hero/display type reaches roughly 117 px in the inspected state; the main manifesto reaches roughly 96 px.
- Mobile scales the main editorial hero role to roughly 35 px and the manifesto role to roughly 24 px while keeping the family contrast.
- UI/project metadata remains compact and neutral.

**Reusable rule**

Use type-role contrast, not random font variety. An expressive editorial face can own thesis/memory while a neutral variable sans owns interface, service language, metadata, and explanatory copy.

**Do not copy**

Do not treat Featuredeck itself as the lesson. The transferable lesson is the role separation and proportional contrast.

### Color + Material

- Global experience begins in a near-black/navy-purple shell.
- The signature hero uses directional purple lighting/material cues rather than a flat gradient pasted behind ordinary UI.
- Later projects can occupy saturated section colors that belong to the individual project; one inspected project becomes a vivid orange field.
- Neutral/white typography provides continuity through color-world changes.
- Small navigation controls use subtle translucent/blurred chrome without turning the whole page into glassmorphism.

**Reusable rule: quiet shell - vivid project worlds**

For portfolio/agency/editorial work, keep global identity restrained enough that case studies can own strong colors. Do not smear one global accent over every project and call that cohesion.

### Media + Rendering

The hero is a hybrid DOM + WebGL stage:

- `WebGLRenderer` owns the live canvas;
- GLTF geometry supplies a branded 3D subject;
- texture maps provide environment/diffuse/normal character;
- explicit lights create directional material depth;
- `EffectComposer` adds FXAA and restrained film treatment;
- DOM text/navigation remains semantic and separate from the renderer.

Outside the hero, portfolio media is delivered through regular media/video/DOM instead of forcing the WebGL renderer to become the entire site architecture.

**Reusable rule: Bounded Immersive Rendering**

Invest in a sophisticated renderer only for the region that actually needs it. Keep the remainder of the information architecture in semantic DOM unless another section genuinely requires a renderer.

### Motion

Runtime evidence showed many triggered animations but relatively few continuously scrubbed relationships.

Important mechanisms:

- ScrollTrigger drives entry/focus/state timing.
- SplitText enables line/character-level control where typography is the experience.
- Blur + opacity produce depth/focus transitions, not only translation.
- The hero maintains continuous rendering while relevant; ordinary content does not inherit the same cost.
- Some scroll-linked relationships use scrubbing, but continuous scrub is not the default for every section.

**Reusable rule**

A premium motion system may have many authored triggers yet only a few continuous control loops. Reserve scrub for relationships that truly need continuous causality. Use discrete reveals for the rest.

### Interaction + Input Grammar

- Pointer movement feeds the 3D subject/world through interpolated state rather than raw jitter.
- Scroll is both navigation through content and an input signal for the signature chapter.
- Click can change material/state in the rendered subject.
- Sound is optional and gated; visual/story comprehension does not depend on autoplay audio.
- Menu/contact remain conventional controls even when the surrounding visual world is experimental.

**Reusable rule**

Pointer input should add materiality, orientation, parallax, or world response?not become cursor theatre across every component.

### Narrative + Proof

The homepage reads as a persuasion sequence rather than a shuffled set of sections:

1. establish the brand/website gap;
2. clarify why the old story no longer fits the company;
3. show recognizable client proof/testimonials;
4. state the agency thesis;
5. demonstrate work through large case-study evidence;
6. reinforce taste/recognition/awards;
7. convert through project/contact paths.

**Reusable rule: proof before fireworks**

For high-consideration creative/technical services, establish credibility before asking the visitor to interpret ambitious showcase work as proof of capability.

### Case Studies

Observed project presentation avoids the default rounded-card gallery.

A project section can separate:

- project title;
- narrative/result statement;
- service/capability list;
- location/context metadata;
- multiple large media frames;
- project-owned background/surface world.

**Reusable rule: editorial case studies, not card grids**

When the work itself is the product, allow each project to become a temporary page/world. Card containment is optional, not default.

## Responsive Brand Payload

Mobile viewport audited at 390?844 with no horizontal overflow.

What survived:

- the dark/purple world;
- the 3D signature mark/world;
- serif editorial display role;
- compact menu/contact chrome;
- core agency statement;
- the same high-level narrative sequence.

What compressed:

- display type scale;
- later section heights;
- proof density;
- overall document length relative to desktop;
- supporting complexity around the signature stage.

This is a strong example of **Responsive Brand Payload**: preserve the identity-bearing mechanism and reduce secondary complexity first.

Do not interpret this as a mandate to keep expensive 3D on every mobile project. Preserve the identity by the cheapest equivalent mechanism that meets performance, accessibility, and product constraints.

## Technical Architecture Lessons

### 1. Bounded renderer lifecycle

The hero application tracks scroll and steps its expensive render pipeline only while the experience is within the relevant initial region. This is stronger than merely hiding a canvas with CSS while its loop continues to spend CPU/GPU.

Transfer:
- create an explicit active/visible state for expensive scenes;
- idle or stop frame work outside the active region;
- resume deterministically when returning.

### 2. Deliberate pixel ratio

The renderer uses an explicit pixel ratio of 1.5 in the audited source.

Transfer:
- treat pixel ratio as a quality/performance dial;
- cap it on costly experiences;
- do not equate maximum DPR with premium quality.

### 3. Pointer interpolation

Raw pointer state is separated from interpolated pointer state before being consumed by the 3D experience.

Transfer:
- smooth high-frequency input at the world/material layer;
- keep UI click/hover semantics immediate where latency would hurt usability.

### 4. Post-processing as finishing, not concept

The pipeline uses `EffectComposer`, FXAA, a mild film pass, and output processing. The memorable result still comes from geometry, lighting, material, composition, and timing?not from post-processing alone.

Transfer:
- establish form/lighting/composition first;
- use post FX to finish a world, not to rescue generic geometry.

### 5. Section-aware chrome

Navigation theme responds to the section currently governing the viewport.

Transfer:
- derive chrome state from the actual visible section/system state;
- avoid hand-authored timers or disconnected scroll guesses.

### 6. Optional sensory enhancement

The visible sound gate proves audio is an enhancement rather than a hidden requirement.

Transfer:
- never rely on autoplay sound for essential meaning;
- expose explicit opt-in and a stable mute state;
- make the muted experience complete.

## Adopt / Adapt / Avoid Matrix

| Pattern | Default decision | Why |
|---|---|---|
| One signature stage | Adopt for premium narrative/marketing work | Concentrates ambition and avoids spectacle fatigue. |
| Quiet shell - vivid project worlds | Adapt | Excellent for portfolios/case studies; less suitable for a single-product SaaS UI. |
| Editorial serif + neutral variable sans roles | Adapt | Transfer the role contrast, not the exact fonts. |
| WebGL hero with branded 3D subject | Adapt only when product/brand earns it | Expensive and highly context dependent. |
| Bounded renderer + explicit pixel ratio | Adopt for expensive rendering | Durable performance principle. |
| Blur/opacity focus choreography | Adapt | Strong for narrative text, wrong for dense product flows if it harms legibility. |
| Social proof before portfolio showcase | Adapt | Strong for high-consideration services, not universal. |
| Editorial project spreads | Adopt for portfolio-heavy surfaces | Avoids generic cardification and gives work visual authority. |
| Exact purple world / exact orange project color | Avoid | Branded/signature-specific. |
| Exact 3D monogram/model | Avoid | Proprietary identity, not transferable system intelligence. |
| Exact copy/award structure | Avoid | Context-specific content. |

## Best-fit Briefs

Use this profile as inspiration for:

- premium creative/technical agencies;
- venture/technology portfolios where the work must feel authored rather than templated;
- brand refreshes that need a memorable signature moment;
- high-end B2B technology storytelling with complex products and strong proof;
- sites where a single WebGL/3D stage can materially increase perceived craft;
- editorial portfolio structures that need to escape rounded-card sameness.

## Weak-fit Briefs

Do not let this profile dominate:

- admin/settings/operations screens;
- dense dashboards where scan speed is the primary job;
- transactional commerce paths where spectacle adds friction;
- low-end hardware contexts with no viable fallback;
- products whose trust language requires conservative motion and minimal rendering complexity.

## Regression Questions

When a future design claims to apply Refokus-derived intelligence, ask:

- Is there one clear signature stage, or did spectacle leak everywhere?
- Does typography have role contrast, or merely multiple trendy fonts?
- Are case studies/content worlds distinct because their content differs, or are colors arbitrary?
- Did proof appear at the right point in the persuasion sequence?
- Is continuous animation bounded to where it creates value?
- Is pointer response smoothed and meaningful rather than decorative cursor chasing?
- Can the experience communicate fully with sound disabled?
- On mobile, what exact Responsive Brand Payload survived?
- Does the result belong to the new brand, or is Refokus still visibly recognizable in assets/colors/composition?

Pass only when the transferable mechanism survives while the source site's proprietary identity does not.
