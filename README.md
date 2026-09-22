# East Asia Historical Recognition Corpus

Reproducible corpus/CSV of official Japanese, South Korean, and Chinese
government statements on historical-recognition issues (war responsibility,
colonial rule, comfort women, Yasukuni, forced labor, apology, compensation,
etc.), 2000-01-01 through 2025-12-31. See `codebook.md` for the full coding
scheme and `config.yaml` for source lists, keyword lists, and crawl settings.

## Current status: Stage 1 pilot (Japan, Korea, China, 2020–2025) — 30/country main axis reached, real data

A later session re-tested network access and found the picture had changed
from the original blocker (see "Network access notes" below), then ran the
pipeline for real across all three countries. A 2026-09-22 phase 2 session
(see `pilot_coverage_report.md`), scoped for a low-priority Japan-journal paper
rather than a full-scale international-journal version, then improved
Korea's and China's discovery methods for real (not just more hand
search — see below) and added a first pre-2020 landmark anchor, bringing
the main axis to 34 records (Japan 16, Korea 10, China 8). Later the same
session, the user set a 30/country scaling target and the pilot was pushed
to it in Japan → Korea → China order, reaching **90 main-axis records
(30/30/30)** — see `pilot_coverage_report.md`'s "History of the scaling
target" section for the discovery methods used per country in that push. A
final round then added 4 Japan Foreign-Minister-level (`speaker_level=
MINISTER`) records via Wayback Machine snapshots of the blocked
`www.mofa.go.jp`, closing a gap where Japan's sample was HEAD-level only —
see `pilot_coverage_report.md`'s "Round 4" section — bringing the corpus to
94 main-axis records (Japan 34, Korea 30, China 30). A final round then
fully reviewed and dispositioned every one of the 718 rows in Japan's
`pilot_manual_review.csv` backlog (7 promoted with a recorded reason each,
711 excluded with a recorded reason each — nothing left pending), adding a
5-record Battle of Okinawa Memorial Ceremony Address series, an earlier
(Jan 2022) point in the Sado Island Gold Mines dispute thread, and a
Japan-U.S. Iwo-To reconciliation-ceremony address — see
`pilot_coverage_report.md`'s "Round 5" section — bringing the corpus to
its current **101 main-axis records (Japan 41, Korea 30, China 30)**. See
`pilot_coverage_report.md` for the full numbers. Summary of the current
state:

- **Japan**: `japan.kantei.go.jp` reachable; `www.mofa.go.jp` blocked
  site-wide (Akamai WAF `403`, independent of headers) — Wayback Machine
  snapshots substitute where MOFA content is needed. 1096 URLs
  discovered via a real archive crawl of every 2020–2025 administration's
  monthly statement archives, 1081 downloaded, 746 kept after the keyword
  filter. **41 fully contextually coded** (`pilot_japan_2020_2025.csv`,
  37 HEAD + 4 MINISTER), up from an initial 10: two further
  proximity-keyword sweeps of the backlog found 6 then 12 more genuinely
  on-topic candidates (a 6-record batch including an Okinawa memorial
  press conference and a forced-labor temporal series, then a 12-record
  Hiroshima/Nagasaki Peace Memorial Ceremony batch spanning
  Abe/Suga/Kishida/Ishiba), plus one deliberate silence/omission record
  (Kishida's July 2024 Sado Island Gold Mines UNESCO message, which omits
  the wartime forced-Korean-labor dispute that was the actual story behind
  the inscription); a further round added 4 Foreign Minister
  (`speaker_level=MINISTER`) records via Wayback snapshots of
  `www.mofa.go.jp` (Motegi 2020, Hayashi ×2 2022, Kamikawa 2024 — the last
  a same-day MINISTER-level companion to the Kishida Sado silence record
  above), closing the corpus's HEAD-only gap for Japan; a final round then
  fully reviewed all 718 `pilot_manual_review.csv` backlog rows and
  promoted 7 more (the Battle of Okinawa Memorial Ceremony Address series,
  2020/2021/2023/2024/2025; a Jan 2022 Sado Mines UNESCO-nomination press
  conference, an earlier point in the same dispute thread as the July 2024
  silence message; a March 2025 Japan-U.S. Iwo-To reconciliation-ceremony
  address), closing the backlog entirely (0 rows now pending).
