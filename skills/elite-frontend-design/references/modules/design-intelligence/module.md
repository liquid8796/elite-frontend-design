---
name: design-intelligence
description: Evidence-driven distillation of reusable design intelligence from strong websites, products, screenshots, videos, and source code. Use when the goal is to learn the quality, design language, or implementation thinking behind references rather than reproduce one reference literally.
---

# Design Intelligence

Use this module when a user supplies one or more references and asks to learn from them, absorb their quality, distill their design language, or improve future work using what makes them effective.

This is different from faithful recreation. `reference-first` establishes what the source actually does. `design-intelligence` decides what is reusable, what is context-specific, and how to transfer the lesson without cloning the source.

## Distill, Don't Clone

The target is **transferable design reasoning**, not a disguised copy.

Do not preserve a reference site's exact logo, proprietary artwork, branded 3D object, copy, bespoke font choice, signature color values, or one-off composition merely because they are attractive. Instead ask what job each choice performs and encode the mechanism at the right level of abstraction.

Examples:

- Do not learn "use this exact purple 3D logo." Learn "put disproportionate technical ambition into one brand-defining stage when that stage carries the identity."
- Do not learn "use this exact serif." Learn "pair an expressive editorial display role with a quieter product/UI role when the contrast serves the story."
- Do not learn "every project must be orange." Learn "let portfolio projects own distinct color worlds while the global shell stays restrained."

When a reference is explicitly licensed or owned by the user, source-level patterns may be reused more directly, but still prefer portable principles over cargo-cult implementation.

## Evidence Stack

For each reference, collect only evidence that can materially improve future decisions.

1. **Rendered evidence** - screenshots at representative scroll positions, hover/focus states, transitions, and responsive viewports.
2. **Structural evidence** - semantic order, section geometry, container logic, content density, real typography, and assets.
3. **Runtime evidence** - animation timelines, scroll triggers, canvas/WebGL behavior, media playback, pointer/input roles, accessibility tree, and network-loaded experience assets.
4. **Source-confirmed mechanisms** - libraries, renderer architecture, shader/post-processing choices, state ownership, responsive branches, lifecycle/performance controls, and reduced-motion behavior when source is inspectable.
5. **Inference** - design intent or mechanisms that cannot be directly proven. Keep these labeled as inference.

Do not infer a sophisticated mechanism from a screenshot when live runtime/source evidence is available.

## Evidence Confidence

Label material findings with one of three confidence levels while distilling:

- **Observed** - directly visible in the rendered reference at a known state/viewport.
- **Source-confirmed** - verified from DOM, computed styles, runtime objects, network activity, or readable source.
- **Inferred** - a reasoned interpretation that explains the evidence but is not directly proven.

Promote a lesson to a reusable rule only when the confidence is high enough for the consequence of the rule. A novel visual guess may remain inspiration; a technical architecture claim should be source-confirmed when possible.

## Reference Landscape Routing

Before deep-auditing or borrowing from a reference, classify what kind of excellence it represents. A reference can be beautiful and still be the wrong teacher for the current product.

Use the lightweight landscape registry at:

`references/design-intelligence/reference-landscape.md`

Route the reference into one primary landscape and, when useful, one secondary landscape:

- **product precision** - clarity, interaction polish, systems discipline, product evidence;
- **experiential / agency** - authored transitions, campaign storytelling, portfolio/world-building, high-ambition media;
- **luxury / editorial** - art direction, restraint, image/type tension, material and pacing;
- **game / cinematic** - world continuity, HUD/content hierarchy, media choreography, sensory density, diegetic cues;
- **developer product** - code/product proof, technical trust, stack/context selection, operational evidence;
- **template commodity** - highly repeated market grammar useful mainly as a baseline or anti-pattern detector.

The landscape is a **routing aid**, not proof. A candidate reference is not audited evidence. Never promote a candidate site's implementation detail, performance claim, responsive behavior, or design rule until it has been inspected through the Evidence Stack or independently confirmed across audited references.

Choose references for the problem they solve, not because they rank highest on a generic "beautiful websites" list.

## Breadth-to-Depth Funnel

Use broad inspiration research to improve selection, then narrow aggressively before extracting rules.

Preferred funnel:

1. **Landscape scan** - collect a broad set of strong candidates across relevant categories.
2. **Archetype classification** - identify which candidates solve the same design problem and which merely share surface style.
3. **Shortlist 1-3 references** - choose sources that best match the new product's audience, proof burden, content model, interaction ambition, and technical constraints.
4. **Deep audit** - inspect rendered states, structure, runtime behavior, source/network evidence, mobile adaptation, accessibility, and performance where available.
5. **Distill** - write site-specific Design DNA with confidence labels.
6. **Promote selectively** - move only durable, cross-project mechanisms into this general module.

Do not load dozens of candidate references into the design context at once. Breadth improves discovery; depth creates trustworthy intelligence. Loading the whole inspiration backlog encourages style averaging and weakens product fit.

## Template Archetype Firewall

Popular templates are useful because they reveal established conventions, but those same conventions can cause a new product to collapse into a generic market look.

Treat repeated combinations as **Template Convergence Risk**, especially when several appear together without product-specific justification:

- centered hero + eyebrow pill + generic gradient headline;
- glowing orb / mesh / aurora used as the main identity despite having no product meaning;
- dark Linear-like shell + tiny mono labels + purple/blue glow + rounded dashboard cards;
- feature bento where every idea is forced into a card regardless of information structure;
- three generic logo rows followed by testimonial cards and a gradient CTA band;
- terminal/code wallpaper that is not authentic product proof;
- oversized rounded rectangles used as the default container for every section;
- identical reveal-on-scroll motion applied to all content blocks.

The firewall does **not** ban familiar patterns. Familiarity is often good for usability. It asks whether the composition has converged on a recognizable template grammar rather than a product-specific system.

When four or more traits from one commodity archetype accumulate, require at least one meaningful differentiator in a structural layer:

- composition or hierarchy;
- information model;
- typography role system;
- proof mechanism;
- interaction/input grammar;
- responsive transformation;
- signature media/rendering mechanism.

Changing only gradient colors, icon sets, radius, or copy does not count as differentiation.

Use template references as **baseline literacy** and anti-pattern detectors. Do not elevate a template convention to premium design intelligence merely because it is widespread.

## Template Residue Quarantine

A complete site audit should cover public routes without treating every public artifact as design DNA.

