# Pilot Coverage Report — Japan, 2020–2025

## Status: BLOCKED before data collection could begin

This pilot could not download or verify a single official government page.
Every attempt to reach `www.mofa.go.jp` and `japan.kantei.go.jp` (and, as
controls, `www.mofa.go.kr` and `en.wikipedia.org`) via both the `WebFetch`
tool and direct `curl` failed with the same cause:

```
curl: (56) CONNECT tunnel failed, response 403
[agent-proxy] connect_rejected (the egress proxy denied the CONNECT — organization policy)
```

This is the execution environment's outbound network policy (set when the
environment was created — see "network policy" in the environment
description), not a per-site failure, a rate limit, or a robots.txt
restriction. `WebSearch` (which runs server-side, outside this sandbox's
proxy) did work and surfaced real candidate URLs, logged in
`data/logs/search_log.csv`, but a search snippet is not a verified page —
using it to populate a corpus record would violate the task's own
non-hallucination rule (Section 21) and provenance rule (Section 14, "must
be opened and verified").

## Coverage table (2020–2025, Japan)

| Year | Archive pages searched | URLs discovered | Downloaded | Keyword hits | Accepted | Rejected | Inaccessible | Manual review |
|------|------------------------|------------------|------------|---------------|----------|----------|--------------|---------------|
| 2020 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2021 | 0 | 2 (search-discovered) | 0 | 0 | 0 | 0 | 2 | 0 |
| 2022 | 0 | 4 (search-discovered) | 0 | 0 | 0 | 0 | 4 | 0 |
| 2023 | 0 | 1 (search-discovered) | 0 | 0 | 0 | 0 | 1 | 0 |
| 2024 | 0 | 1 (search-discovered) | 0 | 0 | 0 | 0 | 1 | 0 |
| 2025 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

("Archive pages searched" = 0 because `01_discover_urls.py`'s archive-crawl
step itself requires the same blocked network access; the discovered rows
above came only from `WebSearch`, not from crawling.)

## Speaker-level distribution

Not computable — 0 accepted records.

## Issue distribution

Not computable — 0 accepted records.

## What worked

- The full 9-stage pipeline (`scripts/01`–`09`), `config.yaml`,
  `codebook.md`, directory scaffolding, deduplication logic, validation
  logic, and CSV schema are built and are unit-testable against any HTML
  fixture once real pages are reachable.
- `WebSearch` successfully located plausible official-domain candidate URLs
  (e.g. Kishida's and Suga's August 15 War Dead Memorial Ceremony addresses,
  MOFA's "History Issues Q&A" and postwar-policy index pages) for later
  processing.

## What failed

- Zero pages could be downloaded, so zero records could be verified,
  extracted, coded, or exported. The pilot CSVs (`pilot_japan_2020_2025.csv`,
  `pilot_manual_review.csv`, `pilot_exclusion_log.csv`,
  `pilot_validation_report.csv`) are therefore header-only — deliberately,
  rather than populated with unverified or fabricated content.

## Likely coverage gaps (once network access exists)

- MOFA's official Press Releases/Press Conferences archives are paginated
  by month; `01_discover_urls.py`'s archive-crawl step will need the actual
  monthly index URLs enumerated (template placeholders currently marked
  `SKIPPED_TEMPLATE_NEEDS_SEED` in `config.yaml`/`01_discover_urls.py`).
- Kantei's statement/action archives are keyed by administration slug
  (`101_kishida`, `100_kishida`, `99_suga`, `98_abe3`, etc.) and by
  year-month; these slugs must be enumerated per administration covering
  2020–2025 (Abe through late 2020, Suga 2020–2021, Kishida 2021–2024,
  Ishiba from late 2024).
- Some Diet/Cabinet answers relevant to "written response" document_type
  are hosted on `www.shugiin.go.jp`/`www.cao.go.jp` rather than MOFA/Kantei
  directly — worth confirming against Section 2's source list before
  excluding them as NOT_OFFICIAL.

## Proposed fixes before scaling

1. Re-run this pipeline from an environment (or with an updated network
   policy on this one) that allows outbound HTTPS to `mofa.go.jp`,
   `kantei.go.jp`, `mofa.go.kr`, `mfa.gov.cn`, and `gov.cn`.
2. Enumerate Kantei administration slugs and MOFA monthly archive URLs for
   2020–2025 and seed them via `01_discover_urls.py --seed-urls` or a small
   slug-list addition to `config.yaml`.
3. Once `06_classify_records.py` produces draft records, perform the
   contextual coding pass described in `README.md` before treating any
   record as final (`classification_confidence` above `LOW`).
4. Only then generate the real `coverage_report.md`, `validation_report.csv`,
   and `human_validation_sample.csv` from actual data.
