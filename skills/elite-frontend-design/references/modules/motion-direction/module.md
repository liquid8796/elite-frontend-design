---
name: motion-direction
description: Controlled frontend motion direction ranging from interaction feedback to cinematic GSAP-style storytelling. Use only when motion materially improves hierarchy, spatial understanding or brand expression.
---

# Motion Direction

Motion is a design system, not a bag of effects.

## Choose a Motion Level

### Level 0 — Static
Use for:
- dense admin tools;
- accessibility-sensitive tasks;
- performance-constrained screens;
- simple maintenance changes.

No decorative animation. Preserve necessary state transitions.

### Level 1 — Interaction
Use:
- hover/press/focus feedback;
- drawers/dialogs;
- expand/collapse;
- success/error state changes;
- subtle route/state transitions.

Prefer short, responsive motion that explains what changed.

### Level 2 — Orchestrated
Use for:
- premium landing pages;
- product storytelling;
- one page-load composition;
- one controlled scroll reveal;
- one signature interactive section.

Limit simultaneous motion systems.

### Level 3 — Cinematic
Use only when explicitly appropriate:
- immersive campaign;
- creative portfolio;
- experiential product launch;
- scroll-driven narrative.

This may justify pinning, scrubbed timelines, layered transforms, WebGL/Three.js or GSAP, but only if the project can support and test them.

If the brief's core value is a **live mouse-reactive WebGL/3D world**, route to `experience-engineering`; that module owns renderer architecture, GPU morphing, deterministic timelines, performance tiers and experiential QA.

If the core experience is a **continuous camera/world flight rendered as video and scrubbed by scroll**, route to `scroll-world` instead of trying to approximate the journey with unrelated section animations. That module owns frame handoff, seam continuity, seek performance, native mobile variants and seam QA.

## Motion Budget

Before coding motion, define:
- one primary motion idea;
- optional secondary interaction language;
- what must remain static;
- reduced-motion fallback;
- mobile simplification.

If every section animates, nothing feels important.

## Implementation Rules

- Prefer transform and opacity for smooth motion.
- Avoid animating layout properties continuously when a transform can express the same effect.
- Do not add a new animation library for trivial transitions.
- Use existing project dependencies when possible.
- If GSAP is present or approved, keep timelines scoped and kill/cleanup triggers on component teardown.
- Test pinned/sticky effects at laptop height and mobile, not only on a tall desktop.
- Avoid scroll-jacking.
- Motion must not block reading or primary actions.

## Motion Stack Discipline

For advanced marketing/portfolio work:

- choose one primary animation system for timeline choreography;
- if using smooth scrolling, choose exactly one smooth-scroll engine; never initialize competing engines together;
- wire smooth scrolling to the timeline/scroll-trigger system correctly and refresh measurements after font/media changes;
- reserve complex timeline tooling for pinning, scrubbing, multi-layer parallax, masked reveals or precise section handoffs;
- use native CSS for ordinary hover/focus/tap transitions;
- use sticky positioning before JS pinning when timeline control is not needed;
- destroy timelines, observers, listeners, animation frames and WebGL resources on teardown;
- pause expensive offscreen or hidden animation when practical.

Three.js/WebGL is justified only when spatial depth, shader treatment or real 3D interaction materially supports the concept. Provide a static fallback and cap render cost on mobile/high-DPR devices.

## Typography + Motion

Large moving type can be effective, but:
- keep lines readable;
- avoid massive multi-line headings on small laptops;
- prevent clipping during transforms;
- preserve a non-animated readable state for reduced motion;
- when visually splitting headings into words/characters for animation, preserve an unsplit accessible name/content and hide purely decorative fragments from assistive technology;
- do not split interactive links or meaningful inline markup solely for animation.

## Dashboards

Default to Level 0–1.

Good:
- row status updates;
- drawer transitions;
- chart hover/focus;
- filter feedback;
- optimistic confirmation.

Usually bad:
- scroll reveals for every panel;
- parallax;
- pinned tables;
- giant animated page titles;
- ambient decorative motion competing with live data.

## Reduced Motion

Respect prefers-reduced-motion.

The reduced experience should preserve:
- content;
- state change meaning;
- navigation;
- interaction completion.

Remove decorative travel/scrubbing, not functionality.

## Visual QA

Motion-heavy work must be tested in the browser:
- initial state;
- during interaction/scroll;
- final state;
- resize;
- reduced-motion behavior when practical;
- cleanup after navigation/unmount.
