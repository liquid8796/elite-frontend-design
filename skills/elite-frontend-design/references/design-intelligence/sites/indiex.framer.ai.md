# Indiex - full-site distilled design intelligence

Source: https://indiex.framer.ai/
Audit date: 2026-10-07
Coverage: 2/2 sitemap URLs + all 15 homepage sections / anchor destinations

Audit scope: robots/sitemap discovery, complete same-origin route inventory, rendered Chrome desktop/mobile audits, full homepage section sequence, /404 recovery route, typography/color/runtime evidence, fixed/sticky ownership, game-selector and FAQ interaction semantics, video/media behavior, forms, SEO/canonical metadata, mobile transformations, and template-residue QA.

This is a whole-site profile, not a homepage-only read.

## Coverage manifest

Sitemap URLs:
- /
- /404

The public homepage is a one-page system with these routed anchor destinations:
- #about
- #service
- #game
- #testimonial
- #faq
- #team
- #contact

Additional authored homepage sections without public anchor IDs:
- featured characters gallery;
- transition/marquee strips;
- final studio proof / call-now block;
- sponsor/trust strips;
- footer.

The sitemap contains /404 even though the route correctly responds with HTTP 404. Arbitrary missing paths also respond with HTTP 404 and render the recovery experience.

## Landscape classification

Primary: compact one-page game-studio / game-service marketing.
Secondary: cinematic template commodity.

Indiex is useful as:
- a compact alternative to a deep multi-route game-studio site;
- evidence that a long one-page studio funnel can carry about, capability, game proof, social proof, FAQ, team, lead capture and trust without separate route families;
- a reference for desktop sticky game-selection released on mobile;
- a reference for poster-first video placement inside an otherwise still/image-heavy page;
- a strong negative reference for template-content contamination and incomplete interaction semantics.

Indiex is closely related to the same game-studio/template visual family already represented by Nexira, but its information architecture is materially different: Indiex compresses the commercial system into one long anchor-driven route rather than using service/case/blog detail families.

Do not treat any company identity, client/testimonial, player count, live-game count, years, contact information, partner/sponsor logo, team member, or game description as verified business evidence.

## Source-confirmed platform and route behavior

- generator: Framer befeeaf;
- sitemap: 2 URLs;
- robots: Allow: / and advertises /sitemap.xml;
- canonical home: https://indiex.framer.ai/;
- canonical 404: https://indiex.framer.ai/404;
- missing route response: HTTP 404;
- /404 response: HTTP 404;
- document language: en;
- home meta description explicitly describes Indiex as a Framer template for game development studios;
- no continuous canvas/WebGL renderer is present;
- primary runtime is DOM/image/video + Framer Motion;
- audited home uses 0 canvas;
- desktop home exposes 4 runtime animations after settle;
- mobile home exposes 0 runtime animations after settle.

## Source-confirmed typography

Rendered roles:
- Oswald: all major display headings and section titles;
- Inter: body, navigation, labels, most utility copy;
- Inter Display: selected supporting/display UI roles;
- Poppins appears as a minor bundled/rendered role.

Desktop 1440x900:
- H1 GAME STUDIO: 96px / 106px, weight 700, uppercase;
- major H2: 48px / 58px, weight 700, uppercase;
- final metric H3: 32px / 42px.

Mobile 390x844:
- H1: 48px / 58px;
- major H2: 32px / 42px;
- final metric H3: 24px / 34px.

Transfer the condensed display / neutral body contrast, not the exact Oswald + Inter pairing.

## Source-confirmed color and material grammar

Dominant rendered colors:
- #0b121d / rgb(11,18,29): deep navy page shell;
- #1b222e / rgb(27,34,46): raised dark section/surface;
- #94cb53 / rgb(148,203,83): acidic green brand/action accent;
- #e0e0e0 / rgb(224,224,224): primary light text;
- #aeaeae / rgb(174,174,174): muted text;
- white for selected high-contrast text/art overlays.

Material language:
- dark navy shell rather than neutral black;
- acid green as the dominant action/HUD accent;
- hard or low-radius structural surfaces;
- 12-20px radius appears mainly on image/card content;
- bracketed labels act as small HUD-like section markers;
- large game photography/illustration supplies most of the atmosphere;
- separators and utility text remain restrained.

Do not normalize game design into "navy + acid green". The transferable rule is one high-energy accent over a disciplined dark shell.

## Whole-home composition grammar

At desktop the homepage is roughly 1425x11401 inside a 1440x900 window.

Observed authored sequence:
1. global header / anchor navigation;
2. hero;
3. about / scale proof;
4. small transition strip;
5. video-led studio interlude;
6. expertise / service cards;
7. featured games + sticky selector;
8. featured character gallery;
9. testimonials;
10. FAQ;
11. team / experts;
12. contact / lead form;
13. final studio scale / call-now proof;
14. sponsor/trust strips;
15. footer.

The page functions as a single conversion spine:
identity -> studio credibility -> capability -> game proof -> visual world -> social proof -> objections -> people -> lead capture -> final reassurance.


## Hero

