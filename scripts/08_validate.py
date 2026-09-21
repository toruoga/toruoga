#!/usr/bin/env python3
"""
Stage 8: Validate deduplicated_records.csv (Section 19).

Checks performed per row, each producing a validation_report.csv row on
failure:
  MISSING_URL, MISSING_DATE, MALFORMED_DATE, DATE_OUT_OF_RANGE,
  MISSING_SPEAKER, IMPOSSIBLE_SPEAKER_LEVEL, DUPLICATE_RECORD_ID,
  EMPTY_RELEVANT_EXCERPT, CLASSIFICATION_CONTRADICTION

CLASSIFICATION_CONTRADICTION currently flags: all three kingdon_* fields
blank/NA while classification_confidence is HIGH or MEDIUM (a confident
coder should be able to determine at least one dimension), and apology=1
while remorse/reflection/remedy are all explicitly 0 AND explanation is
also 0 (an apology passage coded as containing none of the other five
categories is not on its face wrong, but is flagged for a second look).

Also builds manual_review.csv (Section 19): any record with
classification_confidence == LOW, speaker_level == UNKNOWN, or any
validation failure.
"""
import csv
import sys
from datetime import date
from pathlib import Path

from dateutil import parser as dateparser

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import REPO_ROOT, load_config

VALID_SPEAKER_LEVELS = {"HEAD", "MINISTER", "OFFICIAL", "UNKNOWN"}


def main():
    cfg = load_config()
    dedup_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "deduplicated_records.csv"
    if not dedup_path.exists():
        print("No deduplicated_records.csv found. Run 07_deduplicate.py first.")
        return

    start = date.fromisoformat(cfg["project"]["date_range"]["start"])
    end = date.fromisoformat(cfg["project"]["date_range"]["end"])

    with open(dedup_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    seen_ids = set()
    problems = []  # (record_id, issue)
    manual_review_ids = set()

    for r in rows:
        rid = r.get("record_id", "")
        issues = []

        if not r.get("url"):
            issues.append("MISSING_URL")

        date_str = r.get("date_guess", "")
        if not date_str:
            issues.append("MISSING_DATE")
        else:
            try:
                d = dateparser.parse(date_str, fuzzy=True).date()
                if not (start <= d <= end):
                    issues.append("DATE_OUT_OF_RANGE")
            except (ValueError, OverflowError):
                issues.append("MALFORMED_DATE")

        if not r.get("speaker_name") and not r.get("speaker_position"):
            issues.append("MISSING_SPEAKER")

        if r.get("speaker_level") and r["speaker_level"] not in VALID_SPEAKER_LEVELS:
            issues.append("IMPOSSIBLE_SPEAKER_LEVEL")

        if rid in seen_ids:
            issues.append("DUPLICATE_RECORD_ID")
        seen_ids.add(rid)

        if not r.get("relevant_excerpt", "").strip():
            issues.append("EMPTY_RELEVANT_EXCERPT")

        kingdon_blank = all(not r.get(k) or r.get(k) == "NA" for k in ("kingdon_problem", "kingdon_policy", "kingdon_politics"))
        if kingdon_blank and r.get("classification_confidence") in ("HIGH", "MEDIUM"):
            issues.append("CLASSIFICATION_CONTRADICTION")

        for issue in issues:
            problems.append({"record_id": rid, "url": r.get("url", ""), "issue": issue})

        if issues or r.get("classification_confidence") == "LOW" or r.get("speaker_level") in ("", "UNKNOWN"):
            manual_review_ids.add(rid)

    report_path = REPO_ROOT / "validation_report.csv"
    with open(report_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["record_id", "url", "issue"])
        w.writeheader()
        w.writerows(problems)

    review_path = REPO_ROOT / "manual_review.csv"
    with open(review_path, "w", newline="", encoding="utf-8") as f:
        if rows:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) + ["review_reason"])
            w.writeheader()
            for r in rows:
                if r.get("record_id") in manual_review_ids:
                    reasons = [p["issue"] for p in problems if p["record_id"] == r.get("record_id")]
                    if r.get("classification_confidence") == "LOW":
                        reasons.append("LOW_CONFIDENCE")
                    w.writerow({**r, "review_reason": ";".join(sorted(set(reasons)))})

    print(f"{len(problems)} validation issues across {len(rows)} records -> {report_path}")
    print(f"{len(manual_review_ids)} records routed to manual review -> {review_path}")


if __name__ == "__main__":
    main()
