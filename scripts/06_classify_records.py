#!/usr/bin/env python3
"""
Stage 6: Classify each candidate passage per codebook.md.

IMPORTANT (codebook.md Sections 6-7, spec Section 9): apology/responsibility
and Kingdon coding require reading the passage in context -- they are NOT
meant to be assigned by keyword-matching alone ("Do not mechanically
classify. Check context."). This script therefore does two things only:

1. Computes cheap, transparent, keyword-presence SIGNALS for each binary
   field (stored with an "_signal" suffix) to speed up human/LLM review.
2. Leaves every substantive coding column (issue_primary, kingdon_*,
   apology, remorse, ..., responsibility_actor, agency_explicit,
   audience_orientation, speaker_level, etc.) BLANK/NA and sets
   classification_confidence = LOW, so that every record is routed to
   manual_review.csv by 08_validate.py until a qualified coder (human, or
   an LLM coder operating under codebook.md with the full passage in
   context) fills them in and raises the confidence.

This intentionally prevents keyword-matching from silently becoming the
dataset's classification method.

Output: data/metadata/coded_records.csv (superset of candidate_passages.csv
plus blank coding columns + signal columns).
"""
import csv
import re
import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import REPO_ROOT, load_config

SIGNAL_TERMS = {
    "apology_signal": [r"\bapolog(y|ize|ise|ies)\b"],
    "remorse_signal": [r"\bremorse\b", r"\bregret\b", r"\bsorrow\b", r"\bcontrition\b"],
    "reflection_signal": [r"\breflect", r"\bself-examination\b", r"\blearn(ed)? from the past\b"],
    "remedy_signal": [r"\bcompensation\b", r"\breparation", r"\bfund\b", r"\bsettlement\b", r"\bassistance\b"],
    "pardon_or_forgiveness_signal": [r"\bforgiveness\b", r"\bpardon\b", r"\breconcil"],
    "explanation_signal": [r"\bposition of the government\b", r"\bexplain", r"\bas (the government|japan|korea|china) has stated\b"],
}

ISSUE_SIGNAL_TERMS = {
    "COMFORT_WOMEN": [r"comfort women"],
    "SEXUAL_SLAVERY": [r"sexual slavery", r"sex slaves?"],
    "NANJING": [r"nanjing", r"nanking"],
    "YASUKUNI": [r"yasukuni"],
    "HISTORY_TEXTBOOK": [r"textbook"],
    "FORCED_LABOR": [r"forced labor", r"forced labour", r"forced mobilization", r"wartime labor"],
    "COLONIAL_RULE": [r"colonial rule", r"colonialism", r"colonial occupation"],
    "AGGRESSION": [r"aggression", r"aggressor"],
    "COMPENSATION_REPARATION": [r"compensation", r"reparation"],
    "APOLOGY_GENERAL": [r"apolog"],
    "WAR_GENERAL": [r"\bwar\b", r"wartime"],
}


def signals_for(text: str, term_map: dict) -> dict:
    lowered = text.lower()
    return {key: int(any(re.search(p, lowered) for p in patterns)) for key, patterns in term_map.items()}


def issue_primary_guess(text: str) -> str:
    hits = signals_for(text, ISSUE_SIGNAL_TERMS)
    for issue in ["COMFORT_WOMEN", "SEXUAL_SLAVERY", "NANJING", "YASUKUNI", "HISTORY_TEXTBOOK",
                  "FORCED_LABOR", "COLONIAL_RULE", "AGGRESSION", "COMPENSATION_REPARATION",
                  "APOLOGY_GENERAL", "WAR_GENERAL"]:
        if hits.get(issue):
            return issue
    return "HISTORICAL_RECOGNITION_GENERAL"


CODING_COLUMNS = [
    "record_id", "speaker_name", "speaker_position", "speaker_level",
    "issue_primary_suggested", "issue_secondary",
    "kingdon_problem", "kingdon_policy", "kingdon_politics", "kingdon_confidence",
    "apology", "explanation", "remorse", "reflection", "remedy", "pardon_or_forgiveness",
    "responsibility_actor", "agency_explicit", "audience_orientation",
    "source_language", "official_translation", "classification_confidence", "coder_notes",
]


def main():
    cfg = load_config()
    passages_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "candidate_passages.csv"
    if not passages_path.exists():
        print("No candidate_passages.csv found. Run 05_extract_relevant_passages.py first.")
        return

    out_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "coded_records.csv"
    signal_fields = list(SIGNAL_TERMS.keys())

    with open(passages_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        base_fields = reader.fieldnames
        rows = list(reader)

    out_fields = base_fields + signal_fields + CODING_COLUMNS
    out_rows = []
    for r in rows:
        text = f"{r.get('question_text','')} {r.get('response_text','')} {r.get('relevant_excerpt','')}"
        sig = signals_for(text, SIGNAL_TERMS)
        record = dict(r)
        record.update(sig)
        record["record_id"] = str(uuid.uuid4())
        record["issue_primary_suggested"] = issue_primary_guess(text)
        for col in CODING_COLUMNS:
            record.setdefault(col, "")
        record["classification_confidence"] = "LOW"  # forces manual/LLM review, see docstring
        record["coder_notes"] = "AUTO-DRAFT: keyword signals only; requires contextual coding per codebook.md before use."
        out_rows.append(record)

    write_header = not out_path.exists()
    with open(out_path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        if write_header:
            w.writeheader()
        w.writerows(out_rows)

    print(f"Drafted {len(out_rows)} records with keyword signals (all LOW confidence, pending contextual coding) -> {out_path}")


if __name__ == "__main__":
    main()
