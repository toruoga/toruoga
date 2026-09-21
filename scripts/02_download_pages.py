#!/usr/bin/env python3
"""
Stage 2: Download pages discovered in Stage 1.

For every URL in data/metadata/discovered_urls.csv with status DISCOVERED:
  - respect robots.txt and the configured rate limit,
  - save raw HTML verbatim to data/raw/<country>/<deterministic_filename>.html
    (never overwritten -- if the file exists, it is treated as already
    downloaded and skipped),
  - record retrieval_date, http_status, and content hash in
    data/metadata/download_log.csv,
  - on any failure (network error, non-200, timeout, access control),
    append a row to inaccessible_sources.csv with the discovered URL and the
    reason -- the text is NEVER fabricated.
"""
import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import REPO_ROOT, deterministic_filename, is_allowed_by_robots, load_config, polite_sleep, sha256_text


def append_csv(path: Path, fieldnames: list[str], row: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    is_new = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if is_new:
            w.writeheader()
        w.writerow(row)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    cfg = load_config()
    discovered_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "discovered_urls.csv"
    if not discovered_path.exists():
        print("No discovered_urls.csv found. Run 01_discover_urls.py first.")
        return

    with open(discovered_path, newline="", encoding="utf-8") as f:
        candidates = [r for r in csv.DictReader(f) if r["status"] == "DISCOVERED"]

    if args.limit:
        candidates = candidates[: args.limit]

    download_log = REPO_ROOT / cfg["paths"]["metadata_dir"] / "download_log.csv"
    inaccessible_path = REPO_ROOT / "inaccessible_sources.csv"
    dl_fields = ["url", "country", "raw_file", "retrieval_date", "http_status", "content_sha256"]
    inacc_fields = ["url", "date_attempted", "country", "reason"]

    session = requests.Session()
    ua = cfg["crawl"]["user_agent"]

    for row in candidates:
        url, country = row["url"], row["country"]
        if cfg["crawl"]["respect_robots_txt"] and not is_allowed_by_robots(url, ua):
            append_csv(inaccessible_path, inacc_fields, {
                "url": url, "date_attempted": datetime.now(timezone.utc).date().isoformat(),
                "country": country, "reason": "ROBOTS_DISALLOWED",
            })
            continue

        raw_dir = REPO_ROOT / cfg["paths"]["raw_dir"] / country
        raw_dir.mkdir(parents=True, exist_ok=True)
        fname = deterministic_filename(url) + ".html"
        raw_file = raw_dir / fname
        if raw_file.exists():
            continue  # never overwrite raw files (Section 13)

        try:
            resp = session.get(url, headers={"User-Agent": ua}, timeout=cfg["crawl"]["timeout_seconds"])
            status = resp.status_code
            if status != 200:
                append_csv(inaccessible_path, inacc_fields, {
                    "url": url, "date_attempted": datetime.now(timezone.utc).date().isoformat(),
                    "country": country, "reason": f"HTTP_{status}",
                })
                continue
            raw_file.write_bytes(resp.content)
            append_csv(download_log, dl_fields, {
                "url": url, "country": country, "raw_file": str(raw_file.relative_to(REPO_ROOT)),
                "retrieval_date": datetime.now(timezone.utc).date().isoformat(),
                "http_status": status, "content_sha256": sha256_text(resp.text),
            })
        except requests.RequestException as e:
            append_csv(inaccessible_path, inacc_fields, {
                "url": url, "date_attempted": datetime.now(timezone.utc).date().isoformat(),
                "country": country, "reason": f"NETWORK_ERROR: {e}",
            })
        finally:
            polite_sleep(cfg["crawl"]["request_delay_seconds"])

    print(f"Processed {len(candidates)} candidate URLs. See {download_log} and {inaccessible_path}.")


if __name__ == "__main__":
    main()
