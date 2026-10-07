# Baseline Skin: Game Studio

Nexira audited template anchor: ../sites/nexira.framer.ai.md

This skin serves game studios, entertainment brands, service/outsourcing teams, fictional-world portfolios, and cinematic game marketing that needs strong world identity without automatically requiring a high-cost real-time renderer.

Nexira contributes full-site audited evidence for image-led game-studio marketing: condensed display type, dark shell + acid accent, services/case route families, sticky project decks, mobile sticky preservation where it still reads well, and Cinematic Without Heavy Rendering.

For a single franchise/game launch with campaign chapters, trailer orchestration, aspect-ratio art direction, and launch conversion, prefer open-world-cinematic-launch.md.

## Game Studio Routing Boundary

Choose this skin when the organization/studio is the product being marketed:
- game development or outsourcing studio;
- art/animation/character/rigging service company;
- indie studio portfolio;
- publisher/studio corporate presence;
- service + case-study + team + editorial ecosystem.

Do not use this skin when:
- one specific game/franchise launch is the dominant story -> use open-world-cinematic-launch.md;
- the brief is generic entertainment/game marketing without a studio/service proof ecosystem -> use cinematic-game.md;
- a continuous authored 3D world/camera is the product experience -> route implementation through experience-engineering / scroll-world after the design-intelligence decision.

The distinguishing information architecture is capability + proof + people:
service/capability -> case/project evidence -> team/studio credibility -> editorial/contact support.

## Use when

Use for:
- game development studios;
- indie studio portfolios;
- game art/animation/character/rigging services;
- publisher/studio corporate sites;
- entertainment campaigns with still-art-first identity;
- team/case/service sites where game-feel matters;
- launch-adjacent marketing that does not require a continuous world runtime.

If a true authored world, continuous camera, scroll-cinematic renderer, or synchronized 3D state is required, route architecture to experience-engineering or scroll-world.

## Deterministic Design Scaffold

Start with the Game/Experiential Audit Lens.

Then choose the cheapest mechanism that can honestly carry the identity:
1. still-image cinematic composition;
2. authored crop + scale + sticky editorial sequencing;
3. lightweight CSS/Framer motion;
4. pre-rendered video;
5. canvas/WebGL only when the story actually needs continuous rendered state.

This protects lower-capability execution from trying to simulate premium work by adding fragile effects everywhere.

## Token Scaffold

- world-derived dark/neutral shell, typically #171717-#242424 class;
- strong readable light text;
- one faction/world/brand accent plus semantic states;
- optional secondary signal accent used sparingly;
- compact HUD/meta sans or mono;
- high-character condensed/display role for world identity;
- readable neutral sans for body/UI;
- radius 0-10px by default for media/HUD surfaces;
- service/case stages may use 0-16px if the brand is softer;
- content-safe width about 1120-1300px layered over wider art;
- section spacing roughly 96-160px desktop;
- mobile spacing roughly 64-112px;
- large route heading about 52-80px desktop, 36-56px mobile;
- body about 15-18px;
- keep borders, brackets, ticks and metadata thin enough to remain secondary to art.

Nexira uses an acid #adff00 + dark #1d1d1d/#222 family with #ffd335 as a secondary accent. Treat that as evidence of one coherent gaming grammar, not a default palette.

## Typography Roles

Recommended role split:
- world/display: condensed or high-character;
- route/section heading: same family or controlled companion;
- body/UI: neutral sans;
- metadata/HUD: compact sans or mono only when it has a real information job.

Nexira uses Oswald for display and Inter for most body/UI roles, with Fragment Mono bundled in source. Transfer the role contrast, not the exact fonts.

## Composition Grammar

### Studio / home

Reliable sequence for a studio site:
1. world/identity hero;
2. studio thesis + scale/proof;
3. capabilities/services;
4. cases/projects;
5. awards/recognition only when real;
6. editorial/news or community;
7. install/download/contact conversion;
8. footer.

Do not force every gaming site into this exact order. Each section must answer a distinct visitor question.

### Hero

Use:
- one strong still or bounded media field;
- clear title and studio/game identity;
- platform/action metadata only when real;
- one primary action;
- optional secondary action.

HUD-like labels remain subordinate to the hero title and actual navigation.

### Studio proof

Possible evidence:
- shipped/live games;
- player/community scale;
- team size;
- partner/publisher status;
- verified awards;
- real testimonials;
- project count;
- release platforms.

Never fabricate these to make a studio template look established.

## Cinematic Without Heavy Rendering

Prefer static/low-cost cinematic mechanisms when they can carry the brief:
- high-quality still art;
- strong crop;
- high-character display type;
- dark/light contrast;
- one world accent;
- bracket/HUD labels;
- sticky stages;
- overlapping composition;
- restrained Framer/CSS motion.

A site does not become more cinematic merely because it uses WebGL.

Earn the renderer only when continuous camera/world/material state communicates something the static system cannot.

## Capability-to-Case Pairing

For studios that sell services, separate capability from proof.

Capability routes explain:
- what is offered;
- scope;
- process;
- methods/tools when relevant;
- expected deliverable.

Case routes prove:
- project/situation;
- role;
- constraints/challenges;
- work/media;
- decisions;
- outcome/results when real.

Recommended route model:
- home service preview;
- service index;
- service detail;
- home case preview;
- case index;
- case detail.

Cross-link service -> relevant case and case -> relevant capability when it improves understanding.

Do not repeat the same marketing paragraph across both families.

## Sticky Service / Project Sequencing

Optional signature for desktop or mobile.

