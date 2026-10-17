# BridgeBench Opus 5.5 Sunset Ocean — Experiential Scene Toolkit Spec

Reference: user-provided `prompt.txt` (168-line Sunset Ocean mandate); local runnable source `D:\Project\test\bridgebench-opus55-sunset-ocean\index.html`; original `bridgebench-original.html`; `start.bat` opens `http://127.0.0.1:8765/`. Deep source-and-runtime profile: `../../../design-intelligence/sites/bridgebench-opus55-sunset-ocean.md`.

**One-route, one-scene** real-time graphics reference; not a multipage site. Benchmark attribution to Claude Opus 5.5 comes from the local README. A single source HTML + local Three.js 0.182.0 vendor dependencies, not a bundled React app. Never copy this case's precise color/video assets into new products; extract architectural mechanics and the source's **missing requirements**.

## Measured and auditable contract

- Prompt T1–T11: `data/bridgebench-opus55-sunset-ocean-prompt-trace-2026-10-17.csv`.
- Source anatomy (source line ranges, matching implementation and gaps): `data/bridgebench-opus55-sunset-ocean-source-components-2026-10-17.csv`.
- Browser evidence: `data/bridgebench-opus55-sunset-ocean-render-states-2026-10-17.csv`. Includes the successful project smoke run separately documented in profile, source-confirmed controls, software renderer responsive caveat and direct `file://` failure.
- Screenshots: `design-intelligence/sites/bridgebench-opus55-sunset-ocean-1280.webp` and `-390.webp` sampled from local source at 2026-10-17. Static screenshot is not a 60s/FPS validation.

## Shader architecture to transfer

1. **Renderer foundation**: WebGL2/Three.js, ACES Filmic, sRGB, native antialias; capped DPR; camera ~2–4m above near ocean and pitched toward low sun. Source cap=1.5; prompt cap=2. Don't assume user hardware GPU test has passed.
2. **Radial mesh**: polar fan of 384 angular columns ×330 radial steps, logarithmic radial placement near-to-far, single indexed static geometry, long horizon reach. **Never add radial mesh edge or keep world-fixed water if allowing camera XZ travel**.
3. **Wave families**: 8 seeded GPU Gerstner swells with wavelengths 62/41/27/17.5/11.3/7.2/4.6/3.0m and omega=sqrt(g*k), horizontal steepening, amplitude controls; 16 procedural ripple derivatives in pixel shader with screen-derivative filtering (NOT scrolling dual normal maps). Analytical tangents and Jacobian foam. Physically plausible wave shapes take priority over excessive foam and shader sparkle.
4. **Shared sky/sun**: one `uSunDir` and `uSunCol` across water and sky. Source sky is 5-octave FBM cloud layer + manually tuned horizon/mid/zenith directional gradient and sun disc glow; **not formal Preetham or Rayleigh/Mie**. Move toward full physical sky only when prompt explicitly requires more physical correctness.
5. **Water optical shading**: Schlick water F0≈0.02, **Beckmann-like** sun distribution, dynamic half-float 256px sky cubemap, deep-teal/turquoise crest tint, foam from Jacobian and procedural noise, fog to reflected horizon color. **Source captures cubemap every frame (six faces)**; profile and limit refresh cost before claiming a 60 FPS budget.
6. **Temporal director**: deterministic seeded waves, time-based shader phase, eased sea/sun values, subtle camera pitch/roll; requestAnimationFrame with teardown. Source's camera height tracks total max amplitude and lacks local sampled-wave bobbing. Do not misrepresent a sinusoidal sway as true sampled camera/crest motion.
7. **Post/fallback**: source has native MSAA and film grain, but lacks composer, selective sun bloom, vignette, SMAA/FXAA passes and actual low/high quality mode. In new ambitious scenes either **implement and profile these explicitly** or mark them missing, rather than treating a visual glow as post bloom.
8. **Benchmark harness**: `BridgeBenchTaskManifest` and `BridgeBenchTaskApi` support deterministic reset and getState; expose a hidden-by-default quality/debug panel only if requested. Don't ship visible test UI over the cinema without intention.

## UX and responsiveness

Single full-screen canvas with no content cards, boats, characters, floating logos or scroll narrative; horizon and sunset are the only focal point. Camera and sky/water all frame-contiguous. Reduced-motion preference: static frame/poster is an accessibility fallback, not reason to change shader physics by default.

Browser smoke at 1280×800 verified WebGL2 and both UI controls, no console errors. The independent software-GPU test observed a 390px CSS width but stale 1280×800 canvas backbuffer immediately following resize; **this is a warning, not a verified release pass**. Test resize and DPR in the target browser/hardware. Direct `file://` open yielded no canvas/API and errors; startup **must run over HTTP** with `start.bat` in the local version. It does not comply with prompt's unconditional open-HTML T1. A software-rendered 15-second RAF watchdog captured only 19 callbacks; **do not extrapolate this to mid-range integrated hardware FPS**.

## Production-grade transfer checklist

Keep a side-by-side **source evidence / prompt requirement / browser proof / status** matrix. Probe the intended frame at 1920×1080 on target GPU, high/low sea, low/high sun, 390px phone, window resize, page visibility/restore and at least 60 seconds without popping/tiling. Profile draw calls and cubic sky update frequency, watch shader compile time and frame time. Ensure the horizon meets atmosphere without a seam and the glitter stretches toward viewer without broad uniform white stripes. Compare photograph-level visual judgment with a human review; do not certify T2 from a shader regex or color histogram. The same prompt can justify stronger rendering architecture than the current demo; distillation records its reusable good ideas **and** its deficits.
