#!/usr/bin/env python3
"""Bounded public MEXC sitemap census. Read-only: no login, trading or private routes."""
from __future__ import annotations
import argparse, collections, csv, gzip, re, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

BASE = "https://www.mexc.com"
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
UA = "Mozilla/5.0 (compatible; UI research / public sitemap inventory)"
LIMIT = 15_000_000

def get(url: str) -> bytes:
    if urlsplit(url).hostname != "www.mexc.com" or not url.startswith(BASE + "/"):
        raise ValueError("Untrusted sitemap URL")
    with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent": UA}),timeout=22) as res:
        if res.status != 200: raise RuntimeError(f"HTTP {res.status}")
        data=res.read(LIMIT+1)
    if len(data)>LIMIT: raise RuntimeError("Oversize XML")
    if b"<!DOCTYPE" in data.upper() or b"<!ENTITY" in data.upper(): raise ValueError("Unsafe XML")
    return data

def locations(xml: bytes) -> tuple[str,list[str]]:
    root=ET.fromstring(xml)
    return root.tag.rsplit("}",1)[-1],[(v.text or "").strip() for v in root.iter(NS+"loc")]

def family_path(url: str) -> str:
    path=urlsplit(url).path
    seg=[s for s in path.split("/") if s]
    if seg and re.fullmatch(r"[a-z]{2}(?:-[A-Z]{2})?",seg[0]):seg.pop(0)
    if not seg:return "/"
    if seg[0] in ("exchange","futures","price","price-prediction","price-converter","how-to-buy","compare","stocks"):
        if len(seg)>2 and seg[1] in ("information","how-to-buy","analysis","info","tokenomics"):
            return "/" + "/".join(seg[:3])+"/:detail"
        return "/"+seg[0]+"/:instrument"
    if seg[0] in ("learn","support","announcements","links","tools","markets","futures-activity","sitemap"):
        return "/"+"/".join(seg[:min(3,len(seg))])
    return "/"+"/".join(seg[:min(2,len(seg))])

def write_csv(path:Path,cols,rows):
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f);w.writerow(cols);w.writerows(rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out",type=Path,required=True);args=ap.parse_args()
    args.out.mkdir(parents=True,exist_ok=True)
    root_type,roots=locations(get(BASE+"/sitemap.xml"))
    if root_type!="sitemapindex":raise RuntimeError("Unexpected sitemap index root")
    index_records=[];default_shards=[]
    with ThreadPoolExecutor(max_workers=6) as ex:
        fut={ex.submit(get,u):u for u in roots}
        for f in as_completed(fut):
            u=fut[f]; grp=u[len(BASE)+1:].replace("/sitemap-index.xml","")
            try:
                typ,children=locations(f.result())
                if typ!="sitemapindex": raise ValueError(f"Unexpected {typ}")
                own=[x for x in children if urlsplit(x).path.startswith("/"+grp+"/") ]
                index_records.append((grp,u,200,len(children),len(own),""))
                default_shards += [(grp,x) for x in own]
            except Exception as e: index_records.append((grp,u,"ERROR",0,0,str(e)[:120]))
    shard_results=[];data=[];failures=[]
    with ThreadPoolExecutor(max_workers=6) as ex:
        fut={ex.submit(get,url):(grp,url) for grp,url in default_shards}
        for f in as_completed(fut):
            grp,url=fut[f]
            try:
                typ,urls=locations(f.result())
                if typ=="sitemapindex":
                    failures.append((grp,url,"nested sitemap index not traversed"))
                    continue
                if typ!="urlset":raise ValueError(f"Unexpected {typ}")
                shard_results.append((grp,url,200,len(urls)))
                for x in urls:
                    path=urlsplit(x).path.lower()
                    flag=int(bool(re.search(r"\\.php|\\.env|\\.sqlite|%25(?:3c|3e|22)|\\.\\./",path)))
                    data.append((grp,url,x,family_path(x),flag))
            except Exception as e:
                failures.append((grp,url,str(e)[:120]))
                shard_results.append((grp,url,"ERROR",0))
    idx=sorted(index_records);shards=sorted(shard_results);data.sort()
    buckets=collections.Counter((grp,fam) for grp,_sh,url,fam,_bad in data)
    exmap={}
    for grp,sh,url,fam,flag in data:exmap.setdefault((grp,fam),url)
    write_csv(args.out/"mexc-sitemap-index-2026-10-20.csv",["group","index_url","index_http","all_locale_child_refs","default_locale_shards","error"],idx)
    write_csv(args.out/"mexc-default-sitemap-shards-2026-10-20.csv",["group","shard_url","http","declared_urls"],shards)
    write_csv(args.out/"mexc-route-families-2026-10-20.csv",["group","route_family","declarations","example_url"],[(g,f,v,exmap[(g,f)]) for (g,f),v in sorted(buckets.items())])
    write_csv(args.out/"mexc-sitemap-errors-2026-10-20.csv",["group","url","error"],sorted(failures))
    with gzip.open(args.out/"mexc-default-sitemap-declarations-2026-10-20.csv.gz","wt",encoding="utf-8",newline="") as f:
        w=csv.writer(f);w.writerow(["group","sitemap_shard","declared_url","route_family","suspicious_heuristic"]);w.writerows(data)
    print(f"TOP_GROUPS={len(roots)} INDEX_OK={sum(x[2]==200 for x in idx)} DEFAULT_SHARDS={len(default_shards)} SHARDS_OK={sum(x[2]==200 for x in shards)} URL_DECLARATIONS={len(data)} PREFIXES={len(buckets)} ERRORS={len(failures)} SUSPICIOUS={sum(v[-1] for v in data)}")
    print("Only default/no-language sitemap leaves were fetched; declared URLs are not HTTP/render verified.")
if __name__=="__main__":main()
