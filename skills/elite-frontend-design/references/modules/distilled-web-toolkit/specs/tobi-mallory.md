# Tobi Mallory — Toolkit Spec

Source: https://tobi-mallory.framer.website/
Deep profile: `../../../design-intelligence/sites/tobi-mallory.framer.website.md`
Archetype: whimsical-world-portfolio
Primary skin anchor: `whimsical-world-portfolio`

## Live Snapshot — 2026-10-07

- Sitemap/search index: 30/30 matching route keys.
- Route families: 10 core/utility + 7 Fieldbook details + 6 Type details + 4 Journal details + 3 Quest details.
- Framer d485f69.
- Desktop home: target 1440x900; rendered document ~1425x13739; no positive outer overflow.
- Mobile home: 390x844; ~390x13716; zero outer overflow.
- Representative mobile Fieldbook/Type/Isles/Journal/Quest/Contact routes also showed zero document-level horizontal overflow.
- Homepage runtime: 239 animations, 0 canvas, 0 HTML video.
- Type roles: Bricolage Grotesque + Space Mono.
- Shell: warm cream around #fff6e8 with dark plum/ink around #1e1838.
- Breakpoints observed around 810px and 1200px.
- Canonical/robots/sitemap currently point to `eternal-fade-087901.framer.app` instead of the browsed host.

## Archetype Job

Use this archetype when a creative portfolio or small studio can organize real work, disciplines and services through one recurring collectible/world metaphor.

The metaphor must help:
- memory;
- taxonomy;
- navigation;
- proof;
- commercial packaging.

Do not use this archetype merely because mascots or RPG language look distinctive.

## World Model

Audited translation:
- projects -> Fieldbook entries / creatures;
- disciplines -> Types;
- services -> Quests;
- taxonomy overview -> Isles;
- achievements -> Seals;
- experience -> Stats / levelling;
- articles -> Logbook;
- contact -> Save Point;
- helper -> Guide.

The transferable mechanism is the stable mapping, not the source words.

## Composition Grammar

### Home

identity -> teach vocabulary -> collection/work -> case proof -> taxonomy/types -> project evolution -> world map -> truthful stats/achievements -> service packages -> process -> about/origin -> content/logbook -> contact/save point

### Collection index

collection thesis -> numbered/typed records -> mnemonic identity + real project cue -> direct detail action -> conversion

### Case detail

mnemonic title/number/type -> premise -> client/year/scope/result -> brief -> intervention -> outcome -> related/evolved records -> conversion

### Taxonomy detail

real category title -> short promise -> category/world identity -> related work/index -> all categories -> contact

### Service / quest detail

themed service title -> plain outcome -> price/range -> duration -> approach -> deliverables -> primary action -> all services -> contact

## Visual System

Use one stable shell with category-level variation.

Category identity may own:
- accent family;
- badge/emblem;
- illustration/character family;
- local surface tint;
- map position;
- bounded motion cue.

Keep category names visible as text. Never rely on color alone.

## Proof System

### Mnemonic Case-Study Encoding

Each project may have:
- memorable codename/object/creature;
- optional collection number;
- category/type;
- visual emblem/illustration.

Underneath, keep:
- client/product;
- year;
- scope;
- problem;
- intervention;
- result;
- related/evolved work.

### Project Evolution as Relationship Proof

When truthful, connect an earlier and later engagement to show:
- continuity;
- system scalability;
- deeper client/product understanding;
- expanded scope;
- new outcome.

## Metaphor Translation Contract

For every world term write:

`world term -> real user job -> visible cue -> accessible/conventional fallback`

Check:
- navigation labels;
- URLs/page titles;
- headings/subtitles;
- metadata;
- service price/timing;
- form labels;
- accessible names;
- mobile/touch state.

## Motion / Media

Prefer lightweight illustrated/DOM worldbuilding:
- scroll entrances;
- card flips;
- badge responses;
- process/hatching illustration;
- map destination feedback;
- category transitions.

Do not add WebGL unless continuous world state or direct manipulation truly requires it.

Reduced motion should show the final semantic state without requiring animation.

## Responsive Contract

Preserve:
- world vocabulary;
- real-job mapping;
- taxonomy;
- mnemonic project cues;
- client/scope/result proof;
- service clarity;
- category identity.

Transform:
- giant display type -> deliberate smaller role-preserving type;
- hover card backs -> tap/focus or always-visible critical metadata;
- map hotspots -> named touch targets + list fallback;
- decorative motion -> static final state when needed;
- multi-column collection -> stacked readable flow.

Outer document should remain width-stable.

## QA / Anti-Patterns

Reject:
- mascot over proof;
- metaphor that obscures user job;
- hover-only collection meaning;
- color-only taxonomy;
- fake stats/levels/badges;
- copied source creatures/names/palette;
- visual page title with no semantic H1;
- canonical/sitemap host drift;
- game vocabulary that harms conventional contact/service/legal clarity.

## Toolkit Patterns

`tobi-world-metaphor-ia`, `tobi-taxonomy-physics`, `tobi-mnemonic-case`, `tobi-metaphor-translation`, `tobi-project-evolution`, `tobi-light-worldbuilding`, `tobi-service-quests`, `tobi-collection-loop`.

## Best Pairings

Pair with:
- `frontend-design` for art direction;
- `frontend-qa` for semantic/touch/responsive verification;
- `design-intelligence` for Adaptive Capability Routing;
- `ui-ux-pro-max` only when product/system UI concerns exceed the portfolio world layer.

Do not combine this skin with game-studio or cinematic-launch merely because the vocabulary is playful.

## Do Not Transfer

Do not transfer:
- Tobi Mallory identity;
- creature names Bezzle/Curvix/Pixit/Mote/Lumpkin/Hum/Dart;
- source artwork;
- exact palette;
- exact Bricolage/Space Mono pairing;
- Fieldbook/Isles/Quest/Save Point terminology unless independently justified;
- source project/client claims or metrics;
- Framer platform chrome;
- staging/publish host metadata.

## Full Public Site Re-Audit Delta — 2026-10-08

30 sitemap paths audited on both public and canonical source host (60 declared route HTTP requests): 29 HTML 200 plus /404 HTTP 404 per host. Extra invalid path HTTP 404 per host. All 30 public-host canonicals point to eternal-fade-087901.framer.app. The sitemap itself contains /404; remove it from a production SEO sitemap.

Chrome inspected 15 route templates desktop 1440x900 and 15 matching mobile 390x844 with zero outer overflow. Home H1 168->80px, interior H1 112->54px, major H2 92->46px. All route families remain authored and accessible without WebGL.

**New conversion defect:** all three Quest service detail CTAs navigate to ../contact but the Quest dropdown defaults to Identity quest. Website and Motion quest intent is lost (2 of 3). Add pattern tobi-quest-intent-continuity: pass service slug in contact query/state and preselect correct offer, retaining after reload. Six Types icon-only links DO have aria-label, a positive accessible fallback. Detail/article main headings H2 without H1 and empty homepage lang persist.

Evidence: data/tobi-dual-host-routes-2026-10-08.csv; data/tobi-rendered-states-2026-10-08.csv; data/tobi-quest-contact-state-2026-10-08.csv.
