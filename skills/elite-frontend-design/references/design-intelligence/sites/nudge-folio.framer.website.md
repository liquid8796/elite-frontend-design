# Nudge Folio - full-site distilled design intelligence

Source: https://nudge-folio.framer.website/
Audit date: 2026-10-07
Coverage: 19/19 sitemap URLs

Audit scope: sitemap/robots discovery, Framer search-index cross-check, full same-origin internal-link graph, generated HTML/CSS for every public route, all 8 blog detail pages, all 4 case-study detail pages, desktop runtime inspection, mobile 390px checks across representative route families, typography/tokens, sticky/fixed behavior, draggable playground behavior, and template-vendor residue.

This is a whole-site profile, not a homepage-only read.

## Coverage manifest

Primary routes:
- /
- /about
- /case-study
- /blog
- /services
- /play-ground
- /contact

8 blog detail pages:
- /blog/ideas-need-silence
- /blog/geometry-builds-trust
- /blog/everyday-beauty
- /blog/the-power-of-focus
- /blog/a-greener-workspace
- /blog/the-creative-desk
- /blog/materials-and-memory
- /blog/beyond-the-screen

4 case-study detail pages:
- /case-study/meridian-health
- /case-study/stylebook
- /case-study/homestead
- /case-study/north-light

The Framer search index exposes the same 19 route keys. A complete same-origin internal-link crawl found no additional public route.

## Landscape classification

Primary: template commodity, audited.
Secondary: experiential / agency + portfolio/editorial.

Nudge identifies itself as "Nudge - Premium Portfolio Template" and exposes a fixed "BUY NUDGE" action. Use it as an execution baseline and portfolio-system teacher, not as a clone source.

## Evidence confidence

### Source-confirmed platform

- Generator: Framer bc64f0a.
- robots.txt points to /sitemap.xml.
- Sitemap contains 19 URLs.
- Framer search index contains the same 19 route keys.
- /llms.txt is absent.
- Main generated breakpoint branches appear at 810px and 1200px.
- Runtime html classes include "lenis lenis-autoToggle".
- Main Framer bundle contains GSAP code and Draggable implementation.
- Conventional routes use a fixed global navigation layer.

### Source-confirmed typography

Loaded/generated families include:
- Flux Variable
- Inter Display
- DM Mono
- Just Me Again Down Here
- Inter
- Geist Mono
- Fragment Mono

Observed roles:
- Flux Variable: oversized personality/display.
- Inter Display: project titles, section statements, readable large copy.
- DM Mono: metadata and structural labels.
- Just Me Again Down Here: handwritten annotation/personality voice.

Transfer the role separation, not the literal font stack.

### Source-confirmed color tokens

Shared generated tokens include:
- #111212 near-black
- #f1f1f1 / #ededed pale neutrals
- #ffffff
- #36c5f0 blue
- #ecb22e yellow
- #2fbc81 green
- #e01e5a pink/red
- #522e29 dark brown
- #a4e5f8 light blue
- #a1dfc5 light green
- #fabed1 light pink
- #f5dda1 light yellow
- #19bd8c teal

Treat this as a playful accent family, not a palette to copy verbatim.

## Desktop system

Representative audit: 1440x900.

Homepage observations:
- document roughly 7.8k px tall;
- hero "Bejaman" around 150px / 120px in Flux Variable;
- major FEATURED WORKS / conversion headings around 120px / 96px;
- project titles around 68px / 74.8px Inter Display;
- handwritten note role around 32px;
- supporting statements around 40px / 48px;
- fixed global navigation;
- fixed intro overlay "Welcome! / Hey there!" fades to opacity 0 after entry;
- custom cursor/pointer layer exists in fixed runtime stack;
- template-vendor BUY NUDGE control is fixed near bottom-right.

### Full-viewport project stack

Featured work contains four desktop project stages:
- Meridian Health
- StyleBook
- Homestead
- North Light

Runtime evidence:
- project panels are position: sticky;
- top: 0px;
- roughly 1224px wide;
- roughly one viewport high at a 900px viewport.

The mechanism creates a stable editorial stage while project meaning changes.

## Mobile system

