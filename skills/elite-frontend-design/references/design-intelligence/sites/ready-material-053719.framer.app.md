# Echoes of Mars - full-site distilled design intelligence

Source: https://ready-material-053719.framer.app/
Audit date: 2026-10-07
Coverage: 1/1 sitemap URL + complete campaign route + generic 404 recovery

This is a whole-site audit. The site intentionally has one indexable route; completeness means accounting for every authored campaign chapter, anchor, conversion destination, responsive transformation, runtime behavior and recovery surface rather than inventing route families that do not exist.

## Coverage manifest

Sitemap: `/` only. Robots allows `/` and advertises `/sitemap.xml`.

Authored chapter IDs:
`#hero`, `#trailer`, `#premise`, `#world`, `#story`, `#gameplay`, `#mechanics`, `#media`, `#characters`, `#audio`, `#release`, `#press`, `#wishlist`.

Primary navigation exposes WORLD, STORY, GAMEPLAY, MEDIA and WISHLIST as same-page anchors. There are no additional same-origin product/content route families.

`/404` and arbitrary missing paths return HTTP 404. They render Framer's generic "Page Not Found" surface with Back to Home and are not in the sitemap.

External actions observed:
- wishlist/store -> Steam root;
- trailer -> YouTube root;
- soundtrack -> example.com/soundtrack;
- press kit -> example.com/press-kit;
- privacy/terms -> example.com placeholders;
- Instagram, YouTube, Discord and Steam -> platform roots.

These are demo/template destinations, not production conversion evidence.

## Classification

Primary: single-title atmospheric cinematic game launch.
Secondary: documentary / field-report world marketing.

Echoes of Mars is a strong audited anchor for the existing `cinematic-game` skin. It should not create a fourteenth skin.

Compared with Rockstar Games VI, both let a fictional world own the campaign. Rockstar VI leans toward franchise spectacle, multi-chapter promotional media and expensive branded rendering. Echoes of Mars leans toward quiet field evidence, coordinates, sector IDs, mission metadata, still-image proof and one long editorial route.

Compared with Indiex/Nexira, this is not a studio-service funnel. Service/team/business proof is replaced by world, story, gameplay, mechanics, character, soundtrack, release and press proof.

Do not treat the fictional release year, platform availability, soundtrack credit, press quotes, build number, in-engine claim, coordinates, character biography or lore as verified product facts.

## Platform and source evidence

- generator: Framer c9b3949;
- canonical home: https://ready-material-053719.framer.app/;
- OG URL matches canonical;
- home title: Echoes of Mars — Atmospheric Sci-Fi Adventure;
- home robots: max-image-preview:large;
- home html lang is empty;
- generic 404 uses lang=en;
- no authored form;
- 0 HTML video;
- 0 canvas;
- 47 img elements;
- main experience is DOM + responsive images + Framer/source-authored reveals + a custom world-track scroll controller.

The connected Chrome instance exposed Framer editor chrome because its extension sets the editor-bar localStorage flag. Editor iframe/badge chrome is quarantined from design evidence; the Framer badge is vendor residue, not site DNA.

## Whole-route campaign spine

The authored sequence is:
1. fixed navigation;
2. hero;
3. trailer;
4. premise;
5. world survey;
6. story;
7. gameplay;
8. mechanics/systems;
9. recovered-footage media;
10. character;
11. sound;
12. release;
13. press;
14. final wishlist endcap;
15. footer.

Abstract flow:
world identity -> trailer intent -> premise -> place evidence -> story -> gameplay promise -> systems -> visual proof -> character -> sound -> availability -> external validation -> final conversion.

This is a complete single-title campaign spine. It does not need fake service/blog/team routes to feel complete.

## Typography

Primary visible roles:
- Saira Variable: display, headings, narrative body and large gameplay/mechanic words;
- Datatype Variable: coordinates, counters, sector/build labels, navigation and telemetry;
- Inter appears only as Framer/system utility, not authored identity.

Desktop 1440x900:
- hero H1: 190px / 155.8px, weight 400, tracking -9.5px;
- major H2: 70px / 65.8px, tracking -2.45px;
- large gameplay/mechanic words: 126px / 108.36px;
- compact H3: 30px / 31.8px;
- narrative body example: 21px / 31.92px;
- supporting body: 16px / 25.92px;
- telemetry/meta: 11px / 14.3px, +1.54px tracking, uppercase.