Observed:
- dark navy background;
- "INDIE" eyebrow;
- 96px condensed GAME STUDIO headline;
- short studio positioning copy;
- Our Expertise anchor CTA;
- large character/key-art image on the right;
- image-led rather than canvas-led art direction.

Transfer the composition mechanism: compact label + oversized identity line + short proposition + one primary anchor CTA + one authored focal image. Do not transfer the displayed "Nexira Games / ThemeForest" copy; it is residue from another identity/template lineage.

## About / scale proof

Observed:
- ABOUT US bracket label;
- "WE SERVE QUALITY GAMES & ASTRO THING";
- explanatory studio copy;
- 100K active gamers;
- 10+ live games;
- repeated logo/avatar strip;
- "100+ backers ready to support us" conversion bridge.

The useful mechanism is claim -> scale evidence -> ambient trust stream -> next action. The exact counts are template claims.

## Video interlude

The #video section creates a visual reset between company proof and services.

Desktop:
- raised #1b222e section;
- large 1371x528 media surface;
- object-fit: cover;
- muted + loop + playsInline;
- preload: none;
- autoplay: false;
- controls: false;
- poster present.

A second 420x360 video exists in the testimonial region with the same muted/loop/no-controls/no-autoplay posture. During the live audit both videos remained paused with currentTime=0 and readyState=0 after scrolling into view.

Transfer the poster-first media interlude and deferred loading idea. If playback matters, add an explicit accessible play control.

## Expertise / services

Four visible service cards:
- GAME DEVELOPMENT;
- DESIGN OF CHARACTER;
- GAMING ART DESIGN;
- 3D MODULE DESIGN.

Each card uses a bracketed index, concise capability title, one-line outcome statement, large media/art surface, and strong dark/accent contrast.

All four service cards currently link to ./ instead of a meaningful service detail or action. Transfer the anatomy, not the placeholder navigation contract.

## Featured games

The #game section uses:
- FEATURED GAMES bracket label;
- section headline;
- four game selectors: Neurox, Vireon, Frostin, Driftal;
- a sticky selector rail on desktop;
- large game art/detail media;
- descriptive game copy;
- a short differentiator list;
- Get A Quote CTA.

The selector owner is the only authored sticky content block detected after desktop settle. The four selectors are focusable DIV controls with tabindex=0 and pointer cursor but no explicit role or selected-state ARIA. They visually behave like tabs but do not expose tab semantics.

Transfer the sticky selector + stable proof panel pattern, but implement real button/tab semantics, explicit selected state, and predictable keyboard behavior.

## Featured characters

The character section is a pure visual-world reset:
- repeated image tiles;
- paired/duplicated character imagery;
- 20px radius on prominent gallery imagery;
- no new user job beyond visual proof/atmosphere.

Use only when original character/world art is itself evidence.

## Testimonials

The testimonial section combines USER FEEDBACK, multiple quote blocks, portrait/avatar imagery, person/company labels, and a secondary video surface. It places social proof before FAQ and team/contact.

The actual names, companies, quotes and outcomes are template content.

## FAQ

Five FAQ prompts are present. All current questions and answers are gym/fitness content: group classes, personal training, equipment, safety/hygiene and trial/day passes. This is unrelated to the game-studio promise and is high-confidence template residue.

Interaction structure:
- first item expanded at roughly 193px;
- remaining items collapsed at roughly 65px;
- accordion owners have tabindex=0 and pointer cursor;
- no role;
- no aria-expanded.

Transfer the objection-handling placement, but implement semantic buttons with aria-expanded, aria-controls and keyboard behavior.

## Team

The team block contains founder, CEO, designer and developer cards with large portraits, bracketed roles and condensed names. The useful sequence is capability proof -> people proof immediately before conversion.

Do not promote invented profiles into examples.

## Contact and lead capture

The #contact section contains direct email, phone, address, hours, Name/Email/Subject/Budget/Message fields, and GET A QUOTE.

Live form behavior:
- action: home URL;
- method: GET;
- Name/Email/Subject/Budget required;
- Message optional.

The footer newsletter also submits with GET to the current page. These are placeholder mechanics, not a production backend. A real implementation needs POST/server action or a form provider, validation, submission states, privacy context and spam controls.

## Final trust / call-now section

Observed:
- SINCE 1990;
- repeated studio-quality headline;
- 10+ year availability claim;
- Call Us Now CTA;
- Yearly New Users;
- 100 MILLION;
- repeated trust/avatar strips;
- TRUSTED BY 5000+ USERS.

The composition is a final reassurance bridge before the footer. The copy later drifts into fitness language, so only the layout logic is transferable.

## Footer

Footer contains essential anchors, contact, social links, newsletter, sponsor/logo area, FAQ/team/testimonial anchors and Reddevs attribution.

Identity/content residue remains visible:
- INFO@NEXIRA.COM;
- Nexira-style contact details;
- template vendor attribution;
- Framer badge.

A production site should run a release-time content-integrity pass across header, hero, footer, forms, social links, SEO metadata and utility routes.


## 404 route

/404 is part of the sitemap and returns HTTP 404.

