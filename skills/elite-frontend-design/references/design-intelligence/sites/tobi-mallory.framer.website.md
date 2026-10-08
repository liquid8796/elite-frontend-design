# Tobi Mallory - full-site distilled design intelligence

Source: https://tobi-mallory.framer.website/
Audit date: 2026-10-07
Coverage: 30/30 sitemap URLs
Family coverage: 7 Fieldbook detail pages, 6 Type detail pages, 4 Journal detail pages, 3 Quest detail pages.

Tobi Mallory is a personal designer/developer portfolio whose strongest transferable idea is a **whimsical world model that is also the information architecture**. The site does not merely decorate a conventional portfolio with creatures. Projects become Fieldbook entries, disciplines become Types, services become Quests, achievements become Seals, experience becomes Stats, categories become Isles, and contact becomes a Save Point.

The audit covers the complete public sitemap, all dynamic route families, Framer search-index parity, rendered desktop/mobile behavior, source/runtime typography and colors, form behavior, canonical metadata, motion density, and template/semantic residue.

## Evidence confidence

- **Observed**: rendered desktop/mobile structure, typography scale, route height, overflow, form controls, media counts, fixed navigation, Framer motion activity.
- **Source-confirmed**: sitemap/search-index route inventory, canonical URLs, generator, meta descriptions, route titles/headings, breakpoints, loaded font roles.
- **Inferred**: design intent and higher-level narrative/commercial strategy derived from repeated site-wide patterns.

## Source and runtime evidence

- Generator: Framer d485f69.
- robots.txt: public, `Allow: /`.
- Sitemap exposes exactly 30 public URLs.
- Framer search index: `searchIndex-OrWCuQLiopYf.json`.
- Search index contains exactly the same 30 route keys as the sitemap.
- Requested/public browsing host: `tobi-mallory.framer.website`.
- robots.txt, sitemap locs, and every audited canonical point to `eternal-fade-087901.framer.app`.
- This is a **canonical-host drift** / publish-domain mismatch worth fixing before production SEO signoff.
- Global cream shell observed as `#fff6e8`.
- Primary dark-ink family observed as `#1e1838`.
- Main display: Bricolage Grotesque.
- Utility/metadata role: Space Mono.
- Source/runtime responsive thresholds: 810px and 1200px.
- Desktop homepage H1: approximately 168px / 141.12px, weight 800.
- Desktop route H1: approximately 112px / 100.8px.
- Desktop major H2: approximately 92px / 86.48px.
- Mobile homepage H1 at 390x844: 80px / 67.2px.
- Mobile route H1: approximately 54px / 48.6px.
- Mobile major H2: approximately 46px / 43.24px.
- Homepage runtime snapshot exposed **239 runtime animations**.
- No homepage canvas, HTML video, three.js, GSAP, or Lenis dependency was required for the world-building effect.
- The site relies on DOM illustration, Framer animation, type scale, color taxonomy, card/scroll interactions, and static project imagery.
- Representative mobile routes at 390x844 showed **no document-level horizontal overflow**.

## Full route inventory

### Core / utility routes - 10

1. `/`
2. `/fieldbook`
3. `/types`
4. `/isles`
5. `/about`
6. `/journal`
7. `/contact`
8. `/legal`
9. `/quests`
10. `/404`

### Fieldbook detail pages - 7

1. `/fieldbook/bezzle`
2. `/fieldbook/curvix`
3. `/fieldbook/pixit`
4. `/fieldbook/mote`
5. `/fieldbook/lumpkin`
6. `/fieldbook/hum`
7. `/fieldbook/dart`

### Type detail pages - 6

1. `/types/ink`
2. `/types/grid`
3. `/types/spark`
4. `/types/clay`
5. `/types/echo`
6. `/types/signal`

### Journal detail pages - 4

1. `/journal/why-every-project-is-a-creature`
2. `/journal/designing-for-the-first-five-minutes`
3. `/journal/a-week-of-motion-loops`
4. `/journal/listening-before-drawing`

### Quest detail pages - 3

1. `/quests/identity-quest`
2. `/quests/website-quest`
3. `/quests/motion-quest`

Total: 10 + 7 + 6 + 4 + 3 = 30.