This matters especially for templates, demos, Framer/Webflow exports, theme previews, and component playgrounds, which may expose:
- 404/error routes;
- demo/editor/remix chrome;
- placeholder CMS records;
- isolated component pages;
- style-guide or experiment routes;
- generic metadata repeated across unrelated pages;
- template marketing controls that belong to the template vendor rather than the represented product.

Quarantine workflow:

1. keep the route/artifact in the coverage manifest so the audit remains complete;
2. classify its actual role;
3. extract reusable utility behavior only when relevant;
4. exclude placeholder/editor/template-vendor identity from the site's core Design DNA;
5. never promote a mechanism solely because it appeared on one utility/demo page.

Whole-site distillation means **complete accounting plus selective weighting**, not copying every routable artifact.

## Route-Complete Agency Ecosystems

Do not judge an agency reference only by its home hero. Audit service landings, audience landings, work index, current and legacy case studies, editorial/news routes, careers, resources, contact and declared companion products. Transfer route jobs and proof-binding logic, not agency identity.

**Evidence-Dependent Case Depth**: allow strong cases to expand when process/outcome evidence exists and keep legacy/thin cases concise instead of forcing a uniform scroll length.

**Audience-Specific Proof Binding**: preserve one brand voice while changing objections, testimonials, cases and offers to match visitor context.

## Companion Product Surface Integrity

When a parent brand advertises a separate sitemap/product surface, treat it as its own audited design system if typography, color, route grammar or runtime materially differ. Preserve provenance between surfaces without forcing one skin across both.

For technical documentation, prefer **Copy -> Configure -> Verify**: every install recipe should end in a concrete testable state.
## One-Page Studio Conversion Spine

A compact studio or service business can deliberately compress the full commercial decision journey into one anchor-driven route when separate route families would be thin.

A strong sequence is:

`identity -> credibility -> capabilities -> work/product proof -> world/media proof -> social proof -> objections -> people -> contact -> final reassurance`

Use this only when each section has a distinct decision job. Split into dedicated routes when service/search intent, deep case evidence, or content scale requires its own information architecture.

On mobile, preserve the decision order but release desktop mechanics such as sticky project selectors, wide proof panels, and nonessential ambient motion.

## Cross-Section Identity Integrity

Template residue can break a single-page site even when no dynamic route family exists. Treat the page as one bound record and verify the same product/business identity across:

- logo/site name and hero copy;
- metrics, testimonials, project/game names and team;
- FAQ and vertical-specific terminology;
- contact details and form destinations;
- footer, social/legal links and vendor chrome;
- title, description, OG/Twitter data and 404.

A polished visual shell is not evidence that the content is coherently bound. Mixed brands, unrelated vertical copy, conflicting contact data, dead card links, and placeholder GET-to-self forms are release blockers, not harmless demo details.
## Telemetry as Narrative UI

Compact metadata can carry world identity when every field answers a real contextual question. Coordinates, sector/mission IDs, UTC, archive dates, figure/build/platform labels and explicit uncertainty can bridge large media chapters without becoming decorative HUD noise.

Rules:
- one coherent vocabulary, not random terminal strings;
- metadata stays subordinate to primary content;
- context/provenance must be truthful when it describes real product evidence;
- responsive layouts reduce density, not all identity-bearing metadata.

## Pinned Spatial Survey

A sticky horizontal sequence is justified only when the horizontal axis represents meaningful exploration of places/stages.

Desktop contract:
- one sticky viewport and one bounded track;
- explicit start/end and one summary state;
- no competing sticky owner;
- every panel remains semantically readable.

Mobile/reduced-motion contract:
- release sticky ownership;
- restore vertical flow;
- preserve the complete place sequence and facts;
- never require horizontal scrub or pointer precision for core meaning.

## Exact Campaign Destination Integrity

High-intent labels must resolve to the exact intended resource. A platform root is not an acceptable final destination for a wishlist, trailer, community profile, press kit or legal action.

Before release, verify each CTA by user job, destination identity and expected landing state. Placeholder/example URLs and anonymous press quotes remain quarantined from production proof.
## Route-Family Binding Integrity

A page template can look polished in isolation while the **route family is semantically broken**. Whole-site audits must verify that every dynamic/CMS route binds one coherent record across all visible and machine-readable surfaces.

Check the binding chain for each route:

- URL/slug and canonical;
- document title and description;
- eyebrow/category and H1;
- summary/deck;
- primary media/logo;
- metadata such as author, date, client, industry, setup time, difficulty, category, or type;
- body sections and instructions;
- metrics/results;
- related-content cards;
- primary CTA/action.

All material fields should describe the **same underlying record** unless a shared/global field is intentionally documented.

Red flags include:

- unique page titles with the same hero H1 across many detail routes;
- one integration name with another integration's instructions;
- different article titles mapped to near-identical long-form bodies;
- copy/copy-copy slugs, `Tool Name`, placeholder domains, or default CMS records exposed publicly;
- route-specific metrics paired with a generic or wrong case summary;
- server-rendered/default content that changes to another record only after hydration.

Use a route-family scan, not one representative detail page, to detect these failures. A full-site distillation should keep residue in the coverage manifest but quarantine it from Design DNA.

## Integration Detail as Implementation Proof

When a product claims broad integrations, a logo wall proves availability weakly. A strong integration detail route can turn compatibility into **implementation proof**.

A useful sequence is:

**identity + one-line job -> concrete capabilities -> installation/setup -> operational metadata -> primary setup action -> human/sales fallback -> related integrations**

Operational metadata can include:

- setup time;
- difficulty;
- category;
- connection/API type;
- auth method;
- runtime/event model;
- prerequisites or required permissions.

The page should let a visitor answer:

- What does this integration actually do?
- How does it connect?
- What must I configure?
- Roughly how difficult/long is setup?
- What do I do next?

Keep instructions specific to the integration. Reusing another connector's setup copy destroys more trust than a simpler page would. On mobile, stack the proof but preserve the setup sequence and primary action.

Do not fabricate compatibility, setup steps, security/compliance claims, or technical metadata merely to make an integration catalog feel complete.

## Game/Experiential Audit Lens

When the reference is game, entertainment, cinematic campaign, or world-led experiential work, extend the normal Design DNA audit with the following lens:

