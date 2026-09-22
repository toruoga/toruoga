# East Asia Historical Recognition Corpus

Reproducible corpus/CSV of official Japanese, South Korean, and Chinese
government statements on historical-recognition issues (war responsibility,
colonial rule, comfort women, Yasukuni, forced labor, apology, compensation,
etc.), 2000-01-01 through 2025-12-31. See `codebook.md` for the full coding
scheme and `config.yaml` for source lists, keyword lists, and crawl settings.

## Current status: Stage 1 pilot (Japan, 2020–2025) — partially coded, real data

A later session re-tested network access and found the picture had changed
from the original blocker (see "Network access notes" below):

- **`japan.kantei.go.jp`** (Prime Minister's Office) is reachable. 1096
  candidate document URLs were discovered by crawling the real monthly
  statement archives for every 2020–2025 administration (Abe → Suga →
  Kishida → Ishiba), 1081 pages were downloaded and retained verbatim under
  `data/raw/japan/`, and 747 passed the Stage 4 keyword filter.
- **`www.mofa.go.jp`** (Ministry of Foreign Affairs) remains genuinely
  blocked — Akamai's edge WAF returns `403 Access Denied` regardless of
  User-Agent or request headers, confirmed with both `curl` and `WebFetch`.
  This source is absent from the pilot; see `inaccessible_sources.csv`.
- Of the 747 keyword-filtered candidates, **10 have been fully
  contextually coded** per `codebook.md` (read in full, not
  keyword-matched) and are in `pilot_japan_2020_2025.csv`:
  the six annual August 15 National Memorial Ceremony for the War Dead
  addresses (2020–2025, spanning Abe/Suga/Kishida/Ishiba), Prime Minister
  Ishiba's same-day press conference explaining his reintroduction of
  "remorse" language after a 13-year gap, Prime Minister Suga's January
  2021 press conference on the comfort-women court case, and two records
  from the March 2023 Kishida-Yoon rapprochement (the forced-labor-issue
  press conference and the joint press conference restarting "shuttle
  diplomacy").
- The remaining **737 candidates are real, downloaded, keyword-matched
  documents that have not yet been contextually coded** — the keyword
  filter is deliberately recall-oriented (it also matches, e.g., "war" in
  statements about Ukraine, or "victims" in disaster-relief statements),
  so most of the 737 are expected to be coded `OTHER`/excluded once
  reviewed, not additional historical-recognition records. They are in
  `pilot_manual_review.csv` with `classification_confidence=LOW`,
  per the pipeline's design (`06_classify_records.py` never assigns
  substantive codes by keyword alone).

**Scaling this beyond the pilot** means continuing the contextual-coding
pass over `pilot_manual_review.csv`, then re-running `07_deduplicate.py`,
`08_validate.py`, `09_export_csv.py`; and separately resolving MOFA
access (see below) and doing the same discovery/download/code cycle for
Korea and China.

## Network access notes (for future sessions)

- The org-level egress block reported by an earlier session in this
  environment (`CONNECT tunnel failed, response 403` to every government
  domain, including `en.wikipedia.org` as a control) is **no longer
  present** — `curl`/`WebFetch` reach `en.wikipedia.org`, `mfa.gov.cn`, and
  `japan.kantei.go.jp` directly now.
- `japan.kantei.go.jp` returns a **fake-looking custom 404 page** to
  requests with curl's bare default `User-Agent` (or no UA override at
  all) — this is what the earlier session's `curl` probes without a UA
  header actually hit, not a real block. Any explicit `User-Agent` header
  (browser-style or the pipeline's own `AcademicResearchBot/1.0`,
  already set in `config.yaml`) gets a real `200` with real content. All
  of this pipeline's scripts already send that UA, so no further change
  is needed to crawl Kantei.
- `www.mofa.go.jp` is blocked at the site's own edge (Akamai WAF, `403
  Access Denied`) independent of User-Agent — this is a real per-site
  block, not an environment/org policy issue, and headers/UA spoofing do
  not bypass it. Re-test periodically; if still blocked, MOFA content for
  this corpus needs a different network path (e.g. a residential/non-
  datacenter egress IP) or must be sourced from Kantei's mirrored
  statements where available.
- Kantei's site was redesigned at some point after the original archive
  URLs (`https://japan.kantei.go.jp/{pm_slug}/statement/{YYYYMM}/...`)
  were indexed by search engines; those exact URLs are still live and
  correct (verified), but the administration-slug-to-date mapping had to
  be re-derived from `https://japan.kantei.go.jp/past_cabinet/index.html`
  (see git history of `scripts/01_discover_urls.py` for the resolved
  slugs/date ranges used: `98_abe`, `99_suga`, `100_kishida`,
  `101_kishida`, `102_ishiba`, `103`, `104` for 2020-01 through 2025-12).