## Route inventory integrity

The sitemap and Framer search index agree on all 30 route keys.

Every fetched sitemap route returned the expected route-specific title/description. The `/404` route correctly returns HTTP 404 while still using the branded site shell.

Important SEO issue:
- every canonical points at the Framer publish host `eternal-fade-087901.framer.app`, not the requested public host;
- robots.txt also advertises the Framer publish-host sitemap;
- the mismatch is systematic rather than one-route residue.

Treat this as infrastructure/SEO residue, not design DNA.

## Executive Design DNA

Tobi Mallory behaves like a **portfolio collection game with professional proof underneath**.

Core translation:

```text
Projects        -> Fieldbook entries / creatures
Disciplines     -> Types
Service offers  -> Quests
Achievements    -> Seals
Experience      -> Stats / levelling
Taxonomy        -> Isles / map
Contact         -> Save Point
Articles        -> Logbook
Assistant/help  -> Guide
```

The key to the site's quality is that these names are not empty copywriting. They continue into route names, category systems, CTA language, case-study identity, related-content behavior, and visual color/creature grammar.

## Global shell

### Navigation

Global navigation remains conventional enough to decode:
- Tobi Mallory;
- Fieldbook;
- Types;
- Isles;
- About;
- Journal;
- Say hi.

Desktop uses a fixed navigation bar around 74px high.

The playful vocabulary lives inside otherwise predictable navigation. This prevents the world layer from becoming a usability tax.

### Typography

Primary roles:
- **Bricolage Grotesque**: oversized identity, route titles, major section statements;
- **Space Mono**: metadata / utility / collection-system flavor;
- generic/system sans fallbacks for infrastructure/runtime surfaces.

Type is intentionally chunky, friendly, and high-energy rather than cinematic or editorial-luxury.

### Color / material

Global shell:
- warm cream `#fff6e8`;
- dark plum/ink around `#1e1838`;
- soft near-white support surfaces.

Six category/type families observed across the site include saturated coral/red, green, violet, orange, blue, and yellow families. Representative computed colors include:
- coral `#ff6b57`;
- green `#3fd3a0`;
- violet `#9b7bff`;
- orange `#ffb15c`;
- blue `#5bb8ff`;
- yellow `#ffe15a`.

These are evidence of **category color grammar**, not a palette to copy literally.

## Home route

Desktop homepage is approximately 13,739px tall at 1440x900.

Observed section sequence:
1. Tobi Mallory identity hero;
2. `Every craft has a partner.`;
3. The Fieldbook;
4. `Watch one hatch.`;
5. `Six types. One for each craft.`;
6. `Projects evolve too.`;
7. The Isles;
8. Tobi's stats;
9. Seals earned;
10. Open quests;
11. `How an idea hatches.`;
12. About / `Hi, I'm Tobi.`;
13. Ask the guide;
14. Logbook;
15. Save your progress;
16. Save Point footer/contact system.

Homepage role is not simply discovery. It teaches the site's vocabulary and then demonstrates that every metaphor has a real portfolio/service job.

## Fieldbook index

H1: `The Fieldbook`.

Purpose:
- browse seven projects;
- reinforce numbered collection behavior;
- expose type/craft identity;
- encourage hover/card exploration;
- route into full case-study evidence.

Live desktop:
- approximately 3,461px tall;
- 7 project images;
- about 61 runtime animations;
- no document overflow.

The homepage explicitly tells the visitor: `Seven projects, numbered and typed. Hover a card to flip it.`

This is a collectible layer on top of normal portfolio browsing.

## Fieldbook detail family

All 7 detail routes were audited through sitemap/search-index content and fetched source.

Shared case-study grammar:
- creature/project name;
- collection number;
- one-line premise;
- client;
- year;
- work/scope;
- result;
- The brief;
- What hatched;
- Result when present;
- More from the Fieldbook;
- global Save Point/footer.

Representative `/fieldbook/bezzle`:
- title: `Bezzle · Halden identity · Tobi Mallory`;
- No.001;
- client Halden;
- year 2023;
- Brand identity;
- result `11 days to a name`;
- brief: tea company identity problem;
- outcome describes a memorable naming result.