- **HUD vs content hierarchy** - what behaves like interface chrome, what behaves like narrative/world content, and which layer wins attention;
- **world-building continuity** - whether sections feel like one continuous world, authored chapters, or unrelated campaign panels;
- **diegetic vs ordinary UI** - which controls/labels belong visually to the fictional world and which remain conventional for usability;
- **trailer/media choreography** - how video, imagery, 3D, typography, and copy alternate so media does not drown out information;
- **chapter transitions** - how state/scene changes communicate progression and whether they are scroll-, time-, route-, or input-owned;
- **cursor/touch/input grammar** - whether input manipulates world state, camera, selection, navigation, or only decoration;
- **audio dependency** - whether sound is optional enhancement or required to understand the experience;
- **typography under motion** - legibility, dwell time, contrast, and readable states while media is active;
- **sensory density budget** - how many simultaneous moving/bright/audio layers compete in one viewport;
- **loading/performance fallback** - posters, pre-rendered media, quality tiers, progressive loading, idle rules, and low-power alternatives;
- **mobile reduction strategy** - what preserves the world identity when desktop interaction/rendering cannot transfer directly.

If the audit reveals a true authored world, continuous camera system, scroll-cinematic renderer, or cross-channel story-state problem, route implementation guidance to `experience-engineering` (and `scroll-world` when appropriate). `design-intelligence` should distill why the experience works; `experience-engineering` should own how to build and synchronize that class of system.

## Cinematic Without Heavy Rendering

A game, entertainment, or world-led site can feel cinematic without WebGL, live 3D, autoplay video, or continuous canvas rendering.

Use lower-cost identity mechanisms first when they can carry the brief:
- high-quality still imagery with authored crops;
- high-character display typography;
- strong dark/light contrast and one world accent;
- bracket/HUD-like metadata used sparingly;
- sticky or overlapping editorial sequencing;
- spatial scale changes;
- controlled image repetition, collage, and directional composition;
- restrained Framer/CSS motion around otherwise static media.

This is especially useful when:
- the site markets a studio, team, portfolio, or service rather than one playable world;
- production capability is limited;
- performance and mobile stability matter more than runtime spectacle;
- the available evidence is strong still artwork rather than a real-time renderer.

The rule is not "avoid 3D." It is **earn the renderer**. Route to `experience-engineering` or `scroll-world` only when continuous world state, camera ownership, temporal synchronization, or high-ambition rendering is genuinely part of the product story.

A still-image system can remain premium when composition, crop, type, and scroll ownership are authored rather than generic.

## Capability-to-Case Pairing

Studios, agencies, consultancies, and service businesses should separate **what they can do** from **proof that they have done it** while making the relationship between those two route families obvious.

Use two complementary layers:

1. **Capability / service layer**
   - names the service;
   - explains scope and process;
   - describes tools/methods only when useful;
   - clarifies what the buyer receives.

2. **Case / project layer**
   - names the situation/project;
   - records role, constraints, or context;
   - shows the actual work/media;
   - explains challenges, decisions, and results when truthful.

A strong whole-site system may use:
- home previews for both service and case families;
- service index -> service detail;
- case index -> case detail;
- cross-links between relevant services and projects;
- a shared visual grammar while allowing proof routes to be more media-heavy.

Do not use case studies as decorative duplicates of service cards. Do not fabricate project outcomes, budgets, clients, dates, or tools to make the capability layer look credible.

When a site contains both service and case route families, QA should verify that the visitor can answer:
- what do they offer?
- what does that work look like in practice?
- where is the evidence for each major capability?

## Prompt-to-Experience Compile Contract

When a high-ambition experience starts from a short creative prompt, do not implement the prompt as a pile of literal effects. First compile it into an explicit experience contract.

Extract four layers:

1. **Narrative nouns / beats** ? the ordered subjects or events the prompt names.
2. **World mechanics** ? what physically or visually changes in each beat.
3. **Interaction roles** ? what scroll, pointer, touch, sound, navigation, and replay each control.
4. **Payoff** ? the final semantic/emotional moment the whole journey is earning.

Then materialize them as:
- ordered chapter/state configuration;
- dwell/weight per beat;
- rendering/media strategy;
- camera/composition behavior;
- type/copy role;
- color/material state;
- input response;
- audio role if sound is justified;
- responsive/reduced-motion behavior;
- QA checkpoints.

A prompt such as `cloud -> collapse -> galaxy -> first light -> swelling -> fuel -> supernova -> you` should become an authored state system before it becomes code.

This is especially important for AI-generated experiential work: a short prompt may describe a memorable arc while leaving architecture unspecified. The model must create the missing contract deliberately instead of improvising unrelated animations section by section.

## Narrative Parameter Matrix

For a chaptered immersive experience, represent each narrative state with a coordinated parameter set rather than styling text and renderer independently.

A useful matrix may include:
- chapter weight / dwell;
- label, title, body, CTA;
- dominant/accent colors;
- world/material state;
- camera position/FOV;
- scale, density, brightness, glow;
- background/atmosphere parameters;
- post-processing intensity;
- audio mix target;
- semantic cue/event eligibility.

The important property is not the exact parameter list. It is that **every subsystem describes the same narrative moment**.

Do not let:
- copy say one chapter;
- camera imply another;
- palette lag behind;
- HUD/nav switch early;
- audio remain in the previous emotional state.

The matrix can feed a central director or another single state owner. Treat it as the authored source of cross-channel coherence.

## Event Peaks on Continuous Timeline

Most chapter transitions should remain continuous, reversible, and scroll-controlled. Reserve sparse one-shot or high-energy events for moments that deserve punctuation.

Use the continuous timeline for:
- chapter interpolation;
- camera movement;
- color/material change;
- typography entrance/exit;
- ambient sound mix;
- background density/glow.

Use event peaks for rare moments such as:
- ignition;
- impact;
- fracture/collapse;
- launch;
- explosion/supernova;
- arrival/reveal.

An event peak may synchronize:
- FOV kick;
- flash;
- bloom/chromatic pulse;
- shockwave;
- transient audio;
- temporary bed ducking;
- haptic/interaction cue where appropriate.

Keep event triggers derived from the same authoritative progress domain and make forward/backward/replay semantics explicit. Do not scatter independent scroll listeners that can double-fire or drift from the narrative state.

## Adaptive Capability Routing

Do not classify the active model as "strong" or "weak" and do not use model self-assessment as authority. Route the **execution strategy** from observable evidence: task risk, design certainty, optional runtime metadata, user intent, and rendered QA.

Use three execution modes:

- **LOCKED** - one baseline skin, explicit token ranges, fixed composition grammar, Skin Lock, and narrow Controlled Mutation. Use when uncertainty or drift is high.
- **GUIDED** - one skin or audited pattern set as a coherent baseline, bounded token/composition mutation, and one bespoke signature. This is the normal balance between coherence and originality.
- **BESPOKE** - custom art direction, composition, token/system decisions, and interaction language are allowed, but only with a complete contract and strong verification.

