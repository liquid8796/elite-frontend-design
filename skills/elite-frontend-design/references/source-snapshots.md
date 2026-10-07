# Reviewed source snapshots

Deep-review date: 2026-09-20

These commits pin the upstream state inspected while hardening Elite Frontend Design through 3.7.0. They are provenance only; the upstream repositories are not vendored into this skill. Local Cosmos implementation regressions are documented separately because they are not upstream repositories.

| Source | Reviewed commit | Upstream commit date |
|---|---|---|
| anthropics/skills | `34040c9c568585f6929bedeaad110ad08f079624` | 2026-09-10 |
| openai/plugins | `1dc195897af4161d039b80d8471ec0a10c9bbc89` | 2026-09-11 |
| openai/skills | `49f948faa9258a0c61caceaf225e179651397431` | 2026-06-23 |
| dobromirdikov/codex-frontend-design-skill | `983119775a936d123df9fbfbc3821bdee5bb58fd` | 2026-05-14 |
| jinshiqwq/image-first-frontend | `fd0bc3cfc9be6255be39de51ebe3fffa85a527f4` | 2026-07-10 |
| nextlevelbuilder/ui-ux-pro-max-skill | `15de38fb70bc80ae9276fa7703b48ae861a672e6` | 2026-09-15 |
| superdesigndev/superdesign-skill | `f9f05cd988c247dce6c072eaf9ac6b162f2ffc4b` | 2026-08-21 |
| MengTo/Skills | `5f47e389dac337a1bca5cddf376419248b3010f6` | 2026-09-17 |
| tasteskill/tasteskill | `37c8c376b92ebc02456f7c70776b514fddda88e1` | 2026-05-24 |
| yutori-ai/frontend-visualqa | `8866c9fd6bfaf8940f97bbee31c9fdfe4368b1e9` | 2026-09-17 |
| leoisadev1/skills-gpt-bench | `a4c053d76a4718c4e91d7120770688b634f00020` | 2026-05-25 |
| oso95/scroll-world | `71cc36d3bb150248ae36a2c552f9cbf88802a79c` | 2026-07-28 |
| daymade/claude-code-skills | `72dc01ffe8a99b8be12f1bc8f7a87afb37e2b7bc` | 2026-09-19 |
| practicajs/the-frontend-testing-skill | `ae1b7bc8b58a77d3cd70e1d775fa73ecb8767154` | 2026-09-14 |
| maxrihter/claude-skill-visual-regression | `7fa2ea4fdac37867ba3686ef6936fd791a622fab` | 2026-07-09 |
| testdino-hq/playwright-skill | `400e4256cd22669ad69c18d31d3e5541e4e1c2a3` | 2026-09-06 |

## Interpretation

- A later upstream commit may change details; this file states what was actually reviewed for this local version.
- The benchmark repository contains historical/local skill snapshots. A benchmark snapshot is not automatically evidence that an identically named file still exists in the source project's current repository.
- The imported UI/UX Pro Max module in this local skill has its own source/import version metadata; the upstream commit above is a review comparison point, not a claim that the entire local bundle was re-vendored from that commit.