Representative audit: 390px.

Across home/about/services/contact/case-study/blog/playground samples:
- document width remained 390px;
- no document-level horizontal overflow was observed;
- full navigation collapses to Menu;
- homepage H1 drops from about 150px to about 80px / 64px;
- homepage full-viewport sticky project stages are released from sticky behavior;
- case-study title is roughly 56px / 44.8px;
- blog detail title is roughly 28px / 30.8px;
- services keeps an oversized 80px-class personality display role;
- contact keeps the handwritten prompt role;
- about keeps local context but changes geometry;
- blog detail keeps a narrower sticky metadata/summary block;
- playground remains a viewport-locked draggable spatial canvas.

Responsive lesson: preserve type-role identity, proof order, and project personality before preserving desktop spatial tricks.
## Design DNA

### Composition

Nudge separates the portfolio into clear proof modes:
- home = personality + featured-work orientation;
- case-study index = fast project scan;
- case-study detail = long reflective proof;
- about = biography + work principles + selected projects;
- services = capability framing + process + FAQ;
- blog = editorial thinking;
- contact = focused conversion;
- playground = experimental identity surface.

The reusable lesson is route specialization under one visual grammar, not forcing every route into one repeated card system.

### Typography role collision

Nudge combines:
- extreme heavy variable display;
- clean large sans;
- tiny mono metadata;
- handwritten annotation.

The system works because each family owns a distinct semantic role.

Transfer rules:
- do not mix multiple expressive faces inside one semantic layer;
- keep body/readable copy quiet enough for display roles to retain contrast;
- reduce scale on mobile before deleting role distinctions;
- reserve mono for metadata/structure, not terminal cosplay.

### Color and project worlds

The global shell is mostly neutral/light with strong black typography. Individual project/art surfaces introduce more varied color.

Coherence comes from:
- typography;
- fixed navigation;
- spacing;
- repeated metadata;
- project framing;
- shared CTA/footer grammar.

This lets projects own different image/color worlds without making the site feel unrelated.

## Route-family map

### Home

Purpose: personality + portfolio orientation.

Observed:
- entry overlay;
- giant name/identity statement;
- small personality/about cue;
- capabilities;
- FEATURED WORKS;
- four sticky project stages;
- oversized Let's Talk conversion;
- Contact footer.

Home acts as a high-confidence index rather than a compressed version of every case study.

### About

Purpose: biography, principles, selected proof.

Observed:
- giant About title;
- small mono "Main bio" label;
- sticky local context rail with Bio / Story / Work;
- principles including "Starting with why, not what", "Designing for real constraints", "Collaboration over hero design", and "Making the invisible visible";
- selected project links;
- shared conversion/footer.

Desktop runtime shows the local context rail sticky around top: 150px.
At 390px it changes geometry rather than disappearing completely.

### Case-study index

Purpose: project selection.

Observed:
- giant Case studies title;
- Meridian Health;
- StyleBook;
- Homestead;
- North Light;
- project imagery;
- shared conversion/footer.

The index stays lighter than the long-form detail routes.

### 4 case-study detail pages

All 4 case-study detail pages were checked structurally as one CMS family.

Meridian Health exposes the fullest sequence:
- The Real Problem
- Finding the Fix
- What Actually Happened
- What Changed
- What I Had to Work With
- What I'd Do Differently
- What I Learned
- next-project handoff

StyleBook, Homestead, and North Light follow the same reflective family with content-driven variations.

These pages are long-form proof, not screenshot galleries. They explain the designer's judgment under constraints.

## Reflective Case Study Arc

Nudge's strongest transferable portfolio pattern is:

real problem -> approach/fix -> what happened -> what changed -> constraints -> what I would do differently -> what I learned

Why it works:
- separates user/business tension from the design intervention;
- shows consequences rather than only deliverables;
- reveals tradeoffs;
- lets reflection prove professional judgment;
- reduces the "perfect hindsight" feel of generic portfolio templates.

Use only truthful sections. Never fabricate outcomes, research, constraints, metrics, or lessons.

### Blog index

Purpose: editorial discovery.

