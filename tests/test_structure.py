from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.validate_skill import validate

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "elite-frontend-design"


class EliteFrontendDesignStructureTests(unittest.TestCase):
    def test_validator_has_no_errors(self) -> None:
        self.assertEqual([], validate())

    def test_core_orchestration_modules_are_registered(self) -> None:
        manifest = json.loads((SKILL_ROOT / "skill.json").read_text(encoding="utf-8"))
        required = {
            "elite-core",
            "reference-first",
            "visual-qa",
            "frontend-qa",
            "motion-direction",
        }
        self.assertTrue(required.issubset(set(manifest["modules"])))
        for module in required:
            self.assertTrue(
                (
                    SKILL_ROOT
                    / "references"
                    / "modules"
                    / module
                    / "module.md"
                ).is_file()
            )

    def test_root_skill_name_is_elite_frontend_design(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: elite-frontend-design", skill)

    def test_source_map_exists(self) -> None:
        self.assertTrue((SKILL_ROOT / "references" / "source-map.md").is_file())
        self.assertTrue((SKILL_ROOT / "references" / "source-snapshots.md").is_file())

    def test_hardened_reference_and_qa_contracts_exist(self) -> None:
        reference_first = (
            SKILL_ROOT / "references" / "modules" / "reference-first" / "module.md"
        ).read_text(encoding="utf-8")
        visual_qa = (
            SKILL_ROOT / "references" / "modules" / "visual-qa" / "module.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Accepted-reference lock", reference_first)
        self.assertIn("Section/state detail references", reference_first)
        self.assertIn("Define the QA Inventory", visual_qa)
        self.assertIn("Viewport Fit Is a Separate Check", visual_qa)
        self.assertIn("Mismatch Ledger", visual_qa)
        self.assertIn("Cross-System Render Parity", visual_qa)

    def test_source_map_distinguishes_benchmark_snapshot(self) -> None:
        source_map = (SKILL_ROOT / "references" / "source-map.md").read_text(encoding="utf-8")
        self.assertIn("Benchmark-only OpenAI frontend-skill snapshot", source_map)
        self.assertIn("not", source_map[source_map.index("Benchmark-only OpenAI frontend-skill snapshot"):].lower())

    def test_scroll_world_module_is_registered_and_hardened(self) -> None:
        manifest = json.loads((SKILL_ROOT / "skill.json").read_text(encoding="utf-8"))
        self.assertIn("scroll-world", manifest["modules"])

        module = (
            SKILL_ROOT / "references" / "modules" / "scroll-world" / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Continuity Contract — Position AND Velocity",
            "Crossfade Is Insurance, Not a Fix",
            "Scroll → Time Mapping",
            "Runtime Lifecycle Is Mandatory",
            "Seam-Focused QA",
        ):
            self.assertIn(phrase, module)

        snapshots = (SKILL_ROOT / "references" / "source-snapshots.md").read_text(encoding="utf-8")
        self.assertIn("oso95/scroll-world", snapshots)
        self.assertIn("71cc36d3bb150248ae36a2c552f9cbf88802a79c", snapshots)

    def test_frontend_qa_director_contract(self) -> None:
        manifest = json.loads((SKILL_ROOT / "skill.json").read_text(encoding="utf-8"))
        self.assertIn("frontend-qa", manifest["modules"])

        root_skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Full Frontend QA", root_skill)
        self.assertIn("VERIFIED, PARTIAL or BLOCKED", root_skill)

        module = (
            SKILL_ROOT / "references" / "modules" / "frontend-qa" / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Choose QA Depth Deliberately",
            "Write the QA Contract",
            "Build One Shared QA Inventory",
            "Use an Evidence Ladder",
            "Functional Journey QA",
            "Navigation Parity QA",
            "Cross-channel State QA",
            "Responsive Accessibility Snapshot",
            "Accessibility Baseline",
            "Visual Regression",
            "Test Quality and Stability",
            "Trace-Driven Failure Diagnosis",
            "Diagnostic Clean-Context Recheck",
            "Exploratory Pass",
            "Fix-and-Reverify Loop",
            "Signoff Report",
        ):
            self.assertIn(phrase, module)

        source_map = (SKILL_ROOT / "references" / "source-map.md").read_text(encoding="utf-8")
        self.assertIn("Frontend QA synthesis", source_map)
        self.assertIn("daymade/claude-code-skills", source_map)
        self.assertIn("practicajs/the-frontend-testing-skill", source_map)
        self.assertIn("maxrihter/claude-skill-visual-regression", source_map)
        self.assertIn("testdino-hq/playwright-skill", source_map)

        snapshots = (SKILL_ROOT / "references" / "source-snapshots.md").read_text(encoding="utf-8")
        for phrase in (
            "72dc01ffe8a99b8be12f1bc8f7a87afb37e2b7bc",
            "ae1b7bc8b58a77d3cd70e1d775fa73ecb8767154",
            "7fa2ea4fdac37867ba3686ef6936fd791a622fab",
            "400e4256cd22669ad69c18d31d3e5541e4e1c2a3",
        ):
            self.assertIn(phrase, snapshots)

    def test_experience_engineering_regression_contract(self) -> None:
        manifest = json.loads((SKILL_ROOT / "skill.json").read_text(encoding="utf-8"))
        self.assertIn("experience-engineering", manifest["modules"])

        root_skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Ambition Escalation Gate", root_skill)
        self.assertIn("experience-engineering", root_skill)
        self.assertIn("authored-world contract", root_skill)

        module = (
            SKILL_ROOT / "references" / "modules" / "experience-engineering" / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Prevent the Prototype Ceiling",
            "Plan the Experience in Technical Slices",
            "Test Architecture Contracts, Not Only DOM Output",
            "One Progress Domain and Timeline ↔ Layout Synchronization",
            "Rendering Architecture Gate",
            "GPU-First Morphing",
            "Authored World Systems — Story Physics",
            "Analytic State Synthesis and Draw-Call Budget",
            "Sample Structure, Do Not Merely Smear It",
            "Add an Experience Director",
            "Temporal Staging — Hold → Transform → Settle",
            "One Hot-Path Animation Loop",
            "Design an Input Grammar",
            "Narrative Truth Before Poetry",
            "Adaptive Runtime Quality",
            "Build a QA Storyboard Before Signoff",
            "Navigation Parity QA",
            "Cross-channel State QA",
            "Spec-to-Implementation QA Trace",
            "Temporal QA — inspect motion, not only keyframes",
            "Input-grammar QA",
            "Performance-response QA",
            "Cosmos Regression Lessons",
        ):
            self.assertIn(phrase, module)

        benchmark = (
            SKILL_ROOT / "references" / "benchmarks" / "cosmos-gpt56-case-study.md"
        ).read_text(encoding="utf-8")
        self.assertIn("GPU versus CPU morphing", benchmark)
        self.assertIn("Deterministic composition", benchmark)
        self.assertIn("Claude Desktop / Opus 5 result", benchmark)
        self.assertIn("Story physics", benchmark)
        self.assertIn("Experience Director", benchmark)
        self.assertIn("Adaptive runtime quality", benchmark)
        self.assertIn("Rebuilt ChatGPT Web result with Elite v3.6", benchmark)
        self.assertIn("Timeline/layout desynchronization", benchmark)
        self.assertIn("Responsive accessibility regression", benchmark)
        self.assertIn("HUD says chapter X", benchmark)
        self.assertIn("Skill changes derived from this case", benchmark)

    def test_design_intelligence_refokus_contract(self) -> None:
        manifest = json.loads((SKILL_ROOT / "skill.json").read_text(encoding="utf-8"))
        self.assertIn("design-intelligence", manifest["modules"])

        root_skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("design-intelligence", root_skill)
        self.assertIn("inspiration distillation", root_skill.lower())

        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Distill, Don't Clone",
            "Design DNA",
            "Evidence Confidence",
            "Pattern Promotion",
            "Bounded Immersive Rendering",
            "Responsive Brand Payload",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "refokus.com.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Refokus",
            "https://www.refokus.com/",
            "2026-10-05",
            "Featuredeck",
            "Generalsans Variable",
            "WebGLRenderer",
            "ScrollTrigger",
            "SplitText",
            "EffectComposer",
            "pixel ratio",
            "one signature stage",
            "quiet shell",
            "vivid project worlds",
            "sound",
            "mobile",
        ):
            self.assertIn(phrase, profile)

        index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("design-intelligence", index)
        self.assertIn("refokus.com.md", index)

    def test_design_intelligence_resend_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Product Evidence Before Feature Claims",
            "Responsive Fidelity Substitution",
            "Code as Product Proof",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "resend.com.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Resend",
            "https://resend.com/",
            "2026-10-05",
            "Domaine",
            "aBCFavorit",
            "CommitMono",
            "cube.splinecode",
            "cube.mp4",
            "Product Evidence Before Feature Claims",
            "Code as Product Proof",
            "Responsive Fidelity Substitution",
            "test mode",
            "functional tabs",
            "mobile",
        ):
            self.assertIn(phrase, profile)

        index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("resend.com.md", index)

    def test_design_intelligence_landscape_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Reference Landscape Routing",
            "Template Archetype Firewall",
            "Breadth-to-Depth Funnel",
            "Game/Experiential Audit Lens",
            "candidate reference is not audited evidence",
            "experience-engineering",
        ):
            self.assertIn(phrase, module)

        landscape = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Reference Landscape",
            "Candidate, Not Evidence",
            "product precision",
            "experiential / agency",
            "luxury / editorial",
            "game / cinematic",
            "developer product",
            "template commodity",
            "Apple",
            "Stripe",
            "Linear",
            "Refokus",
            "Resend",
            "GTA VI",
            "Cyberpunk 2077",
            "Black Myth: Wukong",
            "Template Convergence Risk",
        ):
            self.assertIn(phrase, landscape)

        index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("reference-landscape.md", index)

    def test_design_intelligence_skin_pack_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Baseline Skin Packs",
            "Skin Lock",
            "Controlled Mutation",
            "Adaptive Capability Routing",
            "Skin-Guided Execution",
            "1 archetype + 1 skin + 1 composition grammar",
            "Deterministic Design Scaffold",
        ):
            self.assertIn(phrase, module)

        root_skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Adaptive Capability Routing", root_skill)
        self.assertIn("GUIDED is the default", root_skill)
        self.assertIn("baseline skin", root_skill.lower())

        skins_root = SKILL_ROOT / "references" / "design-intelligence" / "skins"
        skin_names = (
            "premium-saas-dark.md",
            "clean-product-light.md",
            "developer-infra.md",
            "creative-agency-editorial.md",
            "luxury-editorial.md",
            "bento-product.md",
            "cinematic-game.md",
            "game-studio.md",
            "open-world-cinematic-launch.md",
            "evidence-first-data-directory.md",
            "enterprise-ai-platform-light.md",
            "whimsical-world-portfolio.md",
            "premium-ecommerce.md",
        )
        self.assertEqual({p.name for p in skins_root.glob("*.md") if p.name != "index.md"}, set(skin_names))

        skin_index = (skins_root / "index.md").read_text(encoding="utf-8")
        for skin_name in skin_names:
            self.assertIn(skin_name, skin_index)

        for skin_name in skin_names:
            skin = (skins_root / skin_name).read_text(encoding="utf-8")
            for phrase in (
                "Use when",
                "Token Scaffold",
                "Composition Grammar",
                "Skin Lock",
                "Controlled Mutation",
                "Responsive Contract",
                "Anti-Template Guard",
                "QA Rubric",
            ):
                self.assertIn(phrase, skin, f"{skin_name} missing {phrase}")

        developer_skin = (skins_root / "developer-infra.md").read_text(encoding="utf-8")
        for phrase in (
            "resend.com.md",
            "audited evidence anchor",
            "Product Evidence Before Feature Claims",
            "Code as Product Proof",
            "Responsive Fidelity Substitution",
        ):
            self.assertIn(phrase, developer_skin)

        agency_skin = (skins_root / "creative-agency-editorial.md").read_text(encoding="utf-8")
        for phrase in (
            "refokus.com.md",
            "audited evidence anchor",
            "one signature stage",
            "quiet shell",
            "Responsive Brand Payload",
        ):
            self.assertIn(phrase, agency_skin)

        index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("design-intelligence/skins/index.md", index)

    def test_adaptive_capability_routing_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Adaptive Capability Routing",
            "LOCKED",
            "GUIDED",
            "BESPOKE",
            "Task Complexity Score",
            "Design Preflight",
            "GUIDED is the default",
            "two or more material coherence failures",
            "runtime metadata",
            "self-assessment",
            "downgrade",
            "escalate",
        ):
            self.assertIn(phrase, module)
        self.assertNotIn("Low-Capability Mode", module)

        root_skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "Adaptive Capability Routing",
            "LOCKED / GUIDED / BESPOKE",
            "Task Complexity Score",
            "Design Preflight",
            "GUIDED",
            "two or more material coherence failures",
        ):
            self.assertIn(phrase, root_skill)
        self.assertNotIn("Low-Capability Mode", root_skill)

        skin_index = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "index.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Adaptive Execution Modes",
            "LOCKED",
            "GUIDED",
            "BESPOKE",
            "GUIDED is the default",
            "Task Complexity Score",
            "Design Preflight",
        ):
            self.assertIn(phrase, skin_index)


    def test_design_intelligence_rockstar_vi_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Aspect-Ratio Art Direction",
            "World-Led Campaign Chapters",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "rockstargames.com-vi.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Rockstar Games VI",
            "https://www.rockstargames.com/VI",
            "2026-10-06",
            "ArtDecoBold",
            "HeroBackground",
            "TriggerHeadline",
            "poster_full",
            "shard0",
            "Aspect-Ratio Art Direction",
            "World-Led Campaign Chapters",
            'data-track="hero"',
            "back-of-box",
            "no horizontal overflow",
            "user-scalable=no",
        ):
            self.assertIn(phrase, profile)

        skin = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "open-world-cinematic-launch.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Open-World Cinematic Launch",
            "audited evidence anchor",
            "rockstargames.com-vi.md",
            "Use when",
            "Token Scaffold",
            "Composition Grammar",
            "Skin Lock",
            "Controlled Mutation",
            "Responsive Contract",
            "Anti-Template Guard",
            "QA Rubric",
            "Aspect-Ratio Art Direction",
            "World-Led Campaign Chapters",
            "Trailer as User-Invoked Proof",
            "Back-of-Box Chapter",
        ):
            self.assertIn(phrase, skin)

        skin_index = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "index.md"
        ).read_text(encoding="utf-8")
        self.assertIn("open-world-cinematic-launch.md", skin_index)

        ref_index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("rockstargames.com-vi.md", ref_index)

        landscape = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        self.assertIn("GTA VI - **audited**", landscape)


    def test_design_intelligence_tokenmeter_full_site_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Confidence as Interface",
            "Route-Family Density Ladder",
            "Contain Horizontal Density, Don't Crush It",
            "Human + Machine Surface Parity",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "tokenmeter.info.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Tokenmeter",
            "https://tokenmeter.info/",
            "2026-10-06",
            "Coverage: 26/26 sitemap URLs",
            "/compare/",
            "/faq/",
            "/glossary/",
            "/methodology/",
            "/providers/",
            "/providers/openai/",
            "/providers/together-ai/",
            "20 provider detail pages",
            "Archivo Variable",
            "JetBrains Mono Variable",
            "--accent:#e8590c",
            "Astro v7.0.7",
            "Confidence as Interface",
            "Route-Family Density Ladder",
            "Contain Horizontal Density, Don't Crush It",
            "Human + Machine Surface Parity",
            "llms.txt",
            "sitemap-index.xml",
            "prefers-reduced-motion",
        ):
            self.assertIn(phrase, profile)

        skin = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "evidence-first-data-directory.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Evidence-First Data Directory",
            "audited evidence anchor",
            "tokenmeter.info.md",
            "Use when",
            "Token Scaffold",
            "Composition Grammar",
            "Skin Lock",
            "Controlled Mutation",
            "Responsive Contract",
            "Anti-Template Guard",
            "QA Rubric",
            "Confidence as Interface",
            "Route-Family Density Ladder",
            "Contain Horizontal Density, Don't Crush It",
        ):
            self.assertIn(phrase, skin)

        skin_index = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "index.md"
        ).read_text(encoding="utf-8")
        self.assertIn("evidence-first-data-directory.md", skin_index)

        ref_index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("tokenmeter.info.md", ref_index)

        landscape = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Tokenmeter - **audited**", landscape)


    def test_design_intelligence_novaos_full_site_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Operational Pipeline Storytelling",
            "Proof Surface Cropping",
            "Credibility Through Route Ecosystem",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "novaos.framer.website.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "NovaOS",
            "https://novaos.framer.website/",
            "2026-10-06",
            "Coverage: 23/23 sitemap URLs",
            "/pricing",
            "/company",
            "/blog",
            "/careers",
            "/integrations",
            "/contact",
            "/faq",
            "/book-a-demo",
            "/privacy-policy",
            "/terms",
            "6 career detail pages",
            "6 blog article pages",
            "Framer 95da0c7",
            "DM Sans Variable",
            "Geist",
            "#0082de",
            "Lenis 1.3.26",
            "lerp: 0.085",
            "prefers-reduced-motion",
            "810px",
            "1200px",
            "Operational Pipeline Storytelling",
            "Proof Surface Cropping",
            "Credibility Through Route Ecosystem",
            "no document-level horizontal overflow",
            "Get This Template",
        ):
            self.assertIn(phrase, profile)

        skin = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "enterprise-ai-platform-light.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Enterprise AI Platform Light",
            "audited evidence anchor",
            "novaos.framer.website.md",
            "Use when",
            "Token Scaffold",
            "Composition Grammar",
            "Skin Lock",
            "Controlled Mutation",
            "Responsive Contract",
            "Anti-Template Guard",
            "QA Rubric",
            "Operational Pipeline Storytelling",
            "Proof Surface Cropping",
            "Credibility Through Route Ecosystem",
            "Shared Conversion Tail",
        ):
            self.assertIn(phrase, skin)

        skin_index = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "index.md"
        ).read_text(encoding="utf-8")
        self.assertIn("enterprise-ai-platform-light.md", skin_index)

        ref_index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("novaos.framer.website.md", ref_index)

        landscape = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        self.assertIn("NovaOS (Framer template) - **audited**", landscape)


    def test_design_intelligence_powder_full_site_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Conversation-to-Action Proof",
            "Template Residue Quarantine",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "powder.framer.website.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Powder",
            "https://powder.framer.website/",
            "2026-10-07",
            "Coverage: 21/21 sitemap URLs",
            "10 blog detail pages",
            "/about",
            "/blog",
            "/changelog",
            "/get-started",
            "/pricing",
            "/terms-of-use",
            "/cookie-policy",
            "/privacy-policy",
            "/page",
            "/404",
            "Framer a050651",
            "Fragment Mono",
            "Inter Variable",
            "Inter Display",
            "#000912",
            "#d39794",
            "#177275",
            "810px",
            "1280px",
            "1024px",
            "position: sticky",
            "top: 120px",
            "390px",
            "no document-level horizontal overflow",
            "Conversation-to-Action Proof",
            "Template Residue Quarantine",
            "Sticky Capability Stack",
            "Remix for free",
        ):
            self.assertIn(phrase, profile)

        skin = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "premium-saas-dark.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Powder audited evidence anchor",
            "powder.framer.website.md",
            "Conversation-to-Action Proof",
            "Sticky Capability Stack",
            "Template Residue Quarantine",
            "Use when",
            "Token Scaffold",
            "Composition Grammar",
            "Skin Lock",
            "Controlled Mutation",
            "Responsive Contract",
            "Anti-Template Guard",
            "QA Rubric",
        ):
            self.assertIn(phrase, skin)

        ref_index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("powder.framer.website.md", ref_index)

        landscape = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Powder (Framer template) - **audited**", landscape)


    def test_design_intelligence_nudge_folio_full_site_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Reflective Case Study Arc",
            "Persistent Context Rail",
            "Experimental Surface Isolation",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "nudge-folio.framer.website.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Nudge Folio",
            "https://nudge-folio.framer.website/",
            "2026-10-07",
            "Coverage: 19/19 sitemap URLs",
            "8 blog detail pages",
            "4 case-study detail pages",
            "/about",
            "/case-study",
            "/blog",
            "/services",
            "/play-ground",
            "/contact",
            "Framer bc64f0a",
            "Flux Variable",
            "Inter Display",
            "DM Mono",
            "Just Me Again Down Here",
            "#111212",
            "#36c5f0",
            "#ecb22e",
            "#2fbc81",
            "#e01e5a",
            "810px",
            "1200px",
            "position: sticky",
            "top: 190px",
            "GSAP",
            "Draggable",
            "lenis lenis-autoToggle",
            "390px",
            "no document-level horizontal overflow",
            "Reflective Case Study Arc",
            "Persistent Context Rail",
            "Experimental Surface Isolation",
            "BUY NUDGE",
        ):
            self.assertIn(phrase, profile)

        skin = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "creative-agency-editorial.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Nudge Folio audited template anchor",
            "nudge-folio.framer.website.md",
            "Reflective Case Study Arc",
            "Persistent Context Rail",
            "Experimental Surface Isolation",
            "Use when",
            "Token Scaffold",
            "Composition Grammar",
            "Skin Lock",
            "Controlled Mutation",
            "Responsive Contract",
            "Anti-Template Guard",
            "QA Rubric",
        ):
            self.assertIn(phrase, skin)

        ref_index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("nudge-folio.framer.website.md", ref_index)

        landscape = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Nudge Folio (Framer template) - **audited**", landscape)


    def test_design_intelligence_orbai_full_site_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Commercial Core + Trust Satellites",
            "Pricing-to-Comparison Bridge",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "orbai-template.framer.website.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "OrbAI",
            "https://orbai-template.framer.website/",
            "2026-10-07",
            "Coverage: 8/8 sitemap URLs",
            "4 changelog detail pages",
            "/contact",
            "/privacy",
            "/changelog",
            "/404",
            "Framer 3db8496",
            "Satoshi",
            "Inter",
            "#814fff",
            "#f5f5f5",
            "#04070d",
            "810px",
            "1200px",
            "aMPvRVYHFQxBoB0v2qyJln83jI.mp4",
            "Commercial Core + Trust Satellites",
            "Pricing-to-Comparison Bridge",
            "390px",
            "no document-level horizontal overflow",
            "Framer",
            "Get Template",
        ):
            self.assertIn(phrase, profile)

        skin = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "clean-product-light.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "OrbAI audited template anchor",
            "orbai-template.framer.website.md",
            "Commercial Core + Trust Satellites",
            "Pricing-to-Comparison Bridge",
            "Use when",
            "Token Scaffold",
            "Composition Grammar",
            "Skin Lock",
            "Controlled Mutation",
            "Responsive Contract",
            "Anti-Template Guard",
            "QA Rubric",
        ):
            self.assertIn(phrase, skin)

        ref_index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("orbai-template.framer.website.md", ref_index)

        landscape = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        self.assertIn("OrbAI (Framer template) - **audited**", landscape)


    def test_design_intelligence_nexira_full_site_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Cinematic Without Heavy Rendering",
            "Capability-to-Case Pairing",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "nexira.framer.ai.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Nexira",
            "https://nexira.framer.ai/",
            "2026-10-07",
            "Coverage: 28/28 sitemap URLs",
            "7 primary routes",
            "7 service detail pages",
            "7 case detail pages",
            "7 blog detail pages",
            "/404",
            "Framer b8d5a97",
            "Oswald",
            "Inter",
            "Fragment Mono",
            "#adff00",
            "#ffd335",
            "#1d1d1d",
            "810px",
            "1360px",
            "Framer Motion",
            "Cinematic Without Heavy Rendering",
            "Capability-to-Case Pairing",
            "sticky case deck",
            "390px",
            "350x889",
            "no document-level horizontal overflow",
            "REDDEVS 2024",
        ):
            self.assertIn(phrase, profile)

        studio_skin = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "game-studio.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Nexira audited template anchor",
            "nexira.framer.ai.md",
            "Cinematic Without Heavy Rendering",
            "Capability-to-Case Pairing",
            "Game Studio Routing Boundary",
            "Use when",
            "Token Scaffold",
            "Composition Grammar",
            "Skin Lock",
            "Controlled Mutation",
            "Responsive Contract",
            "Anti-Template Guard",
            "QA Rubric",
        ):
            self.assertIn(phrase, studio_skin)

        cinematic_skin = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "cinematic-game.md"
        ).read_text(encoding="utf-8")
        self.assertNotIn("Nexira audited template anchor", cinematic_skin)
        self.assertNotIn("../sites/nexira.framer.ai.md", cinematic_skin)
        self.assertIn("Generic game / entertainment marketing baseline", cinematic_skin)
        self.assertIn("Use game-studio.md", cinematic_skin)
        self.assertIn("Use open-world-cinematic-launch.md", cinematic_skin)

        ref_index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("nexira.framer.ai.md", ref_index)

        landscape = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Nexira (Framer template) - **audited**", landscape)

    def test_design_intelligence_cosmos_ten_billion_years_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Prompt-to-Experience Compile Contract",
            "Narrative Parameter Matrix",
            "Event Peaks on Continuous Timeline",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "cosmos-10-billion-years-opus5.vercel.app.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Ten Billion Years",
            "https://cosmos-10-billion-years-opus5.vercel.app/",
            "2026-10-07",
            "Coverage: 1/1 public route",
            "9 chapters",
            "1029vh",
            "three.js r185",
            "React Three Fiber",
            "Lenis 1.3.25",
            "Instrument Serif",
            "Inter",
            "JetBrains Mono",
            "AudioContext",
            "Web Audio",
            "Prompt-to-Experience Compile Contract",
            "Narrative Parameter Matrix",
            "Event Peaks on Continuous Timeline",
            "0.85",
            "1.75",
            "220,000",
            "110,000",
            "70,000",
            "390x844",
            "no document-level horizontal overflow",
            "prefers-reduced-motion",
            "Begin with sound",
            "Continue in silence",
            "you.",
        ):
            self.assertIn(phrase, profile)

        scroll_world = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "scroll-world"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Ten Billion Years audited real-time anchor",
            "cosmos-10-billion-years-opus5.vercel.app.md",
            "Weighted Narrative Timeline",
            "Shared Progress Bus",
            "Adaptive Renderer Budget",
        ):
            self.assertIn(phrase, scroll_world)

        ref_index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("cosmos-10-billion-years-opus5.vercel.app.md", ref_index)

        landscape = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Ten Billion Years (Opus 5) - **audited**", landscape)


    def test_design_intelligence_voxai_full_site_contract(self) -> None:
        module = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "design-intelligence"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Integration Detail as Implementation Proof",
            "Route-Family Binding Integrity",
        ):
            self.assertIn(phrase, module)
        self.assertEqual(module.count("## Prompt-to-Experience Compile Contract"), 1)

        frontend_qa = (
            SKILL_ROOT
            / "references"
            / "modules"
            / "frontend-qa"
            / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Route-Family Binding Integrity",
            "same CMS record",
            "duplicate-content canary",
        ):
            self.assertIn(phrase, frontend_qa)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "voxai.framer.ai.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "VoxAI",
            "https://voxai.framer.ai/",
            "2026-10-07",
            "Coverage: 36/36 sitemap URLs + /404 utility route",
            "6 case-study detail pages",
            "8 blog detail pages",
            "13 integration detail pages",
            "5 canonical integration records",
            "8 residue/copy integration routes",
            "Framer a050651",
            "Cal Sans",
            "Inter Display",
            "Poppins",
            "#030014",
            "#0f63b8",
            "#f73e9e",
            "1200px",
            "800px",
            "64px",
            "36px",
            "390x844",
            "no document-level horizontal overflow",
            "Integration Detail as Implementation Proof",
            "Route-Family Binding Integrity",
            "Template Residue Quarantine",
            "Responsive Fidelity Substitution",
            "y1kjVqQmzBxCWoHALMC2UwTOFPU.mp4",
            "8qsenQIIXYW3mI4IYIYBv9PMtkU.mp4",
            "Automating 24/7 Identity Verification and Fraud Triage with Voice AI",
            "Twilio Elastic SIP Trunking",
            "HubSpot CRM",
            "Bridging Design & Development",
        ):
            self.assertIn(phrase, profile)

        ref_index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("voxai.framer.ai.md", ref_index)

        landscape = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        self.assertIn("VoxAI (Framer template) - **audited**", landscape)

    def test_design_intelligence_tobi_mallory_full_site_contract(self) -> None:
        module = (
            SKILL_ROOT / "references" / "modules" / "design-intelligence" / "module.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "World Metaphor as Information Architecture",
            "Taxonomy as Visual Physics",
            "Mnemonic Case-Study Encoding",
            "Metaphor Translation Contract",
        ):
            self.assertIn(phrase, module)

        profile = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "sites"
            / "tobi-mallory.framer.website.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "Tobi Mallory",
            "https://tobi-mallory.framer.website/",
            "2026-10-07",
            "Coverage: 30/30 sitemap URLs",
            "7 Fieldbook detail pages",
            "6 Type detail pages",
            "4 Journal detail pages",
            "3 Quest detail pages",
            "Framer d485f69",
            "Bricolage Grotesque",
            "Space Mono",
            "#fff6e8",
            "#1e1838",
            "810px",
            "1200px",
            "239 runtime animations",
            "390x844",
            "no document-level horizontal overflow",
            "World Metaphor as Information Architecture",
            "Taxonomy as Visual Physics",
            "Mnemonic Case-Study Encoding",
            "Metaphor Translation Contract",
            "Bezzle",
            "Curvix",
            "eternal-fade-087901.framer.app",
            "canonical-host drift",
        ):
            self.assertIn(phrase, profile)

        skin = (
            SKILL_ROOT
            / "references"
            / "design-intelligence"
            / "skins"
            / "whimsical-world-portfolio.md"
        ).read_text(encoding="utf-8")
        for phrase in (
            "tobi-mallory.framer.website.md",
            "World Metaphor as Information Architecture",
            "Taxonomy as Visual Physics",
            "Mnemonic Case-Study Encoding",
            "Metaphor Translation Contract",
        ):
            self.assertIn(phrase, skin)

        ref_index = (SKILL_ROOT / "references" / "index.md").read_text(encoding="utf-8")
        self.assertIn("tobi-mallory.framer.website.md", ref_index)

        landscape = (
            SKILL_ROOT / "references" / "design-intelligence" / "reference-landscape.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Tobi Mallory (Framer portfolio) - **audited**", landscape)

    def test_distilled_web_toolkit_contract(self) -> None:
        import csv
        import subprocess
        import sys

        manifest = json.loads((SKILL_ROOT / "skill.json").read_text(encoding="utf-8"))
        self.assertIn("distilled-web-toolkit", manifest["modules"])

        module_root = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit"
        module = (module_root / "module.md").read_text(encoding="utf-8")
        for phrase in (
            "Distilled Web Toolkit",
            "Audited Pattern Retrieval",
            "Provenance Before Prescription",
            "Pattern Composition Contract",
            "Live Snapshot vs Audited Profile",
            "Audited Design-System Retrieval",
            "Component Recipes",
        ):
            self.assertIn(phrase, module)

        data_root = module_root / "data"
        with (data_root / "sites.csv").open(encoding="utf-8", newline="") as f:
            sites = list(csv.DictReader(f))
        with (data_root / "patterns.csv").open(encoding="utf-8", newline="") as f:
            patterns = list(csv.DictReader(f))
        with (data_root / "route-recipes.csv").open(encoding="utf-8", newline="") as f:
            routes = list(csv.DictReader(f))
        with (data_root / "motion-recipes.csv").open(encoding="utf-8", newline="") as f:
            motions = list(csv.DictReader(f))
        with (data_root / "responsive-recipes.csv").open(encoding="utf-8", newline="") as f:
            responsive = list(csv.DictReader(f))
        with (data_root / "anti-patterns.csv").open(encoding="utf-8", newline="") as f:
            anti = list(csv.DictReader(f))
        with (data_root / "live-audit-2026-10-07.csv").open(encoding="utf-8", newline="") as f:
            live = list(csv.DictReader(f))
        with (data_root / "design-profiles.csv").open(encoding="utf-8-sig", newline="") as f:
            design_profiles = list(csv.DictReader(f))
        with (data_root / "color-systems.csv").open(encoding="utf-8-sig", newline="") as f:
            color_systems = list(csv.DictReader(f))
        with (data_root / "typography-systems.csv").open(encoding="utf-8-sig", newline="") as f:
            typography_systems = list(csv.DictReader(f))
        with (data_root / "component-recipes.csv").open(encoding="utf-8-sig", newline="") as f:
            components = list(csv.DictReader(f))
        with (data_root / "ux-guidelines.csv").open(encoding="utf-8-sig", newline="") as f:
            ux_guidelines = list(csv.DictReader(f))
        with (data_root / "design-primitives-live-2026-10-07.csv").open(encoding="utf-8-sig", newline="") as f:
            design_live = list(csv.DictReader(f))

        self.assertEqual(len(sites), 12)
        self.assertEqual(len(live), 12)
        self.assertGreaterEqual(len(patterns), 70)
        self.assertGreaterEqual(len(routes), 20)
        self.assertGreaterEqual(len(motions), 15)
        self.assertGreaterEqual(len(responsive), 20)
        self.assertGreaterEqual(len(anti), 20)
        self.assertEqual(len(design_profiles), 12)
        self.assertEqual(len(color_systems), 12)
        self.assertEqual(len(typography_systems), 12)
        self.assertEqual(len(components), 36)
        self.assertEqual(len(ux_guidelines), 24)
        self.assertEqual(len(design_live), 12)

        specs = sorted((module_root / "specs").glob("*.md"))
        self.assertEqual(len(specs), 12)

        expected_ids = {
            "refokus",
            "resend",
            "rockstar-vi",
            "tokenmeter",
            "novaos",
            "powder",
            "nudge-folio",
            "orbai",
            "nexira",
            "ten-billion-years",
            "voxai",
            "tobi-mallory",
        }
        self.assertEqual({row["site_id"] for row in sites}, expected_ids)
        self.assertEqual({row["site_id"] for row in live}, expected_ids)
        self.assertEqual({row["site_id"] for row in design_profiles}, expected_ids)
        self.assertEqual({row["site_id"] for row in color_systems}, expected_ids)
        self.assertEqual({row["site_id"] for row in typography_systems}, expected_ids)
        self.assertEqual({row["site_id"] for row in design_live}, expected_ids)
        self.assertEqual({row["site_id"] for row in components}, expected_ids)
        self.assertEqual({row["site_id"] for row in ux_guidelines}, expected_ids)

        search_script = SKILL_ROOT / "scripts" / "distilled_toolkit_search.py"
        result = subprocess.run(
            [sys.executable, str(search_script), "integration setup proof", "--domain", "proof", "--json"],
            cwd=str(SKILL_ROOT), capture_output=True, text=True, check=True,
        )
        self.assertIn("Integration Detail as Implementation Proof", result.stdout)
        self.assertIn("voxai", result.stdout)

        result = subprocess.run(
            [sys.executable, str(search_script), "sticky portfolio case study", "--site", "nudge-folio", "--json"],
            cwd=str(SKILL_ROOT), capture_output=True, text=True, check=True,
        )
        self.assertIn("Persistent Context Rail", result.stdout)

        result = subprocess.run(
            [sys.executable, str(search_script), "particle scroll narrative", "--site", "ten-billion-years", "--json"],
            cwd=str(SKILL_ROOT), capture_output=True, text=True, check=True,
        )
        self.assertIn("Shared Progress Bus", result.stdout)

        result = subprocess.run(
            [sys.executable, str(search_script), "world metaphor portfolio", "--site", "tobi-mallory", "--json"],
            cwd=str(SKILL_ROOT), capture_output=True, text=True, check=True,
        )
        self.assertIn("World Metaphor as Information Architecture", result.stdout)

        result = subprocess.run(
            [sys.executable, str(search_script), "developer api code", "--domain", "typography", "--json"],
            cwd=str(SKILL_ROOT), capture_output=True, text=True, check=True,
        )
        self.assertIn("resend Typography System", result.stdout)
        self.assertIn("Commit Mono", result.stdout)

        result = subprocess.run(
            [sys.executable, str(search_script), "comparison table data", "--domain", "component", "--site", "tokenmeter", "--json"],
            cwd=str(SKILL_ROOT), capture_output=True, text=True, check=True,
        )
        self.assertIn("Sticky Comparison Table", result.stdout)

        result = subprocess.run(
            [sys.executable, str(search_script), "hover touch portfolio", "--domain", "ux", "--site", "tobi-mallory", "--json"],
            cwd=str(SKILL_ROOT), capture_output=True, text=True, check=True,
        )
        self.assertIn("Hover-dependent collection cards", result.stdout)

        result = subprocess.run(
            [sys.executable, str(search_script), "developer api code", "--design-system", "--json"],
            cwd=str(SKILL_ROOT), capture_output=True, text=True, check=True,
        )
        self.assertIn('"source_site": "resend"', result.stdout)
        self.assertIn("Commit Mono", result.stdout)


if __name__ == "__main__":
    unittest.main()

