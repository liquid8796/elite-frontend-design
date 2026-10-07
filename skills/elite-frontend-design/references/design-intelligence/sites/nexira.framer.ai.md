# Nexira - full-site distilled design intelligence

Source: https://nexira.framer.ai/
Audit date: 2026-10-07
Coverage: 28/28 sitemap URLs

Audit scope: robots/sitemap discovery, Framer search-index parity, complete same-origin internal-link crawl, generated HTML/CSS across every public route, all 7 service detail pages, all 7 case detail pages, all 7 blog detail pages, representative desktop and 390px runtime audits, typography/tokens, sticky behavior, forms, content families, and utility /404 residue.

This is a whole-site profile, not a homepage-only read.

## Coverage manifest

7 primary routes:
- /
- /contact
- /about
- /blogs
- /team
- /case
- /service

Service detail routes (7):
- /service/game-development
- /service/gaming-art-design
- /service/design-of-character
- /service/assessment-manage
- /service/4d-module-design
- /service/gaming-4d-art
- /service/character-rigging

Case detail routes (7):
- /case/neurox
- /case/vireon
- /case/frostin
- /case/driftal
- /case/lumora
- /case/chronox
- /case/blazic

Blog detail routes (7):
- /blogs/how-indie-games-are-changing-the-scene
- /blogs/pro-game-art-tips-every-artist-should-know
- /blogs/level-design-secrets-every-dev-should-learn
- /blogs/from-game-idea-to-launch-our-full-process
- /blogs/why-game-sound-is-key-to-player-immersion
- /blogs/how-we-build-worlds-that-truly-feel-alive
- /blogs/inside-our-studio-a-game-dev-journey-log

The Framer search index contains the same 28 route keys. The complete same-origin link graph found no extra public route.

Utility route audited separately:
- /404

## Landscape classification

Primary: game / cinematic studio marketing.
Secondary: experiential / agency and template commodity.

Nexira describes itself as a high-quality Framer template for modern game development studios. It is better evidence for studio/agency marketing than for a single game launch campaign.

Use Nexira as:
- a lower-cost cinematic game-studio baseline;
- a route-system reference for services, cases, team, about, blog, and contact;
- a proof that game identity can remain strong without WebGL or video;
- a sticky project-deck and portfolio-routing reference;
- a template-convergence reference for dark/neon gaming studio sites.

Do not treat its team, clients, budgets, dates, awards, player counts, backer counts, article history, contact information, or case outcomes as real business evidence.

## Source-confirmed platform and runtime

- generator: Framer b8d5a97;
- sitemap: 28 public URLs;
- Framer search index: same 28 routes;
- primary breakpoints: >=1360px, 810-1359px, <=809px;`r`n- key breakpoint thresholds are 810px and 1360px;
- main runtime uses Framer Motion;
- no GSAP, ScrollTrigger, Lenis, Spline, Three.js, WebGL, Rive, or Lottie mechanism was found in the main bundle audit;
- all audited routes render with image-led DOM content rather than a continuous canvas renderer;
- /llms.txt is absent;
- /sitemap-index.xml resolves to the 404 experience.

## Source-confirmed typography

Primary rendered roles:
- Oswald: high-character display and section headings;
- Inter: body, UI, navigation, supporting copy;
- Fragment Mono is bundled in generated source and is available as a compact technical/metadata role, but the inspected home runtime primarily loaded Oswald and Inter.

Observed desktop home scale:
- hero H1: about 80px / 90px;
- section H2: about 48px / 58px;
- service H4: about 32px / 32px;
- case project H3: about 36px / 36px.

Representative interior desktop pages use about 64px route headings.

At 390px:
- hero H1: about 52px / 62px;
- interior route heading: about 38px / 45.6px.

Transfer the condensed-display vs quiet-body role contrast, not the exact Oswald + Inter pairing.

## Source-confirmed color and material tokens

