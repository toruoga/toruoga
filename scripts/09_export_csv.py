#!/usr/bin/env python3
"""
Stage 9: Export the final corpus CSV (Section 12) and the human-validation
sample (Section 20).

Maps deduplicated_records.csv onto the required CSV schema exactly, filling
any column absent upstream with NA, formats date as ISO YYYY-MM-DD (or NA if
it could not be parsed -- never guessed), and writes:
  data/output/corpus.csv
  data/output/human_validation_sample.csv  (>=20% of rows, fixed seed from
                                             config.yaml project.random_seed)
"""
import csv
import random
import sys
from pathlib import Path

from dateutil import parser as dateparser

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import REPO_ROOT, load_config

FINAL_COLUMNS = [
    "record_id", "country", "date", "year", "speaker_name", "speaker_position", "speaker_level",
    "institution", "document_type", "document_title", "question_text", "response_text",
    "relevant_excerpt", "issue_primary", "issue_secondary",
    "kingdon_problem", "kingdon_policy", "kingdon_politics", "kingdon_confidence",
    "apology", "explanation", "remorse", "reflection", "remedy", "pardon_or_forgiveness",
    "responsibility_actor", "agency_explicit", "audience_orientation",
    "source_language", "official_translation", "source_url", "retrieval_date", "archive_url",
    "collection_method", "coder_notes", "classification_confidence",
    "duplicate_group_id", "canonical_record",
]


def to_iso_date(raw: str) -> str:
    if not raw:
        return "NA"
    try:
        return dateparser.parse(raw, fuzzy=True).date().isoformat()
    except (ValueError, OverflowError):
        return "NA"


def main():
    cfg = load_config()
    dedup_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "deduplicated_records.csv"
    if not dedup_path.exists():
        print("No deduplicated_records.csv found. Run 07_deduplicate.py first.")
        return

    with open(dedup_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    out_rows = []
    for r in rows:
        iso_date = to_iso_date(r.get("date_guess", ""))
        out_rows.append({
            "record_id": r.get("record_id", "NA"),
            "country": r.get("country", "NA"),
            "date": iso_date,
            "year": iso_date.split("-")[0] if iso_date != "NA" else "NA",
            "speaker_name": r.get("speaker_name") or "UNKNOWN",
            "speaker_position": r.get("speaker_position") or "UNKNOWN",
            "speaker_level": r.get("speaker_level") or "UNKNOWN",
            "institution": r.get("institution", "NA"),
            "document_type": r.get("document_type_guess", "OTHER"),
            "document_title": r.get("document_title", "NA"),
            "question_text": r.get("question_text", ""),
            "response_text": r.get("response_text", ""),
            "relevant_excerpt": r.get("relevant_excerpt", "NA"),
            "issue_primary": r.get("issue_primary") or r.get("issue_primary_suggested") or "NA",
            "issue_secondary": r.get("issue_secondary", "NA") or "NA",
            "kingdon_problem": r.get("kingdon_problem") or "NA",
            "kingdon_policy": r.get("kingdon_policy") or "NA",
            "kingdon_politics": r.get("kingdon_politics") or "NA",
            "kingdon_confidence": r.get("kingdon_confidence") or "NA",
            "apology": r.get("apology") or "NA",
            "explanation": r.get("explanation") or "NA",
            "remorse": r.get("remorse") or "NA",
            "reflection": r.get("reflection") or "NA",
            "remedy": r.get("remedy") or "NA",
            "pardon_or_forgiveness": r.get("pardon_or_forgiveness") or "NA",
            "responsibility_actor": r.get("responsibility_actor") or "NA",
            "agency_explicit": r.get("agency_explicit") or "NA",
            "audience_orientation": r.get("audience_orientation") or "UNKNOWN",
            "source_language": r.get("source_language") or "NA",
            "official_translation": r.get("official_translation") or "NA",
            "source_url": r.get("url", "NA"),
            "retrieval_date": r.get("retrieval_date", "NA"),
            "archive_url": r.get("archive_url", "NA"),
            "collection_method": r.get("discovered_via", "NA"),
            "coder_notes": r.get("coder_notes", ""),
            "classification_confidence": r.get("classification_confidence", "LOW"),
            "duplicate_group_id": r.get("duplicate_group_id", "NA"),
            "canonical_record": r.get("canonical_record", "NA"),
        })

    out_dir = REPO_ROOT / cfg["paths"]["output_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    corpus_path = out_dir / "corpus.csv"
    with open(corpus_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FINAL_COLUMNS)
        w.writeheader()
        w.writerows(out_rows)

    seed = cfg["project"]["random_seed"]
    frac = cfg["project"]["human_validation_fraction"]
    rng = random.Random(seed)
    n_sample = max(1, int(len(out_rows) * frac)) if out_rows else 0
    sample = rng.sample(out_rows, n_sample) if out_rows else []
    sample_path = out_dir / "human_validation_sample.csv"
    with open(sample_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FINAL_COLUMNS)
        w.writeheader()
        w.writerows(sample)

    print(f"Exported {len(out_rows)} records -> {corpus_path}")
    print(f"Human validation sample: {len(sample)} records (seed={seed}, fraction={frac}) -> {sample_path}")


if __name__ == "__main__":
    main()
