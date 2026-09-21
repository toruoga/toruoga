#!/usr/bin/env python3
"""
Stage 3: Extract cleaned text + structural metadata from each raw HTML file.

Reads data/metadata/download_log.csv, opens each raw file, strips boilerplate
(nav/header/footer/script/style), writes cleaned plain text to
data/cleaned/<country>/<same_stem>.txt, and writes one row per document to
data/metadata/document_metadata.csv with:
  raw_file, cleaned_file, url, country, institution, document_title,
  document_type_guess, date_guess, source_language_guess

date_guess / document_title / date are extracted with conservative,
site-aware heuristics (title tag, <time> tags, common date regexes). Any
field that cannot be extracted with confidence is left blank/UNKNOWN --
04/05/06 downstream, or a human reviewer, must confirm it. This script
never invents a date or speaker.
"""
import csv
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import REPO_ROOT, institution_for_url, load_config

DATE_PATTERNS = [
    re.compile(r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}"),
    re.compile(r"\d{4}-\d{2}-\d{2}"),
    re.compile(r"\d{1,2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}"),
]

DOC_TYPE_HINTS = [
    (re.compile(r"press conference|briefing|kaiken", re.I), "PRESS_CONFERENCE"),
    (re.compile(r"joint statement", re.I), "JOINT_STATEMENT"),
    (re.compile(r"speech|address|remarks", re.I), "SPEECH"),
    (re.compile(r"written response|answer to written", re.I), "WRITTEN_RESPONSE"),
    (re.compile(r"statement", re.I), "STATEMENT"),
]


def guess_document_type(title: str, text: str) -> str:
    for pattern, label in DOC_TYPE_HINTS:
        if pattern.search(title) or pattern.search(text[:2000]):
            return label
    return "OTHER"


def guess_date(title: str, text: str) -> str:
    for pattern in DATE_PATTERNS:
        m = pattern.search(title) or pattern.search(text[:3000])
        if m:
            return m.group(0)
    return ""


def clean_html(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "lxml")
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else ""
    for tag in soup(["script", "style", "nav", "header", "footer", "noscript"]):
        tag.decompose()
    text = soup.get_text("\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return title, text


def main():
    cfg = load_config()
    dl_log = REPO_ROOT / cfg["paths"]["metadata_dir"] / "download_log.csv"
    if not dl_log.exists():
        print("No download_log.csv found. Run 02_download_pages.py first.")
        return

    out_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "document_metadata.csv"
    fields = ["raw_file", "cleaned_file", "url", "country", "institution",
              "document_title", "document_type_guess", "date_guess", "source_language_guess"]

    existing_raw = set()
    if out_path.exists():
        with open(out_path, newline="", encoding="utf-8") as f:
            existing_raw = {r["raw_file"] for r in csv.DictReader(f)}

    rows = []
    with open(dl_log, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["raw_file"] in existing_raw:
                continue
            raw_path = REPO_ROOT / r["raw_file"]
            if not raw_path.exists():
                continue
            html = raw_path.read_text(encoding="utf-8", errors="ignore")
            title, text = clean_html(html)
            cleaned_dir = REPO_ROOT / cfg["paths"]["cleaned_dir"] / r["country"]
            cleaned_dir.mkdir(parents=True, exist_ok=True)
            cleaned_file = cleaned_dir / (Path(r["raw_file"]).stem + ".txt")
            cleaned_file.write_text(text, encoding="utf-8")

            inst, _ = institution_for_url(r["url"])
            rows.append({
                "raw_file": r["raw_file"], "cleaned_file": str(cleaned_file.relative_to(REPO_ROOT)),
                "url": r["url"], "country": r["country"], "institution": inst or "UNKNOWN",
                "document_title": title, "document_type_guess": guess_document_type(title, text),
                "date_guess": guess_date(title, text), "source_language_guess": "en" if re.search(r"[a-zA-Z]{4,}", text[:500]) else "UNKNOWN",
            })

    write_header = not out_path.exists()
    with open(out_path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if write_header:
            w.writeheader()
        w.writerows(rows)

    print(f"Extracted metadata for {len(rows)} documents -> {out_path}")


if __name__ == "__main__":
    main()