Representative `/fieldbook/curvix`:
- No.002;
- same client Halden;
- year 2025;
- Brand relaunch;
- result `+38% sign-ups`;
- explicitly framed as Bezzle growing into a larger system.

Other entries cover:
- Pixit / Larder web build / 0.9 s first load;
- Mote / Kite motion system / 40 loops shipped;
- Lumpkin / Pebble 3D product / 12 renders a week;
- Hum / Tally research sprint / 26 interviews;
- Dart / Courier product launch / 10k users in a month.

These are template/demo claims unless independently verified. Never reuse the metrics as factual evidence for another project.

### Semantic caveat

Fieldbook detail titles are rendered as large H2 rather than H1 in the audited markup. The visual hierarchy is strong, but a production implementation should preserve a single meaningful H1 for document semantics.

## Types index

H1: `Six types`.

The page states the system directly:
`Every project belongs to one craft. The type decides the colour, the badge and the creature.`

Six mappings:
- Ink -> Brand;
- Grid -> Web;
- Spark -> Motion;
- Clay -> 3D;
- Echo -> Research;
- Signal -> Product.

This is the clearest evidence for **Taxonomy as Visual Physics**.

## Type detail family

Each of the six routes is deliberately short and behaves like a taxonomy landing page rather than a full service page.

Examples:
- `/types/ink`: Brand; identity/naming/logo/type systems;
- `/types/grid`: Web; structure/CMS/speed;
- `/types/spark`: Motion; loops/transitions/launch films;
- `/types/clay`: 3D; product renders/scenes/kits;
- `/types/echo`: Research; interviews/audits/maps;
- `/types/signal`: Product; launches/onboarding/growth.

Every detail points back toward the Fieldbook and all Types.

## Isles

H1: `The Isles`.

Purpose:
- spatial visualization of the six-type taxonomy;
- route visitors from one world overview into discipline pages;
- reinforce that the site is one coherent world.

Copy:
`A map of everything Tobi makes. One island per type, one route through them all.`

Instruction:
`Tap an island to visit its type.`

Desktop approximately 3,066px; mobile approximately 2,927px. No document overflow.

## Quests index

H1: `Open quests`.

Purpose:
- convert portfolio interest into three fixed-scope service packages;
- preserve world vocabulary while exposing practical commercial information.

Copy:
`Three fixed-price ways to work together. Pick one, or ask for a custom quest.`

The site explicitly bridges metaphor to purchasing behavior rather than hiding prices/timing behind lore.

## Quest detail family

Three routes:
- Identity quest;
- Website quest;
- Motion quest.

Representative Identity quest:
- `From $8k`;
- `6–8 weeks`;
- names the outcome and deliverables;
- CTA `Accept this quest`;
- escape route `All quests`.

Website quest:
- `From $6k`;
- `4–6 weeks`;
- Framer + CMS positioning;
- concrete working model.

Motion quest:
- `From $5k`;
- `3–5 weeks`;
- loops/transitions/launch film;
- web-weight performance language.

This family demonstrates the **Metaphor Translation Contract**: playful label, practical scope, price, duration, deliverables, and conventional next action all coexist.
## About

H1: `Hi, I’m Tobi.`

About explains the origin of the creature system rather than repeating homepage marketing.

Core story:
- independent designer/developer;
- ten years across brands, websites, and motion;
- a client remembered a rebrand as `the fox one`;
- every project now receives an original creature, type, and numbered field entry.

Supporting sections:
- Tobi's stats;
- Seals earned;
- The party;
- Save your progress.

This is useful because the world model has an origin story tied to memory and client behavior rather than arbitrary decoration.

## Journal / Logbook

Index H1: `Logbook`.

Four article routes:
- Why every project is a creature;
- Designing for the first five minutes;
- A week of motion loops;
- Listening before drawing.

Shared article grammar:
- category;
- date;
- reading time;
- title;
- short deck;
- one or more content sections;
- More from the logbook;
- Save Point/footer.

Article topics reinforce the portfolio's actual disciplines:
- Studio / naming and memory;
- Craft / onboarding;
- Process / motion performance;
- Research / interviews and product behavior.

### Journal semantic caveat