Generated tokens include:
- #adff00 lime/acid-green primary accent;
- #ffffff white;
- #222222 dark surface/ink;
- #aeaeae muted gray;
- #e6e6e6 light neutral;
- #1d1d1d deep shell;
- rgba(255,255,255,.2) translucent white;
- #ffd335 yellow secondary accent;
- rgba(173,255,0,.6) translucent lime;
- #2e2e2e secondary dark surface.

Material grammar:
- near-black/deep-gray shell;
- large edge-to-edge game artwork;
- thin/light separators and metadata;
- acidic lime as the dominant action/accent color;
- yellow used as secondary emphasis rather than another full brand system;
- very small radius or hard-edged media framing compared with rounded SaaS cards.

Do not default every gaming site to #adff00 or copy Nexira's exact token pairing.

## Cinematic Without Heavy Rendering

Nexira feels game-oriented without video or WebGL.

It gets cinematic identity from:
- large static game artwork;
- authored image crop and scale;
- condensed Oswald display type;
- high-contrast dark shell;
- acid accent;
- bracketed/HUD-like labels;
- sticky service and case sequencing;
- dense image galleries/carousels;
- spatial overlap and strong vertical pacing;
- restrained Framer Motion instead of a continuous renderer.

This makes Nexira an important counterexample to the assumption that a premium game site requires a heavy 3D runtime.

Use this pattern when the website markets a studio, team, portfolio, or service and high-quality still art can carry the identity.
## Home route

Desktop home is roughly 10.8k px tall at a 1440x900 browser window.

Observed narrative order:
1. hero / NEXT-GEN GAMING EXPERIENCE;
2. studio/about proof with years, active gamers, live games, and backer statement;
3. OUR SERVICES;
4. CASE STUDY;
5. awards/skill metrics;
6. insights & updates;
7. download/install CTA;
8. footer.

### Hero

Observed:
- large image-led game artwork;
- bracketed INDIE GAMES label;
- hero H1 NEXT-GEN GAMING EXPERIENCE;
- platform links/icons;
- dense still-image composition rather than video;
- site CTA DOWNLOAD LAUNCER in navigation.

Hero identity depends more on typography, crop, contrast, and asset selection than on runtime complexity.

### Studio proof

The second major section combines:
- SINCE FROM 1990;
- WE SERVE QUALITY GAMES & ASTRO THING;
- short studio copy;
- 100K active gamers;
- 10+ live games;
- repeated image strip/carousel;
- backer/contact statement.

These exact metrics are template content. Transfer only the structure of studio scale + credibility + human conversion.

### Services sticky sequence

Desktop home services use a sticky editorial sequence.

Observed sticky geometry at desktop:
- left/heading rail around 460x843px, top: 20px;
- four service cards around 600px wide;
- cards about 344-370px tall;
- each sticky item uses top: 20px.

Home services preview:
- Game Development;
- Gaming Art Design;
- Design of Character;
- Assessment & Manage.

At 390px:
- the services heading/context rail remains sticky around 350x653px;
- individual service cards release from the desktop sticky-card behavior;
- document-level width remains 390px.

This is a good example of responsive partial preservation: keep the section identity, release the geometry that would over-constrain reading.

### Sticky case deck

Home case study uses large full-width sticky project cards.

Desktop audited cards:
- Neurox;
- Vireon;
- Frostin;
- Driftal;
- about 1300x612px each;
- sticky top: 20px.

Unlike many responsive releases, Nexira preserves the case deck on mobile.

At 390px:
- sticky case cards remain about 350x889px;
- top remains 20px;
- all cards remain inside the 390px document;
- no document-level horizontal overflow.

This persistence works because each project card becomes a full reading stage rather than a cramped desktop card.

Treat this as a deliberate storytelling mechanism, not a universal mobile rule.

### Awards and skills

The awards block mixes named recognitions with skill percentages:
- AWWWARDS GAME DESIGN;
- APPLE UI DESIGN;
- GOOGLE DEVELOPMENT;
- ACTIVISION UX DESIGN;
- REAL-TIME ART;
- UIX DESIGN;
- ART DIRECTING.

These claims are template placeholder proof. Do not transfer names or percentages as factual credibility.

### News preview

Home previews four article records before the final install CTA.

