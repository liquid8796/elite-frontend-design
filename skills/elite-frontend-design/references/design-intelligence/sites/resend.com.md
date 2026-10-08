# Resend - distilled design intelligence

Source: https://resend.com/
Audit date: 2026-10-05
Audit surface: live homepage in the user's Chrome, desktop 1910x889 and mobile 390x844, accessibility tree, computed styles, client-side component source, runtime media state, and network-loaded experience assets.

This profile captures transferable design and product-storytelling mechanisms. Do not copy Resend's logo, Rubik-like branded cube, exact black/material treatment, proprietary copy, customer marks, or exact type choices into unrelated products.

## Executive DNA

Resend presents a developer infrastructure product as a sequence of **inspectable proof surfaces** rather than a conventional feature-card landing page.

Its premium character comes from five interacting decisions:

- a restrained near-black material world keeps the shell quiet;
- a high-contrast editorial serif gives the hero and final CTA memory;
- product UI, real-looking code, test states, logs, editor surfaces, and analytics become the main visual content;
- small 3D/material objects punctuate chapters without replacing the product evidence;
- responsive design preserves the branded object while changing its implementation from a live Spline scene on desktop to a pre-rendered `cube.mp4` on mobile.

The useful lesson is not "make a black developer website." It is **make technical evidence beautiful enough to become the marketing visual**.

## Evidence Confidence

### Source-confirmed

- The site is rendered through a Next.js client/application shell with utility-style responsive classes visible in shipped component source.
- The hero desktop experience dynamically loads a `RubiksCube` component with SSR disabled and preloads `/static/cube.splinecode` for wider viewports.
- The network audit confirmed a successful request for `https://resend.com/static/cube.splinecode`.
- The mobile hero hides the desktop live scene and uses an autoplaying, muted, looping, plays-inline `/static/cube.mp4` with `/static/cube-fallback.jpg` poster.
- Supporting chapter ornaments use small pre-rendered videos such as `3d-integrate-morning.mp4`, `3d-broadcast.mp4`, `3d-react.mp4`, and `3d-control.mp4`, with explicit poster/fallback assets.
- The integration section maintains SDK/language and framework selection through real tabs; source shows language/framework state and local-storage persistence for the current SDK/framework choice.
- The integration chapter includes real code syntax/content rather than rasterized code imagery.
- Homepage source exposes reusable section primitives with responsive spacing (`px-6`, mobile/desktop vertical padding) and explicit heading size variants.
- Loaded font roles include Domaine, aBCFavorit, CommitMono, and Inter.

### Observed

- Desktop opens with a centered navigation bar, large left-aligned serif headline, compact supporting copy/actions, and a dark 3D cube stage occupying the right half.
- The hero uses grayscale/black material and lighting rather than a broad chromatic gradient; color is scarce.
- Company logos appear early as trust proof before the deep product walkthrough.
- "Integrate this morning" immediately gives visitors an ecosystem selector and a large code surface rather than a generic illustration.
- "First-class developer experience" demonstrates test mode, delivery-like states, event/output data, and webhooks as product-shaped evidence.
- "Write using a delightful editor", contact/analytics, React-email, deliverability, and control/analytics chapters continue to use product UI or implementation evidence as their dominant visual.
- The page uses functional tabs for SDKs, files/templates, and analytics/control states.
- Product UI is framed with restrained borders, subtle surface elevation, and large amounts of black negative space rather than floating bright cards.
- Mobile has no document-level horizontal overflow at 390px in the audited state; the navigation collapses to logo + menu.
- Mobile keeps the cube, serif hero role, monochrome material world, product-first narrative, and large proof surfaces while stacking/reflowing desktop compositions.

### Inferred

- Resend uses visual restraint to make code syntax, status colors, product states, and the occasional purple material glow feel semantically important.
- The page is designed to reduce developer skepticism by moving rapidly from positioning to recognizable companies, authentic API/code shape, safe test behavior, and operational evidence.
- Small 3D chapter objects behave like punctuation: they supply craft and continuity without competing with the product itself.

## Design DNA

### Composition

The desktop system is centered around a generous max-width content column with large vertical chapter spacing.

- hero: asymmetric two-column composition, text left / branded object right;
- most later chapter introductions: centered title + short description + large product evidence below;
- some evidence chapters split into two product capabilities rather than many equal cards;
- black negative space separates chapters more than surface color changes do;
- major demos are allowed to be much larger than their labels, making the product itself the visual hierarchy.

**Reusable rule**

