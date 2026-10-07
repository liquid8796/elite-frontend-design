# Refokus Webflow Tools — companion full-site design intelligence

Source: https://www.webflow-tools.refokus.com/
Parent brand: https://www.refokus.com/
Audit date: 2026-10-08
Coverage: 19/19 sitemap URLs + 404

Refokus advertises this companion sitemap from the main Refokus `robots.txt`, so it is a first-class product surface rather than an unrelated microsite.

## Topology

- `/` — tool library home;
- `/styleguide` — public implementation styleguide;
- 17 `/tools/*` documentation routes.

All 19 sitemap URLs returned HTTP 200. Unknown paths return HTTP 404.

Tools: API Filler, Automatic Tabs, Bionic Reading, CMS Filters, CMS Load More, CMS Prev/Next, CMS Tabs, Copy to Clipboard, Form Validator, Image Magnifier, Masonry Layout, Page Transitions, Preview Links, Rich Text Enhancer, Slider Generator, Social Share and Time to Read.

## Visual system

- dark shell `#1C1C1C`;
- raised `#2C2C2C` / `#2F2F2F`;
- white primary text;
- purple accents around `#7443FF` / `#9E7BFF`;
- sparse mint highlight;
- Manrope product/display/body;
- Consolas / IBM Plex Mono for technical/code roles.

This is materially different from the parent Featuredeck + General Sans editorial system.

## Library home

Desktop:
- ~1425x5488;
- 98 images, 3 videos, 3 forms;
- fixed navigation and transition layer;
- sticky tool/filter band;
- no positive document overflow;
- visual H1 fragments “Up / Your / Game” at 180px.

Mobile:
- ~390x4703;
- H1 fragments 64px;
- zero outer overflow.

Primary job: discover a utility, understand library/version behavior and route into exact documentation.

## Tool documentation family

All 17 tool pages repeat:

`tool promise -> copy script -> place script -> configure custom attributes -> publish to staging -> verify -> demo/clonable -> project CTA`

Representative `/tools/cms-filters`:
- ~1425x4791 desktop / ~390x5143 mobile;
- Manrope H1 80px -> 36px;
- sticky utility/context band;
- mono roles stay local to technical content.

The reusable mechanism is **Copy -> Configure -> Verify Documentation**. A developer document should end with a concrete validation step.

## Public styleguide

`/styleguide` is ~1425x7802 and exposes:
- class conventions;
- component / child / modifier rules;
- naming practices;
- layout hierarchy;
- sections and containers;
- sticky implementation examples.

This is **Public Implementation Styleguide as Product Trust** when users are builders.

## Responsive

- library display 180px -> 64px;
- docs H1 80px -> 36px;
- sticky context bands remain compact;
- code/configuration stays readable;
- document width remains 390px on tested mobile.

## QA findings

- all 19 sitemap pages lack canonical links;
- rendered `html lang` is empty;
- home splits one visual phrase across four H1 elements.

These are route-quality defects, not reusable patterns.

## Transfer

Transfer dark utility hierarchy, restrained technical mono, discover/install/configure/verify logic, sticky context bands, testable demos and public implementation documentation.

Do not transfer Refokus identity, exact tool code/names, exact purple palette, graphics or multi-H1 semantics.