Observed:
- large journal identity;
- article listing/card family;
- shared conversion/footer.

The blog is visibly related to the portfolio but not forced into the exact project-card grammar.

### 8 blog detail pages

All 8 blog detail pages were checked structurally as one CMS family.

Representative route:
/blog/ideas-need-silence

Desktop:
- left-side context/metadata block around 568px wide;
- position: sticky;
- top: 190px;
- date/category/title/summary stay visible while the article body scrolls;
- main article content occupies the companion column;
- shared closing conversion/footer.

Representative article sections:
- Why the Mind Needs Empty Space
- A Simple Practice for Creative Clarity
- Making Room for Better Work

At 390px the context block is about 358px wide and remains useful without document overflow.

## Persistent Context Rail

Nudge uses persistent context across more than one route family:
- About: Bio / Story / Work local navigation;
- Blog detail: date/category/title/summary;
- fixed global navigation across conventional routes.

Transfer rule:
- keep high-value local context visible when it lowers reader reset;
- let the rail own metadata/navigation while main content changes;
- resize, release, or inline it when mobile geometry becomes intrusive;
- do not use sticky context as decoration;
- preserve semantic reading order and keyboard/touch access.

### Services

Purpose: capability + process explanation.

Observed:
- giant split display "what / i / do";
- Product Design;
- web design;
- Design systems;
- Creative direction;
- How i work;
- Discover / Define / Design / Deliver;
- core capabilities;
- FAQ;
- shared conversion/footer.

The page is roughly 10.4k px tall on desktop, but oversized section anchors make progression obvious.

### Contact

Purpose: focused conversion.

Observed:
- handwritten "leave me a note";
- giant Contact title;
- visible Email and Message fields;
- generated hidden anti-spam/context inputs;
- no unnecessary recap before the form.

At 390px the page stays simple and viewport-scaled.
### Playground

Purpose: experimental personality surface.

Desktop:
- viewport-locked 1440x900 canvas;
- no normal document scroll;
- 14 images/assets in the inspected state;
- image/note fragments positioned in freeform space;
- rotated transforms create collage tension;
- many draggable surfaces expose cursor: grab;
- a top ruler/index layer is fixed;
- source bundle contains GSAP and Draggable implementation;
- runtime contains absolute transformed items outside the initial camera.

Representative captions include:
- Good weather
- Random shot
- Tiny moments
- Not sure what I'm doing
- bus bus bus
- flower!

Mobile:
- viewport remains 390x844;
- document scroll height remains 844px;
- draggable/freeform content extends outside the visible camera;
- exploration is spatial rather than document-scroll driven.

The playground's strength comes from being isolated from case studies, blog reading, and contact.

## Experimental Surface Isolation

Architecture rule:

let the experimental route be weird so the proof routes can stay clear.

Transfer rules:
- isolate drag/freeform/spatial interaction to an explicit playground/lab route;
- keep a clear global escape/navigation path;
- do not require the playground to understand professional proof;
- do not make contact, article, or case-study reading depend on custom drag;
- preserve touch usability when the experiment survives mobile;
- treat the experiment as identity surplus, not core information architecture.

This is identity overflow without usability spillover.

## Motion and input grammar

Observed/source-confirmed mechanisms:
- Framer route/runtime animation;
- fixed global nav;
- one-shot entry overlay;
- smooth-scroll runtime state via lenis lenis-autoToggle;
- GSAP in the main bundle;
- Draggable in the main bundle;
- sticky full-viewport project stages;
- sticky local context rails;
- custom cursor layer;
- drag/grab playground;
- generated hover/button animation systems.

Recommended ownership:
- conventional navigation for core routes;
- scroll for editorial progression;
- sticky for project/context continuity;
- drag only for playground;
- custom cursor as optional desktop personality;
- intro overlay as optional one-shot identity cue.

Do not globalize every interaction just because the template contains it.

## Responsive contract

Source-confirmed branches:
- >= 1200px large desktop;
- >= 810px tablet/desktop;
- <= 809.98px mobile.

