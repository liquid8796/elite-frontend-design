# Refokus — Toolkit Spec

Source: https://www.refokus.com/
Companion: https://www.webflow-tools.refokus.com/
Deep profile: `../../../design-intelligence/sites/refokus.com.md`
Archetype: creative-agency
Primary skin anchor: `creative-agency-editorial`

## Re-Audit Snapshot — 2026-10-08
- Two advertised sitemaps: 102 main URLs + 19 Tools URLs = 121 public URLs.
- Main: 46 projects, 34 articles, 5 careers, 3 categories plus service/audience/authority/work/resource/contact routes.
- Home ~1440x6965 desktop / ~390x5926 mobile; zero outer mobile overflow.
- 82 images, 8 videos, 1 WebGL2 canvas.
- Three/GLTF + model.glb + EffectComposer + GSAP/ScrollTrigger/SplitText/CustomEase re-verified.
- Featuredeck + General Sans Variable.
- Companion Tools is modeled separately as `refokus-tools`.

## Whole-Site Grammar
Home: identity -> founder proof -> thesis -> named case -> recognition.
Service: sticky thesis -> context -> process/capability -> proof -> case -> FAQ.
Audience: audience promise -> social proof -> thesis -> fit -> relevant case -> ways to work -> FAQ.
Work: filters -> media-dense project directory -> testimonials.
Project: facts -> authored evidence -> outcome -> related cases, with depth proportional to evidence.
News: featured thinking -> archive; article -> long-form + optional desktop outline -> related content.
Careers: culture -> roles -> benefits; detail -> expectations + application.
Resource: value -> contents -> sticky conversion.
Contact: compact conversion + proof + FAQ.

## Runtime
Keep one bounded immersive stage. WebGL is identity infrastructure, not a site-wide requirement.

## Patterns
Existing: `refokus-signature-stage`, `refokus-bounded-immersive`, `refokus-motion-focus`, `refokus-responsive-brand-payload`, `refokus-proof-before-fireworks`, `refokus-editorial-case`, `refokus-type-contrast`.

Added: `refokus-service-narrative`, `refokus-audience-proof-binding`, `refokus-evidence-dependent-case-depth`, `refokus-media-proof-directory`, `refokus-longform-outline-flow`.

## QA
Release blockers:
- `/startups` canonical -> `/startup`;
- `/work` and 3 category routes lack canonical;
- companion Tools routes lack canonical and document language;
- VC and Tools home contain multi-H1 patterns.

## Do Not Transfer
Identity, client proof, proprietary media, awards, exact fonts/palette, WebGL assets/code or route-level SEO defects.