Article titles are visually rendered as H2 rather than H1 in the audited markup. Use the visual treatment if desired, but production semantics should expose one meaningful H1.

## Contact

H1: `Say hi.`

Purpose:
- clear conversion route;
- keeps Save Point vocabulary without making the form ambiguous.

Visible fields:
- Name;
- Email;
- Which quest?;
- What are you making?;
- submit: `Save and send`.

Quest select exposes:
- Identity quest;
- Website quest;
- Motion quest;
- custom/something else option.

Generated hidden/context fields also exist in Framer output, including website/company/message/subject/title/description/feedback/notes/details/remarks/comments-style names. Treat these as generated form plumbing rather than visible product content.

Contact copy gives response expectation: replies within a day, Monday to Friday.

## Legal

H1: `Privacy and terms`.

Sections:
- Who I am;
- What I collect;
- Analytics;
- Your rights;
- Creatures and content.

Unlike several audited templates, this legal route is unusually coherent with the represented identity and does not expose obvious jurisdiction/currency placeholders in the audited copy.

However, canonical-host drift still affects the route metadata.

## 404

Title: `Off the map · Tobi Mallory`.

H1: `404`.

Supporting copy:
`This route isn’t on the map.`

Actions:
- Back to the start;
- Open the Fieldbook.

This is a good example of branded utility copy that preserves the world model without hiding the conventional recovery job.

## Motion and interaction grammar

Homepage desktop runtime exposed 239 animations; the audited 390x844 mobile homepage exposed 144.

Despite the number, the implementation remains DOM/Framer based:
- no canvas;
- no HTML video;
- no three.js;
- no GSAP;
- no Lenis required in the audited runtime.

Observed/copy-confirmed mechanisms include:
- project cards intended to flip on hover;
- creatures/content walking or revealing as the visitor scrolls;
- an egg/hatching process tied to scroll;
- badge/creature hover exploration;
- illustrated map destinations;
- ordinary links/buttons underneath the world layer.

The transferable lesson is **Illustrated Worldbuilding Without Heavy Rendering**: a portfolio can feel game-like through naming, taxonomy, illustration, stateful cards, and scroll choreography without a GPU-heavy world.

## Responsive contract

Representative mobile audit at 390x844:
- Home: ~13,716px tall; 0px document overflow;
- Bezzle detail: ~4,383px; 0px overflow;
- Ink/Brand type detail: ~1,948px; 0px overflow;
- Isles: ~2,927px; 0px overflow;
- Journal article: ~4,189px; 0px overflow;
- Identity quest: ~3,157px; 0px overflow;
- Contact: ~3,159px; 0px overflow.

Typography transformation:
- homepage identity 168px desktop -> 80px mobile;
- route H1 112px desktop -> 54px mobile;
- major H2 92px desktop -> 46px mobile.

Important behavior:
- outer document remains width-stable;
- route hierarchy and metaphor vocabulary remain;
- mobile accepts taller pages rather than shrinking information;
- hover-dependent concepts must still expose understandable/tappable content on touch.

This is **Responsive Brand Payload** plus a stronger rule: preserve the world vocabulary and category identity while releasing desktop-only hover geometry.

## World Metaphor as Information Architecture

Tobi Mallory is a strong audited anchor because the metaphor survives the entire route ecosystem.

Evidence:
- `Fieldbook` exists as navigation, index, seven details, related-content language, and CTA;
- `Types` exists as a six-category taxonomy with detail routes;
- `Isles` spatializes that same taxonomy;
- `Quests` exists as an index plus three commercial detail routes;
- `Save Point` consistently means contact/conversion;
- `Logbook` consistently means journal/editorial;
- stats/seals/levelling appear in about/home rather than randomly across unrelated routes.

The metaphor is therefore structural, not decorative copy.

## Taxonomy as Visual Physics

The six types do more than classify projects.

The site's own system statement is:
`The type decides the colour, the badge and the creature.`

This creates three linked layers:
1. semantic craft category;
2. visual category identity;
3. project/creature identity.

The Isles then turns the same taxonomy into spatial navigation.

Transferable rule:
- use one stable taxonomy source;
- let category identity propagate into controlled visual variables;
- preserve category names as text;
- do not make color the only differentiator.