Observed categories/dates include sports, action, and strategy labels. The full blog route expands the editorial family.

## Capability-to-Case Pairing

Nexira separates services from case studies across both home previews and dedicated route families.

Capability side:
- /service index;
- 7 service detail routes;
- service copy explains what the studio does and how the work is approached.

Proof side:
- /case index;
- 7 case detail routes;
- case copy adds project context, role, challenge, and result framing.

The useful system is:
home capability preview -> service index/detail -> home proof preview -> case index/detail

The visitor can understand both the offer and what that offer looks like in practice.

Do not turn service and case routes into duplicates. Service content explains scope/process; case content explains real project evidence.

## About route

Purpose: studio story + selected team + journey.

Observed:
- route hero ABOUT AGENCY;
- repeated studio thesis;
- REAL-TIME ART percentage block;
- GET IN TOUCH CTA;
- OUR EXPERTS with four team members;
- OUR JOURNEY carousel/timeline;
- backer/contact statement;
- shared footer.

Desktop document: roughly 4.5k px.
Mobile 390px document: roughly 7.0k px.

About does not need the home sticky project deck. It shifts to human/team/history credibility.

## Team route

Purpose: people-first credibility.

Observed:
- OUR AVENGERS hero;
- eight team cards in the inspected index;
- role labels including founder, CEO, developer, designer, support engineer;
- social links;
- awards/skill block;
- news preview;
- shared footer.

Desktop uses multi-column imagery and role labels; mobile expands to a long single-column sequence of roughly 10.3k px with no horizontal overflow.

Names and roles are template content and must not be reused as real staff.

## Service index

Purpose: capability catalog + conversion.

Visible index initially shows six service records:
- Game Development;
- Gaming Art Design;
- Design of Character;
- Assessment & Manage;
- 4d Module Design;
- Gaming 4d art;

A Load More control exists, while the seventh Character Rigging detail route is present in sitemap/search index.

After the service list:
- HAVE A PROJECT LET’S TALK!;
- quote/contact form;
- USER FEEDBACK testimonials;
- shared footer.

Desktop form: about 660x650px.
Mobile form: about 350x650px.

At 390px the service index becomes roughly 6.6k px and remains overflow-free.
## 7 service detail pages

All 7 service detail routes were checked structurally as one family.

Shared grammar:
- route hero SERVICE DETAILS;
- service name;
- lead service image;
- introductory service narrative;
- one or more subheads;
- longer process/explanation copy;
- shared footer.

Representative Game Development detail includes:
- GAME DEVELOPMENT;
- FROM IDEAS TO INTERACTIVE WORLDS;
- BUILDING WITH PURPOSE;
- narrative about concept, level/system design, art, mechanics, Unity/Unreal workflow.

The other six routes keep the same layout family while swapping service content.

Desktop representative document: about 2.8k px.
Mobile representative document: about 3.3k px.

Transfer the detail grammar, not the service copy or tool claims.

## Case index

Purpose: visual proof catalog.

Visible index initially shows six case records:
- Neurox;
- Vireon;
- Frostin;
- Driftal;
- Lumora;
- Chronox;

A Load More control exists, while Blazic is the seventh sitemap/search-index case detail route.

Desktop case index keeps the large sticky project deck:
- cards around 1300x612px;
- top: 20px;
- six visible sticky records.

At 390px:
- sticky project deck is preserved;
- cards around 350x889px;
- top: 20px;
- index becomes roughly 8.7k px;
- no document-level horizontal overflow.

The sticky deck is the strongest interaction signature in the template.

## 7 case detail pages

All 7 case detail pages were checked structurally as one CMS family.

Representative Neurox detail:
- CASE DETAILS hero;
- project title;
- introduction;
- project metadata;
- AUTHOR;
- CLIENT;
- BUDGET;
- YEAR;
- large project image;
- project narrative;
- OUR ROLE;
- CHALLENGES & SOLUTIONS;
- RESULTS;
- shared footer.

Desktop representative case detail:
- document around 3.3k px;
- route heading about 64px;
- project/context block around 410x416px remains sticky at top: 20px while the richer narrative/media column scrolls.