When a technical product has strong UI/code evidence, let the evidence occupy the visual scale normally reserved for campaign illustration. Do not shrink a real product into a laptop mockup while giving decorative art the hero role.

### Typography

Observed/source-confirmed roles:

- **Domaine**: editorial serif role for the hero and closing statement; desktop hero measured at roughly 96px, mobile at roughly 64px.
- **aBCFavorit**: primary display/product sans role; major desktop chapter headings measured around 56px and mobile around 48px.
- **CommitMono**: technical/code/data role where monospaced scanning is useful.
- **Inter**: neutral system/body support role in the loaded font set.

The typography hierarchy does not use mono everywhere merely because the audience is developers. Mono is reserved for technical content; editorial and explanatory language remains human-readable and brand-led.

**Reusable rule**

Developer identity does not require turning the entire interface into a terminal. Assign serif/sans/mono by communicative job: memory/thesis, product/explanation, and code/data.

### Color + Material

- base shell is true/near black with low-contrast gray borders and surfaces;
- primary text is soft white rather than high-chroma brand color;
- hero object uses black materials, specular highlights, texture variation, and light to create depth;
- purple appears as a rare material/glow cue rather than the universal accent on every component;
- code syntax and product status colors retain semantic visibility inside the monochrome shell;
- white primary actions are used sparingly, producing strong contrast without needing a global bright accent.

**Reusable rule: semantic accent budget**

In a restrained technical palette, reserve chroma for information that benefits from distinction: syntax, status, selected state, data, or one identity-bearing material cue. If every border, icon, glow, and CTA uses the accent, the semantic value disappears.

### Media + Rendering

The hero is a responsive hybrid:

**Desktop**

- dynamically loaded branded `RubiksCube` scene;
- SSR disabled for the interactive scene;
- `cube.splinecode` preloaded for wide viewports;
- semantic DOM owns the headline, copy, CTAs, and navigation around the scene.

**Mobile**

- live desktop scene is not rendered visibly;
- `/static/cube.mp4` supplies the same recognizable object/material story;
- autoplay is muted, looping, and `playsInline`;
- a poster image supplies a first/fallback frame.

Supporting sections generally avoid loading another full interactive world. Small 170px pre-rendered 3D videos act as chapter punctuation while large DOM/product demos carry the actual evidence.

**Reusable rule: Responsive Fidelity Substitution**

Preserve the identity-bearing result while changing implementation cost by breakpoint. Live interaction is not sacred; perceptual job and product meaning are.

### Product Evidence Before Feature Claims

Resend repeatedly makes the product surface itself the argument.

Examples from the audited homepage:

- SDK tabs lead directly into authentic code;
- test mode exposes safe experimentation and HTTP-like success output;
- modular webhooks are shown in the context of event/delivery behavior;
- the editor chapter shows the actual composition surface;
- contact and analytics sections use real product-shaped views;
- React Email pairs framework/source concepts with a template/code environment;
- later control/analytics content remains stateful/tabbed rather than becoming a static icon grid.

The resulting narrative is closer to a guided product tour than a brochure.

**Transfer**

For developer infrastructure, analytics, workflow software, or APIs, use **claim -> inspectable product evidence -> explanation** whenever the evidence is self-explanatory enough.

### Code as Product Proof

The integration section treats code as first-class product media.

Strong details:

- language choices are explicit and recognizable (Node.js, Python, PHP, Go, Rust, Java, .NET, REST, SMTP, and others);
- a second layer can represent framework/runtime variants;
- selected choices change the large code surface;
- state persistence means the page remembers the developer's ecosystem preference;
- syntax color is restrained inside the black shell, so highlighted API names/values aid scanning rather than becoming neon decoration.

**Reusable rule**

If ease of integration is a core value proposition, the shortest real integration path is stronger proof than an illustration that says integration is easy.

### Functional Tabs as Persuasion

Tabs are not used only to save vertical space. They let visitors answer "does this fit my stack/use case?" themselves.

On this page, tab families select:

- SDK/language;
- framework/snippet variants;
- React email files/templates;
- analytics/control capabilities.

This turns personalization into low-friction persuasion.

**Reusable rule**

Use tabs when each option represents a meaningful visitor context and the content underneath materially changes. Avoid tabs whose panels are cosmetic variations of the same marketing sentence.

### Motion

The dominant motion language is restrained relative to the amount of content:

- hero text has a coordinated load/reveal treatment;
- the branded cube supplies continuous/looping material motion;
- chapter ornaments use small looping video rather than making every DOM block animate independently;
- product demos provide state change and interaction as motion;
- selected/tab states communicate causality without requiring large scroll choreography.