**GUIDED is the default** when evidence is inconclusive. A model never enters BESPOKE merely because it claims to be capable, because a model name sounds powerful, or because the brief is visually ambitious.

### Evidence Order

Evaluate these signals in order. Later evidence may override earlier assumptions.

1. **User intent** - an explicit request for conservative/template-like execution can start LOCKED; a request for guided polish can start GUIDED; an explicit request for experimental/bespoke work makes BESPOKE eligible but does not waive production QA.
2. **Runtime metadata** - if the host explicitly exposes a constrained/fast tier, increase scaffolding; if it exposes a high-capability/reasoning tier, permit a higher ceiling. Treat runtime metadata as optional evidence, never the sole authority.
3. **Task Complexity Score** - measure design/implementation risk. Complexity raises the proof required for freedom; it does not automatically raise the mode.
4. **Design Preflight** - count unresolved design primitives before implementation. Uncertainty is a direct signal to add scaffolding.
5. **Rendered QA** - use the real output to keep, downgrade, or selectively escalate mode. Rendered evidence outranks confidence.

### Task Complexity Score

Add risk points only for requirements actually present:

- +1 multiple responsive layouts or nontrivial breakpoint transformations;
- +1 complex information architecture, dense product state, or many content types;
- +1 strong bespoke brand/art-direction requirement;
- +1 unusual typography role system;
- +1 multiple reference sources that must be synthesized;
- +1 existing codebase/architecture constraints that limit visual freedom;
- +1 accessibility-sensitive or input-rich interaction;
- +1 advanced authored motion/choreography;
- +2 live WebGL/3D, continuous camera world, or renderer-owned storytelling.

Interpretation:

- 0?2: low design risk;
- 3?5: moderate design risk;
- 6+: high design risk.

A high Task Complexity Score means **require more certainty and QA**, not "choose BESPOKE." A high-risk task with unresolved primitives should become more scaffolded, not more improvisational.

### Design Preflight

Before substantial implementation, confirm these eight primitives can be stated concretely:

- typography roles;
- spacing rhythm;
- surface hierarchy;
- composition grammar;
- responsive transformation;
- signature mechanism;
- motion ownership;
- proof/content strategy.

Routing rule:

- 3+ unresolved primitives -> **LOCKED**;
- 1?2 unresolved primitives -> **GUIDED**;
- 0 unresolved primitives -> remain **GUIDED** by default; BESPOKE becomes eligible only when user intent/product fit calls for it and the verification budget can support it.

Vague phrases such as "modern cards," "some gradients," or "smooth animation" do not count as resolved primitives.

### Mode Contracts

**LOCKED**

- choose exactly one baseline skin;
- materialize its Token Scaffold;
- preserve Skin Lock through the page;
- use its composition grammar;
- mutate only brand accent, product content/proof, hero arrangement, and one signature differentiator;
- prefer explicit values/ranges over open-ended style invention.

**GUIDED**

- choose one baseline skin or one coherent audited pattern set;
- preserve typography roles, surface hierarchy, spacing cadence, and interaction consistency;
- allow bounded token changes and composition changes when product fit justifies them;
- allow one bespoke signature mechanism;
- keep the Template Archetype Firewall active.

**BESPOKE**

- skin packs are optional references rather than locks;
- custom design system, composition grammar, and interaction language are allowed;
- the Design Preflight must be fully resolved;
- the task must have a reason for bespoke treatment beyond novelty;
- rendered responsive/accessibility QA is mandatory before keeping the mode.

### Rendered QA Feedback Loop

After the first representative render, check for material coherence failures:

- typography role/scale drift;
- inconsistent spacing cadence;
- unexplained radius/surface-system changes;
- generic cardification or template convergence;
- accent/glow proliferation;
- repeated decorative motion with no hierarchy;
- hero language disconnected from later sections;
- mobile losing the signature/proof hierarchy.

If there are **two or more material coherence failures** in one representative QA pass, downgrade one step: `BESPOKE -> GUIDED` or `GUIDED -> LOCKED`. If one material failure persists after a repair pass, also downgrade. Repair the inconsistent layers rather than rebuilding stable parts.

To **escalate** one step, require all of the following: the current mode renders coherently at representative desktop and mobile widths, the design contract is fully resolved, there are no material coherence failures, and the user/product benefits from additional freedom. Passing QA does not require escalation; staying GUIDED is a successful outcome.

User intent can choose the starting ambition, but execution scaffolding may still increase internally to protect usability, accessibility, coherence, and production quality.

## Aspect-Ratio Art Direction

When a hero or campaign surface is dominated by authored imagery, responsive quality may depend on the **shape of the viewport**, not only its width.

Use aspect-ratio art direction when one crop cannot preserve the focal subject, text-safe area, and narrative balance across tall mobile, landscape desktop, and ultra-wide displays.

Preferred contract:

- identify focal subject and protected text/control zones;
- author alternate portrait/landscape/ultra-wide crops or compositions when necessary;
- route media with aspect-ratio/orientation conditions in addition to width breakpoints;
- preserve the same narrative job even when the asset/crop changes;
- test intermediate and extreme shapes, not only canonical device widths;
- use Responsive Fidelity Substitution when the rendering mechanism itself should change with the device.

Do not solve a fundamentally incompatible composition with increasingly fragile crop offsets.

## World-Led Campaign Chapters

For games, entertainment, cultural launches, and fictional-world campaigns, organize the page as authored chapters with explicit roles instead of one undifferentiated stream of spectacle.

A chapter may own world/identity establishment, release/platform conversion, trailer proof, edition/offer explanation, narrative/world thesis, people/place exploration, media/community, updates/news, or final conversion.

Chapters may vary local color, art, and density while sharing one world grammar: typography roles, navigation/chrome, CTA semantics, media framing, motion intensity, and responsive behavior.

The goal is not to make every section cinematic. The goal is to make every cinematic section **legible as part of the same world and responsible for one clear campaign job**.

## Baseline Skin Packs

Use `references/design-intelligence/skins/index.md` when the task needs a high-quality visual baseline more deterministic than open-ended art direction. These packs are **Deterministic Design Scaffolds**: coherent token, composition, motion, responsive, and QA contracts that reduce the number of simultaneous aesthetic decisions.

