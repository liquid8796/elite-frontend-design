from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "references" / "modules" / "distilled-web-toolkit" / "data"

ALIASES = {
    "sticky": {"pin", "pinned", "rail", "stage", "hold"},
    "case": {"case-study", "project", "portfolio", "outcome"},
    "integration": {"connector", "ecosystem", "setup", "installation"},
    "proof": {"evidence", "result", "code", "implementation", "outcome"},
    "scroll": {"timeline", "scrollytelling", "progress", "sticky"},
    "particle": {"renderer", "world", "webgl", "glsl", "canvas"},
    "mobile": {"responsive", "narrow", "viewport", "breakpoint"},
    "video": {"media", "trailer", "playback"},
    "ai": {"agent", "automation", "model"},
    "developer": {"code", "api", "technical"},
    "data": {"directory", "comparison", "metric", "confidence"},
    "portfolio": {"case", "project", "creative", "studio"},
    "game": {"gaming", "cinematic", "world", "hud"},
    "service": {"agency", "consulting", "pricing", "process"},
    "style": {"visual", "theme", "aesthetic", "art-direction"},
    "color": {"palette", "accent", "contrast", "surface"},
    "font": {"typography", "type", "heading", "mono"},
    "component": {"card", "panel", "navigation", "table", "pricing"},
    "ux": {"accessibility", "interaction", "responsive", "usability"},
}


def tokens(value: str) -> set[str]:
    return set(re.findall(r"[a-z0-9][a-z0-9+.-]*", value.lower()))


def expanded_query(query: str) -> set[str]:
    base = tokens(query)
    out = set(base)
    for term in list(base):
        out.update(ALIASES.get(term, set()))
    return out


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def normalize_records() -> list[dict[str, str]]:
    records: list[dict[str, str]] = []

    for row in read_csv("patterns.csv"):
        records.append({
            "kind": "pattern",
            "id": row["pattern_id"],
            "name": row["name"],
            "domain": row["domain"],
            "archetype": row["archetype"],
            "sites": row["sites"],
            "summary": row["applies_when"],
            "recipe": row["recipe"],
            "avoid": row["avoid"],
            "implementation": row["implementation"],
            "evidence": row["evidence"],
        })

    for row in read_csv("route-recipes.csv"):
        records.append({
            "kind": "route",
            "id": row["recipe_id"],
            "name": row["name"],
            "domain": "route-system",
            "archetype": row["archetype"],
            "sites": row["sites"],
            "summary": row["use_when"],
            "recipe": row["sequence"],
            "avoid": row["notes"],
            "implementation": "",
            "evidence": "high",
        })

    for row in read_csv("motion-recipes.csv"):
        records.append({
            "kind": "motion",
            "id": row["recipe_id"],
            "name": row["name"],
            "domain": "motion",
            "archetype": row["archetype"],
            "sites": row["sites"],
            "summary": row["job"],
            "recipe": row["mechanism"],
            "avoid": "",
            "implementation": row["reduced_motion"],
            "evidence": "high",
        })

    for row in read_csv("responsive-recipes.csv"):
        records.append({
            "kind": "responsive",
            "id": row["recipe_id"],
            "name": row["name"],
            "domain": "responsive",
            "archetype": "",
            "sites": row["sites"],
            "summary": row["transform"],
            "recipe": row["preserve"],
            "avoid": row["avoid"],
            "implementation": "",
            "evidence": "high",
        })

    for row in read_csv("anti-patterns.csv"):
        records.append({
            "kind": "anti-pattern",
            "id": row["anti_id"],
            "name": row["name"],
            "domain": "qa",
            "archetype": "",
            "sites": row["sites"],
            "summary": row["symptom"],
            "recipe": row["replacement"],
            "avoid": row["symptom"],
            "implementation": "",
            "evidence": row["severity"],
        })

    for row in read_csv("design-profiles.csv"):
        records.append({
            "kind": "design-profile",
            "id": f'{row["site_id"]}-design-profile',
            "name": f'{row["name"]} Design Profile',
            "domain": "style",
            "archetype": row["archetype"],
            "sites": row["site_id"],
            "summary": " | ".join([row["product_types"], row["style_keywords"], row["best_for"]]),
            "recipe": " | ".join([row["composition"], row["visual_signature"], row["mobile_strategy"]]),
            "avoid": row["avoid_for"],
            "implementation": row["implementation_checklist"],
            "evidence": row["evidence"],
        })

    for row in read_csv("color-systems.csv"):
        records.append({
            "kind": "color-system",
            "id": f'{row["site_id"]}-color-system',
            "name": f'{row["site_id"]} Color System',
            "domain": "color",
            "archetype": "",
            "sites": row["site_id"],
            "summary": " | ".join([row["mode"], row["background"], row["foreground"], row["accent"], row["secondary_accent"]]),
            "recipe": " | ".join([row["semantic_strategy"], row["contrast_strategy"]]),
            "avoid": "Do not clone observed hex values as a preset.",
            "implementation": row["transfer_rule"],
            "evidence": row["evidence"],
        })

    for row in read_csv("typography-systems.csv"):
        records.append({
            "kind": "typography-system",
            "id": f'{row["site_id"]}-typography-system',
            "name": f'{row["site_id"]} Typography System',
            "domain": "typography",
            "archetype": "",
            "sites": row["site_id"],
            "summary": " | ".join([row["display_font"], row["heading_font"], row["body_font"], row["utility_font"], row["mood_keywords"]]),
            "recipe": " | ".join([row["role_strategy"], row["desktop_scale"], row["mobile_scale"]]),
            "avoid": row["avoid"],
            "implementation": row["transfer_rule"],
            "evidence": row["evidence"],
        })

    for row in read_csv("component-recipes.csv"):
        records.append({
            "kind": "component",
            "id": row["component_id"],
            "name": row["name"],
            "domain": "component",
            "archetype": "",
            "sites": row["site_id"],
            "summary": " | ".join([row["category"], row["job"]]),
            "recipe": " | ".join([row["anatomy"], row["interaction"], row["responsive_strategy"]]),
            "avoid": row["avoid"],
            "implementation": row["accessibility"],
            "evidence": row["evidence"],
        })

    for row in read_csv("ux-guidelines.csv"):
        records.append({
            "kind": "ux-guideline",
            "id": row["guideline_id"],
            "name": row["issue"],
            "domain": "ux",
            "archetype": "",
            "sites": row["site_id"],
            "summary": " | ".join([row["category"], row["platform"], row["issue"]]),
            "recipe": row["do"],
            "avoid": row["dont"],
            "implementation": "",
            "evidence": row["evidence"],
        })

    return records


