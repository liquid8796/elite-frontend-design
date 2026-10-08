# Fizens — Whole-Site Toolkit Spec

Source: https://fizens.framer.ai/
Deep profile: ../../../design-intelligence/sites/fizens.framer.ai.md
Archetype: light-finance-saas
Skin: clean-product-light (existing baseline).

## Full topology

Sitemap 43/43 HTTP 200: home 1; core 9; legal 2; integration details 9; team details 8; job details 4; articles 10. Four separately tested invalid/non-declared routes including /404 and /jobs returned HTTP 404. Route evidence: data/fizens-route-inventory-2026-10-08.csv. 17 desktop and 15 phone rendered route states, zero positive outer overflow.

## Art and Layout

White #FFFFFF; dark #171717; muted #4B5563; Fizens blue #0040C1; visible Poppins large headings, 64px desktop ->36px at 390px. Product dashboards/cards/screenshots, calm fintech proof, 0 canvas/video on homepage; About includes 4 videos. Avoid invented 3D/motion patterns.

## Route Jobs

Home: financial control thesis -> feature proof -> goals/security -> testimonials -> three plans -> educational articles -> FAQ -> CTA.
Features: individual product capabilities and screenshot-led benefit cards.
About: origin/company trust/team media narrative.
Pricing: $0/$20/$40 template tiers -> compare features -> lead action (checkout not verified).
Contact: required first/last name, email, phone, message + global newsletter.
Integrations: nine-partner directory -> individual compatibility/benefit detail, NOT verified OAuth/live data connectivity.
Download: Finora/Credexa/Investa catalog -> app store path, product-specific store URL verification needed.
Articles: ten long-form investment/insurance/aid posts, archive -> detail -> reading continuation.
Team: eight individual staff profiles.
Jobs: four details but no index /jobs; all four job pages wrongly show Product Designer H1.
Changelog: public release updates.
Legal: terms and privacy.
Overview: vendor template package index; NOT an end-user product dashboard.
404: real status 404.

## Searchable Patterns

fizens-finance-benefit-proof; fizens-integration-hub-detail; fizens-download-app-portfolio; fizens-pricing-matrix-route; fizens-people-career-proof; fizens-financial-editorial; fizens-template-sales-boundary.

## QA

21/43 generic document titles despite self canonical. 4/4 job detail visible H1 mismatched with distinct CMS page titles. Homepage/pricing use multiple H1 nodes. Demo download links point to generic Apple/Play Games pages. Template publisher promos, financial performance/security, live integration/OAuth and employer identity claims unverified. Forms are visible; successful processing untested.

## Responsive

Phone 390 CSS px zero outer overflow across all sampled page types. General hero text 64 ->36px, editorial section H2 36 ->24px. Complex cards, multi-tier plans, partner grids and long articles vertically stack; preserve actual task content without copying imagery.

Auditable rendered-state data: data/fizens-rendered-states-2026-10-08.csv; four role H1 comparisons: data/fizens-career-title-audit-2026-10-08.csv.
