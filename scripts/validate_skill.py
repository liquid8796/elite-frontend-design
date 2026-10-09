#!/usr/bin/env python3
"""Validate Elite Frontend Design structural invariants."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "elite-frontend-design"
MANIFEST = SKILL_ROOT / "skill.json"
MODULE_ROOT = SKILL_ROOT / "references" / "modules"
PLUGIN_MANIFEST = ROOT / "plugin.json"
CODEX_MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
SKILL_AGENT = SKILL_ROOT / "agents" / "openai.yaml"
REQUIRED_CORE_MODULES = {
    "elite-core",
    "reference-first",
    "design-intelligence",
    "visual-qa",
    "frontend-qa",
    "motion-direction",
}


def _load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def _root_skill_name() -> str:
    path = SKILL_ROOT / "SKILL.md"
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8")
    match = re.search(r"(?m)^name:\s*([^\n]+)$", text)
    return match.group(1).strip().strip('"').strip("'") if match else ""


def validate() -> list[str]:
    errors: list[str] = []

    for required in ("plugin.json", "README.md", "CHANGELOG.md", "LICENSE"):
        if not (ROOT / required).is_file():
            errors.append(f"Missing root {required}")

    for required in ("SKILL.md", "skill.json", "agents/openai.yaml"):
        if not (SKILL_ROOT / required).is_file():
            errors.append(f"Missing skill payload {required}")

    if not CODEX_MANIFEST.is_file():
        errors.append("Missing .codex-plugin/plugin.json compatibility manifest")

    if errors and not MANIFEST.is_file():
        return errors

    if not MANIFEST.is_file():
        return errors + ["Missing skill.json"]

    manifest = _load_manifest()

    try:
        plugin = json.loads(PLUGIN_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid plugin.json: {exc}")
        plugin = {}

    try:
        codex = json.loads(CODEX_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid .codex-plugin/plugin.json: {exc}")
        codex = {}

    if plugin.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("plugin.json must use the Agent Plugins 1.0.0 schema")

    for label, value in (("plugin.json", plugin), ("Codex manifest", codex)):
        if value.get("name") != "elite-frontend-design":
            errors.append(f"{label} has unexpected name: {value.get('name')!r}")

    if codex.get("skills") != "./skills/":
        errors.append("Codex manifest must declare skills: './skills/'")

    interface = (
        plugin.get("extensions", {})
        .get("com.openai", {})
        .get("interface", {})
    )
    if interface.get("displayName") != "Elite Frontend Design":
        errors.append("plugin.json OpenAI interface has unexpected displayName")
    if not interface.get("developerName"):
        errors.append("plugin.json OpenAI interface is missing developerName")
    if interface.get("category") != "Developer Tools":
        errors.append("plugin.json OpenAI interface must use Developer Tools category")
    for field, expected_path in (
        ("composerIcon", "./assets/icon.svg"),
        ("logo", "./assets/logo.svg"),
    ):
        if interface.get(field) != expected_path:
            errors.append(f"plugin.json OpenAI interface has unexpected {field}")
        asset = ROOT / expected_path.removeprefix("./")
        if not asset.is_file():
            errors.append(f"Missing plugin branding asset: {expected_path}")

    agent_text = SKILL_AGENT.read_text(encoding="utf-8") if SKILL_AGENT.is_file() else ""
    for phrase in (
        'display_name: "Elite Frontend Design"',
        'short_description: "Design and QA frontend UI"',
        "- CHAT",
        "- CODEX",
        "allow_implicit_invocation: true",
    ):
        if phrase not in agent_text:
            errors.append(f"agents/openai.yaml missing required plugin metadata: {phrase}")

    if manifest.get("name") != "elite-frontend-design":
        errors.append(f"Unexpected manifest name: {manifest.get('name')!r}")

    if _root_skill_name() != "elite-frontend-design":
        errors.append(f"Unexpected SKILL.md name: {_root_skill_name()!r}")

    modules = manifest.get("modules", [])
    expected = set(modules)

    if len(modules) != len(expected):
        errors.append("skill.json contains duplicate module names")

    missing_core = REQUIRED_CORE_MODULES - expected
    if missing_core:
        errors.append(f"Missing required core modules in manifest: {sorted(missing_core)}")

    actual = (
        {p.name for p in MODULE_ROOT.iterdir() if p.is_dir()}
        if MODULE_ROOT.is_dir()
        else set()
    )
    if actual != expected:
        errors.append(
            f"Module registry mismatch: expected={sorted(expected)} actual={sorted(actual)}"
        )

    for name in sorted(expected):
        module_dir = MODULE_ROOT / name
        if not (module_dir / "module.md").is_file():
            errors.append(f"{name}: missing module.md")

    nested_skill_files = (
        list(MODULE_ROOT.rglob("SKILL.md")) if MODULE_ROOT.exists() else []
    )
    if nested_skill_files:
        errors.append(
            "Nested SKILL.md files remain: "
            + ", ".join(str(p.relative_to(ROOT)) for p in nested_skill_files)
        )

    if not (SKILL_ROOT / "references" / "index.md").is_file():
        errors.append("Missing references/index.md")

    if not (SKILL_ROOT / "references" / "source-map.md").is_file():
        errors.append("Missing references/source-map.md")

    if not (SKILL_ROOT / "references" / "source-snapshots.md").is_file():
        errors.append("Missing references/source-snapshots.md")

    design_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "refokus.com.md"
    if not design_profile.is_file():
        errors.append("Missing Refokus design-intelligence profile")
    else:
        profile_text = design_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://www.refokus.com/",
            "Coverage: 121/121",
            "46 project",
            "34 article",
            "WebGLRenderer",
            "EffectComposer",
            "Service Narrative Landing System",
            "Evidence-Dependent Case Depth",
            "Refokus Webflow Tools",
            "Canonical/Language Route Invariant",
        ):
            if phrase not in profile_text:
                errors.append(f"Refokus design-intelligence profile missing phrase: {phrase}")

    tools_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "webflow-tools.refokus.com.md"
    if not tools_profile.is_file():
        errors.append("Missing Refokus Webflow Tools design-intelligence profile")
    else:
        tools_text = tools_profile.read_text(encoding="utf-8-sig")
        for phrase in (
            "19/19 sitemap URLs",
            "Copy -> Configure -> Verify Documentation",
            "Public Implementation Styleguide as Product Trust",
            "Manrope",
            "IBM Plex Mono",
            "canonical",
            "html lang",
        ):
            if phrase not in tools_text:
                errors.append(f"Refokus Tools design-intelligence profile missing phrase: {phrase}")

    resend_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "resend.com.md"
    if not resend_profile.is_file():
        errors.append("Missing Resend design-intelligence profile")
    else:
        profile_text = resend_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://resend.com/",
            "cube.splinecode",
            "cube.mp4",
            "Product Evidence Before Feature Claims",
            "Code as Product Proof",
            "Responsive Fidelity Substitution",
            "Functional Tabs as Persuasion",
            "Whole-Site Re-Audit",
            "1,015",
            "Three-Rail Documentation Reader",
            "Migration Converter Bridge",
            "Public Operating System as Trust Proof",
        ):
            if phrase not in profile_text:
                errors.append(f"Resend design-intelligence profile missing phrase: {phrase}")

    resend_inventory = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit" / "data" / "resend-route-inventory-2026-10-08.csv"
    if not resend_inventory.is_file():
        errors.append("Missing complete Resend route inventory")
    else:
        with resend_inventory.open(encoding="utf-8", newline="") as f:
            resend_rows = list(csv.DictReader(f))
        if len(resend_rows) != 1015:
            errors.append(f"Resend inventory expected 1015 sitemap URLs, found {len(resend_rows)}")
        if sum(r["http_status"] == "200" for r in resend_rows) != 1014:
            errors.append("Resend inventory expected 1014 HTTP 200 routes")
        if not any(r["url"] == "https://resend.com/shop" and r["http_status"] == "404" for r in resend_rows):
            errors.append("Resend inventory missing the observed /shop 404 regression")

    battlez_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "battlez-template.framer.website.md"
    if not battlez_profile.is_file():
        errors.append("Missing full-site Battlez design-intelligence profile")
    else:
        battlez_text = battlez_profile.read_text(encoding="utf-8")
        for phrase in (
            "75/75",
            "53",
            "Game Discovery -> Marketplace Bridge",
            "Cross-Vertical CMS Fixture Leak",
            "Battlez - Gaming Framer Template",
            "390x9441",
        ):
            if phrase not in battlez_text:
                errors.append(f"Battlez design-intelligence profile missing phrase: {phrase}")

    battlez_inventory = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit" / "data" / "battlez-route-inventory-2026-10-08.csv"
    if not battlez_inventory.is_file():
        errors.append("Missing Battlez full sitemap inventory")
    else:
        with battlez_inventory.open(encoding="utf-8", newline="") as f:
            battlez_rows = list(csv.DictReader(f))
        if len(battlez_rows) != 75:
            errors.append(f"Battlez inventory expected 75 URLs, found {len(battlez_rows)}")
        if sum(r["http_status"] == "200" for r in battlez_rows) != 74:
            errors.append("Battlez inventory expected 74 HTTP 200 routes")
        if not any(r["url"].endswith("/404") and r["http_status"] == "404" for r in battlez_rows):
            errors.append("Battlez inventory missing deliberate /404 status")
        if len({r["title"] for r in battlez_rows}) != 1:
            errors.append("Battlez audit drift: expected captured site-wide duplicate title")

    nouva_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "nouva-template.framer.website.md"
    if not nouva_profile.is_file():
        errors.append("Missing complete Nouva design-intelligence profile")
    else:
        nouva_text = nouva_profile.read_text(encoding="utf-8")
        for phrase in (
            "8/8 sitemap URLs",
            "FrameAuth",
            "Scroll-triggered metric reveal",
            "Contact-First SaaS Conversion",
            "390x15559",
        ):
            if phrase not in nouva_text:
                errors.append(f"Nouva profile missing whole-site evidence: {phrase}")

    nouva_inventory = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit" / "data" / "nouva-route-inventory-2026-10-08.csv"
    if not nouva_inventory.is_file():
        errors.append("Missing Nouva complete route inventory")
    else:
        with nouva_inventory.open(encoding="utf-8", newline="") as f:
            nouva_rows = list(csv.DictReader(f))
        if len(nouva_rows) != 9:
            errors.append(f"Nouva inventory expected 8 sitemap + 1 linked 404, found {len(nouva_rows)}")
        if sum(r["http_status"] == "200" and r["sitemap_declared"] == "true" for r in nouva_rows) != 8:
            errors.append("Nouva declared sitemap should contain 8 HTTP 200 pages")
        if not any(r["url"].endswith("/404") and r["http_status"] == "404" and r["sitemap_declared"] == "false" for r in nouva_rows):
            errors.append("Nouva linked 404 should return 404 outside sitemap")

    fizens_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "fizens.framer.ai.md"
    if not fizens_profile.is_file():
        errors.append("Missing Fizens entire-site finance template deep profile")
    else:
        fizens_text = fizens_profile.read_text(encoding="utf-8")
        for phrase in (
            "43/43 sitemap URLs",
            "21 of 43 sitemap URLs",
            "four",
            "Product Designer",
            "390x19177",
            "Template Vendor and End User Surface Firewall",
        ):
            if phrase not in fizens_text:
                errors.append(f"Fizens full-site profile missing phrase: {phrase}")

    fizens_data = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit" / "data"
    inventory = fizens_data / "fizens-route-inventory-2026-10-08.csv"
    rendered = fizens_data / "fizens-rendered-states-2026-10-08.csv"
    careers = fizens_data / "fizens-career-title-audit-2026-10-08.csv"
    if not inventory.is_file() or not rendered.is_file() or not careers.is_file():
        errors.append("Missing complete Fizens sitemap/rendered/career audit inventory")
    else:
        with inventory.open(encoding="utf-8", newline="") as f:
            fizens_routes = list(csv.DictReader(f))
        with rendered.open(encoding="utf-8", newline="") as f:
            fizens_states = list(csv.DictReader(f))
        with careers.open(encoding="utf-8", newline="") as f:
            fizens_jobs = list(csv.DictReader(f))
        declared = [r for r in fizens_routes if r["sitemap_declared"] == "true"]
        if len(fizens_routes) != 47 or len(declared) != 43 or any(x["http_status"] != "200" for x in declared):
            errors.append("Fizens must have 43 sitemap 200 and 4 sampled 404 rows")
        if len(fizens_states) != 32 or any(int(x["outer_overflow"]) > 0 for x in fizens_states):
            errors.append("Fizens requires 32 overflow-free rendered route states")
        if len(fizens_jobs) != 4 or sum(x["mismatch"] == "true" for x in fizens_jobs) != 3:
            errors.append("Fizens career identity QA expected 3 mismatches among 4 job routes")




    spector_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "spector.framer.website.md"
    spector_data = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit" / "data"
    sp_files = (
        spector_data / "spector-route-inventory-2026-10-09.csv",
        spector_data / "spector-internal-links-2026-10-09.csv",
        spector_data / "spector-rendered-states-2026-10-09.csv",
        spector_data / "spector-interaction-probes-2026-10-09.csv",
    )
    if not spector_profile.is_file() or not all(f.is_file() for f in sp_files):
        errors.append("Spector full-site profile or four route/link/render/interaction files missing")
    else:
        text = spector_profile.read_text(encoding="utf-8-sig")
        for phrase in ("19/19", "Plus Jakarta Sans", "Case Archive vs Hidden Detail Parity", "All **19 official pages"):
            if phrase not in text:
                errors.append(f"Spector profile missing audited principle: {phrase}")
        with sp_files[0].open(encoding="utf-8-sig", newline="") as f:
            sp_routes = list(csv.DictReader(f))
        with sp_files[1].open(encoding="utf-8-sig", newline="") as f:
            sp_links = list(csv.DictReader(f))
        with sp_files[2].open(encoding="utf-8-sig", newline="") as f:
            sp_states = list(csv.DictReader(f))
        with sp_files[3].open(encoding="utf-8-sig", newline="") as f:
            sp_probes = list(csv.DictReader(f))
        published = [r for r in sp_routes if r["sitemap_declared"] == "true"]
        extras = [r for r in sp_routes if r["sitemap_declared"] == "false"]
        if len(sp_routes) != 29 or len(published) != 19 or any(r["status"] != "200" for r in published):
            errors.append("Spector expected 19 sitemap-declared HTTP 200 and ten extra path probes")
        if len(extras) != 10 or any(r["status"] != "404" for r in extras):
            errors.append("Spector expected ten HTTP 404 supplementary paths")
        for fam,count in (("projects-detail",6),("lab-detail",5),("legal",3)):
            if sum(r["family"] == fam for r in published) != count:
                errors.append(f"Spector missing {fam} routes (expected {count})")
        broken_sources = {r["source"] for r in sp_links if r["target"] == "https://spector.framer.website/instagram.com"}
        if broken_sources != {r["url"] for r in published}:
            errors.append("Spector malformed social href should appear across all 19 audited pages")
        if len(sp_states) != 40 or any(r.get("error") or int(r["overflow"]) > 0 for r in sp_states):
            errors.append("Spector expected 40 error-free dual-viewport Chromium states without outer overflow")
        if len(sp_probes) != 11:
            errors.append("Spector expected eleven bounded UI/semantics observations")

    arpeggio_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "arpeggio.framer.website.md"
    arpeggio_data = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit" / "data"
    ar_files = (
        arpeggio_data / "arpeggio-route-inventory-2026-10-09.csv",
        arpeggio_data / "arpeggio-internal-links-2026-10-09.csv",
        arpeggio_data / "arpeggio-rendered-states-2026-10-09.csv",
        arpeggio_data / "arpeggio-interaction-probes-2026-10-09.csv",
    )
    if not arpeggio_profile.is_file() or not all(f.is_file() for f in ar_files):
        errors.append("Arpeggio full-site profile or four route/link/render/interaction ledgers missing")
    else:
        text = arpeggio_profile.read_text(encoding="utf-8-sig")
        for phrase in ("22/22", "Inter Display", "Template Vendor Firewall", "Budget-First Qualified Contact"):
            if phrase not in text:
                errors.append(f"Arpeggio profile missing audited principle: {phrase}")
        with ar_files[0].open(encoding="utf-8-sig", newline="") as f:
            ar_routes = list(csv.DictReader(f))
        with ar_files[2].open(encoding="utf-8-sig", newline="") as f:
            ar_states = list(csv.DictReader(f))
        with ar_files[3].open(encoding="utf-8-sig", newline="") as f:
            ar_probes = list(csv.DictReader(f))
        published = [r for r in ar_routes if r["sitemap_declared"] == "true"]
        supplemental = [r for r in ar_routes if r["sitemap_declared"] == "false"]
        if len(ar_routes) != 30 or len(published) != 22 or any(r["status"] != "200" for r in published):
            errors.append("Arpeggio census expected 22 declared 200 and 8 supplemental paths")
        if len(supplemental) != 8 or any(r["status"] != "404" for r in supplemental):
            errors.append("Arpeggio supplementary paths expected eight HTTP 404")
        for fam,count in (("work-detail",7),("journal-detail",7),("legal",3)):
            if sum(r["family"] == fam for r in published) != count:
                errors.append(f"Arpeggio sitemap requires {count} {fam} routes")
        if len(ar_states) != 46 or any(r.get("error") or int(r["overflow"]) > 0 for r in ar_states):
            errors.append("Arpeggio required 46 overflow-free Chromium route states")
        if len(ar_probes) != 10:
            errors.append("Arpeggio required ten bounded interaction observations")

    bridgemind_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "bridgemind.ai.md"
    bridgemind_data = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit" / "data"
    bm_inv = bridgemind_data / "bridgemind-route-inventory-2026-10-09.csv"
    bm_links = bridgemind_data / "bridgemind-internal-links-2026-10-09.csv"
    bm_render = bridgemind_data / "bridgemind-rendered-states-2026-10-09.csv"
    bm_actions = bridgemind_data / "bridgemind-interaction-probes-2026-10-09.csv"
    if not bridgemind_profile.is_file() or not all(p.is_file() for p in (bm_inv, bm_links, bm_render, bm_actions)):
        errors.append("Missing BridgeMind full 153-route website/docs inventory or rendered interaction evidence")
    else:
        bp = bridgemind_profile.read_text(encoding="utf-8-sig")
        for marker in ("153/153", "BridgeVoice", "BridgeVerse", "Cross-Host Capability Claim Invariant"):
            if marker not in bp:
                errors.append(f"BridgeMind profile missing evidence: {marker}")
        with bm_inv.open(encoding="utf-8-sig", newline="") as f:
            bm_urls = list(csv.DictReader(f))
        with bm_render.open(encoding="utf-8-sig", newline="") as f:
            bm_states = list(csv.DictReader(f))
        with bm_actions.open(encoding="utf-8-sig", newline="") as f:
            bm_probes = list(csv.DictReader(f))
        declared = [x for x in bm_urls if x["sitemap_source"] in ("www.bridgemind.ai", "docs.bridgemind.ai")]
        if len(bm_urls) != 165 or len(declared) != 153 or any(x["status"] != "200" for x in declared):
            errors.append("BridgeMind must preserve 153 verified sitemap routes plus 12 extra path probes")
        if sum(x["sitemap_source"] == "www.bridgemind.ai" for x in declared) != 143:
            errors.append("BridgeMind main-host sitemap expected 143 routes")
        if sum(x["sitemap_source"] == "docs.bridgemind.ai" for x in declared) != 10:
            errors.append("BridgeMind companion docs sitemap expected 10 routes")
        if sum(x["route_family"] == "changelog-detail" for x in declared) != 120:
            errors.append("BridgeMind release history expected 120 detail routes")
        if len(bm_states) != 46 or any(x.get("error") or int(x["overflow"]) > 0 for x in bm_states):
            errors.append("BridgeMind Chromium evidence expected 46 rendered overflow-free states")
        if len(bm_probes) != 13:
            errors.append("BridgeMind requires 13 limited interaction probes")

    tobi_data = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit" / "data"
    tobi_routes_path = tobi_data / "tobi-dual-host-routes-2026-10-08.csv"
    tobi_rendered_path = tobi_data / "tobi-rendered-states-2026-10-08.csv"
    tobi_quests_path = tobi_data / "tobi-quest-contact-state-2026-10-08.csv"
    if not all(p.is_file() for p in (tobi_routes_path, tobi_rendered_path, tobi_quests_path)):
        errors.append("Missing Tobi Mallory full-site dual-host/rendered/service-intent evidence")
    else:
        with tobi_routes_path.open(encoding="utf-8", newline="") as f:
            tobi_routes = list(csv.DictReader(f))
        with tobi_rendered_path.open(encoding="utf-8", newline="") as f:
            tobi_rendered = list(csv.DictReader(f))
        with tobi_quests_path.open(encoding="utf-8", newline="") as f:
            tobi_quests = list(csv.DictReader(f))
        declared = [x for x in tobi_routes if x["declared_sitemap"] == "true"]
        if len(tobi_routes) != 62 or len(declared) != 60:
            errors.append("Tobi dual-host census requires 60 sitemap and 2 extra invalid HTTP checks")
        if sum(x["http_status"] == "200" for x in declared) != 58 or sum(x["http_status"] == "404" for x in declared) != 2:
            errors.append("Tobi census requires 29 content 200 and one authored 404 per host")
        if sum(x["host"] == "https://tobi-mallory.framer.website" and x["canonical"].startswith("https://eternal-fade-087901.framer.app") for x in declared) != 30:
            errors.append("Tobi all 30 browsed-host canonicals must be recorded as source-host drift")
        if len(tobi_rendered) != 30 or any(int(x["outer_overflow"]) > 0 for x in tobi_rendered):
            errors.append("Tobi Chrome render evidence requires 30 overflow-free route states")
        if len(tobi_quests) != 3 or sum(x["preserved"] == "false" for x in tobi_quests) != 2:
            errors.append("Tobi commercial CTA evidence requires 2 of 3 lost-service cases")

    rockstar_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "rockstargames.com-vi.md"
    if not rockstar_profile.is_file():
        errors.append("Missing Rockstar Games VI design-intelligence profile")
    else:
        profile_text = rockstar_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://www.rockstargames.com/VI",
            "ArtDecoBold",
            "HeroBackground",
            "TriggerHeadline",
            "Aspect-Ratio Art Direction",
            "World-Led Campaign Chapters",
            "back-of-box",
            "user-scalable=no",
        ):
            if phrase not in profile_text:
                errors.append(f"Rockstar Games VI profile missing phrase: {phrase}")

    tokenmeter_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "tokenmeter.info.md"
    if not tokenmeter_profile.is_file():
        errors.append("Missing Tokenmeter full-site design-intelligence profile")
    else:
        profile_text = tokenmeter_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://tokenmeter.info/",
            "Coverage: 26/26 sitemap URLs",
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
        ):
            if phrase not in profile_text:
                errors.append(f"Tokenmeter design-intelligence profile missing phrase: {phrase}")

    novaos_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "novaos.framer.website.md"
    if not novaos_profile.is_file():
        errors.append("Missing NovaOS full-site design-intelligence profile")
    else:
        profile_text = novaos_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://novaos.framer.website/",
            "Coverage: 23/23 sitemap URLs",
            "6 career detail pages",
            "6 blog article pages",
            "Framer 95da0c7",
            "DM Sans Variable",
            "Geist",
            "#0082de",
            "Lenis 1.3.26",
            "lerp: 0.085",
            "Operational Pipeline Storytelling",
            "Proof Surface Cropping",
            "Credibility Through Route Ecosystem",
            "Get This Template",
        ):
            if phrase not in profile_text:
                errors.append(f"NovaOS design-intelligence profile missing phrase: {phrase}")

    powder_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "powder.framer.website.md"
    if not powder_profile.is_file():
        errors.append("Missing Powder full-site design-intelligence profile")
    else:
        profile_text = powder_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://powder.framer.website/",
            "Coverage: 21/21 sitemap URLs",
            "10 blog detail pages",
            "Framer a050651",
            "Fragment Mono",
            "Inter Variable",
            "Inter Display",
            "#000912",
            "#d39794",
            "#177275",
            "Conversation-to-Action Proof",
            "Template Residue Quarantine",
            "Sticky Capability Stack",
            "Remix for free",
        ):
            if phrase not in profile_text:
                errors.append(f"Powder design-intelligence profile missing phrase: {phrase}")

    nudge_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "nudge-folio.framer.website.md"
    if not nudge_profile.is_file():
        errors.append("Missing Nudge Folio full-site design-intelligence profile")
    else:
        profile_text = nudge_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://nudge-folio.framer.website/",
            "Coverage: 19/19 sitemap URLs",
            "8 blog detail pages",
            "4 case-study detail pages",
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
            "GSAP",
            "Draggable",
            "lenis lenis-autoToggle",
            "Reflective Case Study Arc",
            "Persistent Context Rail",
            "Experimental Surface Isolation",
            "BUY NUDGE",
        ):
            if phrase not in profile_text:
                errors.append(f"Nudge Folio design-intelligence profile missing phrase: {phrase}")

    orbai_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "orbai-template.framer.website.md"
    if not orbai_profile.is_file():
        errors.append("Missing OrbAI full-site design-intelligence profile")
    else:
        profile_text = orbai_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://orbai-template.framer.website/",
            "Coverage: 8/8 sitemap URLs",
            "4 changelog detail pages",
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
            "no document-level horizontal overflow",
            "Get Template",
        ):
            if phrase not in profile_text:
                errors.append(f"OrbAI design-intelligence profile missing phrase: {phrase}")

    nexira_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "nexira.framer.ai.md"
    if not nexira_profile.is_file():
        errors.append("Missing Nexira full-site design-intelligence profile")
    else:
        profile_text = nexira_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://nexira.framer.ai/",
            "Coverage: 28/28 sitemap URLs",
            "7 service detail pages",
            "7 case detail pages",
            "7 blog detail pages",
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
            "350x889",
            "no document-level horizontal overflow",
            "REDDEVS 2024",
        ):
            if phrase not in profile_text:
                errors.append(f"Nexira design-intelligence profile missing phrase: {phrase}")

    cosmos_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "cosmos-10-billion-years-opus5.vercel.app.md"
    if not cosmos_profile.is_file():
        errors.append("Missing Ten Billion Years Opus 5 full-site design-intelligence profile")
    else:
        profile_text = cosmos_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://cosmos-10-billion-years-opus5.vercel.app/",
            "Coverage: 1/1 public route",
            "9 chapters",
            "1029vh",
            "three.js r185",
            "React Three Fiber",
            "Lenis 1.3.25",
            "Instrument Serif",
            "JetBrains Mono",
            "AudioContext",
            "Web Audio",
            "Prompt-to-Experience Compile Contract",
            "Narrative Parameter Matrix",
            "Event Peaks on Continuous Timeline",
            "220,000",
            "110,000",
            "70,000",
            "390x844",
            "no document-level horizontal overflow",
            "prefers-reduced-motion",
            "Full-Site Browser Re-Audit",
            "aria-current",
            "Begin again",
        ):
            if phrase not in profile_text:
                errors.append(f"Ten Billion Years profile missing phrase: {phrase}")

    voxai_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "voxai.framer.ai.md"
    if not voxai_profile.is_file():
        errors.append("Missing VoxAI full-site design-intelligence profile")
    else:
        profile_text = voxai_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://voxai.framer.ai/",
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
            "Automating 24/7 Identity Verification and Fraud Triage with Voice AI",
            "Twilio Elastic SIP Trunking",
            "HubSpot CRM",
            "Bridging Design & Development",
        ):
            if phrase not in profile_text:
                errors.append(f"VoxAI design-intelligence profile missing phrase: {phrase}")

    tobi_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "tobi-mallory.framer.website.md"
    if not tobi_profile.is_file():
        errors.append("Missing Tobi Mallory full-site design-intelligence profile")
    else:
        profile_text = tobi_profile.read_text(encoding="utf-8")
        for phrase in (
            "https://tobi-mallory.framer.website/",
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
            "Project Evolution as Relationship Proof",
            "eternal-fade-087901.framer.app",
            "canonical-host drift",
        ):
            if phrase not in profile_text:
                errors.append(f"Tobi Mallory design-intelligence profile missing phrase: {phrase}")

    indiex_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "indiex.framer.ai.md"
    if not indiex_profile.is_file():
        errors.append("Missing Indiex full-site design-intelligence profile")
    else:
        profile_text = indiex_profile.read_text(encoding="utf-8-sig")
        for phrase in (
            "https://indiex.framer.ai/",
            "Coverage: 2/2 sitemap URLs",
            "Framer befeeaf",
            "Oswald",
            "Inter Display",
            "#0b121d",
            "#94cb53",
            "1440x900",
            "390x844",
            "2 video",
            "Template Residue Firewall",
            "One-Page Studio Conversion Spine",
            "Sticky Game Selector",
            "HTTP 404",
            "gym/fitness",
            "tabindex=0",
        ):
            if phrase not in profile_text:
                errors.append(f"Indiex design-intelligence profile missing phrase: {phrase}")
    echoes_profile = SKILL_ROOT / "references" / "design-intelligence" / "sites" / "ready-material-053719.framer.app.md"
    if not echoes_profile.is_file():
        errors.append("Missing Echoes of Mars full-site design-intelligence profile")
    else:
        profile_text = echoes_profile.read_text(encoding="utf-8-sig")
        for phrase in (
            "https://ready-material-053719.framer.app/",
            "Coverage: 1/1 sitemap URL",
            "Framer c9b3949",
            "Saira Variable",
            "Datatype Variable",
            "#0B0A09",
            "#C9743F",
            "1440x900",
            "390x844",
            "Pinned Sector Survey",
            "Telemetry as Narrative UI",
            "Recovered Footage Proof",
            "47 images",
            "0 video",
            "0 canvas",
            "HOVER TO SURVEY",
            "HTTP 404",
            "Whole-Site Re-Audit",
            "810–1199px",
            "5320px",
            "reduced_motion=reduce",
        ):
            if phrase not in profile_text:
                errors.append(f"Echoes of Mars design-intelligence profile missing phrase: {phrase}")
    echoes_breakpoints = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit" / "data" / "echoes-survey-breakpoints-2026-10-08.csv"
    if not echoes_breakpoints.is_file():
        errors.append("Missing Echoes of Mars three-mode breakpoint evidence")
    else:
        with echoes_breakpoints.open(encoding="utf-8", newline="") as f:
            echo_rows = list(csv.DictReader(f))
        if len(echo_rows) != 9:
            errors.append(f"Echoes viewport census expected 9 states, got {len(echo_rows)}")
        mode_by_width = {int(x["viewport_width"]): x["mode"] for x in echo_rows if x["reduced_motion"] == "no-preference"}
        if mode_by_width.get(809) != "vertical" or mode_by_width.get(810) != "compact-horizontal" or mode_by_width.get(1199) != "compact-horizontal" or mode_by_width.get(1200) != "wide-horizontal":
            errors.append("Echoes responsive mode breakpoints do not match runtime audit")
        if not any(x["reduced_motion"] == "reduce" and x["viewport_position"] == "sticky" and x["track_width"] == "5320" for x in echo_rows):
            errors.append("Echoes reduced-motion source behavior snapshot missing")

    cosmos_data = SKILL_ROOT / "references" / "modules" / "distilled-web-toolkit" / "data"
    routes = cosmos_data / "cosmos-route-census-2026-10-08.csv"
    samples = cosmos_data / "cosmos-runtime-checkpoints-2026-10-08.csv"
    if not routes.is_file() or not samples.is_file():
        errors.append("Missing Ten Billion Years full-site route or runtime audit evidence")
    else:
        with routes.open(encoding="utf-8", newline="") as f:
            cosmos_routes = list(csv.DictReader(f))
        with samples.open(encoding="utf-8", newline="") as f:
            cosmos_samples = list(csv.DictReader(f))
        if len(cosmos_routes) != 8 or len(cosmos_samples) != 11:
            errors.append("Ten Billion Years audit evidence requires 8 route and 11 timeline rows")
        if sum(x["http_status"] == "200" for x in cosmos_routes) != 1:
            errors.append("Ten Billion Years audit root is sole confirmed HTTP 200 route")
        if not any(x["viewport"] == "390x844" and x["hud_chapter"] == "The Swelling" for x in cosmos_samples):
            errors.append("Ten Billion Years mobile runtime milestone missing")

    landscape = SKILL_ROOT / "references" / "design-intelligence" / "reference-landscape.md"
    if not landscape.is_file():
        errors.append("Missing design-intelligence reference landscape")
    else:
        landscape_text = landscape.read_text(encoding="utf-8")
        for phrase in (
            "Candidate, Not Evidence",
            "product precision",
            "experiential / agency",
            "luxury / editorial",
            "game / cinematic",
            "developer product",
            "template commodity",
            "Template Convergence Risk",
        ):
            if phrase not in landscape_text:
                errors.append(f"Reference landscape missing phrase: {phrase}")

    skins_root = SKILL_ROOT / "references" / "design-intelligence" / "skins"
    expected_skins = {
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
    }
    skin_index_path = skins_root / "index.md"
    if not skin_index_path.is_file():
        errors.append("Missing baseline skin index")
    else:
        skin_index_text = skin_index_path.read_text(encoding="utf-8")
        for phrase in (
            "Adaptive Execution Modes",
            "LOCKED",
            "GUIDED",
            "BESPOKE",
            "GUIDED is the default",
            "Task Complexity Score",
            "Design Preflight",
        ):
            if phrase not in skin_index_text:
                errors.append(f"Baseline skin index missing phrase: {phrase}")
    actual_skins = {p.name for p in skins_root.glob("*.md") if p.name != "index.md"} if skins_root.is_dir() else set()
    if actual_skins != expected_skins:
        errors.append(f"Baseline skin set mismatch: {sorted(actual_skins)}")
    for skin_name in sorted(expected_skins):
        skin_path = skins_root / skin_name
        if not skin_path.is_file():
            continue
        skin_text = skin_path.read_text(encoding="utf-8")
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
            if phrase not in skin_text:
                errors.append(f"Baseline skin {skin_name} missing phrase: {phrase}")

    engine = MODULE_ROOT / "ui-ux-pro-max" / "scripts" / "search.py"
    if not engine.is_file():
        errors.append("Missing bundled UI/UX search engine")

    wrapper = SKILL_ROOT / "scripts" / "ui_ux_search.py"
    if not wrapper.is_file():
        errors.append("Missing root UI/UX search facade")


    toolkit_root = MODULE_ROOT / "distilled-web-toolkit"
    toolkit_search = SKILL_ROOT / "scripts" / "distilled_toolkit_search.py"
    if not toolkit_search.is_file():
        errors.append("Missing distilled web toolkit search facade")

    toolkit_data = toolkit_root / "data"
    toolkit_counts = {
        "sites.csv": 18,
        "patterns.csv": 140,
        "route-recipes.csv": 70,
        "motion-recipes.csv": 25,
        "responsive-recipes.csv": 45,
        "anti-patterns.csv": 63,
        "live-audit-2026-10-07.csv": 18,
        "design-profiles.csv": 18,
        "color-systems.csv": 18,
        "typography-systems.csv": 18,
        "component-recipes.csv": 70,
        "ux-guidelines.csv": 54,
        "design-primitives-live-2026-10-07.csv": 18,
    }
    for filename, minimum in toolkit_counts.items():
        path = toolkit_data / filename
        if not path.is_file():
            errors.append(f"Missing distilled web toolkit dataset: {filename}")
            continue
        try:
            with path.open(encoding="utf-8", newline="") as f:
                count = sum(1 for _ in csv.DictReader(f))
        except Exception as exc:
            errors.append(f"Invalid distilled web toolkit dataset {filename}: {exc}")
            continue
        if count < minimum:
            errors.append(f"Distilled web toolkit dataset {filename} has {count} rows; expected >= {minimum}")

    toolkit_module = toolkit_root / "module.md"
    toolkit_module_text = toolkit_module.read_text(encoding="utf-8") if toolkit_module.is_file() else ""
    for phrase in (
        "Audited Design-System Retrieval",
        "Component Recipes",
        "--design-system",
    ):
        if phrase not in toolkit_module_text:
            errors.append(f"Distilled web toolkit module missing phrase: {phrase}")

    try:
        toolkit_search_text = toolkit_search.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"Cannot read distilled toolkit search: {exc}")
        toolkit_search_text = ""
    for phrase in ("--design-system", "--variance", "--motion", "--density", "component-recipes.csv", "ux-guidelines.csv"):
        if phrase not in toolkit_search_text:
            errors.append(f"Distilled toolkit search missing capability: {phrase}")

    toolkit_specs = toolkit_root / "specs"
    if not toolkit_specs.is_dir() or len(list(toolkit_specs.glob("*.md"))) != 21:
        errors.append("Distilled web toolkit must contain exactly 21 standardized site specs")

    version = str(manifest.get("version", ""))
    assembly = str(manifest.get("assemblyVersion", ""))

    if plugin.get("version") != version:
        errors.append(f"plugin.json version must match skill version: {plugin.get('version')} != {version}")
    if codex.get("version") != version:
        errors.append(f"Codex manifest version must match skill version: {codex.get('version')} != {version}")

    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append(f"Invalid semantic version: {version!r}")

    if assembly != f"{version}.0":
        errors.append(
            f"assemblyVersion must equal version + '.0': version={version}, assembly={assembly}"
        )

    readme = (
        (ROOT / "README.md").read_text(encoding="utf-8")
        if (ROOT / "README.md").is_file()
        else ""
    )
    changelog = (
        (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        if (ROOT / "CHANGELOG.md").is_file()
        else ""
    )
    skill = (
        (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        if (SKILL_ROOT / "SKILL.md").is_file()
        else ""
    )

    if version and version not in readme:
        errors.append("README.md does not mention current version")

    if version and version not in changelog:
        errors.append("CHANGELOG.md does not mention current version")

    for phrase in (
        "VARIANCE",
        "MOTION",
        "DENSITY",
        "Rendered Visual QA",
        "Do Not Over-Stack",
        "actual render branch",
        "QA inventory",
        "Full Frontend QA",
        "VERIFIED, PARTIAL or BLOCKED",
        "Ambition Escalation Gate",
        "experience-engineering",
        "authored-world contract",
        "one authoritative progress domain",
        "spec-to-implementation traceability",
        "responsive controls retain accessible names",
        "inspiration distillation",
        "design-intelligence",
        "Adaptive Capability Routing",
        "LOCKED / GUIDED / BESPOKE",
        "Task Complexity Score",
        "Design Preflight",
        "two or more material coherence failures",
        "baseline skin",
        "Audited Website Pattern Toolkit",
        "distilled-web-toolkit",
    ):
        if phrase not in skill:
            errors.append(f"SKILL.md missing core orchestration phrase: {phrase}")

    contract_phrases = {
        "elite-core": ("Existing-Codebase Discipline", "actual render branch", "Diagnose before redesigning", "Fix in place"),
        "reference-first": ("Evidence Hierarchy", "Accepted-reference lock", "Section/state detail references"),
        "design-intelligence": (
            "Distill, Don't Clone",
            "Design DNA",
            "Evidence Confidence",
            "Pattern Promotion",
            "Bounded Immersive Rendering",
            "Responsive Brand Payload",
            "Product Evidence Before Feature Claims",
            "Code as Product Proof",
            "Responsive Fidelity Substitution",
            "Reference Landscape Routing",
            "Template Archetype Firewall",
            "Breadth-to-Depth Funnel",
            "Game/Experiential Audit Lens",
            "Baseline Skin Packs",
            "Skin Lock",
            "Controlled Mutation",
            "Adaptive Capability Routing",
            "Task Complexity Score",
            "Design Preflight",
            "GUIDED is the default",
            "two or more material coherence failures",
            "Skin-Guided Execution",
            "Deterministic Design Scaffolds",
            "Aspect-Ratio Art Direction",
            "World-Led Campaign Chapters",
            "Confidence as Interface",
            "Route-Family Density Ladder",
            "Contain Horizontal Density, Don't Crush It",
            "Human + Machine Surface Parity",
            "Operational Pipeline Storytelling",
            "Proof Surface Cropping",
            "Credibility Through Route Ecosystem",
            "Conversation-to-Action Proof",
            "Template Residue Quarantine",
            "Reflective Case Study Arc",
            "Persistent Context Rail",
            "Experimental Surface Isolation",
            "Commercial Core + Trust Satellites",
            "Pricing-to-Comparison Bridge",
            "Cinematic Without Heavy Rendering",
            "Capability-to-Case Pairing",
            "Prompt-to-Experience Compile Contract",
            "Narrative Parameter Matrix",
            "Event Peaks on Continuous Timeline",
            "Integration Detail as Implementation Proof",
            "Route-Family Binding Integrity",
            "World Metaphor as Information Architecture",
            "Taxonomy as Visual Physics",
            "Mnemonic Case-Study Encoding",
            "Metaphor Translation Contract",
            "Project Evolution as Relationship Proof",
        ),
        "distilled-web-toolkit": (
            "Distilled Web Toolkit",
            "Audited Pattern Retrieval",
            "Provenance Before Prescription",
            "Pattern Composition Contract",
            "Live Snapshot vs Audited Profile",
        ),
        "visual-qa": ("Define the QA Inventory", "Visual Claim Discipline", "Viewport Fit Is a Separate Check", "Mismatch Ledger", "Cross-System Render Parity"),
        "frontend-qa": (
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
            "Route-Family Binding Integrity",
        ),
        "experience-engineering": (
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
        ),
        "scroll-world": (
            "Continuity Contract — Position AND Velocity",
            "Crossfade Is Insurance, Not a Fix",
            "Scroll → Time Mapping",
            "Runtime Lifecycle Is Mandatory",
            "Seam-Focused QA",
            "Ten Billion Years audited real-time anchor",
            "Weighted Narrative Timeline",
            "Shared Progress Bus",
            "Adaptive Renderer Budget",
        ),
    }
    for module, phrases in contract_phrases.items():
        path = MODULE_ROOT / module / "module.md"
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"{module}: missing hardened contract phrase: {phrase}")

    source_map_path = SKILL_ROOT / "references" / "source-map.md"
    source_map = source_map_path.read_text(encoding="utf-8") if source_map_path.is_file() else ""
    for phrase in (
        "Benchmark-only OpenAI frontend-skill snapshot",
        "Local audited website corpus ? Distilled Web Toolkit",
        "playwright-interactive",
        "Actual render branch",
        "Benchmark limitations",
        "Scroll World",
        "position continuity",
        "velocity continuity",
        "Local three-way regression",
        "Opus 5",
        "story physics",
        "Experience Director",
        "experience-engineering",
        "Frontend QA synthesis",
        "daymade/claude-code-skills",
        "practicajs/the-frontend-testing-skill",
        "maxrihter/claude-skill-visual-regression",
        "testdino-hq/playwright-skill",
        "Local Cosmos rerun",
        "synchronization hardening",
    ):
        if phrase.lower() not in source_map.lower():
            errors.append(f"source-map.md missing deep-read provenance phrase: {phrase}")

    snapshots_path = SKILL_ROOT / "references" / "source-snapshots.md"
    snapshots = snapshots_path.read_text(encoding="utf-8") if snapshots_path.is_file() else ""
    if "oso95/scroll-world" not in snapshots or "71cc36d3bb150248ae36a2c552f9cbf88802a79c" not in snapshots:
        errors.append("source-snapshots.md missing pinned scroll-world review commit")

    qa_snapshot_pins = {
        "daymade/claude-code-skills": "72dc01ffe8a99b8be12f1bc8f7a87afb37e2b7bc",
        "practicajs/the-frontend-testing-skill": "ae1b7bc8b58a77d3cd70e1d775fa73ecb8767154",
        "maxrihter/claude-skill-visual-regression": "7fa2ea4fdac37867ba3686ef6936fd791a622fab",
        "testdino-hq/playwright-skill": "400e4256cd22669ad69c18d31d3e5541e4e1c2a3",
    }
    for source, commit in qa_snapshot_pins.items():
        if source not in snapshots or commit not in snapshots:
            errors.append(f"source-snapshots.md missing pinned QA review source: {source}")


    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Elite frontend design validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    manifest = _load_manifest()
    print(
        "Elite frontend design validation OK "
        f"(version={manifest['version']}, assembly={manifest['assemblyVersion']}, "
        f"modules={len(manifest['modules'])})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