The page therefore feels dynamic because **evidence changes**, not because every section slides upward.

### Interaction + Input Grammar

- navigation remains conventional and predictable;
- SDK/framework tabs let a developer choose their technical context;
- test mode exposes a safe simulation concept rather than encouraging real-world side effects inside marketing;
- editor/product demonstrations use familiar UI controls and states;
- desktop branded 3D is a signature visual layer, while product controls stay ordinary enough to understand immediately;
- mobile collapses navigation and substitutes the expensive signature mechanism without changing primary actions.

**Reusable rule**

Experimental visuals can surround conventional product controls. Do not force novel interaction grammar onto code tabs, editors, logs, analytics, or actions whose familiarity is part of their credibility.

### Narrative + Developer Trust Ladder

The homepage roughly follows this trust-building sequence:

1. concise category promise: email for developers;
2. recognizable company proof;
3. immediate integration evidence through real code;
4. safe operational evidence through test mode/webhooks;
5. higher-level authoring/product workflow evidence;
6. contact/analytics and React ecosystem depth;
7. infrastructure/deliverability detail;
8. high-authority testimonial;
9. operational control/analytics evidence;
10. broad customer validation;
11. simple closing conversion.

This sequence answers developer objections in increasing depth: "is it credible?", "can I integrate it?", "can I test it safely?", "can my team operate it?", "is the infrastructure serious?", "do respected teams trust it?"

**Reusable rule**

For technical products, organize proof around likely adoption objections rather than around the company's internal feature taxonomy.

## Responsive Brand Payload

Mobile was audited at 390x844.

What survived:

- black material world;
- branded cube silhouette/material;
- Domaine serif hero role;
- product-first narrative;
- primary conversion actions;
- code/product evidence as the dominant content type.

What changed:

- desktop navigation collapses to logo + menu;
- hero becomes vertically stacked and centered;
- headline scales from roughly 96px to 64px;
- live Spline desktop scene is replaced by the 225px pre-rendered `cube.mp4`;
- later two-column/product layouts stack or narrow;
- major sans headings scale from roughly 56px to 48px;
- mobile document width remains 390px in the audited viewport with no document-level horizontal overflow.

This is a strong example of combining **Responsive Brand Payload** with **Responsive Fidelity Substitution**: retain the recognizable brand result while reducing interaction/runtime cost.

## Technical Architecture Lessons

### 1. Progressive enhancement for the signature visual

Desktop earns a richer interactive Spline scene. Mobile receives a pre-rendered equivalent with a poster.

Transfer:

- define the visual job independently of renderer technology;
- allow breakpoint/device capability to choose the implementation;
- provide first-frame/fallback media;
- keep essential meaning and actions in semantic DOM.

### 2. Pre-rendered 3D as chapter punctuation

Several chapter objects are small MP4 assets rather than additional live WebGL scenes.

Transfer:

- use live rendering only where interaction or state needs it;
- use short pre-rendered loops when the job is visual continuity/atmosphere;
- use posters and `playsInline` for resilient mobile behavior.

### 3. Persist visitor technical context

Source shows SDK/framework selection stored in local state/local storage.

Transfer:

- when a visitor selects an ecosystem context, keep subsequent evidence consistent where reasonable;
- persistence should reduce repeated choice, not silently change product behavior.

### 4. Reusable section/type primitives without visual sameness

The page has clear shared Section/SectionTitle/Description and heading size primitives, but the evidence area inside each chapter changes substantially.

Transfer:

- standardize rhythm, gutters, typography roles, and accessibility;
- vary the proof mechanism according to the feature rather than forcing one card component everywhere.

### 5. Product state is higher-value motion than decorative entrance effects

Tabs, test results, editor state, logs, analytics, and code selection create meaningful change.

Transfer:

- spend animation/interaction budget on cause-and-effect users can understand;
- add ambient motion only after product evidence is already legible.

## Cross-Site Synthesis with Refokus

Resend and Refokus look different, but together they strengthen several general lessons:

- **allocation of ambition**: both keep the shell disciplined and give a small number of regions disproportionate craft;
- **type-role contrast**: both use expressive editorial type selectively while neutral product/body roles do most explanatory work;
- **signature vs system**: memorable 3D/material work is separated from ordinary semantic content and controls;
- **responsive brand payload**: mobile preserves recognizable identity rather than collapsing into a generic stacked template;
- **proof is structural**: Refokus uses client/case-study proof; Resend uses code/product/operational proof. Premium quality is not only aesthetic polish - it is the sequencing of credible evidence.