## Mnemonic Case-Study Encoding

Each Fieldbook project combines:
- a memorable creature/codename;
- a collection number;
- a type/craft;
- project/client metadata;
- one-line premise;
- result;
- case-study detail.

Examples:
- Bezzle / No.001 / Ink / Halden / Brand identity;
- Pixit / No.004 / Grid / Larder / Web build;
- Mote / No.007 / Spark / Kite / Motion system;
- Lumpkin / No.010 / Clay / Pebble / 3D product;
- Hum / No.013 / Echo / Tally / Research sprint;
- Dart / No.016 / Signal / Courier / Product launch.

The creature makes the project memorable; client/work/result keeps it credible.

## Metaphor Translation Contract

Tobi's world vocabulary remains decodable because it repeatedly pairs metaphor with conventional product/service information.

Examples:
- Fieldbook -> project portfolio -> client/year/work/result;
- Types -> disciplines -> Brand/Web/Motion/3D/Research/Product;
- Isles -> taxonomy map -> named tappable destinations;
- Quest -> service package -> price/duration/deliverables;
- Save Point -> contact -> visible email/form/response expectation;
- Logbook -> journal -> category/date/read-time/article titles.

This is the boundary between cohesive personality and confusing renaming.

## Project Evolution as Relationship Proof

`Projects evolve too.` is not only a visual motif.

Bezzle -> Curvix shows:
- same client Halden;
- first identity in 2023;
- later relaunch in 2025;
- scope expands into packaging/site/subscriptions;
- later result is framed as subscription growth.

The relationship communicates retention, system scalability, and the designer's ability to grow with a client.

Never fabricate this type of lineage. It is powerful only when the project relationship is real.

## Illustrated Worldbuilding Without Heavy Rendering

The site achieves game-like/world-like memory using:
- character/creature illustration;
- collection numbering;
- map metaphor;
- large friendly typography;
- category color grammar;
- card flip intent;
- scroll-triggered DOM animation;
- quest/stat/seal/save-point vocabulary.

No continuous 3D renderer is required.

This is a strong counterexample to the assumption that playful/game-adjacent web identity requires WebGL.

## Route-family density

Representative desktop heights:
- Home: ~13,739px;
- Fieldbook index: ~3,461px;
- Bezzle detail: ~3,271px;
- Types index: ~3,163px;
- Isles: ~3,066px;
- Journal detail: ~3,739px;
- Identity quest: ~2,505px;
- Contact: ~2,612px;
- Legal: ~2,373px.

The density ladder is healthy:
- Home teaches the world;
- indexes support discovery;
- case/articles carry proof/content;
- type pages stay short;
- quests compress service decisions;
- contact/legal/404 remain focused utility routes.

## QA and failure modes

### Canonical-host drift

All audited canonical URLs and sitemap locs use `eternal-fade-087901.framer.app` while the browsed host is `tobi-mallory.framer.website`.

Before production signoff:
- choose one public canonical host;
- update canonical tags;
- update robots sitemap reference;
- regenerate sitemap URLs;
- verify search/share metadata;
- test redirects between aliases.

### Heading semantics

Fieldbook details and Journal details have no H1 in fetched/rendered markup; their main title is H2.

Preserve the visual scale but give each document one meaningful H1.

### Hover translation

Fieldbook cards and badge interactions explicitly invite hover.

On touch/keyboard:
- project identity and action must remain visible;
- flip content cannot be the only place important metadata exists;
- badge meaning must remain available without hover;
- focus state should expose the same action as pointer hover.

### World-language ambiguity

Do not let `Quest`, `Fieldbook`, `Isles`, or `Save Point` appear without enough nearby context for a first-time visitor to infer the real task.

## Template / platform residue

Observed Framer platform chrome:
- fixed Framer free-site overlay;
- editor iframe/runtime surface.

Exclude these from the site's Design DNA.

The canonical publish-domain mismatch is also platform/deployment residue.

## Cross-site synthesis

### Versus Nudge Folio

Both are expressive portfolios, but the organizing logic differs:
- Nudge: editorial personality + reflective case arcs + isolated playground;
- Tobi: one persistent collectible/world metaphor across navigation, taxonomy, projects, services, contact, and content.

