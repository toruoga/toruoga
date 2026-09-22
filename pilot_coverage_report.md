# Pilot Coverage Report — Japan, 2020–2025

## Status: real data collected; 10 records fully contextually coded, 737 pending

An earlier session in this repository's history reported the pilot fully
blocked by an org-level egress policy denying every government domain
(`mofa.go.jp`, `kantei.go.jp`, `mofa.go.kr`, and even `en.wikipedia.org` as
a control). A later session re-tested and found that policy no longer in
effect: `en.wikipedia.org` and `mfa.gov.cn` are reachable directly, and
`japan.kantei.go.jp` — the earlier 404s were actually the site rejecting
curl's bare default `User-Agent`, not an access block — is reachable with
any explicit UA (the pipeline's own `AcademicResearchBot/1.0`, already
configured, works). `www.mofa.go.jp` remains genuinely blocked, now
confirmed as the site's own Akamai WAF returning `403 Access Denied`
regardless of headers/UA (tested with both `curl` and `WebFetch`) — a
per-site block, not an environment policy issue. See "Network access
notes" in `README.md` for full detail.

## Coverage table (2020–2025, Japan)

Per-year columns are computed by extracting the `YYYYMM` segment from each
URL's path. This is exact for "URLs discovered" (grouped by the monthly
archive page it was crawled from). "Downloaded" and "kept after keyword
filter" are grouped by the *document's own* URL month, which occasionally
differs by one adjacent month from its archive page (e.g. a "previous
month" navigation link on a January index page pointing to a December
document) — real boundary noise from the crawl, not an error; the **Total**
row is exact regardless.

| Year | URLs discovered (by archive month) | Downloaded (by document URL month) | Kept after keyword filter (by document URL month) |
|------|--------------------------------------|--------------------------------------|------------------------------------------------------|
| 2020 | 106 | 53 | 39 |
| 2021 | 187 | 176 | 115 |
| 2022 | 222 | 180 | 146 |
| 2023 | 169 | 156 | 115 |
| 2024 | 206 | 196 | 139 |
| 2025 | 206 | 207 | 158 |
| pre-2020 / post-2025 stragglers (adjacent-month nav links) | — | 24 | 6 |
| **Total** | **1096** | **1081** *(1081 successful of 1096 attempted; 15 failed — see below)* | **747** *(one document, an `index.html` itself, was picked up as a candidate — see coder_notes discipline in Stage 6)* |

The 10 fully-coded records (`pilot_japan_2020_2025.csv`) are dated 2020-08-15,
2021-01-08, 2021-08-15, 2022-08-15, 2023-03-06, 2023-03-16, 2023-08-15,
2024-08-15, 2025-08-15 (×2) — i.e. at least one coded record in every
pilot year. The other 737 keyword-filtered candidates are pending
contextual coding (`pilot_manual_review.csv`), unevenly distributed across
2020–2025 per the "kept after keyword filter" column above.

The 15 download failures were robots.txt-disallowed social/third-party
links (Twitter, Facebook, a gov-online.go.jp video portal) and
pre-2020/MOFA URLs incidentally linked from in-range Kantei archive pages
— see `inaccessible_sources.csv` for the full list with reasons.

MOFA (`www.mofa.go.jp`) contributed **0** documents — blocked site-wide;
see `inaccessible_sources.csv` for the specific URLs attempted (some
entries from the earlier session's "EGRESS_BLOCKED" diagnosis remain in
that log verbatim for history; the underlying URLs are still inaccessible,
just for the corrected reason above).

## Speaker-level distribution (10 coded records)

All 10 records: `speaker_level = HEAD` (Prime Minister). Speakers: ABE
Shinzo (1), SUGA Yoshihide (2), KISHIDA Fumio (5), ISHIBA Shigeru (2).

## Issue distribution (10 coded records)

- `WAR_GENERAL`: 6 (the six annual Aug 15 National Memorial Ceremony
  addresses, 2020–2025)
