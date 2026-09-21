#!/usr/bin/env python3
"""
Stage 7: Deduplicate coded records (Section 15).

Deduplication keys, applied in order:
  1. exact URL + section_index
  2. normalized title + date_guess
  3. sha256 of the relevant_excerpt (catches the same statement mirrored on
     two official domains, e.g. Kantei + MOFA reposting the same speech)

Records sharing any key are grouped into a duplicate_group_id (a stable
uuid5 derived from the group's sorted URLs). Within a group, canonical_record
= 1 is assigned to the row whose institution matches the preferred-source
order in config (Kantei > MOFA for Japan PM material; otherwise first seen);
all other members of the group get canonical_record = 0. No rows are
deleted -- provenance to every known official copy is retained.
"""
import csv
import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import REPO_ROOT, load_config, normalized_title, sha256_text

PREFERRED_INSTITUTION_ORDER = [
    "Prime Minister's Office of Japan (Kantei)",
    "Ministry of Foreign Affairs of Japan",
    "Office of the President, Republic of Korea",
    "Ministry of Foreign Affairs, Republic of Korea",
    "State Council of the People's Republic of China",
    "Ministry of Foreign Affairs of the People's Republic of China",
]


def group_key(row: dict) -> tuple:
    return (
        row["url"], row.get("section_index", ""),
        normalized_title(row.get("document_title", "")), row.get("date_guess", ""),
        sha256_text(row.get("relevant_excerpt", "")),
    )


def main():
    cfg = load_config()
    coded_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "coded_records.csv"
    if not coded_path.exists():
        print("No coded_records.csv found. Run 06_classify_records.py first.")
        return

    with open(coded_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)

    # Union-find over three separate key types
    parent = {i: i for i in range(len(rows))}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    by_url_section, by_title_date, by_excerpt_hash = {}, {}, {}
    for i, r in enumerate(rows):
        k1 = (r["url"], r.get("section_index", ""))
        k2 = (normalized_title(r.get("document_title", "")), r.get("date_guess", ""))
        k3 = sha256_text(r.get("relevant_excerpt", ""))
        for table, key in ((by_url_section, k1), (by_title_date, k2), (by_excerpt_hash, k3)):
            if key in table:
                union(i, table[key])
            else:
                table[key] = i

    groups = {}
    for i in range(len(rows)):
        groups.setdefault(find(i), []).append(i)

    out_fields = fields + ["duplicate_group_id", "canonical_record"]
    for members in groups.values():
        urls_sorted = sorted(rows[i]["url"] for i in members)
        group_id = str(uuid.uuid5(uuid.NAMESPACE_URL, "|".join(urls_sorted)))
        canonical_idx = members[0]
        best_rank = len(PREFERRED_INSTITUTION_ORDER)
        for i in members:
            inst = rows[i].get("institution", "")
            if inst in PREFERRED_INSTITUTION_ORDER:
                rank = PREFERRED_INSTITUTION_ORDER.index(inst)
                if rank < best_rank:
                    best_rank, canonical_idx = rank, i
        for i in members:
            rows[i]["duplicate_group_id"] = group_id
            rows[i]["canonical_record"] = 1 if i == canonical_idx else 0

    out_path = REPO_ROOT / cfg["paths"]["metadata_dir"] / "deduplicated_records.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        w.writeheader()
        w.writerows(rows)

    n_dupes = sum(1 for members in groups.values() if len(members) > 1 for _ in members[1:])
    print(f"{len(rows)} records -> {len(groups)} groups ({n_dupes} marked non-canonical). Output: {out_path}")


if __name__ == "__main__":
    main()
