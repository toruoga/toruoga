#!/usr/bin/env python3
"""
Stage 4: Keyword-filter cleaned documents down to historical-recognition
candidates, and enforce the source/date exclusion rules from Section 2/6.

Reads data/metadata/document_metadata.csv + cleaned text.
Writes data/metadata/candidate_documents.csv (docs that matched >=1 keyword
from config.yaml search_terms and pass source/date checks) and appends
rejected documents to exclusion_log.csv with a controlled reason code:
  NOT_HISTORY_RELATED, NOT_OFFICIAL, OUTSIDE_DATE_RANGE
"""
import csv
import re
import sys
from datetime import date
from pathlib import Path

from dateutil import parser as dateparser

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import REPO_ROOT, load_config


def matched_keywords(text: str, terms: list[str]) -> list[str]:
    lowered = text.lower()
    return [t for t in terms if t.lower() in lowered]


def in_date_range(date_guess: str, start: date, end: date) -> bool | None:
    if not date_guess:
        return None
    try:
        d = dateparser.parse(date_guess, fuzzy=True).date()
    except (ValueError, OverflowError):
        return None
    return start <= d <= end


def append_exclusion(path: Path, row: dict):
    fields = ["url", "date", "country", "reason_for_exclusion"]
    is_new = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if is_new:
            w.writeheader()
        w.writerow(row)


def main():
    cfg = load_config()
    meta_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "document_metadata.csv"
    if not meta_path.exists():
        print("No document_metadata.csv found. Run 03_extract_metadata.py first.")
        return

    start = date.fromisoformat(cfg["project"]["date_range"]["start"])
    end = date.fromisoformat(cfg["project"]["date_range"]["end"])
    terms = cfg["search_terms"]
    excluded_kw = cfg["excluded_domains_keywords"]

    out_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "candidate_documents.csv"
    exclusion_path = REPO_ROOT / "exclusion_log.csv"
    out_fields = ["url", "country", "institution", "document_title", "document_type_guess",
                  "date_guess", "cleaned_file", "matched_keywords"]

    rows = []
    with open(meta_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if any(kw in r["url"].lower() for kw in excluded_kw):
                append_exclusion(exclusion_path, {"url": r["url"], "date": r["date_guess"],
                                                    "country": r["country"], "reason_for_exclusion": "NOT_OFFICIAL"})
                continue

            date_ok = in_date_range(r["date_guess"], start, end)
            if date_ok is False:
                append_exclusion(exclusion_path, {"url": r["url"], "date": r["date_guess"],
                                                    "country": r["country"], "reason_for_exclusion": "OUTSIDE_DATE_RANGE"})
                continue

            cleaned_path = REPO_ROOT / r["cleaned_file"]
            text = cleaned_path.read_text(encoding="utf-8", errors="ignore") if cleaned_path.exists() else ""
            hits = matched_keywords(text, terms)
            if not hits:
                append_exclusion(exclusion_path, {"url": r["url"], "date": r["date_guess"],
                                                    "country": r["country"], "reason_for_exclusion": "NOT_HISTORY_RELATED"})
                continue

            rows.append({**{k: r[k] for k in out_fields if k in r}, "matched_keywords": ";".join(hits)})

    write_header = not out_path.exists()
    with open(out_path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        if write_header:
            w.writeheader()
        w.writerows(rows)

    print(f"{len(rows)} candidate documents -> {out_path}. Exclusions logged to {exclusion_path}.")


if __name__ == "__main__":
    main()
