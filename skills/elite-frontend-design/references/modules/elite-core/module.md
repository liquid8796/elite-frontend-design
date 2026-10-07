---
name: elite-core
description: Core art-direction and implementation discipline for elite frontend work. Defines product grounding, variance/motion/density dials, the design contract, anti-slop checks, page-type rules and completion quality.
---

# Elite Core

Use this module for substantial frontend creation or redesign. It is the bridge between visual ambition and product usefulness.

## 1. Start With the Job, Not the Style

Write down:

- what the user is trying to accomplish;
- what must be visible or actionable;
- what the page should make them notice first;
- what information must remain scannable;
- what device constraints matter;
- what brand/system constraints already exist.

A dashboard is a working surface, not a landing page. A product page helps a buyer decide. A marketing page earns attention and communicates a proposition. Let the page type shape the composition.

## 2. Design Dials

Set:

- VARIANCE 0–3: how far layout/art direction can depart from familiar patterns.
- MOTION 0–3: static → interaction-only → orchestrated → cinematic.
- DENSITY 0–3: sparse → balanced → rich → operational.

Do not maximize all three. High variance plus high motion plus high density usually produces noise.

## 3. Design Contract

A useful contract fits on roughly one screen.

### Visual thesis
One sentence describing the character and why it fits the subject.

### Signature
Pick one memorable element:
- hero composition;
- unusual but usable grid;
- type treatment;
- product visualization;
- material/texture system;
- interactive transition;
- data visualization.

Everything else supports it.

### Tokens
Define a compact semantic set:
- background;
- surface;
- elevated surface;
- primary text;
- secondary text;
- border;
- accent;
- success/warning/error/info;
- spacing rhythm;
- radius family;
- shadow family.

### Type
Specify:
- display/UI/body roles;
- width/weight character;
- max line length;
- heading wrap target;
- numeric/mono usage only when meaningful.

### Layout
Specify:
- max width/container model;
- major columns;
- content alignment;
- rhythm between sections;
- desktop-to-mobile transformation.

### Anti-goals
Name the defaults most likely to ruin this specific design.

## 4. Page-Type Guidance

### Landing / marketing
- First viewport needs one unmistakable product/brand signal.
- One primary CTA.
- Treat a fixed/sticky header as part of the first-viewport budget. Header + hero must fit the intended initial view without hiding the primary message or action.
- Let the opening view suggest that more content follows when the page is meant to scroll; avoid turning every hero into a sealed poster.
- Avoid filling the hero with badges, fake metrics and miniature dashboard cards.
- Give each section one job, one dominant visual idea, and one primary takeaway or action.
- Vary section rhythm rather than repeating one layout formula.
- Use proof/content that is specific enough to be believable.

### Dashboard / operations
- Start with the working surface.
- Prioritize scanning, filtering, exceptions and detail inspection.
- Keep controls close to the data they affect.
- Use status color semantically, not decoratively.
- Dense does not mean cramped: maintain clear grouping and alignment.
- For numeric-heavy UI, use tabular figures or an appropriate numeric/mono treatment when it improves column scanning.
- Mobile needs a deliberate priority strategy, not a shrunken desktop grid.

### Product detail / commerce
- Make the object/configuration understandable.
- Show variants, materials/specs, included items and decision support.
- Maintain a visible purchase/configuration path.
- Do not substitute testimonials for product information.

### Multi-page product suite
- Share tokens/navigation/component language.
- Give each route a distinct job and structure.
- Reuse patterns where behavior repeats; do not copy-paste complete page compositions.

## 5. Existing-Codebase Discipline

When working inside a real codebase:

1. **Scan** the actual target route, framework, styling system, tokens, components, assets and runtime conventions.
2. **Read the actual render branch** for the viewport/state being changed. Responsive conditions, feature flags and route variants can make an imported component irrelevant to the rendered surface.
3. **Trace only UI-touching dependencies** needed to understand that target. Prefer compact theme/token summaries and relevant line ranges over dumping giant global files into context.
4. **Diagnose before redesigning**: list the weak hierarchy, generic patterns, missing states, responsive failures or fidelity drift that materially affect the user.
5. **Fix in place** when the architecture is sound. Preserve useful components, routing, state and business behavior instead of rewriting the app to obtain a new aesthetic.
6. If a third-party library seems useful, verify it exists in the project before importing it. Do not hallucinate dependencies or introduce a package for a minor effect.

Context quality matters more than context volume. If a faithful target cannot be understood within the available context, narrow large files to their relevant render/token sections instead of dropping the real page and inventing a generic substitute.

## 6. Controlled Iteration

Prefer variants over rerolls.

Once a direction has good bones:
- lock the layout/hierarchy that works;
- change only 1–2 variables per iteration;
- record what must be preserved and what is changing;
- avoid replacing palette, typography, layout, media treatment and motion all at once unless the concept is being intentionally discarded.

Keep a project-local, gitignored reference pack when ongoing design work benefits from persistent visual calibration. Do not rely on model memory as the source of taste.

For assets:
- use supplied or properly sourced assets where possible;
- do not invent customer logos, partnerships, testimonials, employee identities or product proof;
- never present generated people as real customers/staff/endorsers;
- every decorative image should have a role in hierarchy, narrative, demonstration or atmosphere.

## 7. Anti-Slop Review

Ask:

- Could this page belong to ten unrelated SaaS products?
- Are cards being used because the content truly forms independent units?
- Is the palette chosen from the subject or from model habit?
- Are labels and badges conveying information or merely decorating empty space?
- Is typography doing useful hierarchy work?
- Is the same shape/radius/shadow repeated at every level?
- Is copy specific to the actual domain?
- Does the first viewport immediately reveal what this thing is?
- Is the memorable idea strong enough to justify itself?
- Could one decorative element be removed without losing meaning? If yes, remove it.

## 8. Implementation Discipline

- Build components around repeated behavior/content, not arbitrary visual fragments.
- Prefer explicit variants to duplicated one-off markup.
- Keep layout rules close to their owning component or established styling layer.
- Use tokens for repeated visual values.
- Do not overwrite existing design tokens with a parallel system unless requested.
- Preserve semantic landmarks and heading order.
- Keep interactions keyboard-usable.
- Avoid absolute positioning for primary layout unless the visual genuinely requires it.
- Prevent layout shift by reserving media space.
- Use real icons/assets when available instead of placeholder glyphs.
- Do not fabricate backend behavior; if data is mocked, keep the UI structurally honest.

## 9. Responsive Contract

For each major region decide one of:

- stays;
- stacks;
- collapses;
- becomes horizontally scrollable;
- becomes a drawer/sheet;
- becomes a condensed summary;
- moves lower in priority;
- hides because it is truly nonessential.

Do not rely on "everything becomes one column" for dense tools.

## 10. Completion

This module is not complete until visual-qa has been run when browser tools are available.