The operating rule is **1 archetype + 1 skin + 1 composition grammar**. Avoid averaging multiple skins.

### Skin Lock

After choosing a skin, lock its typography roles, surface hierarchy, radius family, spacing rhythm, action treatment, and motion language. Later sections inherit those choices unless a concrete product constraint forces a documented deviation.

### Controlled Mutation

Customize brand accent, hero composition, imagery, product proof, one signature interaction/media idea, and section order when the narrative requires it. Cosmetic recoloring alone is not differentiation.

### Skin-Guided Execution

Use skin packs when Adaptive Capability Routing selects LOCKED or GUIDED, or when a rendered pass shows visual drift:

1. select the closest baseline skin instead of inventing an unrelated system;
2. materialize its Token Scaffold in the design contract;
3. keep Skin Lock fixed through implementation at LOCKED, or preserve its core hierarchy while allowing bounded mutation at GUIDED;
4. use the skin's Composition Grammar instead of improvising every section;
5. allow Controlled Mutation only where product identity requires it;
6. run the skin QA Rubric and Template Archetype Firewall before signoff.

Prefer explicit values/ranges and known composition relationships whenever uncertainty is high. BESPOKE may use skin packs only as diagnostic references, but intentional deviations must still be named, justified by product fit, and visually re-verified.

### Audited Evidence Anchors

- `developer-infra.md` inherits mechanisms from audited Resend evidence: Product Evidence Before Feature Claims, Code as Product Proof, functional context tabs, semantic accent restraint, and Responsive Fidelity Substitution.
- `creative-agency-editorial.md` inherits mechanisms from audited Refokus evidence: one signature stage, quiet shell around project worlds, editorial case-study grammar, motion-as-focus, bounded immersive rendering, and Responsive Brand Payload.

The site profiles are evidence anchors, not skins to copy. Exclude source-specific fonts, branded objects, artwork, copy, exact palettes, and one-off composition.

## Design DNA

Describe a reference across the same axes so multiple sites can later be compared instead of becoming isolated moodboards.

### 1. Composition

Capture:
- first-viewport hierarchy;
- alignment anchors and grid logic;
- asymmetry vs symmetry;
- negative-space budget;
- open-layout vs card/container segmentation;
- how section identities change down the page.

### 2. Typography

Capture:
- display, narrative, body, UI, and data roles;
- serif/sans/mono contrast only where it serves a role;
- scale ratios and wrapping behavior;
- weight/width/letter-spacing character;
- responsive changes to typographic hierarchy.

### 3. Color + Material

Capture:
- shell/background character;
- whether one accent is global or sections own distinct palettes;
- surface, border, glass, texture, grain, lighting, and image treatment;
- which colors communicate identity vs state vs project content.

### 4. Media + Rendering

Capture:
- static imagery, video, illustration, 2D canvas, WebGL/3D, shader, or hybrid roles;
- whether expensive rendering is global or bounded to a signature region;
- asset fidelity and media framing;
- post-processing only when it materially changes the look.

### 5. Motion

Capture:
- triggered vs scrubbed motion;
- continuous vs one-shot motion;
- spatial, opacity, blur/focus, mask, scale, or typographic mechanisms;
- easing/staging character;
- which moments are intentionally still.

### 6. Interaction + Input Grammar

Capture:
- navigation behavior;
- pointer, hover, drag, scroll, keyboard, touch, and sound roles;
- whether input affects content, world materiality, camera, state, or only decoration;
- recovery and accessibility behavior.

### 7. Narrative + Proof

Capture:
- information order;
- what tension/question is introduced first;
- where social proof appears;
- how claims turn into demonstrated work/product evidence;
- where conversion happens relative to trust-building.

### 8. Responsive Behavior

Capture:
- what survives unchanged because it is core identity;
- what changes scale only;
- what reflows or changes hierarchy;
- what is removed because it is expendable;
- touch and mobile performance adaptations.

### 9. Performance + Accessibility

Capture only relevant evidence:
- pixel-ratio caps and quality tiers;
- expensive-loop visibility bounds;
- media lazy loading/posters;
- animation cleanup and hidden-tab behavior;
- explicit sound opt-in;
- accessible names, keyboard path, focus visibility, reduced-motion and semantic continuity.

## Signature vs System

Separate two layers before reusing anything:

- **Signature** - the rare, memorable move that gives this particular source identity.
- **System** - the quieter rules that make the whole experience coherent and production-ready.

The goal is rarely to transplant the signature literally. Preserve the **allocation of ambition**: understand why one moment earns unusual type, 3D, motion, sound, or color while the rest of the page stays disciplined.

## One Signature Stage

For premium marketing/editorial experiences, prefer **one signature stage** over distributing equal spectacle across every section.

A signature stage may be a hero renderer, a product demo, a strong editorial composition, or a single motion sequence. Surround it with quieter structure so the high point has contrast.

This rule does not mean every site needs a cinematic hero. Product fit still decides whether the signature is visual, interactive, informational, or absent.

## Bounded Immersive Rendering

If a reference gains impact from WebGL/canvas/continuous animation, extract the performance contract with the look:

- render expensive worlds only while they are visible/relevant;
- cap effective pixel ratio instead of blindly following device DPR;
- own resize/breakpoint state explicitly;
- smooth pointer/world signals before feeding them into material/camera state;
- separate the immersive renderer from ordinary DOM/editorial content;
- preserve a usable non-WebGL/reduced-motion path when the product needs it.

Do not imitate "premium" by leaving a heavy renderer running through the whole page.

## Motion as Focus, Not Confetti

High-end motion often changes **attention** more than position.

Blur, opacity, line/word splitting, focus depth, controlled reveals, and deliberate pauses can create a cinematic experience without translating every block. Prefer a motion hierarchy:

1. input/state feedback;
2. one or two authored narrative transitions;
3. continuous scrub only where a continuous relationship matters;
4. ambient motion only after the first three are justified.

The number of animation triggers is not itself a quality signal. Ask how many motions require continuous ownership and how many can be discrete.

## Responsive Brand Payload

Mobile adaptation should preserve the smallest set of traits that still makes the experience unmistakably itself. Call this the **Responsive Brand Payload**.

Preserve, when they are truly identity-bearing:
- the signature visual/world or an equivalent reduced version;
- the distinctive type-role contrast;
- the dominant composition idea;
- the narrative order;
- recognizable project/media treatment.

Compress scale, scroll distance, secondary motion, decorative labels, and proof density before deleting the brand-defining idea and replacing it with a generic stacked template.

