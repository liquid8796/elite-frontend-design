# Refokus — whole-site re-audited design intelligence

Source: https://www.refokus.com/
Companion surface: https://www.webflow-tools.refokus.com/
Re-audit date: 2026-10-08
Coverage: 121/121 declared sitemap URLs across two Refokus-advertised sitemaps + both-host 404 recovery

This supersedes the 2026-10-05 homepage-only read. The earlier hero/runtime findings were re-verified, but Refokus is now modeled as a route-complete agency/content/product ecosystem rather than one signature landing page.

## Coverage topology

`robots.txt` advertises:
- `https://www.refokus.com/sitemap.xml` — 102 public URLs;
- `https://www.webflow-tools.refokus.com/sitemap.xml` — 19 public URLs.

All 121 declared URLs returned HTTP 200. Missing paths on both hosts return HTTP 404.

Main-site families:
- home 1; About 1;
- Branding, Websites, Brand Marketing service landings;
- Startups, Enterprise Websites, Venture Capital Websites, Webflow Agency audience/authority landings;
- Work 1 + 46 project details;
- News 1 + 34 article details + 3 category archives;
- Careers 1 + 5 career details;
- resource 1; Contact 1.

Companion Tools:
- home 1;
- public styleguide 1;
- tool documentation details 17.

## What the earlier distillation missed

The original profile correctly captured the immersive hero, editorial shell, typography contrast and bounded WebGL principle. It under-modeled the route system.

Newly confirmed:
- reusable service narrative grammar;
- audience-specific persuasion and proof binding;
- deep Webflow authority route;
- media-dense Work directory connected to 46 cases;
- case depth that varies with available evidence;
- News/categories/long-form articles with desktop sticky outlines;
- careers index/details and sticky desktop application UI;
- resource lead-magnet route;
- distinct Webflow Tools product/docs/styleguide surface;
- route-level canonical, language and heading defects invisible from homepage-only review.

## Main-site visual system

- body `#FFFFFF`; ink `#0F1215`;
- General Sans Variable owns navigation, body, utility and long-form;
- Featuredeck owns editorial identity;
- dark proof/media bands use near-black + white;
- accent remains sparse and project-dependent.

Desktop type evidence:
- homepage signature Featuredeck 88px;
- homepage semantic H1 20.8px;
- service H1 88px;
- audience/news/careers H1 up to 128px;
- project title 128px; article H1 72px.

Mobile:
- signature 35.2px; homepage H1 17.6px;
- project/careers ~48px;
- service ~35.2px; article 24px.

Transfer the role contrast, not the exact fonts.

## Signature hero runtime — re-verified

Current evidence:
- one `c-hero-canvas` with a real WebGL2 context;
- dynamic `https://js.refokus.com/main.js`;
- GSAP, ScrollTrigger, SplitText, CustomEase and Three internals;
- WebGLRenderer, GLTFLoader, PerspectiveCamera, EffectComposer, ShaderPass, FilmPass, FXAAShader;
- runtime request for `https://js.refokus.com/model.glb` plus environment/diffuse/normal textures;
- renderer pixel ratio 1.5;
- scroll and pointer interpolation state.

This validates **Bounded Immersive Rendering**: premium rendering belongs to one identity stage, not every route.

## Homepage

Desktop 1440x900 -> ~1440x6965; 82 images, 8 videos, 1 WebGL canvas, 1 form; fixed 64px nav; tall sticky hero; zero positive overflow.

Mobile 390x844 -> ~390x5926; zero outer overflow; desktop sticky hero ownership releases.

Sequence:
1. identity stage;
2. founder testimonials;
3. agency thesis;
4. named case proof;
5. recognition;
6. footer/contact.

Useful rule: **identity -> credibility -> thesis -> named proof**.

## Service Narrative Landing System

Branding, Websites and Brand Marketing share:
1. sticky editorial thesis hero;
2. problem/context;
3. strategic questions/process;
4. capabilities;
5. differentiation;
6. testimonials/proof;
7. relevant case;
8. FAQ;
9. contact continuation.

Geometry:
- Branding ~1440x10611 / ~390x11766;
- Websites ~1440x11949;
- Brand Marketing ~1440x5889.

Branding releases its desktop sticky hero on mobile while preserving content.

## Audience-Specific Proof Binding

Startups, Enterprise and Venture Capital are real audience routes, not thin SEO pages:
1. audience promise;
2. audience-framed proof;
3. category/problem thesis;
4. why the agency model fits;
5. relevant case;
6. ways to work;
7. audience FAQ.

Startups and Enterprise use 128px Featuredeck H1s. VC currently exposes two H1 elements.

Transfer stable brand voice + context-bound evidence, not keyword substitution.

## Webflow authority route

`/webflow-agency` is ~1440x18301 with 136 images, 9 videos and 17 sections. It combines platform expertise, proof of pushing Webflow, community/event evidence, Refokus Tools promotion, client examples, FAQ and conversion.

Authority pages may be deeper than service pages when there is real ecosystem proof.

## Work — Media-Dense Proof Directory

`/work` desktop: ~1440x10862; 141 images; 37 videos; 3 forms; zero positive overflow.
Mobile: ~390x12839; zero outer overflow.

It combines filters, named projects, service/category metadata, previews and testimonials.

Transfer:
- filters serve a selection job;
- project identity/action remains readable without playback;
- defer/pause preview media;
- mobile cannot depend on hover;
- enforce a media budget.

## Project details — Evidence-Dependent Case Depth