Mobile 390x844:
- hero H1: 56px / 49.28px;
- major H2: 33px / 33px;
- large gameplay/mechanic words: 46px / 41.4px;
- compact H3: 21px / 23.1px.

Transfer the role contrast: high-character display + readable narrative + compact monospaced telemetry. Do not make Saira/Datatype a genre preset.

## Color and material grammar

Observed semantic roles:
- #0B0A09 main warm near-black shell;
- #15110E raised/differentiated dark surface;
- #E7E0D6 bone/ivory primary text;
- rgba(231,224,214,.54) secondary narrative;
- rgba(231,224,214,.32) telemetry;
- rgba(231,224,214,.14) quiet borders;
- #C9743F rust/Mars accent.

The useful rule is world-derived color semantics: rust + warm dark rock + bone telemetry. Transfer that relationship, not the exact palette.

Material treatment is mostly square/low-radius, thin telemetry lines, large cinematic stills, negative space and repeated decorative grain/noise overlays. It avoids neon-card/HUD chrome as the primary identity.


## Hero, trailer and premise

Hero combines full-viewport Martian key art, transmission coordinates/status, A SCI-FI ADVENTURE / 2027, the oversized title, "Something is still listening.", WISHLIST NOW and WATCH TRAILER. Small context includes MARS / SECTOR 07, SIGNAL DETECTED and 03:47 UTC.

The metadata behaves as world context rather than random decoration. Transfer one coherent set of contextual fields; do not fill corners with unrelated pseudo-HUD strings.

The trailer chapter uses a cinematic still, PLAY TRAILER, 02:17, OFFICIAL GAMEPLAY TRAILER and MEDIA / 001. Playback is not embedded; the current YouTube-root link is placeholder residue. The mechanism is explicit user intent for heavy media.

Premise / 002 pairs a 70px statement with concise story copy, YEAR 2097 / MARS, RECOVERY MISSION 04, an abandoned-colony image, FIG. 01 — COLONY STATION ARES-1 and LAST CONTACT 2067.11.04. The transferable pattern is prose plus documentary facts that add context rather than repeat the paragraph.

## The World / 003 — Pinned Sector Survey

This is the signature interaction.

Desktop evidence at 1440x900:
- world section ~3780px tall;
- one ~900px sticky viewport;
- one ~5320px horizontal track;
- explicit Scroll Start, Scroll Range, Scroll End and Scroll Tail;
- title panel + six sector panels + survey-complete panel;
- runtime writes `translate3d(...)` on `#world-track`.

Sector order:
- 01 — The Red Basin;
- 04 — Ares-1 Station;
- 07 — The Descent;
- 09 — Dust Line;
- 12 — The Structure;
- 14 — Long Walk.

Closing state: SURVEY / COMPLETE, SIX SECTORS. ONE SIGNAL., sector-survey status and ARES-1 / 2097.

This is **Pinned Sector Survey**: vertical page progress temporarily becomes horizontal spatial exploration while the viewport remains stable. Horizontal movement is justified because the user is surveying places in one world; it is not a decorative sideways-scroll recipe.

Mobile evidence at 390x844:
- world section ~3412px;
- `#world-viewport` becomes relative, not sticky;
- `#world-track` collapses to ~390px;
- content flows vertically;
- document overflow remains 0.

This is a strong responsive substitution: desktop spatial sweep -> mobile vertical chapter stack. Preserve sector order, coordinates, names, descriptions and conclusion; drop sticky ownership and horizontal translation dependency.

## Story / 004

Story uses a compact archive model:
- 30 YEARS OF SILENCE;
- 2067—2097 archive context;
- CLASSIFIED status;
- 01 THE SIGNAL;
- 02 THE DESCENT;
- 03 THE DISCOVERY;
- 04 THE ECHO.

It compresses a long fictional timeline into one fact block plus four beats instead of a lore wall.

## Gameplay / 005

Gameplay uses three large media-led promises:
- G01 / TRAVERSAL -> EXPLORE;
- G02 / INVESTIGATION -> DISCOVER;
- G03 / SURVIVAL -> ENDURE.

Each has one atmospheric still plus a short explanation. Large desktop verbs measure ~126px and step to ~46px mobile.

Transfer the verb-led proof hierarchy, not the exact words or art.

## Systems / 006 — Mechanics Survey Rows

Systems uses four full-width indexed rows rather than a feature-card grid:
- M01 SIGNAL;
- M02 OXYGEN;
- M03 LIGHT;
- M04 MEMORY.

