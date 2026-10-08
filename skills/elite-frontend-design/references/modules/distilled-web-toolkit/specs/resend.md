# Resend ? Toolkit Spec

Source: https://resend.com/
Deep profile: `../../../design-intelligence/sites/resend.com.md`
Archetype: developer-product
Primary skin anchor: `developer-infra`

## Live Snapshot ? 2026-10-07
- Sitemap index: 11 child sitemaps containing 1,015 distinct URL entries (2026-10-08 full-site re-audit); the former 11-URL count was incorrect.
- Desktop: ~1430x12319; mobile: ~390x14146; no positive outer overflow.
- Runtime: canvas appears desktop, 5 video elements, 73 images.
- Type roles: Domaine editorial display, Inter/ABC Favorit technical/product roles.
- Desktop hero ~96px; mobile hero ~64px centered.

## Composition Grammar
- Editorial headline + immediate technical/product proof.
- Product capabilities are modular, each paired with code/UI/event/output evidence.

## Proof Grammar
- Code is product proof, not decoration.
- Evidence precedes or tightly accompanies broad feature claims.

## Motion / Media
- Keep dense technical surfaces stable; animate state change only when it explains behavior.

## Responsive Contract
- Replace wide technical proof with narrower truthful representation rather than shrinking to illegibility.

## Toolkit Patterns
`resend-product-evidence`, `resend-code-proof`, `resend-dev-hero`, `resend-responsive-fidelity`, `resend-dark-precision`, `resend-modular-proof`, `resend-editorial-dev-type`.

## Do Not Transfer
Exact API syntax unless implementing Resend, proprietary product screenshots, brand fonts, or dark shell as a universal devtool default.

## Whole-Site Routing Contract — 2026-10-08

Full profile: ../../../design-intelligence/sites/resend.com.md

Full declared-route inventory: data/resend-route-inventory-2026-10-08.csv
Coverage: 1,015/1,015 requested; 1,014 returned 200; /shop returned 404.

Family counts: docs 413, blog 176, changelog 111, other/core 124, handbook 65, humans 59, customers 46, legal 7, clubs 6, migrate 5, security 3.

### Family grammar
- Marketing home: editorial identity -> trusted names -> code/product tour -> operational proof -> final CTA.
- Product/features: capability job -> inspectable UI/code demonstration -> supporting system proof -> trust -> CTA.
- Stack integration: stack promise -> authentic SDK/code fit -> short setup -> platform continuity -> CTA.
- Enterprise: scale promise -> customer-scale evidence -> compliance -> implementation -> contact.
- Pricing: plans -> usage pricing -> add-ons -> category/feature comparison.
- Migration: competitor promise -> code converter -> concepts/SDK/API/webhooks/security mappings -> CTA.
- Docs API: fixed left navigation + internal main scroll + right outline; method/params/request-response examples.
- Docs dashboard: task story -> UI steps + API branch -> troubleshooting/next step.
- Docs knowledge base: failure/context -> diagnosis -> corrective action.
- Docs provider guide: vendor-specific context -> step-by-step illustrated fix -> verification.
- Blog: featured/archive -> long-form article with technical proof -> related content.
- Changelog: chronological sticky dates -> release cards -> deep details and product links.
- Customers: named proof directory -> evidence-scaled short/long stories.
- Handbook: expressive index -> department pages -> principle/process content + side rail.
- Humans/clubs: people directory -> authored contributions; curated culture collections.
- Event: independent branded microsite runtime, separated from product/docs shell.

### Promoted patterns
resend-route-complete-system, resend-capability-inspectable-state, resend-integration-adapter, resend-migration-converter, resend-three-rail-docs, resend-sticky-release-chronology, resend-public-operating-system, resend-human-attribution, resend-evidence-scaled-cases, resend-content-lifecycle-lattice.

### Responsive / performance
Zero outer overflow in tested 390px representative routes. Marketing is normal document scroll; docs uses a ~714px contained scroll-main (root document stays ~390x844). Preserve focus, anchoring and reading order across nested scroll. Changelog index measured ~68,260px and 273 images desktop: avoid unlimited heavy content as a generic default.

### QA
Stale sitemap URL /shop returns HTTP 404; 20 HTTP-200 'other' routes lacked HTML H1; selected product/docs/handbook/migration routes have multiple H1 elements. Define route-level status/semantic invariants. Prior homepage-only pattern claims remain valid but are not whole-site specifications.