def score_record(row: dict[str, str], q: set[str], site: str | None, archetype: str | None) -> float:
    weighted_fields = [
        ("name", 5.0),
        ("id", 3.0),
        ("summary", 2.5),
        ("recipe", 2.0),
        ("avoid", 1.25),
        ("implementation", 1.25),
        ("archetype", 1.5),
        ("sites", 1.5),
    ]
    score = 0.0
    for field, weight in weighted_fields:
        score += len(q & tokens(row.get(field, ""))) * weight

    if site and site in row.get("sites", "").split("|"):
        score += 8.0
    if archetype and archetype == row.get("archetype"):
        score += 5.0

    if row.get("evidence") == "high":
        score += 0.4
    elif row.get("evidence") == "medium":
        score += 0.2
    return score


def ranked_records(
    query: str,
    domain: str | None = None,
    site: str | None = None,
    archetype: str | None = None,
    max_results: int = 12,
    kinds: set[str] | None = None,
) -> list[dict[str, str]]:
    q = expanded_query(query)
    records = normalize_records()
    if domain:
        records = [r for r in records if r["domain"] == domain]
    if site:
        records = [r for r in records if site in r["sites"].split("|")]
    if archetype:
        records = [r for r in records if r["archetype"] == archetype]
    if kinds:
        records = [r for r in records if r["kind"] in kinds]

    ranked: list[tuple[float, dict[str, str]]] = []
    for row in records:
        score = score_record(row, q, site, archetype)
        if score > 0 or site or archetype:
            ranked.append((score, row))
    ranked.sort(key=lambda item: (-item[0], item[1]["name"].lower()))
    return [
        dict(row, score=round(score, 2))
        for score, row in ranked[: max(1, max_results)]
    ]