At 390px:
- document around 4.6k px;
- route heading about 38px;
- the desktop sticky project/context block is released;
- reading becomes normal single-column flow;
- no horizontal overflow.

This is a useful contrast with the case index: preserve sticky when it creates a deliberate project stage; release sticky when it would interfere with long-form reading.

Project author, client, budget, dates, results, and all case narratives are template data. Never treat them as factual evidence.

## Blog index

Purpose: editorial thought/SEO surface.

Visible index initially shows six article records:
- How Indie Games Are Changing the Scene;
- Pro Game Art Tips Every Artist Should Know;
- Level Design Secrets Every Dev Should Learn;
- From Game Idea to Launch: Our Full Process;
- Why Game Sound Is Key to Player Immersion;
- How We Build Worlds That Truly Feel Alive;

A Load More control exists, while Inside Our Studio: A Game Dev Journey Log is the seventh sitemap/search-index blog detail route.

Each card exposes category, date, headline, and read-more action.

Desktop document: about 2.6k px.
Mobile document: about 4.8k px.

## 7 blog detail pages

All 7 blog detail pages were checked structurally as one family.

Representative article:
- BLOG DETAILS hero;
- category;
- date;
- article title;
- lead image;
- introductory paragraphs;
- multiple section headings;
- paired inline images;
- closing article section;
- shared footer.

Representative How Indie Games Are Changing the Scene uses:
- BREAKING AWAY FROM THE FORMULA;
- COMMUNITY-DRIVEN DEVELOPMENT;
- INFLUENCE ON THE MAINSTREAM;
- THE FUTURE IS INDEPENDENT.

Desktop article document: about 3.5k px.
Mobile article document: about 4.4k px.

Unlike case detail, the representative article does not use a sticky local rail. Reading stays straightforward.

## Contact route

Purpose: direct studio conversion.

Observed:
- GET IN TOUCH hero;
- phone link;
- email link;
- location link;
- HAVE A PROJECT LET’S TALK!;
- Name;
- Email;
- Message;
- GET A QUOTE submit action;
- shared footer.

Desktop form: about 660x650px.
Mobile form: about 350x650px.

At 390px the route remains exactly document width with no horizontal overflow.

Template phone, email, and address must be replaced by real business data.

## Utility /404

/404 is outside the 28-route sitemap count and was audited under Template Residue Quarantine.

Observed:
- shared navigation;
- large 404 artwork;
- LOOKS LIKE HERE IS NOTHING;
- RETURN HOME recovery action;
- shared footer.

Desktop document is roughly 1.5k px.
Mobile document is roughly 2.0k px and remains 390px wide.

Transfer recovery clarity, not the exact artwork/copy.

## Responsive contract

Source-confirmed responsive families:
- >=1360px large desktop;
- 810-1359px intermediate/tablet;
- <=809px mobile.

Observed 390px behavior across route families:
- home hero 80px -> about 52px;
- interior route headings 64px -> about 38px;
- multi-column team/service/blog layouts stack;
- contact/service forms fit about 350px;
- desktop case-detail sticky context releases;
- home/service heading context may remain sticky when it does not block reading;
- case index/home project cards preserve sticky storytelling at about 350x889px;
- all audited representative routes maintain no document-level horizontal overflow.

Do not automatically remove every desktop sticky mechanism on mobile. Decide by job:
- keep it when each item becomes a readable full-stage chapter;
- release it when it competes with long-form content.

## Motion and input grammar

Observed/source-confirmed:
- Framer Motion runtime;
- sticky positioning is the primary scroll-owned storytelling mechanism;
- carousel controls on journey/about content;
- Load More controls on service/case/blog indexes;
- conventional links/forms for core tasks;
- no evidence of continuous WebGL/video world rendering.

Motion hierarchy should remain:
1. navigation/input feedback;
2. sticky project/service continuity;
3. carousel/index state changes;
4. small entrance/hover motion;
5. decorative motion only if it does not compete with artwork.

## Template residue and fictional proof

