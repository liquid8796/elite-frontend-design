#!/usr/bin/env python3
"""Stable facade for the bundled UI/UX Pro Max search engine."""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


def main() -> None:
    skill_root = Path(__file__).resolve().parents[1]
    engine_dir = skill_root / "references" / "modules" / "ui-ux-pro-max" / "scripts"
    engine = engine_dir / "search.py"

    if not engine.is_file():
        raise SystemExit(f"Bundled search engine not found: {engine}")

    # The upstream engine imports sibling modules (core, design_system, ...).
    sys.path.insert(0, str(engine_dir))
    sys.argv[0] = str(engine)
    runpy.run_path(str(engine), run_name="__main__")


if __name__ == "__main__":
    main()