## Proof Before Fireworks

When the product depends on trust, social proof can precede the most visually ambitious case-study/product showcase. A useful narrative pattern is:

**tension/problem - credibility/proof - thesis - demonstrated evidence - validation - conversion**

Do not apply this mechanically to transactional products, dashboards, or flows where immediate task completion matters more than persuasion.

## Editorial Case Study, Not Card Grid

For portfolio/case-study surfaces, do not assume each project should be a rounded card. An editorial spread can separate project name, narrative, capabilities/metadata, and media across a grid, then give each project its own surface/color world.

Use card containment only when it clarifies interaction, comparison, or repeated data structure.

## Reflective Case Study Arc

Portfolio proof becomes more credible when a case study shows judgment, constraints, and learning rather than presenting a frictionless success story.

A useful arc is:

**context / real problem -> approach / fix -> what happened -> measurable or observable change -> constraints -> what I would do differently -> what I learned**

Use the parts that are truthful and relevant. The sequence may change, but preserve the distinction between:
- the problem as experienced by users/business;
- the designer/team's intervention;
- evidence of what changed;
- constraints or tradeoffs that shaped the work;
- reflective learning after delivery.

Do not fabricate outcomes, metrics, research, constraints, or retrospective lessons to make a portfolio appear mature. A shorter truthful case study is stronger than a polished fictional postmortem.

## Persistent Context Rail

Long editorial, portfolio, documentation, or article routes can keep local orientation visible while the main content scrolls.

A Persistent Context Rail may hold:
- section labels or local navigation;
- article metadata and summary;
- project role/date/status;
- progress markers;
- related anchors that help the reader understand where they are.

Use sticky/fixed context only when it reduces cognitive reset. The rail must not steal too much viewport, cover reading content, or become the only way to understand the page.

Responsive rule:
- keep the information if it matters;
- change sticky geometry when viewport width/height makes it intrusive;
- convert to an inline block, compact rail, or released-flow section when necessary;
- preserve keyboard/touch access and reading order.

## Experimental Surface Isolation

A portfolio, studio, or expressive brand can support a highly playful interaction without forcing that interaction model onto every task-oriented route.

When an experiment is valuable primarily for personality, exploration, or creative range:
- give it a bounded route/section with an explicit interaction grammar;
- keep core portfolio, case-study, article, contact, and conversion routes conventionally navigable;
- let the experiment use drag, collage, freeform spatial layout, unusual cursor behavior, or other higher-risk input patterns only inside its boundary;
- preserve an obvious escape/navigation path;
- ensure the experiment does not become required evidence for understanding the person's work.

This pattern allows **identity overflow without usability spillover**.

## World Metaphor as Information Architecture

A strong world metaphor can organize an entire portfolio, studio, cultural, education, or narrative product when the metaphor maps cleanly to real information jobs.

Examples of functional translation:
- projects -> field entries / creatures / artifacts;
- disciplines -> types / classes / schools;
- services -> quests / missions / packages;
- achievements -> seals / badges / milestones;
- experience -> stats / levels;
- taxonomy overview -> map / isles / constellations;
- contact -> save point / camp / checkpoint.

The metaphor is valuable only when it creates **memory, navigation, and cohesion at the same time**.

Rules:
- each metaphor term must map to one stable product/content concept;
- the mapping must stay consistent across home, indexes, details, CTA, navigation, and mobile;
- conventional labels should remain available in context, metadata, URLs, headings, or supporting copy when the metaphor alone could be ambiguous;
- route jobs must remain understandable without learning fictional lore first;
- decorative lore must not replace proof, pricing, contact details, accessibility, or legal clarity.

Use this pattern when the world model reduces cognitive fragmentation. Do not invent a fantasy vocabulary merely to make a normal sitemap sound clever.

## Taxonomy as Visual Physics

A category system can become part of the site's visual behavior instead of remaining a filter menu.

When a stable taxonomy matters, let each category consistently influence a bounded set of identity variables such as:
- accent family;
- badge / glyph / emblem;
- illustration or creature family;
- local background/surface tint;
- metadata label;
- motion character;
- map position or collection grouping.

This creates recognition across index, detail, navigation, and related-content surfaces.

Keep the semantic category name available. Color or illustration must never be the only carrier of category meaning.

Do not let category theming fragment the global shell. The taxonomy should act like visual physics inside one coherent world, not six unrelated mini-sites.

## Mnemonic Case-Study Encoding

Portfolio work becomes easier to remember when each project has a compact mnemonic identity layered on top of normal proof.

A mnemonic identity may combine:
- a short project codename or creature/object name;
- a number or collection position;
- one category/type;
- a distinctive illustration, shape, or emblem;
- one short premise.

Keep the sober evidence underneath:
- client or product;
- year/timeframe;
- work/scope;
- problem/brief;
- intervention;
- result/outcome;
- related/evolved work.

The mnemonic layer helps recall and collection behavior; it must not hide who the work was for, what was actually done, or whether the result is real.

Do not fabricate metrics or use cute naming as a substitute for case-study substance.

## Metaphor Translation Contract

Playful or diegetic language must remain operationally decodable.

For every metaphor-heavy route or control, maintain a translation contract:

**world term -> real user job -> visible cue -> accessible/conventional fallback**

Examples:
- `Fieldbook` -> project portfolio -> project cards + client/work metadata -> descriptive page title/URL;
- `Quest` -> fixed-scope service -> price/timeline/deliverables -> explicit service copy;
- `Save point` -> contact/conversion -> email/form/response expectation -> standard form labels;
- `Isles` -> discipline taxonomy -> named destinations -> text category list/tappable controls.

QA questions:
- can a first-time visitor infer the job within seconds?
- does keyboard/screen-reader interaction expose the real action?
- is the route title/metadata conventional enough for search and sharing?
- on mobile, where hover is absent, does the meaning remain visible?

Use metaphor for identity and memory, not for obscurity.

## Project Evolution as Relationship Proof

When a later project genuinely grows from earlier work, show the relationship explicitly.

A useful sequence is:

**original engagement -> what changed in the client/product -> expanded problem -> evolved system -> new observable outcome**

This can prove:
- client continuity;
- system scalability;
- maturity of the original design;
- ability to extend rather than restart;
- deeper understanding earned over time.

Do not manufacture an evolution narrative between unrelated projects. Relationship proof works only when the lineage is real and clearly explained.

## Commercial Core + Trust Satellites