Each row has a compact index, huge mechanic name, one-line explanation and a hidden/filtered image layer prepared as hover enhancement. Desktop rows measured about 188px high within ~1297px content width.

The source literally says HOVER TO SURVEY and that instruction remains on mobile. Text meaning is still present without hover, but pointer-specific instruction copy must be replaced/hidden for coarse pointers.

Semantic issue: SIGNAL, OXYGEN, LIGHT and MEMORY are H1 elements in addition to the hero H1. Transfer the visual hierarchy, not the heading misuse; use H2/H3/list semantics appropriate to the page outline.

## Media / 007 — Recovered Footage Proof

Media is an asymmetric screenshot proof system, not a generic gallery. It combines:
- RECOVERED FOOTAGE.;
- IN-GAME / PC / 4K labels;
- scene/location captions and coordinates;
- SUIT TELEMETRY / RECOVERY UNIT 04;
- BUILD 0.9.4 / PRE-ALPHA;
- a claim that captures were taken in-engine at 4K.

The transferable mechanism is **evidence with provenance**: screenshot + source type + scene/location + capture/build/platform context where truthful.

Never fabricate in-engine, build, resolution or pre-alpha claims.

## Character, sound, release, press and final conversion

Character / 008 presents Mara Voss as a personnel record: portrait, FIG. 02, recovery unit, role, age and years of service. The reusable mechanism is consistent documentary grammar across places, media and people.

Sound / 009 gets its own chapter: LISTEN CLOSELY., soundtrack label, composer credit and listening action. The current soundtrack URL is an example.com placeholder.

Release / 010 combines 2027, platform labels, WISHLIST NOW and NO EXACT DATE ANNOUNCED over full-bleed Mars art. Stating uncertainty explicitly is good; linking wishlist to Steam root is not production-ready.

Press / 011 contains three polished quotes but only generic labels (PRESS OUTLET, GAME PUBLICATION, REVIEW SITE). Without publication identity, URL/date or attributable source, this is placeholder social proof.

The final endcap repeats SOMETHING IS STILL LISTENING., ECHOES OF MARS, WISHLIST NOW and COMING 2027. It echoes the opening action after the page has earned conversion through world/gameplay/media proof.


## Image/media inventory and performance

Live home:
- 47 images;
- 21 lazy-loaded;
- 0 video;
- 0 canvas;
- 12 non-empty alt values;
- 35 empty alt values;
- 0 images missing the alt attribute.

Many empty-alt images are repeated grain/texture overlays, where decorative empty alt is appropriate. Meaningful hero, trailer, premise, gameplay, footage, character and release art carry non-empty alt descriptions.

The repeated grain asset unifies disparate stills but still counts toward media/runtime cost. The site proves that a premium cinematic game page can remain still-image-led rather than defaulting to autoplay video or WebGL.

## Motion evidence

The live page exposed 0 settled Web Animations API animations in sampled states, but source/render evidence contains authored reveal preparation:
- ~207 `opacity:0` occurrences;
- ~79 `translateY(...)`;
- ~48 `translateX(...)`;
- ~48 `scale(...)`;
- 29 `will-change:transform`;
- 9 `data-framer-appear-id`.

Rendered story elements showed initial states such as opacity 0 plus translateY(20/30px). The signature movement is the world-track spatial sweep; ordinary section reveals remain supporting motion.

Transfer hierarchy:
1. one signature spatial transition;
2. restrained local reveals;
3. still imagery carries complete meaning without motion.

Do not make every telemetry label loop, blink or glitch.

## Responsive behavior

Desktop audit target 1440x900:
- document about 1425x18690;
- 47 images;
- 0 video;
- 0 canvas;
- fixed authored nav;
- one authored sticky world viewport;
- world track ~5320px;
- no positive document-level overflow.

Mobile 390x844:
- document 390x17608;
- 47 images in DOM;
- 0 video;
- 0 canvas;
- no outer overflow;
- world sticky behavior removed;
- world track becomes ~390px vertical flow;
- H1 190 -> 56;
- H2 70 -> 33;
- large gameplay/mechanic display 126 -> 46;
- compact H3 30 -> 21.

The mobile version preserves almost the entire campaign payload rather than falling back to a generic title + CTA page.

## Accessibility and semantic findings