Observed transformations:
- 150px-class display -> roughly 80px mobile;
- full navigation -> Menu;
- full-viewport sticky project stack -> released normal flow;
- case-study detail -> single-column long-form reading;
- blog context rail narrows but can remain sticky;
- about local rail changes geometry;
- playground keeps spatial drag rather than becoming a normal article;
- no document-level horizontal overflow observed in 390px family audits.

Preserve type-role identity, project order, and proof narrative before preserving desktop sticky geometry.

## Template residue and vendor identity

Nudge is an audited Framer template.

Template/vendor evidence:
- title "Nudge - Premium Portfolio Template";
- fixed BUY NUDGE control;
- Framer free-site platform overlay;
- generic template description reused across routes.

Apply Template Residue Quarantine:
- keep vendor/platform artifacts in audit coverage;
- exclude them from new brand identity;
- do not copy placeholder project names, dates, case-study claims, article copy, captions, or vendor UI;
- do not mistake platform overlays for authored navigation.

## Cross-site synthesis

Compared with Refokus:
- both occupy creative/agency/editorial territory;
- Refokus teaches high-ambition signature stage, bounded 3D, motion-as-focus, and vivid project worlds;
- Nudge teaches a lower-cost portfolio/template system with expressive typography, sticky editorial framing, reflective case-study narrative, and isolated experimental interaction;
- they are complementary anchors for creative-agency-editorial.md, not styles to average.

Compared with Powder:
- both use desktop sticky storytelling and release some geometry on mobile;
- Powder's sticky stage proves product capability;
- Nudge's sticky stage compares portfolio projects;
- sticky is therefore a mechanism, not an identity.

Compared with Tokenmeter:
- Tokenmeter routes one dataset into different densities;
- Nudge routes one creative identity into different proof modes;
- both show that route-family specialization can preserve a shared system without forcing one component everywhere.

## Adopt / Adapt / Avoid

| Pattern | Decision | Why |
|---|---|---|
| Reflective Case Study Arc | Adopt for portfolios | Shows judgment and constraints, not just polished outcomes. |
| Persistent Context Rail | Adopt when long-form reading benefits | Reduces cognitive reset. |
| Experimental Surface Isolation | Adopt for expressive portfolios/studios | Allows playful input without contaminating task routes. |
| Full-viewport sticky project stack | Adapt | Strong desktop storytelling; release when mobile geometry is costly. |
| Four-role expressive typography | Adapt | Effective only when semantic roles remain disciplined. |
| Multi-palette project worlds | Adapt | Useful when the global shell stays stable. |
| Custom cursor / intro overlay | Adapt cautiously | Identity cue, not required proof. |
| Exact Flux/handwritten/mono stack | Avoid | Template-specific identity. |
| Exact Nudge project names/case stories/captions | Avoid | Template content. |
| BUY NUDGE / Framer overlays | Avoid | Template/platform residue. |

## Best-fit briefs

Use this profile for:
- product designer portfolios;
- independent creative portfolios;
- design studios;
- creative agencies;
- art-direction-heavy case-study sites;
- portfolios that need a safe baseline plus one experimental route;
- lower-capability execution needing explicit typography, route, and case-study contracts.

## Weak-fit briefs

Do not let this profile dominate:
- transactional SaaS;
- dense dashboards;
- developer APIs;
- enterprise compliance sites;
- ecommerce catalogs;
- publications where playful identity competes with reading;
- portfolios with no real process/reflection material.

## Regression questions

- Was coverage really 19/19 sitemap URLs?
- Were all 8 blog detail pages checked as one CMS family?
- Were all 4 case-study detail pages checked as one CMS family?
- Does the case study expose problem, intervention, result, constraints, and reflection only when truthful?
- Is the Persistent Context Rail helping orientation?
- Does Experimental Surface Isolation keep the playground out of required proof/conversion paths?
- Does mobile preserve typography roles while releasing desktop sticky geometry?
- Does the 390px document remain free of unintended horizontal overflow?
- Are exact fonts, project copy, captions, dates, and vendor controls excluded from transfer?
- Does the portfolio stay coherent when projects carry different image/color worlds?
- Is the result more than generic big type + project cards?

Pass only when Nudge Folio functions as an audited portfolio-template teacher, not as a clone target.