- **Korea**: `en.president.go.kr` (current, Lee Jae Myung administration)
  and `webarchives.pa.go.kr` (the National Archives of Korea's official web
  archive, covering the Moon Jae-in and Yoon Suk Yeol eras whose original
  English-language domains are now DNS-dead) both reachable;
  `www.mofa.go.kr` blocked site-wide (TLS ClientHello reset, independent
  of headers — same class of block as MOFA Japan) for automated crawling,
  though its content is directly fetchable by URL once found via search
  (used extensively in the final push below). The current administration's
  listing turned out to load via an AJAX POST
  (`/ajaxf/frBoard/bbsViewGalleryList.do`), not the dead end an earlier
  session assumed from the `?page=N` GET failing — a single call returns
  the full listing. The Moon-era National Archives listing also supports
  real `?page=N` pagination; the Yoon-era one does not (its snapshot only
  ever captured page 1 of each category — a hard limit, confirmed
  unfixable). **30 fully contextually coded**, up from an initial 10 (6
  hand-verified + 4 archive-crawled) via a final push that added: the
  `eng.president.go.kr/speeches/*` path (distinct from `/briefing/*`,
  found via Wayback CDX), a 6-year (2021-2026) MOFA Spokesperson
  textbook-protest statement series (found via web search identifying the
  `mofa.go.kr` press-release board's `seq=` numbering, then fetched live),
  a MOFA Yasukuni statement, two March First Independence Day addresses, a
  Keio University lecture, and several Lee Jae Myung-era records.
- **China**: `www.mfa.gov.cn` reachable (with intermittent, retriable
  connection resets). Its press-conference archive
  (`mfa.gov.cn/eng/xw/fyrbt/lxjzh/index_N.html`) is real and date-ordered,
  but has a hard lower bound around July 2022 — earlier content isn't
  reachable through it at all, and there's no working site search, so
  finding relevant content means grepping full daily transcripts around
  known high-salience weeks (Yasukuni's biannual shrine festivals) rather
  than a keyword search. **30 fully contextually coded**, up from an
  initial 8 (5 hand-verified + 4 newly found, 1 stale) via a final push
  that added three new annual-commemoration genres: Dec 13 Nanjing
  Massacre Memorial Day (2021-2024), Sept 18 Mukden Incident sirens
  ceremony (2020, 2023, 2024), and July 7 Lugou/Marco Polo Bridge Incident
  commemoration (2021, 2023, 2024) — all found via targeted web search of
  `english.www.gov.cn`'s Xinhua/State Council news archive, since that
  archive's own page-number index turned out not to map linearly to
  dates. Also added the corpus's first HEAD-level China records outside
  the Sept 3, 2025 Xi speeches: three Xi-Japan PM APEC-summit readouts
  (2022, 2023, 2024).
- **101 main-axis records total are fully contextually coded** per
  `codebook.md` (read in full, not keyword-matched) — Japan 41 (37 HEAD +
  4 MINISTER), Korea 30, China 30 — see `pilot_east_asia_2020_2025.csv`
  for all 101, or the per-country file (`pilot_japan_2020_2025.csv`).
  Every row's
  `coder_notes` documents the specific textual basis for every field,
  including explicitly-flagged borderline calls. Several Korea/China
  records added in the final push use a wire-service report (Xinhua, or
  Yonhap via Korea Times/Korea Herald) quoting an official statement
  directly, rather than a directly-fetched primary-source page, where the
  primary page could not be reached after repeated attempts — each such
  record is flagged in its own `coder_notes` with `classification_confidence`
  downgraded to `MEDIUM`.
- **Plus 1 pre-2020 landmark anchor** — the 1995 Murayama Danwa, retrieved
  via a Wayback Machine snapshot of the blocked `mofa.go.jp` — in the
  separate `landmark_anchors.csv`, kept apart from the main-axis file
  because it follows a different, purposive sampling design (historical
  flashpoints across 1995-2025, not the 2020-2025 window). See
  `pilot_coverage_report.md` for the rest of the planned anchor set (Koizumi's
  2001-2006 Yasukuni visits, the 2005 textbook controversy, the 2015
  Japan-Korea "comfort women" agreement, the 2018 Korea Supreme Court
  forced-labor ruling), blocked as of 2026-09-22 by a site-wide Internet
  Archive outage encountered mid-session.
- The Japan backlog (`pilot_manual_review.csv`, 718 keyword-matched
  candidates never contextually coded) has now been **fully reviewed and
  closed**: every row was individually dispositioned (7 promoted above, 711
  excluded with a recorded reason each, tracked in the file's own
  `full_review_status`/`full_review_reason` columns — see
  `pilot_coverage_report.md`'s "Round 5" section). As expected from the
  keyword filter's deliberately recall-oriented design (it also matches,
  e.g., "war" in statements about Ukraine, or "victims" in disaster-relief
  statements), the large majority resolved to genuinely unrelated content —
  COVID-19/pandemic press conferences, Ukraine/Russia-related "war"
  mentions, natural-disaster condolences, and generic diplomatic messages
  to third countries account for most of the 711 exclusions. 0 rows remain
  pending.

**Scaling this beyond the pilot** now means primarily new discovery, since
Japan's backlog is closed: separately resolving MOFA Japan/Korea access
(both remain blocked at the network level as of 2026-09-22 — see "Network
access notes" below); improving discovery for China's State Council source
(real and working at `english.www.gov.cn/news/page_N.html`, but its
page-number index does not map linearly to dates — a `site:` web-search
workaround for its broken in-site search was found but not yet fully
exploited, see `pilot_coverage_report.md`'s "China State Council discovery"
section); and extending `landmark_anchors.csv` with the four still-planned
pre-2020 flashpoints, currently blocked on a `web.archive.org` outage (same
section). Korea's live-site pagination, previously thought JS-only, turned
out to be a discoverable AJAX endpoint (see `pilot_coverage_report.md`), so
that specific gap is resolved; its Yoon-era archive gap is a confirmed
final limit instead (same section). The genre/speaker-level/administration
confound stress-test and the paper's quantitative tables have already been
re-run against the 90-record (30/30/30) sample and again, for Japan's
speaker-level split, against the 94-record sample — see
`pilot_coverage_report.md`'s "Confound stress-test" and "Round 4" sections;
re-running it once more against the current 101-record sample (which adds
7 more Japan HEAD-level records from the backlog review, not new
speaker-level data) is a lower-priority follow-up than folding the
existing 94-record speaker-level finding into `draft_paper_ja.md` itself,
which has not yet been done.

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
- **Korea**: `www.mofa.go.kr` and its embassy subdomains (`*.mofa.go.kr`)
  reset the TLS connection at the ClientHello regardless of headers/UA —
  the same class of block as MOFA Japan, confirmed reproducible (not a
  one-off flake) and not fixed by retrying. `eng.president.go.kr` /
  `english1.president.go.kr` / `english.president.go.kr` (the pre-Lee-
  administration English presidential domains) do not resolve at all
  (DNS `NXDOMAIN`, confirmed via both this environment's proxy and
  WebFetch's independent network path) — genuinely retired when the
  presidential administration changed (Yoon → Lee, June 2025), not
  blocked. Their content is preserved verbatim on
  `webarchives.pa.go.kr` (the National Archives of Korea's official
  web-archiving service) at
  `http://webarchives.pa.go.kr/<ordinal>th/<original-host>/<original-path>`
  — `19th` for Moon Jae-in, `20th` for Yoon Suk Yeol (ordinals per
  `https://japan.kantei.go.jp/past_cabinet/` \-style numbering, but on
  the Korean side at `https://en.president.go.kr/eng/index.do`'s "Previous
  Presidents" equivalent). The current administration's live site,
  `en.president.go.kr`, is reachable directly but paginates its
  `/president/statements-remarks` index via client-side JS — `?page=N`
  query strings return no additional links over plain HTTP GET, so it
  could not be archive-crawled the way Kantei was within this pilot;
  candidate URLs were found via targeted web search instead.
- **China**: `www.mfa.gov.cn` and `english.www.gov.cn` are both reachable,
  but intermittently reset the TLS connection mid-handshake (not a hard
  block — retrying the same request, sometimes seconds later, routinely
  succeeds; observed ~1-in-3 failure rate). `config.yaml`'s
  `english.www.gov.cn/news/` section is a general links/portal page
  (links to ~200 unrelated provincial government offices), not a news
  article archive as originally assumed — do not treat its crawl results
  as candidate documents without checking first. MFA China's real,
  working "Regular Press Conferences" archive is
  `https://www.mfa.gov.cn/eng/xw/fyrbt/lxjzh/index_1.html` (config.yaml's
  `xwfw_665399/s2510_665401/` path redirects to an unrelated treaties
  page — stale, like Kantei's and Korea's pre-redesign URLs).

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
