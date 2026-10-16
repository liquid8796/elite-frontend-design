---
name: creative-media
description: Proactively plan, generate, integrate and verify bespoke frontend images and motion/video assets using available local image-generation tools and deterministic FFmpeg motion rendering.
---

# Creative Media — Proactive Generation & Production Integration

## Standing authorization: do not wait for a separate media request

Whenever implementing or materially redesigning a UI, **inspect its genuine media opportunities without waiting for the user to ask for images or videos**. If a custom visual materially improves a hero, product/story section, case card, collection cover, editorial illustration, immersive scene, onboarding panel or meaningful background, **generate it proactively** using a connected/authorized tool, then integrate its actual output into the repository. This is not a request to generate random pictures for every empty container. Avoid visual filler for data tables, financial figures, account identifiers, factual diagrams, or established product screenshots.

This module is a **capability-specific recipe, not a required companion on every task**. When image/video generation is relevant, consult it in addition to the selected frontend design profile; avoid loading unrelated modules.

### Media opportunity scan (during design contract)

For each major surface, make a compact internal media brief:

| Field | Decision |
| --- | --- |
| Surface | Hero, product mockup, editorial section, feature card, gallery, teaser or ambient layer |
| User job | What the image/video communicates beyond decoration |
| Source priority | User-owned assets > exact supplied brand references > original generated asset > licensed repository media |
| Form | Static raster, transparent asset, animated video, native CSS/SVG/Canvas/WebGL |
| Art direction | Subject, identity limits, composition, camera, lighting, mood, palette, negative space |
| Delivery | Ratio, desktop/mobile crops, desired dimensions, formats, path and descriptive alternative |
| Motion | Real movement/camera need vs subtle transform; static poster fallback |
| Risk | Copyright/identity, misleading claims, network/performance budget, accessibility |

**Default to generation** when the region has high visual salience and brand-specific custom art can improve clarity or distinction. Prefer existing accurate assets for recognized products, real people, registered marks, data visualizations and exact reference recreation. Never replace a user-provided photo/logo or change its identity without a reason permitted by the brief. Avoid stock clones, watermark/logo impersonations, copyrighted character replication or fake client proof.

## Image generation: prefer the user's Jarvis MCP tool

1. Inspect currently exposed media tools. In Jarvis-connected desktop sessions prefer `mcp__Jarvis_MCP__image_gen__get_state` to inspect the **existing authorized browser binding and session ownership**, then `mcp__Jarvis_MCP__image_gen__imagegen` for **new, original** imagery. The imagegen call accepts `prompt`, optional same-session `referenced_image_paths` / `num_last_images_to_include`, and optional **stable** `request_id` for idempotency. **The tool requires a valid Jarvis session and selected Chrome/Edge extension binding**; never bypass its account, permission, or rate-limit controls or invent a browser binding.
2. Write a production brief, not "make a cool image": unique visual concept + actual design system + subject/identity + required pixel dimensions/aspect + requested transparent/crop behavior + placement/negative space + exclusions (usually no embedded text, fake logos, marks or UI elements).
3. A request returns a durable `jobId`. **Poll `mcp__Jarvis_MCP__image_gen__read`** to resolve success and original local file path; if it times out, inspect existing state/job and **do not resubmit a duplicate job**. Preserve original generated files.
4. Use the **verified path in the local/project filesystem** and create web-ready derivative(s) (e.g. WebP/AVIF where supported, PNG for transparency). Move/copy derived asset into an appropriate project assets/public path. Preserve naming, source path, generation prompt and ownership in a local asset ledger. Do not present a remote preview URL as a permanent project asset.
5. Wire actual imports/URLs into the React/Vue/HTML/CSS project; use responsive crop/position, intrinsic dimensions, lazy load below the fold, meaningful alt or empty alt for purely decorative art. Audit the result at real breakpoints and refine a failed crop by re-prompting rather than stretching.
6. If Jarvis ImageGen is unbound, unavailable, out of quota or disallowed, **do not silently claim success**. Try other explicitly available, authorized image-generation providers or existing legitimate local assets; otherwise use purposeful CSS/SVG and report the limitation. Never ask for permission merely to generate normal UI art when authorized tools exist; stop only if account connection or explicit approval is genuinely needed.

**Do not regenerate** existing satisfactory visuals on every patch: preserve the asset unless requirements or rendered evidence justify a new variant. Source supplied images are not automatically permission to modify their identities; new image generation must reflect user intent and ownership constraints.

## Proactive video selection — two distinct capabilities

### A. Genuine generative video model (if actually connected)

Discover available **video-generation** tools at runtime. If a real, authorized model supports text/image-to-video and the design needs coherent physical movement, characters, scene changes or a cinematic product sequence, **invoke it proactively** with storyboard, shot durations, aspect ratio, reference images when permitted, style consistency, output resolution and no unauthorized subject impersonation. Resolve actual finished output, inspect frames, create poster/format derivatives and integrate the video. A "video" keyword in a description or browser playback feature is **not** evidence a text-to-video model exists.

Never invent a tool, endpoint, purchase, generation status or artifact. If a provider needs user connection, do not bypass consent.

### B. Local motion clip from generated stills (FFmpeg fallback)

If no video model is connected **but FFmpeg is available**, turn original generated stills into an **actual MP4 video** with slow crop/pan/zoom and crossfades using the bundled local helper:

```bash
python "<skill-root>/references/modules/creative-media/scripts/render_motion_clip.py" \
  --images path/to/hero-1.webp path/to/hero-2.png \
  --output path/to/project/public/media/agency-reel.mp4 \
  --width 1280 --height 720 --fps 24 --seconds-per-image 3 --transition 0.6
```

Output is a **motion-graphics/animated-still video**, NOT a new cinematic text-to-video model. Best for abstract worlds, mood loops, editorial image transitions, teaser backdrops and product still hero reels. Do not use it to portray unobserved real-person activity, misleading real-world evidence, or complex character actions it cannot produce. If a still should remain still, use it as an image instead.

FFmpeg is optional, must be installed and discoverable on PATH or supplied via `--ffmpeg`. Do not download software, contact external generators, consume paid credits or modify user credentials as an implicit side effect. The helper outputs muted H.264 MP4 (and a JPEG poster), not genuine synthesized actions; it must return actionable failures on missing input/tool. If no renderer is available, favor CSS/SVG/native transitions and report no exported clip was generated.

### Frontend video integration contract

Use `<video muted playsInline loop preload="none" poster="...">` for intentional decorative ambient reels; autoplay only when justified and legal in browser, and pause offscreen/hidden. For meaning-bearing clips, expose labeled Play/Pause, captions/transcript when applicable, duration and controls. Prefer WebM/MP4 source fallback only when files actually exist. Respect `prefers-reduced-motion` by showing a static poster and avoiding automatic play. Avoid giant network payloads or an expensive reel behind every card; allocate one or two visual focal points.

## Acceptance and provenance

Before declaring the page done, verify: local artifacts exist and are in the build output; no broken `src`/URL; aspect and focus are correct on desktop and mobile; no watermarks/fake marks; legible overlay contrast; alt/poster are accurate; both reduced-motion and normal motion are usable; video can be decoded and is muted or explicitly user-controlled; load/lazy behavior and encoded dimensions are acceptable. Add media success/failure to the QA evidence report; **only call it generated when the tool returned and integration was verified**.

Media generation is an enhancement to the user's frontend task, **not a reason to override a brief, replace existing correct photography or spend unbounded calls**. Generate a small, deliberate set of high-impact assets, iterate against screenshots, and keep the rest of the UI focused.