The important divergence is equally useful:

- Refokus sells creative transformation, so authored motion/editorial case studies can carry proof.
- Resend sells developer infrastructure, so authentic product/code/operational states must carry more of the proof burden.

Do not average these sites into one style. Route the proof mechanism to the product.

## Adopt / Adapt / Avoid Matrix

| Pattern | Default decision | Why |
|---|---|---|
| Product Evidence Before Feature Claims | Adopt for software/developer products | Lets the real product carry credibility. |
| Code as Product Proof | Adopt when integration/API quality is a core value proposition | Directly answers developer adoption questions. |
| Functional tabs as persuasion | Adapt | Strong when users genuinely differ by stack/context; unnecessary otherwise. |
| Responsive Fidelity Substitution | Adopt for expensive signature visuals | Preserves identity without forcing desktop rendering cost onto mobile. |
| Serif + product sans + technical mono roles | Adapt | Transfer the role logic, not the exact fonts. |
| Monochrome material shell + scarce semantic accents | Adapt | Strong for developer/infrastructure brands but can become a generic devtool cliché. |
| Small pre-rendered 3D chapter ornaments | Adapt | Useful when they reinforce a material world; remove if they become decorative filler. |
| Exact black cube / purple underglow | Avoid | Signature-specific identity. |
| Exact Resend code/API/copy | Avoid | Proprietary/context-specific product truth. |
| Copying the exact page section order | Avoid | The trust ladder must follow the new product's real objections. |

## Best-fit Briefs

Use this profile as inspiration for:

- developer tools, APIs, infrastructure, observability, deployment, data, and workflow products;
- technical SaaS where integration ease is a key purchase/adoption concern;
- products with strong UI/code evidence that can replace generic marketing illustrations;
- premium dark product sites that need restraint without losing specificity;
- responsive experiences where a live desktop signature should degrade to a cheaper equivalent rather than disappear.

## Weak-fit Briefs

Do not let this profile dominate:

- consumer/lifestyle products where code evidence is irrelevant;
- dense operational applications where the visitor is already inside the tool and needs task speed, not persuasion;
- brands whose visual identity depends on warmth, photography, craft material, or high chroma;
- products whose interface is not mature enough to survive being used as the primary marketing visual;
- cases where adding fake code would misrepresent the real API or integration quality.

## Regression Questions

When future work claims to apply Resend-derived intelligence, ask:

- Does product/code evidence prove a real claim, or is it decorative technical wallpaper?
- Does the code match the new product's real API and supported ecosystems?
- Do functional tabs correspond to meaningful visitor contexts?
- Is color scarce because semantics/brand call for it, or because "developer site = black" became a cliché?
- Are 3D/video ornaments subordinate to the product evidence?
- Does the trust ladder answer the new product's adoption objections in the right order?
- On mobile, what exact experience value was preserved when the implementation changed?
- If desktop uses a live renderer and mobile uses media, do they still communicate the same identity-bearing subject/material role?
- Does the result belong to the new product, or is Resend visibly recognizable in its cube, palette, copy, or page order?

Pass only when the mechanisms improve credibility and clarity while the source site's proprietary identity disappears.

## Whole-Site Re-Audit — 2026-10-08

**Scope correction.** The original 2026-10-05 research was homepage-deep; the 2026-10-07 toolkit snapshot recorded 11 URLs, which were actually 11 child sitemaps in a sitemap index, not the number of pages. This 2026-10-08 re-audit inventoried and requested **1,015/1,015 sitemap-declared URLs**. 1,014 returned HTTP 200 and the declared /shop URL returned HTTP 404. The audit additionally used actual Chrome rendered states across the major route families, with representative desktop and 390x844 mobile checks. Individual document interaction flows were sampled, not exhaustively replayed on each of the 1,015 pages.

### Eleven sitemap surfaces / 1,015 declared URLs

| Surface | URLs | Route job |
| --- | ---: | --- |
| docs | 413 | search/browse API reference, dashboard tasks, webhooks, troubleshooting and guides |
| blog | 176 | company/engineering/editorial knowledge |
| changelog | 111 | chronological product trust and release evidence |
| other | 124 | core marketing, 11 feature landings, 3 product landings, pricing, enterprise, language/platform integrations, migration index, careers, brand, launches and events |
| handbook | 65 | operating culture, design process, engineering, people, marketing and sales |
| humans | 59 | people attribution, authored work and team identity |
| customers | 46 | named customer proof |
| legal | 7 | compliance/policy |
| clubs | 6 | team-curated culture collections |
| migrate | 5 | competitor-specific migration bridges |
| security | 3 | dedicated trust/compliance |
| **Total** | **1,015** | **1,014 200 + 1 sitemap 404** |

