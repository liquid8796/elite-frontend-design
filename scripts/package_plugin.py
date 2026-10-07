#!/usr/bin/env python3
"""Build a skills-only ZIP for ChatGPT/Codex plugin upload."""

from __future__ import annotations

import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PLUGIN_MANIFEST = ROOT / "plugin.json"
PACKAGE_FILES = (
    "plugin.json",
    ".codex-plugin",
    "assets",
    "skills",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
)
SKIP_PARTS = {"__pycache__", ".pytest_cache"}


def _iter_files(path: Path):
    if path.is_file():
        yield path
        return
    for item in sorted(path.rglob("*")):
        if item.is_file() and not any(part in SKIP_PARTS for part in item.parts):
            if item.suffix.lower() not in {".pyc", ".pyo"}:
                yield item


def build() -> Path:
    manifest = json.loads(PLUGIN_MANIFEST.read_text(encoding="utf-8"))
    name = manifest["name"]
    version = manifest["version"]
    archive = DIST / f"{name}-{version}.zip"
    prefix = f"{name}/"

    DIST.mkdir(parents=True, exist_ok=True)
    if archive.exists():
        archive.unlink()

    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for relative in PACKAGE_FILES:
            source = ROOT / relative
            if not source.exists():
                raise FileNotFoundError(f"Missing package input: {source}")
            for file_path in _iter_files(source):
                arcname = prefix + file_path.relative_to(ROOT).as_posix()
                zf.write(file_path, arcname)

    return archive


def main() -> int:
    archive = build()
    size_mb = archive.stat().st_size / (1024 * 1024)
    print(f"Built {archive} ({size_mb:.2f} MiB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