## Pipeline

```
01_discover_urls.py          -- crawl archive/index pages; log search-derived URLs
02_download_pages.py         -- download + save raw HTML (never overwritten)
03_extract_metadata.py       -- clean text, guess title/date/doc-type
04_filter_history_documents.py -- keyword filter + source/date exclusion
05_extract_relevant_passages.py -- split Q&A, extract verbatim excerpts
06_classify_records.py       -- keyword SIGNALS only; real coding needs
                                 contextual review per codebook.md (see below)
07_deduplicate.py            -- group duplicates across official mirrors
08_validate.py                -- validation_report.csv + manual_review.csv
09_export_csv.py             -- data/output/corpus.csv +
                                 data/output/human_validation_sample.csv
```

### Reproduction steps

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python3 scripts/01_discover_urls.py --country japan
# config.yaml's Kantei sections are {pm_slug} templates (the site has no
# single "all statements" index); resolve slugs/months and crawl them as a
# further archive level with --seed-index-urls, e.g.:
python3 scripts/01_discover_urls.py --country japan --seed-index-urls \
  "https://japan.kantei.go.jp/101_kishida/statement/202208/index.html"
# --seed-urls (singular) instead enqueues specific document URLs directly,
# e.g. from search-discovered candidates:
python3 scripts/01_discover_urls.py --country japan --seed-urls \
  "https://japan.kantei.go.jp/101_kishida/statement/202208/_00006.html"

python3 scripts/02_download_pages.py
python3 scripts/03_extract_metadata.py
python3 scripts/04_filter_history_documents.py
python3 scripts/05_extract_relevant_passages.py
python3 scripts/06_classify_records.py
```

At this point, **stop and perform contextual coding**: open
`data/metadata/coded_records.csv`, and for every row, read the full passage
(`question_text` + `response_text` + `relevant_excerpt`, plus the raw file
under `data/raw/<country>/` if more context is needed) and fill in, per
`codebook.md`: `speaker_name`, `speaker_position`, `speaker_level`,
`issue_primary` (starting from `issue_primary_suggested`, override if wrong),
`issue_secondary`, `kingdon_problem/policy/politics` + `kingdon_confidence`,
`apology`/`explanation`/`remorse`/`reflection`/`remedy`/
`pardon_or_forgiveness`, `responsibility_actor`, `agency_explicit`,
`audience_orientation`, `source_language`, `official_translation`, and raise
`classification_confidence` from `LOW` once done. This step is intentionally
not automated — codebook.md and the task spec both require contextual
judgment, not keyword matching, for these fields.

```bash
python3 scripts/07_deduplicate.py
python3 scripts/08_validate.py
python3 scripts/09_export_csv.py
```

Final outputs: `data/output/corpus.csv`,
`data/output/human_validation_sample.csv`, `validation_report.csv`,
`manual_review.csv`, plus `exclusion_log.csv` and `inaccessible_sources.csv`
accumulated throughout the run.

### Coverage report

After a run, compile `coverage_report.md` (Section 22) by aggregating
`data/metadata/discovered_urls.csv`, `download_log.csv`,
`candidate_documents.csv`, `data/output/corpus.csv`, `exclusion_log.csv`,
and `inaccessible_sources.csv` by country/year — there is no separate script
for this because the report's exact grouping tends to change with each
scaled run; a short pandas snippet over those five files is sufficient.

## Directory structure

```
data/
  raw/{japan,korea,china}/        raw HTML, never overwritten
  cleaned/{japan,korea,china}/    boilerplate-stripped plain text
  metadata/                       per-stage intermediate CSVs
  logs/                           search_log.csv, search_term_log.csv
  output/                         corpus.csv, human_validation_sample.csv
```

## Non-hallucination guarantees enforced by this pipeline

- A record only exists in `coded_records.csv`/`corpus.csv` if a page was
  actually downloaded (`02_download_pages.py`) and its raw HTML retained.
- `relevant_excerpt`/`question_text`/`response_text` are always verbatim
  slices of the cleaned text, never paraphrases (see `05_extract_relevant_passages.py`).
- Any field that cannot be reliably determined is written as `UNKNOWN`/`NA`,
  never guessed (see `06_classify_records.py`, `09_export_csv.py`).
- Pages that fail to download are logged to `inaccessible_sources.csv` with
  a reason; their text is never fabricated.
