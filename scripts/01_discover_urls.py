#!/usr/bin/env python3
"""
Stage 1: URL discovery.

Two complementary strategies (Section 16 of the spec):
  A. Archive crawling  -- enumerate index/archive pages listed in config.yaml
     and follow their internal links to individual document pages.
  B. Search discovery  -- supplementary only. Search queries and the URLs
     they return are appended to data/logs/search_log.csv for manual/other
     tooling to feed into --seed-urls; discovery via search is never treated
     as a complete inventory (Section 16).

Output: data/metadata/discovered_urls.csv with columns
  url, country, institution, discovered_via, discovered_date, archive_source, status

This script only performs HTTP GETs against the archive/index pages named in
config.yaml (or explicit --seed-urls); it does not call any search API itself
(search discovery is logged separately, see 00_log_search_query() below, and
is meant to be run wherever the operator has a search tool available, e.g.
inside an interactive agent session -- see README.md).
"""
import argparse
import csv
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import REPO_ROOT, institution_for_url, is_allowed_by_robots, load_config, polite_sleep


def crawl_index_page(url: str, cfg: dict, session: requests.Session):
    """Fetch one archive/index page and return absolute links found on it."""
    ua = cfg["crawl"]["user_agent"]
    if cfg["crawl"]["respect_robots_txt"] and not is_allowed_by_robots(url, ua):
        return [], "ROBOTS_DISALLOWED"
    try:
        resp = session.get(url, headers={"User-Agent": ua}, timeout=cfg["crawl"]["timeout_seconds"])
        resp.raise_for_status()
    except requests.RequestException as e:
        return [], f"FETCH_ERROR: {e}"
    soup = BeautifulSoup(resp.text, "lxml")
    links = set()
    for a in soup.find_all("a", href=True):
        abs_url = urljoin(url, a["href"])
        if urlparse(abs_url).scheme in ("http", "https"):
            links.add(abs_url.split("#")[0])
    return sorted(links), "OK"


def log_search_query(query: str, engine: str, returned_urls: list[str], cfg: dict):
    """Append one row to the search discovery log (Section 16)."""
    log_path = REPO_ROOT / cfg["paths"]["logs_dir"] / "search_log.csv"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not log_path.exists()
    with open(log_path, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if is_new:
            w.writerow(["query", "engine", "date", "returned_urls", "processed_status"])
        w.writerow([query, engine, date.today().isoformat(), ";".join(returned_urls), "PENDING"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--country", choices=["japan", "korea", "china", "all"], default="all")
    ap.add_argument("--seed-urls", nargs="*", default=[], help="Additional explicit URLs to enqueue")
    ap.add_argument(
        "--seed-index-urls", nargs="*", default=[],
        help="Additional archive/index pages (e.g. resolved {pm_slug} monthly archives) to crawl "
             "for document links, exactly like the section_url archive-crawl path -- for cases where "
             "config.yaml can only express a template (Section 16: administration-slug enumeration is "
             "left to the operator, not guessed by the script).",
    )
    args = ap.parse_args()

    cfg = load_config()
    out_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "discovered_urls.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    existing = set()
    if out_path.exists():
        with open(out_path, newline="", encoding="utf-8") as f:
            existing = {row["url"] for row in csv.DictReader(f)}

    rows = []
    session = requests.Session()
    countries = [args.country] if args.country != "all" else ["japan", "korea", "china"]

    for country in countries:
        for src in cfg["sources"].get(country, []):
            for section_url in src["sections"]:
                if "{pm_slug}" in section_url or "{" in section_url:
                    # Requires enumerating administration slugs / year archives;
                    # left for manual seeding via --seed-urls, logged as SKIPPED_TEMPLATE.
                    rows.append({
                        "url": section_url, "country": country, "institution": src["name"],
                        "discovered_via": "ARCHIVE_TEMPLATE", "discovered_date": date.today().isoformat(),
                        "archive_source": section_url, "status": "SKIPPED_TEMPLATE_NEEDS_SEED",
                    })
                    continue
                links, status = crawl_index_page(section_url, cfg, session)
                polite_sleep(cfg["crawl"]["request_delay_seconds"])
                for link in links:
                    if link in existing:
                        continue
                    existing.add(link)
                    rows.append({
                        "url": link, "country": country, "institution": src["name"],
                        "discovered_via": "ARCHIVE_CRAWL", "discovered_date": date.today().isoformat(),
                        "archive_source": section_url, "status": "DISCOVERED",
                    })

    for index_url in args.seed_index_urls:
        inst, country = institution_for_url(index_url)
        country = country or (args.country if args.country != "all" else "UNKNOWN")
        links, status = crawl_index_page(index_url, cfg, session)
        polite_sleep(cfg["crawl"]["request_delay_seconds"])
        if status != "OK":
            rows.append({
                "url": index_url, "country": country, "institution": inst or "UNKNOWN",
                "discovered_via": "ARCHIVE_CRAWL_SEEDED_INDEX_FAILED", "discovered_date": date.today().isoformat(),
                "archive_source": index_url, "status": f"SKIPPED_{status}",
            })
            continue
        for link in links:
            if link in existing:
                continue
            existing.add(link)
            rows.append({
                "url": link, "country": country, "institution": inst or "UNKNOWN",
                "discovered_via": "ARCHIVE_CRAWL_SEEDED_INDEX", "discovered_date": date.today().isoformat(),
                "archive_source": index_url, "status": "DISCOVERED",
            })

    for url in args.seed_urls:
        if url in existing:
            continue
        inst, country = institution_for_url(url)
        rows.append({
            "url": url, "country": country or "UNKNOWN", "institution": inst or "UNKNOWN",
            "discovered_via": "SEARCH_DISCOVERY_MANUAL_SEED", "discovered_date": date.today().isoformat(),
            "archive_source": "manual/search", "status": "DISCOVERED",
        })

    write_header = not out_path.exists()
    with open(out_path, "a", newline="", encoding="utf-8") as f:
        fieldnames = ["url", "country", "institution", "discovered_via", "discovered_date", "archive_source", "status"]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            w.writeheader()
        w.writerows(rows)

    print(f"Discovered {len(rows)} new URL rows -> {out_path}")


if __name__ == "__main__":
    main()