Use sticky stages when:
- each item can own a substantial viewport;
- image + text remain readable during overlap;
- scroll ownership helps comparison or progression;
- stage height is intentional.

Nexira shows two distinct strategies:
- service cards are strongly sticky on desktop but individual service-card stickiness releases on mobile;
- project/case cards remain sticky on mobile because each becomes a readable full-stage chapter.

Therefore responsive logic should follow the mechanism's job, not a blanket rule to remove sticky at a breakpoint.

## Case Index

Good project index anatomy:
- year/status/category;
- project name;
- short context;
- strong art/media;
- obvious route into detail.

A large sticky deck can replace a generic card grid when the projects themselves are the identity.

## Case Detail

Recommended truthful anatomy:
- project title;
- short context;
- role/team;
- client only when public;
- timeline/year;
- budget only when appropriate and publishable;
- hero/project media;
- role/work performed;
- challenges and decisions;
- results/outcomes;
- related capability or next project.

A desktop Persistent Context Rail may hold project metadata, but release it on mobile when it competes with reading.

## Service Index / Detail

Service index:
- service title;
- one-sentence outcome;
- optional image/art sample;
- route into detail;
- conversion after enough capability context.

Service detail:
- service title;
- what it is;
- what work includes;
- process;
- tools/technical constraints when useful;
- expected output;
- relevant case links.

Do not pad service detail with generic game-development prose.

## Team / About

Use about for:
- studio thesis;
- verified history;
- selected team;
- journey/process;
- contact.

Use team for:
- broader people visibility;
- role clarity;
- social/professional links only when real.

Do not invent founders, awards or decades of history.

## Editorial / Blog

Use editorial content to demonstrate thinking and process, not just SEO quantity.

Index should expose:
- topic/category;
- date when real;
- clear headline;
- readable route into article.

Article detail should be calmer than the home page:
- title;
- date/category;
- lead image;
- structured headings;
- readable paragraphs;
- supporting images.

Do not keep sticky spectacle active through long-form reading unless it truly helps orientation.

## Contact

Keep conversion conventional:
- phone/email/location only if real;
- short form;
- visible labels;
- success/error states;
- touch-safe mobile width;
- no custom interaction required to submit.

## Skin Lock

Lock:
- world/chrome hierarchy;
- type roles;
- accent semantics;
- art/media framing;
- metadata/bracket grammar;
- sticky ownership rules;
- Capability-to-Case Pairing;
- responsive identity priorities;
- motion hierarchy;
- proof truthfulness.

## Controlled Mutation

May mutate:
- world accent;
- dark-shell temperature;
- typography families;
- hero composition;
- art crop;
- service/case stage geometry;
- whether sticky survives mobile;
- metadata styling;
- editorial/news presence;
- one signature interaction;
- media cost tier.

Must mutate away from audited identities:
- Nexira name/logo;
- exact Oswald + Inter pairing;
- exact #adff00 / #ffd335 palette;
- exact images/art;
- team names;
- case names/content;
- fake budgets/clients/years/results;
- award names;
- DOWNLOAD LAUNCER wording;
- REDDEVS 2024/vendor identity;
- Framer badge/editor chrome.

## Responsive Contract

Preserve the Responsive Brand Payload:
- display/body role contrast;
- dark/light world grammar;
- recognizable project art treatment;
- capability -> proof narrative;
- one identity-bearing scroll/media mechanism.

Adapt:
- large headings;
- multi-column service/team grids;
- route hero height;
- image crop;
- sticky ownership;
- metadata density;
- navigation complexity.

Use job-based sticky decisions:
- keep stage-like sticky cards if each is still readable and intentional;
- release sticky sidebars/rails that obstruct long-form reading;
- never allow sticky overlap to hide focusable content.

Required:
- no unintended document-level horizontal overflow;
- touch-safe controls;
- forms stay within viewport;
- text stays readable over art;
- reduced-motion users retain content/navigation.

## Motion Language

Priority:
1. navigation and input feedback;
2. sticky stage continuity;
3. gallery/carousel/index state;
4. one or two authored reveals;
5. optional ambient motion.

Avoid:
- random glitch effects;
- universal parallax;
- autoplay media layers with no narrative job;
- fake HUD movement;
- continuous animation that competes with project art;
- pointer-only controls.

## Anti-Template Guard

High-risk game-studio template bundle:
- charcoal shell;
- acid-lime accent;
- Oswald/condensed all-caps headings;
- bracket labels;
- giant game character still;
- sticky project cards;
- fake awards;
- fake player counts;
- team grid;
- game-dev blog;
- download launcher CTA.

Any individual choice can work. Using the whole bundle unchanged creates Template Convergence Risk.

Require structural differentiation in at least one:
- studio proof model;
- capability taxonomy;
- case-study narrative;
- art direction;
- typography system;
- interaction grammar;
- route architecture;
- responsive transformation.

Changing only logo/name/accent is not enough.

## QA Rubric

Pass only if:
- the Game/Experiential Audit Lens has been applied;
- HUD/chrome stays subordinate to content;
- Cinematic Without Heavy Rendering remains intentional rather than cheap;
- the renderer/media cost matches the story;
- Capability-to-Case Pairing lets visitors understand offer and proof separately;
- sticky stages have a clear job;
- mobile sticky behavior is explicitly verified rather than inherited accidentally;
- case-detail reading is not trapped behind desktop geometry;
- team/awards/metrics/cases are truthful;
- article routes are readable;
- contact remains conventional and accessible;
- no document-level overflow;
- reduced-motion and non-pointer users keep a usable path;
- the design remains distinctive after removing Nexira's exact fonts, lime accent, art, names, awards and template copy.
