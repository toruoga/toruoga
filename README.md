# East Asia Historical Recognition Corpus

Reproducible corpus/CSV of official Japanese, South Korean, and Chinese
government statements on historical-recognition issues (war responsibility,
colonial rule, comfort women, Yasukuni, forced labor, apology, compensation,
etc.), 2000-01-01 through 2025-12-31. See `codebook.md` for the full coding
scheme and `config.yaml` for source lists, keyword lists, and crawl settings.

## ⚠️ Current status: Stage 1 pilot blocked by network access

This repository currently contains the **full pipeline scaffolding**
(scripts, config, codebook) but **no verified corpus records yet**. The
Stage 1 pilot (Section 24 of the task spec: Japan, 2020–2025) could not be
completed in the session that built this scaffolding because outbound
network access to every required official domain
(`mofa.go.jp`, `kantei.go.jp`, `mofa.go.kr`, `mfa.gov.cn`, `gov.cn`, and even
`en.wikipedia.org` as a control) was blocked by that environment's egress
policy (confirmed via both the `WebFetch` tool and direct `curl`, which
returned `CONNECT tunnel failed, response 403` / "denied by organization
policy"). Only GitHub's own API was reachable; a web-search tool that runs
server-side (not through the local proxy) also worked, but it returns
snippets only, and this project's own integrity rules (Section 14/21 of the
spec) forbid building a record from a search snippet instead of the opened,
verified page.

Real candidate URLs discovered via search during that session are logged in
`data/logs/search_log.csv` and `inaccessible_sources.csv` (reason:
`EGRESS_BLOCKED`) rather than being used to fabricate record text.

**To actually populate the corpus**, run this pipeline from an environment
whose network policy allows outbound HTTPS to the domains in `config.yaml`
(`sources:` section) — e.g. locally, or in a Claude Code on the web
environment configured with a permissive/allowlisted network policy that
includes those government domains.

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
# Optionally seed with search-discovered URLs, e.g.:
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
