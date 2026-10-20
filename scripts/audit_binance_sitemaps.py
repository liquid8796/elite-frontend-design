#!/usr/bin/env python3
"""Read-only Binance sitemap-family census, preserving complete English URL inventory.

Do NOT treat sitemap URLs as HTTP-verified pages. Reject remote XML entities,
keep network requests bounded, and never send account credentials or trade.
"""
from __future__ import annotations

import argparse
import collections
import csv
import gzip
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

DOMAIN = "https://www.binance.com"
FAMILIES = (
    "Trade", "Blog", "Nft", "SupportAndAnnouncement", "Futures",
    "Earn", "Loan", "Market", "Default", "Fiat",
    "Crypto", "Square", "Academy_New", "Muses", "Growth",
)
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
UA = "Mozilla/5.0 (compatible; sitemap-audit/1.0; research-only)"


def fetch(url: str) -> bytes:
    if not url.startswith(DOMAIN + "/sitemap_output/"):
        raise ValueError("Only the public same-origin sitemap can be fetched")
    with urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": UA}),
        timeout=25,
    ) as res:
        if res.status != 200:
            raise RuntimeError(f"HTTP {res.status} for {url}")
        data = res.read(15_000_001)
    if len(data) > 15_000_000:
        raise ValueError("XML sitemap too large")
    if b"<!DOCTYPE" in data.upper() or b"<!ENTITY" in data.upper():
        raise ValueError("Do not parse XML entities")
    return data


def locs(payload: bytes) -> list[str]:
    return [(el.text or "").strip() for el in ET.fromstring(payload).iter(NS + "loc")]


def route_family(url: str) -> str:
    chunks = [v for v in urlsplit(url).path.split("/") if v]
    if chunks and chunks[0].lower() in ("en", "vi"):
        chunks.pop(0)
    if not chunks:
        return "/"
    if chunks[0] in ("price", "how-to-buy", "trade", "trade-cl", "futures", "convert", "stocks", "eoptions"):
        return "/" + chunks[0] + "/:instrument"
    if chunks[0] in ("support", "academy", "blog", "square", "nft", "crypto", "markets", "fiat", "loan", "earn", "about-legal", "events"):
        return "/" + "/".join(chunks[:min(2, len(chunks))])
    return "/" + chunks[0]


def suspicious_path(url: str) -> bool:
    s = url.lower()
    return bool(
        re.search(r"(?:%25(?:3c|3e|22|27)|\.php|\.env|\.sqlite|%253c|%253e|\{\{|\.\./|<script|%2522)", s)
    )


def write_csv(path: Path, headers: list[str], rows: list[tuple]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    indexes = []
    for family in FAMILIES:
        u = f"{DOMAIN}/sitemap_output/domain=www.binance.com/sitemap_{family}_index.xml"
        children = locs(fetch(u))
        en = [x for x in children if re.search(rf"sitemap_{re.escape(family)}_en_\d+\.xml$", x)]
        indexes.append((family, len(children), en))
    inventory = []
    by_file = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures = {
            ex.submit(fetch, url): (family, url)
            for family, _n, urls in indexes for url in urls
        }
        for future in as_completed(futures):
            family, url = futures[future]
            items = locs(future.result())
            by_file.append((family, url.rsplit("/", 1)[-1], len(items)))
            for item in items:
                inventory.append((family, url, item, route_family(item), int(suspicious_path(item))))
    inventory.sort()
    counts = collections.Counter((family, route) for family, _shard, _url, route, _flag in inventory)
    examples = {}
    for family, shard, url, route, flag in inventory:
        examples.setdefault((family, route), url)
    group_rows = [
        (family, route, count, examples[(family, route)])
        for (family, route), count in sorted(counts.items())
    ]
    index_rows = [
        (family, shard_count, len(english_shards), sum(n for fam, _file, n in by_file if fam == family))
        for family, shard_count, english_shards in indexes
    ]
    write_csv(args.out / "binance-sitemap-index-2026-10-20.csv",
              ["family", "all_locale_shards", "english_shards", "english_declared_urls"], index_rows)
    write_csv(args.out / "binance-english-sitemap-shards-2026-10-20.csv",
              ["family", "shard", "declared_urls"], sorted(by_file))
    write_csv(args.out / "binance-english-route-families-2026-10-20.csv",
              ["sitemap_family", "route_family", "declared_urls", "example_url"], group_rows)
    with gzip.open(args.out / "binance-english-sitemap-inventory-2026-10-20.csv.gz", "wt", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["family", "sitemap_shard_url", "declared_url", "route_family", "suspicious_url_heuristic"])
        writer.writerows(inventory)
    print(f"INDEXES={len(indexes)} EN_SHARDS={len(by_file)} EN_URLS={len(inventory)} "
          f"ROUTE_FAMILIES={len(group_rows)} HEURISTIC_SUSPICIOUS={sum(v[-1] for v in inventory)}")
    print("These are sitemap declarations, NOT verified HTTP 200 URLs or authenticated runtime proof.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