The machine-readable per-route census lives at references/modules/distilled-web-toolkit/data/resend-route-inventory-2026-10-08.csv. It records sitemap group, URL, HTTP status, title and H1 count for each declared URL. Counts are a dated sitemap snapshot, not timeless constants.

### Marketing and product route grammar

Homepage identity and original design DNA remain accurate: black/near-black background, Domaine editorial headline, aBCFavorit product explanatory headings, CommitMono code, responsive live Spline cube vs mobile video fallback, and truthful product evidence.

But the product expands into many separate buyer jobs:
- /products/transactional-emails — identity -> SDK proof -> API observability -> event/webhook evidence -> use cases -> trust. Representative 1910x8364 desktop, 390x mobile without document overflow.
- /products/marketing-emails — audience management -> subscribe/unsubscribe API -> performance visualization -> all-in-one product bridge. Desktop ~1910x9679; mobile ~390x12572, zero outer overflow.
- /features/email-api — framework fit -> log/event/webhook observability -> special capabilities -> idempotency/reliability. Desktop ~1910x7573; mobile ~390x9025.
- /features/inbound — received-message event model -> attachments -> structured data -> setup steps.
- /features/automations — trigger/events -> condition/wait/delay diagram -> run observability -> recipes.
- /features/templates — templates library -> collaboration -> drafts -> version history.
- /enterprise — enterprise concerns -> named scale proof -> compliance -> implementation -> contact form.
- /pricing — plans -> pay-as-you-go -> add-ons -> feature-category comparison, not one simple price list.

**Capability-as-Inspectable-State** applies across these routes: the art direction is consistent, but the proof surface changes to show the actual product job. Avoid generic feature-page clones.

### Integration-specific landing adapters

Dozens of top-level language, framework, platform, AI-agent and integration routes (for example /nodejs, /nextjs, /python, /cloudflare, /codex) use a repeatable job:
stack-specific promise -> recognizable code/SDK fit -> minimal setup -> general platform benefits -> CTA.
Rendered /nodejs is ~1910x4273 with a selectable code surface. This turns broad developer infrastructure into stack-specific entry points without changing the core technical identity.

### Migration Converter Bridge

/migrate has five competitor destinations. /migrate/sendgrid is ~1910x13438 desktop and ~390x15146 mobile with zero outer overflow. It combines:
competitor-specific promise -> code converter -> conceptual comparison -> SDK/send API/SMTP/webhook mappings -> security/idempotency considerations -> migration CTA.
A migration route must reduce actual switch cost, not only attack a competitor or repeat landing-page claims. Code conversion is a proof interaction; implementation guides remain selectable textual content.

### Dedicated docs reader — three context rails

413 declared docs routes span:
- 143 API reference paths;
- 69 dashboard task paths;
- 55 knowledge-base paths;
- 44 webhook paths;
- 19 explicit guides, plus integration/tutorial entry points.

Rendered docs are materially different from marketing pages. At desktop the shell has a fixed header, left navigation, a contained **main scroll viewport**, and a sticky right page outline. On 390x844 the document root remains 390x844 with **main clientHeight ~714px** and its own multi-thousand-pixel scrollHeight; outer horizontal overflow is zero. This is **Three-Rail Documentation Reader / Scroll Ownership Contract**, not a full-page scroll layout.

Representative observations:
- /docs/introduction — quickstart and framework entry; ~3551px main scroll content at 390.
- /docs/api-reference/emails/send-email — parameter/header reference and 23 preformatted code blocks; ~7100px main scroll content at 390.
- /docs/dashboard/automations/create-automation — task/action guidance with dashboard and API branches; ~9014px internal main content desktop.
- /docs/knowledge-base/audience-hygiene — explanatory troubleshooting/operational guidance.
- /docs/guides/dns/godaddy — provider-specific illustrated operational steps; ~9153px internal main content desktop.
- /docs/webhooks/introduction — event model, requirements and quickstart.

Important distinctions: API reference pages need parameter tables/request-response code; dashboard instructions need UI/action sequences; DNS guides need provider-specific screenshots; knowledge-base routes need plain-language failure diagnosis. They share reading chrome, not identical content structure.