Do not merge them into one generic `creative portfolio` recipe.

### Versus Nexira / Rockstar VI

Tobi borrows game-like language but is not game marketing:
- no fictional franchise being sold;
- no cinematic world renderer;
- no HUD-heavy campaign system;
- the world metaphor exists to organize a real professional portfolio/service business.

### Versus Ten Billion Years

Tobi demonstrates the opposite technical path:
- rich world identity;
- almost entirely DOM/illustration/Framer animation;
- no continuous canvas world;
- traditional route ecosystem remains central.

## Adopt

- World Metaphor as Information Architecture;
- Taxonomy as Visual Physics;
- Mnemonic Case-Study Encoding;
- Metaphor Translation Contract;
- Project Evolution as Relationship Proof;
- collectible numbering/related-work continuity when truthful;
- one stable world vocabulary across route families;
- light DOM/illustration worldbuilding when heavy rendering adds no value;
- short commercial Quest details with visible price/timing/scope;
- branded utility routes that remain operationally obvious.

## Adapt

- creature/object metaphor;
- number of categories/types;
- map/islands representation;
- badges/seals/stats vocabulary;
- card flip mechanics;
- category palette;
- large rounded display type;
- quest packaging;
- density and amount of animation.

Replace all source-specific nouns with a metaphor that belongs to the new product/person.

## Avoid

- copying Tobi, the creature names, artwork, exact taxonomy names, project copy, client claims, or exact palette;
- inventing mascots that have no information-architecture job;
- replacing case-study evidence with cute creatures;
- using color as the sole category indicator;
- hover-only project metadata;
- renaming basic actions until first-time visitors cannot decode them;
- fake stats, seals, levels, or project outcomes;
- treating game vocabulary as an excuse for inaccessible controls;
- keeping canonical URLs on a staging/publish host;
- omitting H1 purely to reproduce the source markup.

## Best fit

Strong:
- individual creative portfolios;
- small studios with several disciplines;
- illustrators/designers/developers with a strong original visual world;
- education/collection/catalog experiences;
- brands where recurring characters/objects can encode real categories;
- service businesses that want personality without sacrificing pricing/scope clarity.

Weak:
- regulated enterprise tools;
- transactional ecommerce;
- dense admin/product UI;
- serious legal/financial experiences;
- products whose audience would interpret fantasy vocabulary as friction;
- portfolios without original visual assets or enough case-study substance.

## Regression questions

- Was the full 30/30 sitemap covered?
- Do sitemap and search index still agree?
- Are all 7 Fieldbook details represented?
- Are all 6 Type details represented?
- Are all 4 Journal details represented?
- Are all 3 Quest details represented?
- Does every metaphor term map to one stable real-world job?
- Do creature/project entries keep client/year/work/result evidence?
- Is taxonomy represented by text as well as color/illustration?
- Can mobile/touch users access the same information as hover users?
- Does the world survive responsive simplification without document overflow?
- Are project evolution relationships truthful?
- Does contact expose conventional form labels and response expectations?
- Are legal/404 routes clear despite branded vocabulary?
- Is the public canonical host correct?
- Does every detail/article document expose a meaningful H1?
- Is the new implementation transferring the mechanism rather than cloning Tobi Mallory?

Pass only when the world model improves memory/navigation/proof while remaining understandable to a first-time visitor.

## Complete-Site Re-Audit — 2026-10-08

The original 30-route full-site profile remains valid. This fresh audit validates all 30 sitemap paths on both the browsed host https://tobi-mallory.framer.website/ and canonical host https://eternal-fade-087901.framer.app/. The public site's robots.txt advertises the canonical host sitemap, and the sitemap document itself contains **30 loc entries pointing to that other host**.

- All **29 content routes return HTTP 200** on both hosts; the sitemap-listed /404 route returns proper HTTP **404** on both; one extra nonexistent URL also returns 404.
- All **30/30 canonical links on browsed host point to eternal-fade-087901.framer.app**, not the browsed hostname. Canonical drift is site-wide, not homepage-only.
- Public sitemap includes /404 even though it is a real 404. Exclude invalid routes from public sitemaps.
- Families: 10 core/utility including /404, 7 Fieldbook details, 6 Types, 4 Journal, 3 Quests.
- Two-host HTTP record: modules/distilled-web-toolkit/data/tobi-dual-host-routes-2026-10-08.csv (62 rows).