The 46 project URLs do not force identical length.

`/projects/jungle`:
- ~1440x7209; 41 images, 2 videos, 9 sections;
- hero facts -> video -> sticky zoom stage -> mobile-marquee substitute -> highlights -> testimonial/outcome -> related cases;
- mobile releases desktop sticky zoom ownership.

`/projects/spotify`:
- ~1440x2760; 21 images, 2 videos;
- much shorter: hero/context + related cases.

Let available proof determine route depth; do not pad weak cases.

## News and articles

`/news`: ~1440x11837, sticky desktop category filter, 34 article destinations.

Representative article:
- ~1440x11902 desktop / ~390x16021 mobile;
- Featuredeck H1 72px -> 24px;
- desktop sticky article outline ~272px;
- mobile releases the outline;
- related articles continue the journey.

Transfer **Long-Form Outline -> Flow**.

## Careers, resource and contact

Careers index: ~1440x5275 / ~390x5553; culture -> principles -> roles -> benefits.
Career detail: ~1440x3873; role -> expectations -> benefits; desktop can use sticky application UI.

Resource `/resources/visual-brand-archetypes`: value -> what you get -> why -> how -> community -> download, with sticky desktop form.

Contact `/contact`: compact ~1440x1942, project form + proof + practical FAQ. Conversion routes should not replay the portfolio.

## Companion — Refokus Webflow Tools

Main Refokus robots advertises this sitemap, so it is part of the discoverable ecosystem.

19 URLs:
- home;
- styleguide;
- 17 tool docs: API Filler, Automatic Tabs, Bionic Reading, CMS Filters, CMS Load More, CMS Prev/Next, CMS Tabs, Copy to Clipboard, Form Validator, Image Magnifier, Masonry Layout, Page Transitions, Preview Links, Rich Text Enhancer, Slider Generator, Social Share, Time to Read.

Distinct system:
- background `#1C1C1C`; raised `#2C2C2C` / `#2F2F2F`;
- white foreground;
- purple accents around `#7443FF` / `#9E7BFF`; sparse mint;
- Manrope product/display/body;
- Consolas / IBM Plex Mono technical roles;
- no Three/GSAP signature runtime required.

Toolkit models it separately as `refokus-tools`.

### Tools home

Desktop ~1425x5488; 98 images, 3 videos, 3 forms; fixed nav + transition layer + sticky filter band. Visual H1 fragments “Up / Your / Game” at 180px.

Mobile ~390x4703; fragments 64px; zero outer overflow.

### Tool detail family

All 17 tools repeat:

`tool promise -> copy script -> place script -> configure attributes -> publish staging -> verify -> demo/clonable -> project CTA`

CMS Filters: ~1425x4791 desktop / ~390x5143 mobile; H1 80px -> 36px; sticky context band.

This is **Copy -> Configure -> Verify Documentation**.

### Public styleguide

`/styleguide` is ~1425x7802 and exposes class conventions, component/child/modifier rules, naming practices, layout hierarchy, sections/containers and sticky examples.

This is **Public Implementation Styleguide as Product Trust**.

## Responsive system

Main:
- all tested 390px routes held zero outer overflow;
- sticky hero/article/case ownership commonly releases;
- Featuredeck scales aggressively while General Sans stays readable;
- fixed nav persists; overlay menu expands to viewport;
- media proof remains available without hover.

Tools:
- 180px home display -> 64px;
- 80px docs heading -> ~36px;
- sticky context bands stay compact;
- zero document-level overflow at 390px.

## Performance and media policy

Muted looping previews commonly use `preload=none` or metadata; sampled offscreen previews were usually paused.

Extremes:
- home 82 images / 8 videos / 1 canvas;
- Webflow authority 136 images / 9 videos;
- Work 141 images / 37 videos.

Transfer conditional media density: defer bytes, pause offscreen, preserve labels/actions without playback, bound WebGL, measure mobile cost.

## SEO / semantic QA deltas

Whole-site audit exposed:
- `/startups` canonical -> `/startup`;
- `/work` lacks canonical;
- all 3 blog-category pages lack canonical;
- all 19 Tools sitemap pages lack canonical;
- Tools rendered pages have empty `html lang`;
- Tools home visually splits one hero across four H1 elements;
- VC landing exposes two H1 elements;
- both hosts return HTTP 404 for missing paths.

Promote **Canonical/Language Route Invariant**.

## Transferable principles

1. Signature Stage, Calm System.
2. Service Narrative Landing System.
3. Audience-Specific Proof Binding.
4. Evidence-Dependent Case Depth.
5. Media-Dense Proof Directory.
6. Long-Form Outline -> Flow.
7. Copy -> Configure -> Verify Documentation.
8. Public Styleguide as Trust.
9. One Brand, Multiple Product Surfaces.
10. Route-Level SEO Integrity.

## Do not transfer

Do not copy Refokus/client identities, proprietary case media, awards/testimonials, exact fonts/palettes, model.glb/textures/shaders/runtime code, DPR 1.5 as a universal target, the exact “Up Your Game” composition, tool code/content, or route-level SEO defects.

## Distilled role after re-audit

- `refokus`: full agency ecosystem — signature stage, service/audience landings, work/cases, knowledge, careers, resource and contact.
- `refokus-tools`: companion developer-tool discovery/docs/styleguide surface.

Refokus is not “a homepage with a great WebGL hero.” It is a route-complete agency/content/product ecosystem where the signature stage is one layer of a broader reusable system.