Small B2B, service, agency, and focused SaaS sites do not always need a large route ecosystem. A useful architecture is one commercial core plus a few supporting trust routes.

Use the commercial core to concentrate the buying story:
- promise / positioning;
- benefits and capabilities;
- service or product explanation;
- process / delivery model when it matters;
- proof / projects / outcomes;
- pricing or engagement model;
- differentiation / objections;
- FAQ and conversion.

Use satellite routes only when they deserve independent depth, such as:
- contact;
- privacy / legal;
- changelog / updates;
- help or documentation;
- other trust/support material.

Navigation from a satellite route may deep-link back into meaningful sections of the commercial core when that is clearer than duplicating the entire sales narrative.

Do not force a five-page corporate sitemap onto a focused offer merely to look mature. Conversely, do not cram security, legal, documentation, or long-form trust material into one landing page when separate routes improve comprehension or accountability.

## Pricing-to-Comparison Bridge

When pricing appears before the visitor has fully resolved the question "why this option instead of the alternative?", follow packaging with a focused comparison layer.

A useful bridge is:

**plan / offer -> included value -> comparison criteria -> objection resolution -> next action**

Comparison criteria must be:
- specific enough to matter to the buying decision;
- symmetric enough to compare fairly;
- supported by real product/service capability;
- written without inventing competitor deficiencies.

Good comparisons can contrast:
- manual vs automated workflow;
- generic vs tailored scope;
- batch vs real-time availability;
- limited vs scalable capacity;
- included vs excluded support;
- delivery speed, governance, integration, or service level when verifiable.

Do not use a vague "Us vs Others" table filled with unsubstantiated superiority claims. If the difference cannot be defended, use a buyer-fit guide, scope table, or FAQ instead.

## Product Evidence Before Feature Claims

For technical products, a strong marketing page should let the visitor inspect believable product evidence before asking them to accept a long list of abstract capabilities.

Prefer proof surfaces such as:

- authentic product UI in the same state the claim describes;
- a code/API example that could plausibly be copied into a real project;
- a small interactive demo with safe, reversible controls;
- logs, status, analytics, delivery state, or other observable outputs;
- ecosystem choices that let the visitor select the language/framework relevant to them.

The evidence does not need to be a fully functional embedded application, but it must preserve the product's real information model and visual/interaction character. Do not replace specific proof with a decorative dashboard mockup whose metrics and controls exist only to make the page look technical.

Use the sequence **claim -> inspectable evidence -> explanation** when the product is best understood by seeing it work. Reverse the order when context is required before the evidence makes sense.

## Code as Product Proof

For developer tools, code can carry the same persuasive weight that product photography carries for a physical product.

When code is used as proof:

- show the shortest authentic path to the promised outcome;
- preserve real package names, API shape, request/response structure, and syntax conventions;
- let users switch language/framework only when those variants are genuinely supported;
- keep code copyable/readable rather than turning it into tiny decorative texture;
- pair code with the resulting product/system state when the cause-and-effect relationship matters;
- syntax color should support scanning, not become the page's primary decoration.

Do not fabricate an API surface merely because a code panel looks credible. Source truth outranks visual drama.

## Responsive Fidelity Substitution

Responsive design does not require the same rendering mechanism at every breakpoint. Preserve the **perceptual job** and identity-bearing result, then choose the cheapest reliable mechanism appropriate to the device.

Examples:

- live interactive 3D on desktop -> pre-rendered video or still sequence on mobile;
- dense multi-pane demo -> focused single-pane state on small screens;
- pointer-reactive effect -> touch-safe passive motion or static material cue;
- continuously animated visualization -> poster plus user-triggered playback under constrained conditions.

This is different from simply deleting the signature experience on mobile. The mobile variant should still carry the same subject, silhouette, material language, narrative role, and approximate visual weight when those traits are identity-bearing.

When applying this pattern, verify both sides:

1. desktop is not paying for a low-fidelity fallback when richer interaction materially improves the story;
2. mobile is not paying desktop's runtime/rendering cost merely to claim implementation parity.

Record the substitution explicitly in the responsive contract so QA compares **equivalent experience value**, not identical implementation technology.

## Conversation-to-Action Proof

For AI agents, copilots, and automation products, a chat transcript alone rarely proves the product can do useful work.

When the product genuinely supports it, show a causal sequence such as:

**intent / question -> contextual answer -> source / confidence -> artifact or action -> next operational state**

Good proof may include:
- what the user asked;
- what context, documents, systems, or prior state informed the answer;
- where sources/provenance are surfaced;
- the draft, ticket, update, workflow step, or other artifact produced;
- the resulting system state or next action.

The goal is to prove that conversation connects to work. Do not fabricate citations, tool access, integrations, actions, approval state, or autonomy merely to make the mockup persuasive.

Use Conversation-to-Action Proof when the product's differentiation is execution, trustworthy context, or workflow continuity. For pure chat products, the shorter conversational loop may be sufficient.

## Operational Pipeline Storytelling

For complex AI, automation, infrastructure, or orchestration products, a flat feature list often hides how the system actually produces value.

When the product genuinely has multiple operational stages, explain it as a causal pipeline such as:

**engine/model -> context/data -> agent/workspace -> tools/integrations -> workflow -> observable output**

Use this pattern when:
- each stage has a distinct responsibility;
- the relationship between stages matters to trust or comprehension;
- the visitor needs to understand where data enters, how decisions are made, what systems are touched, and what output appears.

Prefer believable product/system evidence at each stage. Do not invent architecture or stretch a simple product into an artificial pipeline merely to look sophisticated.

## Proof Surface Cropping

Responsive marketing proof does not always need to scale the entire product UI down until it fits the viewport.

When shrinking would make the proof unreadable:
- keep the outer proof viewport within the document width;
- allow the inner proof surface to remain larger;
- crop with overflow hidden/clip around an intentional focal region;
- preserve zero unintended document-level horizontal overflow;
- never crop away controls/content that users must interact with to complete a task;
- use accessible pan/scroll/focus affordances when offscreen content is required.

This is a marketing-evidence technique, not a substitute for making the actual product responsive.

## Credibility Through Route Ecosystem

For high-trust products, credibility can be a whole-site architecture problem rather than a single testimonial/security-logo section.

Use adjacent routes to independently support the same product truth:

- integrations prove ecosystem fit;
- pricing proves operational packaging and limits;
- company content explains who is building the system and why;
- technical resources demonstrate domain depth;
- legal/security/privacy routes make constraints and commitments inspectable;
- careers reveal whether the claimed disciplines exist in the organization;
- contact/demo routes support the actual buying motion;
- FAQ/help resolves recurring objections.