### Independent desktop/mobile render audit

Installed Chrome headless rendered **15 distinct route types on desktop (1440x900) and mobile (390x844)**: home, Fieldbook index+Bezzle+Curvix, Types index+Ink, Isles, Quests index+Identity, About, Journal index+detail, Contact, Legal and /404. 30/30 tested UI states had **zero positive outer document overflow**.

| Route | Desktop document height | Mobile document height |
| --- | ---: | ---: |
| Home | 13742 | 13716 |
| Fieldbook | 3464 | 5746 |
| Fieldbook Bezzle | 3275 | 4383 |
| Types | 3118 | 4057 |
| Types Ink | 1759 | 1948 |
| Isles | 3069 | 2927 |
| Quests | 4632 | 5558 |
| Identity quest | 2508 | 3157 |
| About | 4385 | 4516 |
| Journal | 3630 | 4069 |
| Journal detail | 3371 | 3826 |
| Contact | 2616 | 3159 |
| Legal | 2376 | 2524 |
| 404 | 1889 | 1751 |

Computed type scale: homepage H1 **168px desktop -> 80px mobile**; interior H1 **112 -> 54px**; H2 **92 -> 46px**; H3 **40 -> 28px**. Cream #FFF6E8 and plum #1E1838 remain; Bricolage Grotesque and Space Mono roles. Home had 11 images, 0 HTML videos, 0 canvas and 0 forms. Contact one real form. Source snapshot in modules/distilled-web-toolkit/data/tobi-rendered-states-2026-10-08.csv.

### NEW: Quest CTA loses selected service context

All three named service detail CTAs **Accept this quest** were clicked in Chrome:
- /quests/identity-quest -> ../contact -> contact Quest select = Identity quest (correct).
- /quests/website-quest -> ../contact -> Quest select = Identity quest (WRONG; should be Website quest).
- /quests/motion-quest -> ../contact -> Quest select = Identity quest (WRONG; should be Motion quest).

Thus 2 of 3 productized service routes silently misclassify commercial interest. Contact dropdown contains Identity quest, Website quest, Motion quest and Something custom. Name, Email and Message are required, Quest optional. Actual form submissions were NOT sent.

**Quest-to-Contact Intent Continuity:** preserve selected offering via an explicit query such as /contact?quest=website-quest or equivalent application state, decode into the selected form value, and keep it after refresh/navigation. A default is fine on generic Contact entry but not after the visitor explicitly chooses another service. Match visual label and accessible select semantics. Evidence: modules/distilled-web-toolkit/data/tobi-quest-contact-state-2026-10-08.csv.

### Semantics and interaction QA

- The six visual icon-only links to Types are **correctly labelled with accessible aria-labels** such as Ink type: Brand and Grid type: Web, while six conventional description cards also expose readable text. Preserve this good pattern.
- A homepage button is accessibly named Next line and the dialog uses aria-live=polite. One click during sampled runtime didn't alter line text, but sequencing/timing were not exhaustively exercised; do NOT claim a confirmed broken carousel.
- Fieldbook and Journal detail primary titles remain H2 without route-specific H1, as previously recorded.
- Homepage html lang remains empty. Specify the actual document language when building production sites.
- The playful branded /404 correctly returns 404, even though it should not be included in sitemap.
- Real template service prices: Identity from $8k / 6-8 weeks; Website from $6k / 4-6 weeks; Motion from $5k / 3-5 weeks. These are source fixtures, not transfer-ready pricing.
- Full runtime is DOM/Framer illustration (no observed homepage 3D engine).

### Transfer and validation rules

Original eight Tobi patterns, profile archetype and 13 base skins remain intact; **do not duplicate** them. The meaningful new rule is cross-route service intent retention. Adopt a negative QA for mismatched service -> contact field and positive keyboard-labelled icon taxonomy. Align the site-wide canonical/sitemap/robots/OG/redirect host; do not invent additional content routes. No forms were submitted, finances exchanged or external accounts accessed.
