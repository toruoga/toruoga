#!/usr/bin/env python3
"""
Stage 5: Split each candidate document into Q&A pairs / speech sections and
extract the passage(s) that actually concern a historical-recognition issue.

Heuristic Q&A splitter: looks for repeated "Question:" / "Q:" / "Reporter:"
style markers common to MOFA/Kantei/spokesperson-briefing transcripts. If no
Q&A structure is detected, the whole document is treated as a single SPEECH-
type section.

Output: data/metadata/candidate_passages.csv with:
  url, country, section_index, question_text, response_text, relevant_excerpt,
  matched_keywords_in_passage

relevant_excerpt is always a VERBATIM slice of the cleaned text (never
paraphrased), taken as the sentence(s) containing the matched keyword plus
one sentence of surrounding context.
"""
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import REPO_ROOT, load_config

QA_SPLIT_RE = re.compile(
    r"(?m)^(?:Question|Reporter|Q)\s*[:.]\s*", re.I
)
ANSWER_SPLIT_RE = re.compile(r"(?m)^(?:Foreign Minister|Prime Minister|Spokesperson|A|Answer)\s*[:.]\s*", re.I)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")


def split_qa(text: str) -> list[tuple[str, str]]:
    parts = QA_SPLIT_RE.split(text)
    if len(parts) <= 1:
        return []
    pairs = []
    for chunk in parts[1:]:
        m = ANSWER_SPLIT_RE.search(chunk)
        if m:
            q = chunk[: m.start()].strip()
            a = chunk[m.start():].strip()
        else:
            q, a = chunk.strip(), ""
        pairs.append((q, a))
    return pairs


def extract_excerpt(text: str, terms: list[str], context_sentences: int = 1) -> tuple[str, list[str]]:
    sentences = SENTENCE_SPLIT_RE.split(text)
    lowered_terms = [t.lower() for t in terms]
    hit_indices = []
    hits = set()
    for i, s in enumerate(sentences):
        sl = s.lower()
        for t in lowered_terms:
            if t in sl:
                hit_indices.append(i)
                hits.add(t)
                break
    if not hit_indices:
        return "", []
    excerpt_indices = set()
    for i in hit_indices:
        for j in range(max(0, i - context_sentences), min(len(sentences), i + context_sentences + 1)):
            excerpt_indices.add(j)
    excerpt = " ".join(sentences[j] for j in sorted(excerpt_indices))
    return excerpt.strip(), sorted(hits)


def main():
    cfg = load_config()
    cand_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "candidate_documents.csv"
    if not cand_path.exists():
        print("No candidate_documents.csv found. Run 04_filter_history_documents.py first.")
        return

    terms = cfg["search_terms"]
    out_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "candidate_passages.csv"
    fields = ["url", "country", "institution", "document_title", "document_type_guess", "date_guess",
              "section_index", "question_text", "response_text", "relevant_excerpt", "matched_keywords_in_passage"]

    already_seen = set()
    if out_path.exists():
        with open(out_path, newline="", encoding="utf-8") as f:
            already_seen = {r["url"] for r in csv.DictReader(f)}

    rows = []
    with open(cand_path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["url"] in already_seen:
                continue
            cleaned_path = REPO_ROOT / r["cleaned_file"]
            text = cleaned_path.read_text(encoding="utf-8", errors="ignore") if cleaned_path.exists() else ""
            qa_pairs = split_qa(text)
            if qa_pairs:
                for idx, (q, a) in enumerate(qa_pairs):
                    excerpt, hits = extract_excerpt(q + " " + a, terms)
                    if not excerpt:
                        continue
                    rows.append({
                        "url": r["url"], "country": r["country"], "institution": r["institution"],
                        "document_title": r["document_title"], "document_type_guess": r["document_type_guess"],
                        "date_guess": r["date_guess"], "section_index": idx,
                        "question_text": q, "response_text": a,
                        "relevant_excerpt": excerpt, "matched_keywords_in_passage": ";".join(hits),
                    })
            else:
                excerpt, hits = extract_excerpt(text, terms, context_sentences=2)
                if not excerpt:
                    continue
                rows.append({
                    "url": r["url"], "country": r["country"], "institution": r["institution"],
                    "document_title": r["document_title"], "document_type_guess": r["document_type_guess"],
                    "date_guess": r["date_guess"], "section_index": 0,
                    "question_text": "", "response_text": text,
                    "relevant_excerpt": excerpt, "matched_keywords_in_passage": ";".join(hits),
                })

    write_header = not out_path.exists()
    with open(out_path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if write_header:
            w.writeheader()
        w.writerows(rows)

    print(f"Extracted {len(rows)} candidate passages -> {out_path}")


if __name__ == "__main__":
    main()
