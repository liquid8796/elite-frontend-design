# Adaptive Capability Routing Spec

The plugin must not ask a model to self-identify as "strong" or "weak". It must route design execution using observable evidence.

Required behavior:

- replace binary strong/weak framing with three execution modes: `LOCKED`, `GUIDED`, and `BESPOKE`;
- start from `GUIDED` by default unless explicit runtime capability metadata or user intent justifies another mode;
- use a Task Complexity Score, Design Preflight, and rendered QA evidence to choose or change mode;
- runtime/model metadata is optional evidence, never the sole authority;
- never enter `BESPOKE` only because a model claims it is capable;
- `LOCKED` uses one baseline skin with Skin Lock and narrow Controlled Mutation;
- `GUIDED` uses one skin as a coherent baseline but allows bounded composition/token mutation plus one bespoke signature;
- `BESPOKE` allows custom art direction/design systems but still keeps explicit contracts and QA;
- unresolved design primitives in preflight must push routing toward more scaffolding;
- two or more material coherence failures in rendered QA must downgrade the execution mode;
- successful evidence may justify escalation, but mode changes must be explicit and re-verified;
- user intent overrides automatic mode selection when it is clear, except accessibility/usability/production constraints still apply.