Desktop 1440x900:
- document about 1425x1537;
- 19 images;
- 0 video;
- 0 canvas;
- 0 runtime animations;
- centered "LOOKS LIKE HERE IS NOTHING";
- Return Home action;
- full footer retained.

Mobile 390x844:
- document 390x2030;
- 7 images;
- 0 video/canvas/animation;
- no outer horizontal overflow.

The 404 route reuses the homepage title/meta description/OG identity and self-canonicalizes /404. Because it appears in sitemap.xml, search hygiene should be checked before shipping a derived implementation.

## Responsive behavior

Desktop home:
- viewport: 1440x900;
- document: about 1425x11401;
- 141 images;
- 2 video;
- 0 canvas;
- 4 runtime animations;
- 2 forms;
- desktop sticky featured-game selector;
- no positive outer overflow.

Mobile home:
- viewport: 390x844;
- document: 390x17793;
- 70 images in the live mobile variant;
- 2 video elements remain in DOM;
- 0 canvas;
- 0 runtime animations after settle;
- sticky game selector releases;
- navigation collapses into a fixed compact header;
- no document-level horizontal overflow.

Observed type step-down:
- H1 96 -> 48px;
- H2 48 -> 32px;
- H3 32 -> 24px.

The transferable rule is aggressive mechanical simplification while preserving narrative order and game identity.

## Accessibility / semantic findings

Positive:
- document lang=en;
- email input types are used;
- main page has one visible H1;
- mobile avoids outer horizontal overflow;
- missing routes return correct HTTP 404;
- FAQ/game controls are at least keyboard-focusable via tabindex.

Needs correction:
- game selectors are DIVs with tabindex=0 but no tab/button role or selected-state semantics;
- FAQ owners are DIVs with tabindex=0 but no button role or aria-expanded;
- video elements have controls=false and no explicit accessible player control was identified;
- image alt text is inconsistent/generic;
- duplicate/placeholder contact identity undermines trust;
- contact/newsletter forms use GET to the current route and expose no real submission contract.

## Content-integrity findings

High-confidence residue:
- hero says "Nexira Games" on an Indiex page;
- hero references ThemeForest, Inc.;
- about copy again says Nexira;
- "OUR EXPERTISE0" typo;
- FAQ is entirely gym/fitness copy;
- final trust copy references fitness;
- contact uses info@onepage.com while footer uses info@nexira.com;
- service cards link back to ./;
- footer/social identity is generic/template data.

This makes Indiex especially useful as a **Template Residue Firewall** reference: a visually coherent page can still be production-invalid when semantic/business identity drifts across sections.

## Transferable principles

### 1. One-Page Studio Conversion Spine

For a compact offering, one route can sequence:
identity -> credibility -> capabilities -> work/game proof -> world art -> testimonials -> objections -> team -> lead form -> final reassurance.

Use when the service set is focused and dedicated route families would otherwise be thin. Do not use when service/case SEO or deep project proof deserves separate routes.

### 2. Sticky Game Selector as Compact Portfolio Navigation

Use a sticky selector only while it helps compare a small set of games/projects against one stable proof region.

Contract:
- real button/tab semantics;
- announced selected state;
- explicit keyboard behavior;
- each selector changes meaningful proof;
- release sticky ownership on narrow screens.

### 3. Poster-First Media Interlude

Let a poster/still carry the initial composition and defer video bytes.

If playback matters:
- provide a visible play control;
- support pause/mute;
- retain complete meaning in poster/copy;
- respect reduced motion/data constraints.

### 4. Proof -> Objection -> People -> Contact

The latter half is structurally useful despite bad content:
testimonials -> FAQ -> team -> contact.

It answers:
- does it work?
- what about my objections?
- who will do the work?
- how do I start?

Transfer the decision logic, not placeholder testimonials or identities.

### 5. Template Residue Firewall

Before treating a template as implementation-ready, verify one consistent identity across:
- logo/site name;
- hero/company copy;
- metrics;
- project/game names;
- FAQ;
- team;
- contact details;
- forms;
- footer;
- meta/OG;
- 404;
- legal/social links.

A coherent visual system is not evidence of coherent content binding.

## Do not transfer

Do not transfer:
- Indiex/Nexira/ThemeForest identity or copy;
- exact game art/character imagery;
- fake player/backer/user counts;
- fake testimonials/team/contact data;
- gym/fitness FAQ and fitness copy;
- Reddevs/Framer vendor residue;
- exact #94cb53 / #0b121d palette pairing as a gaming preset;
- Oswald/Inter as a required pairing;
- placeholder GET forms;
- service links returning to ./;
- DIV-based pseudo-tabs/accordion semantics.

## Distilled role in the toolkit

Indiex strengthens the existing game-studio family rather than creating another skin.

Primary contributions:
- compact one-page game-studio conversion architecture;
- sticky project/game selector released on mobile;
- poster-first media interlude;
- proof -> FAQ -> team -> contact late-funnel sequence;
- Template Residue Firewall;
- accessibility warning for focusable DIV controls without roles/states;
- production warning for placeholder forms and dead service links.
