# CreateStudio / Create® — Entire Website Toolkit Spec

Source: https://createstudio.framer.media/
Deep profile: ../../../design-intelligence/sites/createstudio.framer.media.md
Archetype: swiss-creative-agency-media
Existing skin: **creative-agency-editorial**, with distinct near-white Figtree system; avoid duplicate skin.

## Route Coverage and Ground Truth

Full sitemap **21/21 HTTP 200 confirmed by Chromium**: home, /work index + **five details**, /studio, /contact, /whispers index + **seven essays**, **four legal URLs** including two separate Terms-of-Service URLs. /legal/terms-of-service and /legal/Terms%20of%20Service have self-referential distinct canonical and different sampled body openings; treat as competing content, not one canonical legal policy. One initial requests TLS EOF for /work/numeriq-fashion was reconciled with two Chromium 200 renders.

Ten extra missing/demo URLs HTTP 404; /404 is linked and serves a 404. Audit artifacts in data/createstudio-*-2026-10-16.csv: 31 route rows (21 official + 10 extra), internal href graph, **44 Chromium states at 1440x900/390x844, 0 outer overflow**, **12 bounded interactive probes**. Complete route coverage, not proof of commercial transaction.

## Design Tokens and Media

Near-white **#F2F2F2** body with near-black editorial type and **Figtree** display, occasional orange/red accent and project-specific media. Degrees/serial fragments // 00.01° accent the Swiss layout; big graphic type, documentary/showreel imagery and utility captions. Home DOM **99 images + 6 videos desktop; 252 images + 7 videos phone; zero canvas**. Responsive DOM/media copies must not be interpreted as 252 downloaded pictures. Desktop home H1 ~121px; /work and /studio H1 ~160px (also on sampled 390px, so test visible content/crops before transferring any literal mobile size). Home is ~29,328px desktop and ~31,347px phone. Preserve contrast, load/perf budget and reduced motion fallback.

## Full Route Recipes

- Home: small numbered Swiss-like masthead -> manifesto/client logo/showreel -> selected case stories -> numbered case metrics and logos -> 6 services (Brand Identity/Strategy/Design & Innovation/Development/Marketing & Growth/Content & Production) -> process and team -> interactive three plan preview -> **home #pricing Core/Studio/Scale** with project price/terms -> availability/booking invitation -> FAQ/Whispers/newsletter/footer.
- Work index: **three initially linked cases vs five sitemap details**, Project Name field, category select; search input did not alter sampled href subset and category modified membership but not count. Distinguish curated from total portfolio and implement actual result state, no-match/reset.
- Work detail: five client-specific campaign pages (Aurelis, Blackwell, Aspen877, Monolith, Numeriq), title/year/industry/tech -> Brief -> Challenge -> Solution -> Results -> Credits -> next work/CTA. Source text and results are template fixtures. Source sometimes uses H2 for case title; implement H1.
- Studio: founder/team/process/agency method, metrics, founder quote, case link and booking. Demo addresses and hello@create.com / hello@createme.com inconsistent; verify before shipping.
- Whispers index: seven real linked essays + Search articles input; query "Architecture" did not reduce sampled href set. No asserted functional search.
- Whispers detail: theme/author/date -> long design story and images -> related essays -> contact/newsletter. Seven distinct CMS slugs.
- Contact: Name, Company, Email, Your message as required sample fields + Terms notice and Submit; separate newsletter email. Browser validity sampled but nothing submitted. Add genuine H1 and receipt/error state.
- Legal: Privacy, Disclaimer, two competing Terms routes. Choose one authoritative URL and redirect/canonicalize only after legal owner review. Keep actual 404 fallback and remove demo 404 menu link.
- Vendor layer: Tamas Bodo's Framer $129 template and Framerpod gallery are outside a genuine digital-agency engagement.

## Distilled Pattern System

createstudio-swiss-story-stage; createstudio-numeric-sections; createstudio-portfolio-parity; createstudio-work-search-contract; createstudio-whispers-archive; createstudio-case-evidence; createstudio-three-plan-pricing; createstudio-presence-accuracy; createstudio-legal-canonical; createstudio-vendor-firewall.

Interaction limitations: sampled work/Whispers search did not prove correct filtering, pricing links do not prove charge or booking, no real form delivery, no FPS check, zero canvas says nothing about CSS/video animation. Claim provenance, domain/legal consistency, heading/accessible form structure and phone media burden are production QA gates.