The routes should reinforce one coherent operating model without fabricating customers, compliance, technical claims, metrics, legal guarantees, or organizational maturity.

## Confidence as Interface

When a product publishes uncertain, editorial, sampled, stale, or partially verified data, confidence is part of the information model and should appear in the interface.

Prefer:
- a small, consistent confidence vocabulary;
- visible source/freshness status near records or metrics;
- a methodology route that defines the vocabulary;
- per-record caveats only when they materially differ;
- visual precision that matches evidentiary precision.

Do not render an approximate value with authoritative visual weight while hiding uncertainty in footer legal copy.

## Route-Family Density Ladder

One structured dataset may need several visual projections.

Choose density by route purpose:

1. orientation/home - a few extracted facts and a compact preview;
2. directory/list - medium-density scanning;
3. compare - maximum useful density;
4. detail - one-record depth;
5. methodology/provenance - trust model;
6. glossary/help - cognitive support.

Keep tokens, semantics, and data meaning stable while changing the container and density. Do not force one card component across every route merely for consistency.

## Contain Horizontal Density, Don't Crush It

For genuinely comparative tables, preserving column relationships may matter more than eliminating horizontal scrolling.

When the comparison needs many columns:
- give the table a readable minimum width;
- put overflow on an internal table container;
- keep the outer document horizontally stable;
- retain column labels, sort controls, and semantic table structure;
- collapse surrounding grids before compressing critical metrics;
- consider changing sticky-header behavior at narrow widths.

Horizontal scrolling inside a clearly bounded comparison surface can be the correct responsive behavior. Document-level overflow is not.

## Human + Machine Surface Parity

Public reference, catalog, documentation, and data products should maintain the same information architecture in human-facing and machine-readable surfaces.

When appropriate, keep these aligned:
- sitemap and canonical routes;
- robots/crawler policy;
- llms.txt or equivalent AI-readable summary;
- structured metadata and search actions;
- visible route names, data scope, confidence vocabulary, and freshness caveats.

Machine-readable surfaces should not silently omit limitations that materially qualify the visible data, and they should not describe routes or facts that no longer match the human product.

## Pattern Promotion

Site profiles start as **site-specific evidence**, not universal truth.

Promote a pattern from a site profile into general design guidance only when at least one is true:

- the mechanism directly solves a recurring design problem;
- multiple strong references independently demonstrate the same principle;
- the pattern follows from a durable technical/perceptual constraint;
- local benchmark results show it improves outcomes across more than one brief.

Keep highly branded signatures in the site profile even if they are memorable.

## Transfer Matrix

Before using a reference-derived pattern on a new project, classify it:

| Decision | Meaning |
|---|---|
| Adopt | The mechanism directly fits the new product and can transfer with new visual/content values. |
| Adapt | The underlying principle fits, but form, intensity, hierarchy, or technology must change. |
| Avoid | It is signature-specific, conflicts with product usability, or would become imitation/cargo cult. |

Write the reason, not just the label.

## Site Profiles

Detailed evidence lives under:

`references/design-intelligence/sites/<domain>.md`

Load a site profile only when it is relevant to the current brief. Do not preload every inspiration profile; that would turn reference intelligence into style averaging.

A site profile should include:
- source and audit date;
- what was actually inspected;
- confidence labels;
- Design DNA;
- runtime/source architecture when known;
- responsive evidence;
- reusable mechanisms;
- signatures not to copy;
- adopt/adapt/avoid guidance;
- briefs where the profile is useful or misleading.

## QA for Reference-Derived Work

When a design deliberately borrows a mechanism from a profile, verify the **intended property**, not resemblance to the source.

Examples:
- if using "one signature stage," verify the rest of the page is actually quieter;
- if using section-owned color worlds, verify each palette belongs to the new content rather than mimicking the source;
- if preserving Responsive Brand Payload, compare desktop/mobile and name what identity-bearing traits survived;
- if using Bounded Immersive Rendering, verify the heavy loop stops or idles outside its active region.

A successful distillation should produce a site that belongs unmistakably to the new product while benefiting from stronger design judgment learned from the reference.

## Route-Complete Developer Product Ecosystems

Do not infer the whole product design from one cinematic homepage. Use sitemap-index recursion and classify route jobs: product/features, stack-specific integration, migration bridge, API reference, dashboard task docs, knowledge base/provider guides, changelog, blog, customers, public operating handbook, human attribution, security/legal and independent campaigns.

**Three-Rail Documentation Reader:** fixed global header + left route tree + an independently scrollable article + right outline are a distinct scroll-ownership system. Verify keyboard focus, anchors, internal overflow and small-screen behavior, not only document scrollWidth.

**Migration Converter Bridge:** real competitor-to-product mappings and code transformation reduce switching friction more than slogans.

**Public Operating System as Trust Proof:** publish genuine engineering/design practices and people contributions when safe. Do not replace product proof with superficial culture photography.

**Sitemap Status Parity:** a route declared in an XML sitemap still needs live status and semantic validation. Do not confuse a sitemap index count with the count of underlying URLs.

## Game Commerce Route Integrity

For game-focused ecommerce templates, audit the complete CMS inventory, not only featured cards: split campaign, store, product detail, category, editorial, subscription, company/help and error route jobs. Adopt **Game Discovery -> Marketplace Bridge** only when real item names, prices, links and actions remain usable. Separate recurring member plans from one-off item checkout.

Never promote unrelated imported product fixtures as genre taxonomy. A clean campaign hero and six polished featured game cards can conceal dozens of toy/beauty/home/sports records. Check sitemap-to-title specificity, cart action semantics and reusable footer/header behavior.

Select **cinematic-game** for the genre identity and **premium-ecommerce** conversion mechanisms without creating a redundant skin or copying vendor imagery.

## AI SaaS Marketing to Authentication Route Continuity

When a marketing site links to account-related routes, audit the full declared public system: homepage/anchors, lead/contact, sign-up, sign-in, OTP, account, terms, privacy and 404. Distinguish real checkout/trial from **contact-first lead conversion**. Sample pricing interaction and reduced-motion metric states; visible static pricing and social proof are not evidence of genuine billing or successful customer outcomes.

FrameAuth- or vendor-powered screens are useful evidence of **branded auth shell continuity** but do not establish secure session guards, rate limits, code delivery or token handling. Keep interaction/security claims clearly labeled observed vs not tested.