def profile_score(
    row: dict[str, str],
    q: set[str],
    site: str | None,
    archetype: str | None,
    variance: int | None,
    motion: int | None,
    density: int | None,
) -> float:
    fields = [
        ("name", 5.0),
        ("archetype", 4.0),
        ("product_types", 3.5),
        ("style_keywords", 3.0),
        ("theme", 2.0),
        ("composition", 2.0),
        ("visual_signature", 2.0),
        ("best_for", 2.0),
        ("prompt_keywords", 2.5),
        ("mobile_strategy", 1.0),
    ]
    score = sum(
        len(q & tokens(row.get(field, ""))) * weight
        for field, weight in fields
    )
    if site and row["site_id"] == site:
        score += 20
    if archetype and row["archetype"] == archetype:
        score += 12
    for key, target in (
        ("variance", variance),
        ("motion", motion),
        ("density", density),
    ):
        if target is not None:
            score += max(0.0, 5.0 - abs(int(row[key]) - target))
    return score


def one_for_site(filename: str, site_id: str) -> dict[str, str]:
    return next(
        (row for row in read_csv(filename) if row["site_id"] == site_id),
        {},
    )


def build_design_system(
    query: str,
    site: str | None,
    archetype: str | None,
    variance: int | None,
    motion: int | None,
    density: int | None,
) -> dict:
    q = expanded_query(query)
    profiles = read_csv("design-profiles.csv")
    if site:
        profiles = [row for row in profiles if row["site_id"] == site]
    if archetype:
        profiles = [row for row in profiles if row["archetype"] == archetype]
    if not profiles:
        return {}

    scored = sorted(
        (
            (
                profile_score(
                    row, q, site, archetype,
                    variance, motion, density,
                ),
                row,
            )
            for row in profiles
        ),
        key=lambda item: (-item[0], item[1]["name"].lower()),
    )
    score, profile = scored[0]
    if (
        score <= 0
        and not site
        and not archetype
        and all(value is None for value in (variance, motion, density))
    ):
        return {}

    site_id = profile["site_id"]
    related = ranked_records(query, site=site_id, max_results=10)

    return {
        "query": query,
        "source_site": site_id,
        "source_name": profile["name"],
        "archetype": profile["archetype"],
        "match_score": round(score, 2),
        "audited_dials": {
            "variance": int(profile["variance"]),
            "motion": int(profile["motion"]),
            "density": int(profile["density"]),
        },
        "requested_dials": {
            "variance": variance,
            "motion": motion,
            "density": density,
        },
        "style": {
            "theme": profile["theme"],
            "keywords": profile["style_keywords"],
            "composition": profile["composition"],
            "visual_signature": profile["visual_signature"],
            "best_for": profile["best_for"],
            "avoid_for": profile["avoid_for"],
            "performance": profile["performance_profile"],
            "accessibility_watch": profile["accessibility_watch"],
            "mobile_strategy": profile["mobile_strategy"],
            "implementation_checklist": profile["implementation_checklist"],
        },
        "color": one_for_site("color-systems.csv", site_id),
        "typography": one_for_site("typography-systems.csv", site_id),
        "components": [
            row for row in read_csv("component-recipes.csv")
            if row["site_id"] == site_id
        ],
        "patterns": [row for row in related if row["kind"] == "pattern"][:3],
        "routes": [row for row in related if row["kind"] == "route"][:2],
        "responsive": ranked_records(
            query, site=site_id, max_results=2, kinds={"responsive"}
        ),
        "motion_recipes": ranked_records(
            query, site=site_id, max_results=1, kinds={"motion"}
        ),
        "ux_guidelines": [
            row for row in read_csv("ux-guidelines.csv")
            if row["site_id"] == site_id
        ],
        "provenance_rule": (
            "Use this as audited reference-derived design intelligence. "
            "Transfer mechanisms and role systems; do not clone source identity, "
            "exact palette, proprietary fonts/assets, copy, metrics or "
            "brand-specific artwork."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Search the audited distilled web toolkit.")
    ap.add_argument("query")
    ap.add_argument("--domain")
    ap.add_argument("--site")
    ap.add_argument("--archetype")
    ap.add_argument("-n", "--max-results", type=int, default=12)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--design-system", action="store_true")
    ap.add_argument("--variance", type=int)
    ap.add_argument("--motion", type=int)
    ap.add_argument("--density", type=int)
    args = ap.parse_args()

    for label in ("variance", "motion", "density"):
        value = getattr(args, label)
        if value is not None and not 1 <= value <= 10:
            ap.error(f"--{label} must be between 1 and 10")

    if args.design_system:
        ds = build_design_system(
            args.query,
            args.site,
            args.archetype,
            args.variance,
            args.motion,
            args.density,
        )
        if args.json:
            print(json.dumps({"design_system": ds}, indent=2, ensure_ascii=False))
            return 0
        if not ds:
            print("No verified audited design-system match.")
            return 0

        dials = ds["audited_dials"]
        style = ds["style"]
        color = ds["color"]
        typography = ds["typography"]
        print(
            f"Audited Design System - {ds['source_name']} "
            f"[{ds['archetype']}]"
        )
        print(
            f"source: {ds['source_site']} | match: {ds['match_score']} | "
            f"dials: V{dials['variance']} M{dials['motion']} D{dials['density']}"
        )
        print("\nSTYLE")
        print(f"  theme: {style['theme']}")
        print(f"  keywords: {style['keywords']}")
        print(f"  composition: {style['composition']}")
        print(f"  signature: {style['visual_signature']}")
        print("\nCOLOR")
        print(
            f"  mode: {color.get('mode', '')} | "
            f"bg: {color.get('background', '')} | "
            f"fg: {color.get('foreground', '')} | "
            f"accent: {color.get('accent', '')}"
        )
        print(f"  strategy: {color.get('semantic_strategy', '')}")
        print(f"  transfer: {color.get('transfer_rule', '')}")
        print("\nTYPE")
        print(
            f"  display: {typography.get('display_font', '')} | "
            f"heading: {typography.get('heading_font', '')} | "
            f"body: {typography.get('body_font', '')} | "
            f"utility: {typography.get('utility_font', '')}"
        )
        print(f"  roles: {typography.get('role_strategy', '')}")
        print(
            f"  scale: {typography.get('desktop_scale', '')} -> "
            f"{typography.get('mobile_scale', '')}"
        )
        if ds["components"]:
            print("\nCOMPONENTS")
            for row in ds["components"][:4]:
                print(
                    f"  - {row['name']}: {row['job']} | "
                    f"{row['responsive_strategy']}"
                )
        if ds["patterns"]:
            print("\nPATTERNS")
            for row in ds["patterns"]:
                print(f"  - {row['name']}: {row['recipe']}")
        if ds["ux_guidelines"]:
            print("\nUX WATCH")
            for row in ds["ux_guidelines"]:
                print(f"  - {row['issue']}: {row['do']}")
        print(f"\nPROVENANCE\n  {ds['provenance_rule']}")
        return 0

    selected = ranked_records(
        args.query,
        domain=args.domain,
        site=args.site,
        archetype=args.archetype,
        max_results=args.max_results,
    )

    if args.json:
        print(json.dumps({
            "query": args.query,
            "domain": args.domain,
            "site": args.site,
            "archetype": args.archetype,
            "results": selected,
        }, indent=2, ensure_ascii=False))
        return 0

    if not selected:
        print("No verified audited pattern match.")
        return 0

    print(f"Distilled Web Toolkit - {len(selected)} result(s)")
    for i, row in enumerate(selected, 1):
        print(f"\n{i}. {row['name']} [{row['kind']} / {row['domain']}]")
        print(
            f"   sites: {row['sites']} | "
            f"archetype: {row['archetype'] or '-'} | score: {row['score']}"
        )
        if row["summary"]:
            print(f"   when: {row['summary']}")
        if row["recipe"]:
            print(f"   recipe: {row['recipe']}")
        if row["avoid"]:
            print(f"   avoid: {row['avoid']}")
        if row["implementation"]:
            print(f"   implementation: {row['implementation']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