Quarantine:
- Framer free-site/editor chrome;
- REDDEVS 2024 designer credit;
- DOWNLOAD LAUNCER copy and template-specific CTA language;
- Nexira logo/name;
- team names and social links;
- 100K active gamers / 10+ live games;
- backer count;
- award names;
- skill percentages;
- service testimonials;
- case author/client/budget/year/results;
- blog dates/categories/article copy;
- phone/email/address;
- exact artwork and image assets.

These artifacts belong to the template/demo identity, not to transferable truth.

## Cross-site synthesis

Compared with Rockstar Games VI:
- GTA VI is a world-launch campaign with authored cinematic chapters, aspect-ratio art direction, trailer/media choreography, and franchise identity;
- Nexira is a studio/service portfolio template;
- GTA VI can justify high media ambition because the entertainment world itself is the product;
- Nexira demonstrates Cinematic Without Heavy Rendering and Capability-to-Case Pairing;
- use Nexira when marketing the people/capabilities behind games, not when launching a single blockbuster world.

Compared with Nudge Folio:
- both use strong type, image-led proof, and portfolio route families;
- Nudge isolates experimental drag/collage in a playground;
- Nexira keeps interaction conventional and puts more emphasis on sticky project stages, service/case separation, and game-studio credibility.

Compared with Powder:
- both use sticky storytelling;
- Powder uses sticky capability stages for an AI product;
- Nexira uses sticky service/project stages for studio proof;
- sticky is a narrative mechanism, not a skin identity.

## Adopt / Adapt / Avoid

| Pattern | Decision | Why |
|---|---|---|
| Cinematic Without Heavy Rendering | Adopt for studio/portfolio game sites | Strong identity without expensive runtime. |
| Capability-to-Case Pairing | Adopt for service businesses | Separates offer from proof while connecting them. |
| Sticky case deck | Adapt | High-impact when each project can own a full stage; verify mobile carefully. |
| Sticky case-detail context | Adapt | Useful desktop orientation; release when reading becomes constrained. |
| Condensed display + quiet UI sans | Adapt | Strong genre signal when role separation stays clear. |
| Bracket/HUD metadata | Adapt cautiously | Useful as a small grammar, easy to overuse. |
| Acid-lime accent on dark shell | Adapt | Effective, but highly recognizable template/game grammar. |
| Index + detail CMS families | Adopt | Supports browse -> inspect behavior. |
| Fake awards/metrics/clients/budgets | Avoid | Template proof is not evidence. |
| Exact artwork, Nexira identity, REDDEVS credit | Avoid | Source/template identity. |

## Best-fit briefs

Use this profile for:
- game development studios;
- art/animation/character studios;
- game outsourcing/service companies;
- indie studio portfolios;
- publisher/studio corporate sites;
- entertainment agencies that need a dark cinematic identity without heavy rendering;
- lower-capability execution that still needs strong game-feel.

## Weak-fit briefs

Do not let this profile dominate:
- a single cinematic franchise/game launch where campaign chapters and trailer proof matter more;
- dense product dashboards;
- developer/API products;
- ecommerce catalogs;
- enterprise legal/compliance sites;
- publications where sticky project stages would distract from reading.

## Regression questions

- Was coverage verified as 28/28 sitemap URLs?
- Were all 7 service detail pages checked as one family?
- Were all 7 case detail pages checked as one family?
- Were all 7 blog detail pages checked as one family?
- Was /404 audited but excluded from the 28 public-route count?
- Were hidden seventh records accounted for despite Load More?
- Does Capability-to-Case Pairing keep services distinct from case proof?
- Does the design stay cinematic without pretending a heavy renderer exists?
- Is the sticky case deck intentional on mobile rather than accidental?
- Does case-detail sticky context release when long-form reading needs it?
- Does every representative 390px route avoid document-level horizontal overflow?
- Are exact template awards, metrics, names, budgets, dates, art, contact data, and vendor identity excluded from transfer?

Pass only when Nexira functions as an audited game-studio/template teacher, not as a source of fictional studio credibility.