### Knowledge and release lifecycle

Blog index is a featured + latest-post archive (176 details; desktop ~1910x23432 with many image nodes). Representative /blog/email-verification-api is a technical article with section headings, code and some video. Mobile article remains readable with no outer overflow.

Changelog has **111 details** and a very deep index (~1910x68260 / 390x54602), with **sticky dates and chronology markers**. Individual updates pair the change description with concrete API / UI proof and related product destinations. Use **Sticky Release Chronology** but cap initial DOM/render cost and provide navigation/filtering; a 68k-pixel document and 273 image nodes are a performance warning, not a default pattern.

### Customer proof and public operating system

Customers directory (46 stories) is a visual named-proof hub; the individual case /customers/basedash is intentionally concise (~1910x1519) rather than padded. Use **Evidence-Scaled Customer Stories**.

The public handbook is a separate editorial experience:
- root /handbook uses an oversized expressive H1 (~450px desktop -> ~156px mobile), then seven departments (Company, People, Engineering, Design, Success, Marketing, Sales);
- 65 handbook details;
- /handbook/design/how-we-think-about-design uses an ~80px heading, compact policy headings and persistent departmental wayfinding.

Humans is a people index with 59 profile routes. /humans/zeno-rocha connects the individual to authored articles, product releases and company history; this **Human Attribution Graph** turns content authorship into inspectable credibility rather than an anonymous corporate blog. Clubs (6 pages) are curated real-human interests with themed lists; they contribute culture signals rather than direct conversion.

This family promotes **Public Operating System as Trust Proof**: company process, people and published engineering/design methods reinforce product credibility. Do not clone private biographies or treat culture collections as a replacement for product proof.

### Event and brand subsystems

/forward is an event microsite with its own fixed full-viewport 4-canvas composition, rather than the standard dark marketing shell; /forward/agenda and /forward/faq are related destinations. /brand exposes naming, logo and screenshot guidance. /careers and /security have dedicated trust/recruiting narratives. Keep campaign worlds isolated from day-to-day product/documentation runtime.

### Responsive contracts and QA

At 390x844, tested representative homepage, feature, product, pricing, migration, docs, article, changelog, handbook, people, clubs and careers routes had **zero document-level horizontal overflow**. Homepage retains the existing Spline desktop -> video mobile substitution (desktop 1 canvas and 5 videos; mobile 0 canvas and 5 videos). Product display H1 commonly scales from ~76.8px to 64px, section H2 from ~56px to 48px. Docs instead uses H1 ~36px desktop / 30px mobile with internal main scrolling.

Full census: **1,014 HTTP 200, 1 HTTP 404** at /shop. The 404 is a stale sitemap entry, not a deliberate product experience. 20 sitemap-backed 200 pages in the diverse 'other' surface lacked an H1 in the HTML response (notably private deal/confirmation/campaign variants), and some pages expose multiple H1s (/migrate, selected product/docs/handbook routes); heading semantics need route-specific QA.

QA rule: **Sitemap -> HTTP Status -> Semantic Route Parity**. Do not assume a route exists just because the sitemap declares it. Do not assume a decorative visual title is a valid H1. For internally scrolling docs, test scroll ownership, focus, anchor navigation and mobile viewport keyboard accessibility — a zero outer overflow reading alone does not guarantee that inner interaction works.

### Newly promoted transfer mechanisms

1. Route-Complete Developer Product Ecosystem — segment by actual visitor job, not one beautiful homepage.
2. Capability-as-Inspectable-State — demo UI/code/logs/effects appropriate to the capability.
3. Stack-Specific Integration Adapter — credible stack-specific entry and code.
4. Migration Converter Bridge — reduce effort to migrate via concrete mappings.
5. Three-Rail Documentation Reader — distinct side navigation, internal document scroll and right outline.
6. Sticky Release Chronology — treat dated shipped work as a proof stream.
7. Public Operating System as Trust Proof — handbook + people + authorship reinforce product reliability.
8. Human Attribution Graph — link makers to work and thinking.
9. Evidence-Scaled Customer Stories — case length follows available facts.
10. Content Lifecycle Lattice — docs/changelog/blog/customers cross-link product learning and trust.

### Non-transferable / caveats

Do not copy Resend's proprietary code, SDK examples as generic API fixtures, team profiles, editorial copy, brand assets, exact fonts, cube/film, or event canvas assets. Any numerical geometry and page counts above are observations from the 2026-10-08 audit. Full HTTP census != deep interaction audit of 1,015 individual pages.