- `FORCED_LABOR`: 2 (Kishida, March 2023)
- `COMFORT_WOMEN`: 1 (Suga, January 2021)
- `HISTORICAL_RECOGNITION_GENERAL`: 1 (Ishiba's Aug 15, 2025 press
  conference on "recognition of history")

## Notable substantive finding

The six annual Aug 15 addresses show a consistent pattern across Abe
(2020), Suga (2021), and Kishida (2022–2024): domestically-oriented
mourning for Japan's own war dead, with no apology, no remorse language,
and no reference to foreign victims of Japanese aggression/colonial rule —
a marked contrast with landmark anniversary statements (Murayama 1995,
Koizumi 2005, Abe's 70th-anniversary statement 2015). Ishiba's 80th
Memorial Ceremony address (August 15, 2025) breaks this pattern, using the
word "remorse" for the first time in this annual address in 13 years — a
change Ishiba directly addresses in the same-day press conference record
also included in the pilot, where he frames it as consistent with, not a
departure from, "the position held by previous administrations." Both
records are in `pilot_japan_2020_2025.csv` with `coder_notes` documenting
the textual basis.

## What worked

- The full 9-stage pipeline (`scripts/01`–`09`), `config.yaml`,
  `codebook.md`, directory scaffolding, deduplication logic, validation
  logic, and CSV schema all ran end-to-end against real data.
- `scripts/01_discover_urls.py` was extended with `--seed-index-urls` to
  crawl resolved administration-slug/month archive pages (the config.yaml
  `{pm_slug}` templates require this manual resolution step — see
  `https://japan.kantei.go.jp/past_cabinet/index.html` for the
  slug-to-date mapping used).
- 1081 real, verified pages were downloaded and retained verbatim.
- 10 records were fully read in context and coded per `codebook.md`
  (not keyword-matched) — see `coder_notes` on each row in
  `pilot_japan_2020_2025.csv` for the specific textual basis of every
  field, including borderline calls flagged for a second look.

## What is still pending

- 737 real, downloaded, keyword-filtered candidates have not yet been
  contextually coded (`pilot_manual_review.csv`, all
  `classification_confidence=LOW`). Given the filter's deliberate
  recall-orientation (matches generic terms like "war", "fund",
  "aggression", "victim" — mostly hits on Ukraine, North Korea, natural
  disasters, and COVID-19 press conferences, not Japan's own historical
  recognition), most of these are expected to resolve to `OTHER`/excluded
  on review, not to additional historical-recognition records — but that
  determination requires the same per-document contextual reading applied
  to the 10 coded records, which this pilot did not have scope to
  complete for all 747.
- MOFA (`www.mofa.go.jp`) is entirely unrepresented; its "History Issues
  Q&A" (`faq16.html`) and postwar-policy pages in particular would likely
  add COMFORT_WOMEN/SEXUAL_SLAVERY/HISTORY_TEXTBOOK records this Kantei-
  only pilot cannot surface (Kantei's PM statements skew toward war
  memorial and forced-labor/diplomatic-summit genres; MOFA's spokesperson
  briefings are where textbook and comfort-women legal-position statements
  are typically most detailed).
- Korea and China were out of scope for this pilot (Japan-only per the
  task spec's Section 24).

## Proposed next steps

1. Continue the contextual-coding pass over `pilot_manual_review.csv`
   (737 rows), reading each full document (not the `relevant_excerpt`
   alone, which is a keyword-context slice) before assigning any code
   above `LOW` confidence.
2. Periodically re-test `www.mofa.go.jp` access (see README's "Network
   access notes"); if it opens up, re-run Stages 1–9 to add MOFA sources.
3. Once Japan coding is materially more complete, repeat discovery/
   download/coding for Korea (`eng.president.go.kr`, `www.mofa.go.kr`) and
   China (`english.www.gov.cn`, `www.mfa.gov.cn`) and re-run
   `07_deduplicate.py` onward across all three countries together.