Positive:
- main navigation and actions are links;
- important imagery has meaningful alt;
- decorative texture layers use empty alt;
- missing routes return real HTTP 404;
- mobile has no outer horizontal overflow;
- mechanics text remains readable without hover.

Needs correction:
- home `html lang` is empty;
- mechanic names are repeated H1 elements;
- HOVER TO SURVEY remains pointer-specific copy on mobile;
- generic 404 has no canonical;
- external high-intent destinations are placeholders;
- press praise is unattributed.

Anchor targets land at viewport top while navigation is fixed. Derived implementations should use `scroll-margin-top` or equivalent when the target's first content would be obscured.

## Conversion Destination Integrity

A high-intent label must resolve to the exact intended destination, not merely the right platform category.

Observed failures:
- wishlist -> Steam root;
- trailer -> YouTube root;
- soundtrack/press/legal -> example.com;
- community/social -> platform root pages.

A Steam-root link is not a wishlist link. A YouTube-root link is not a trailer. Treat these as release blockers.

## Telemetry as Narrative UI

The strongest transferable mechanism is not "sci-fi HUD"; it is one coherent metadata vocabulary:
- coordinates;
- sector and mission IDs;
- UTC;
- archive years;
- figure numbers;
- recovery units;
- build/version;
- platform/resolution;
- release uncertainty.

Each field should answer a real contextual question, localize the visitor or strengthen provenance. Avoid random coordinates, fake terminal strings and unreadable pseudo-code.

## Numbered Field-Report Chapters

The campaign uses a compact ledger from MEDIA / 001 through PRESS / 011. The chapter counter creates continuity across a very long single route while the chapter name still explains the user job.

The duplicate MEDIA name at 001 and 007 is a naming oddity, but numbering remains useful. Chapter number should never become the only navigation cue.

## Pinned Sector Survey contract

Use when a bounded sequence of places/stages is itself part of the story.

Desktop:
- one sticky viewport;
- one horizontal track;
- explicit start/end;
- bounded progress;
- one summary state;
- no competing sticky owner.

Mobile/reduced motion:
- release sticky;
- restore vertical document flow;
- preserve all place facts;
- never require horizontal scrub to understand the content.

## Recovered Footage Proof contract

Use when images are product proof rather than wallpaper.

Anatomy:
- screenshot/still;
- source type;
- scene/location;
- capture/build/platform context when truthful;
- optional caption;
- variable scale when hierarchy is intentional.

The reusable mechanism is evidence with provenance, not "put mono labels over a gallery".

## Mechanics Survey Rows contract

Use full-width indexed rows when a small capability/mechanic set deserves high salience.

Anatomy:
- rule/border;
- compact index;
- large name;
- short description;
- optional image reveal as enhancement.

Text must remain visible without hover, pointer-language must adapt on coarse pointers, and headings must match document hierarchy.

## Transferable principles

1. **Telemetry as Narrative UI** — contextual metadata sustains world identity between large images.
2. **Pinned Spatial Survey** — horizontal exploration is earned only when space/sequence has meaning; mobile returns to vertical flow.
3. **Recovered Footage Proof** — media gains credibility from truthful provenance.
4. **Numbered Field-Report Chapters** — one small ledger binds a long campaign.
5. **Mechanics Survey Rows** — high-salience mechanics can avoid generic feature cards.
6. **World First, Conversion Repeated** — open with one action, earn it through proof, repeat it at release/endcap.
7. **Cinematic Without Continuous Rendering** — 47 still images, no video and no canvas can still produce a premium campaign.

## Do not transfer

Do not transfer Echoes of Mars identity/lore, Mara Voss, Ares-1, exact coordinates/sector names, 2027/platform/soundtrack/build/in-engine claims, fictional press quotes, exact Mars palette, exact Saira + Datatype pairing, source imagery/grain assets, root/example destinations, Framer chrome, repeated H1 misuse or pointer-only instruction copy.

## Distilled role in the toolkit

Echoes of Mars becomes the first full-site audited evidence anchor for the generic `cinematic-game` skin.

Primary contributions:
- Telemetry as Narrative UI;
- Numbered Field-Report Chapters;
- Pinned Sector Survey;
- Recovered Footage Proof Grid;
- Mechanics Survey Rows;
- desktop horizontal -> mobile vertical world substitution;
- still-image cinematic campaign evidence;
- CTA destination integrity QA;
- pointer-language mobile QA;
- semantic H1/lang QA.

It strengthens the existing cinematic-game family rather than creating a new skin.
