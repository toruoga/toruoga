# Phase 2 plan: 2020-2025 main axis + landmark anchors (Japan-journal, non-full-scale version)

Agreed scope (see chat with user, 2026-09-22): the 法政論叢 invited paper stays
low-priority and does **not** attempt Japan-scale exhaustive archive crawling
for Korea/China, and does **not** attempt uniform 1990-2025 coverage (that
would require ~324 documents and re-solving URL discovery for all three
countries in the pre-2016 era, where Korea's older MOFA-hosted material is
already known to be ~0% recoverable per
`political_apology_vol4_url_liveness_check.csv`).

Instead:

- **Main axis**: 2020-2025, matching the existing pilot. Target ~15-16 fully
  coded records per country (Japan already has 10; Korea has 6; China has
  4-5). Add ~10 more candidates each for Korea and China via the sources
  below. Japan's existing 736-candidate keyword-filtered pool already covers
  this period more than adequately — no new Japan discovery needed for the
  main axis itself.
- **Landmark anchors**: a small, purposively-selected set of pre-2020
  historical-recognition flashpoints, added as qualitative reference points
  rather than a dense annual time series:
  1. 1995 Murayama Danwa (Japan)
  2. 2001-2006 Koizumi Yasukuni Shrine visits (Japan statement + Korea/China
     reactions)
  3. 2005 history-textbook controversy (Japan + Korea/China reactions)
  4. 2015 Japan-Korea "comfort women" agreement (Japan + Korea)
  5. 2018 Korea Supreme Court forced-labor ruling (Korea ruling context +
     Japan reaction)

All sourcing follows codebook.md Section 2: official government domains only,
Wayback Machine snapshots of an official domain are acceptable as a fallback
(same precedent as the vol.4 liveness check and the Korea
webarchives.pa.go.kr sourcing already in this repo), but third-party mirrors
(academic databases, news, Wikipedia) are not.

## Status tracker

| Item | Status | Notes |
|---|---|---|
| Japan: 1995 Murayama Danwa | **downloaded (raw+cleaned)** | via Wayback snapshot of mofa.go.jp (site itself blocked, intermittent resets on web.archive.org too — needed retries). Not yet contextually coded. |
| Japan: 2001-2006 Koizumi Yasukuni | **blocked** | Not on current Kantei site (redesigned); depends on Wayback. archive.org went fully offline site-wide 2026-09-22 ("Temporarily Offline" outage page) mid-session — retry next session. |
| Japan: 2005 textbook controversy | blocked | same Wayback dependency as above |
| Japan: 2015 CW agreement (Japan side) | blocked | likely on blocked mofa.go.jp/kantei; needs Wayback |
| Japan: 2018 forced-labor ruling (Japan reaction) | blocked | same |
| Korea: Koizumi Yasukuni reaction | not started | |
| Korea: 2005 textbook reaction | not started | |
| Korea: 2015 CW agreement (Korea side) | not started | |
| Korea: 2018 forced-labor ruling (Korea side) | not started | |
| China: Koizumi Yasukuni reaction | not started | |
| China: 2005 textbook reaction | not started | |
| **Korea main axis (2020-2025+)** | **+4 downloaded (raw+cleaned)** | Solved the JS-pagination problem for real: `en.president.go.kr`'s listing is an AJAX POST to `/ajaxf/frBoard/bbsViewGalleryList.do` (params in the page's `#sendForm`), not unreachable — just not a plain GET. A `pagePerCnt=100` POST returned the full 48-item listing for the current (Lee Jae Myung) administration in one call. 3 of the 48 are on-topic: 81st Liberation Day address (2026, `MK8xT9SG`), 80th Liberation Day address (2025, `96ecUYVL`), Korea-Japan summit joint statement with PM Takaichi (`VWkmhWnq`, mentions Chosei coal mine forced-labor remains repatriation). Separately, `webarchives.pa.go.kr`'s **Moon-era (19th)** listing at `.../BriefingSpeeches/Speeches?page=N` is a genuine, working archive crawl (plain GET pagination works, unlike the live site) — pulled ~200 titles across pages 1-20 (covers roughly Apr 2021-Mar 2022) and found Moon's 103rd March First Independence Movement Day address (2022-03-01, `Speeches/1157`), which has substantial Japan-colonial-history content ("Japan must squarely face history and be humble before it"). The **Yoon-era (20th)** archive listing at `eng.president.go.kr/speeches` is *not* similarly crawlable: `?page=N` returns the identical page-1 shell every time (the archived snapshot never captured the live AJAX backend for pages beyond 1) -- capped at the 5 items already visible on page 1, all already checked (none new/on-topic beyond what's coded). None of the 4 new Korea documents are contextually coded yet. |
| **China main axis (2020-2025)** | **+2 downloaded (raw+cleaned)**, method validated | `mfa.gov.cn/eng/xw/fyrbt/lxjzh/index_N.html` is a real date-paginated archive (~7 daily transcripts/page, index_1 = most recent), but it has a **hard lower bound around index_140 ≈ July 2022** (index_145+ all 302-redirect) — pre-mid-2022 China MFA content is not reachable through this path at all, archive or no archive. No site search endpoint exists (`search.fmprc.gov.cn` has a TLS cert mismatch), and article titles are always generic ("Regular Press Conference on DATE"), never topical — so finding historical-recognition content means downloading and grepping full daily transcripts one by one, not a keyword search. Targeting known high-salience weeks (Yasukuni's biannual shrine festivals, PM transitions) rather than crawling every day paid off: found (1) **Oct 17, 2025** — spokesperson response to PM Ishiba's masakaki offering and incoming PM Takaichi's personal monetary offering to Yasukuni, explicitly framed against "80th anniversary of victory" (a 4th Yasukuni-response instance, extending the existing Oct2023/Apr2024/Oct2024 pattern into the Ishiba-to-Takaichi transition); (2) **Apr 30, 2025** — a Japan-Philippines-summit question that pivots into Japan's WWII "aggression" and "colonial rule" over the Philippines and Nansha Qundao, a COLONIAL_RULE/WAR_GENERAL-coded instance distinct from the existing Yasukuni-heavy sample. Still want a few more (target ~10 total per country); Dec 13 Nanjing-memorial weeks (2022-2024) and Aug 15 (2022-2024) not yet checked — each check costs ~5-7 page fetches per candidate week for maybe 1 hit, so this is inherently slow, labor-per-document work, not a one-shot crawl. |

## Korea Yoon-era (20th) gap-filling attempt (② in the 2026-09-22 priority order)

Tried: `?pageIndex=N` (200 but same shell), `/speeches/list?page=N` (503),
and the sibling `/briefing` and `/visits` listings under
`webarchives.pa.go.kr/20th/eng.president.go.kr/`. `/briefing` has its own
5-item cap (same archived-snapshot limitation) and its one Japan-adjacent
item (a Nov 2024 Japan-ROK-US trilateral statement) turned out to be
security/economic only, no historical-recognition content, matching the
existing "non-engagement" pattern from Yoon's later terms rather than
adding a new instance. `/visits` returned no parseable items at all.

**Conclusion: this is a real, final limit, not a solvable crawl problem.**
The National Archives of Korea's snapshot of the Yoon-era site only
preserved page 1 of each listing category — there is no way to page further
back through this source. Korea's Yoon-era candidates stay at what's
already coded (3 Liberation Day addresses) plus what the current-admin
listing and Moon-era archive turned up this session. Reaching further into
Yoon-era Japan-relevant content would need a different source entirely
(e.g. targeted web search for specific known events, the same
hand-verification method the original pilot used).

## Contextual coding (③ in the 2026-09-22 priority order) -- complete

All 8 newly collected documents have been read in full and coded per
`codebook.md`, producing **9 records** (the Oct 17, 2025 China page yielded
two separate Q&A records: the Yasukuni response and a separate response
about Murayama Tomiichi's death) in `phase2_new_records.csv` (repo root,
same column schema as `pilot_east_asia_2020_2025.csv`). None are LOW
confidence, so none needed to be added to `manual_review.csv` (matching the
precedent set by the original 20-record pilot, which also kept its 9
MEDIUM-confidence records out of `pilot_manual_review.csv` -- that file is
reserved for keyword-matched-but-uncoded candidates, not fully-coded
records regardless of confidence).

Notable coding decisions:
- The Murayama 1995 Danwa is coded `HISTORICAL_RECOGNITION_GENERAL`
  (secondary: `COLONIAL_RULE;AGGRESSION;APOLOGY_GENERAL`) since it
  substantively covers all three rather than one narrow issue.
- All three China Yasukuni-response records (Aug 2022, Oct 2025, plus the
  three already in the main pilot file) code `reflection=0` despite
  containing "reflect on its history" language, following the established
  precedent: that phrase demands Japan's reflection, it is not China's own
  reflection on its own conduct. The same logic applies to the new
  Murayama-death response (`APOLOGY_GENERAL`, `apology=0`) -- it describes
  and endorses Murayama's historical apology rather than being one itself.
- The Korea-Japan summit joint statement (2026-05-19) is the lowest-
  confidence new record (`MEDIUM`): its sole relevant passage (Chosei coal
  mine remains DNA analysis) names no responsible actor
  (`responsibility_actor=UNSPECIFIED`, `agency_explicit=0`), and no
  "(Unofficial Translation)" marker was found on the page, so
  `official_translation=NA` rather than assumed.

## Running tallies after 2026-09-22 session

- Japan: 10 main-axis (unchanged) + 1 landmark anchor (Murayama 1995, coded)
- Korea: 6 → 10 candidates, +4 new ones now coded (9 records total incl.
  the 2-record China page = see below)
- China: 4-5 → 8 candidates, +3 new ones now coded (yielding 4 new records,
  since one page had 2 relevant Q&A pairs)
- **9 new fully-coded records** in `phase2_new_records.csv`, none LOW
  confidence. Combined with the original pilot's 20, phase 2 now has 29
  fully-coded records across the two files (not yet merged into one).

## Methodology stress-test (2026-09-22, later in session): is the 3-type claim actually supported?

The user asked directly whether "日本=政策管理型、韓国=被害政治型、中国=主権・
正統性型" is a defensible conclusion. A genre/speaker-level cross-tab over the
28-row main axis (at the time) showed:

- **Japan**: agency_explicit=0 holds across BOTH document_type=SPEECH (the
  annual ceremony) AND document_type=PRESS_CONFERENCE within the sample --
  i.e. not purely a ceremonial-genre artifact. Relatively well supported.
- **Korea**: the aggregate "60%" hid a sharp split by *administration*, not
  genre: Moon (4/4 agency_explicit=1) and Lee (2/3) cluster opposite Yoon
  (0/3, with 2 NA). "被害政治型" describes Moon/Lee-era discourse, not a
  stable Korean national trait -- Yoon is a real counter-example within the
  same country and genre.
- **China**: 7 of 8 records are the same genre (spokesperson press
  conference), so the "100%/100%" finding is *not decomposable* from this
  sample alone -- cannot rule out "this is just how MFA briefings talk
  about anything" vs. a memory-regime-specific finding. Weakest-supported
  leg of the three.

Diagnosis of what would fix each, discussed with the user:
- **Korea**: fixable by more data of the *same kind* (Yoon-era press
  conferences specifically, more per-administration N) -- but the fix
  changes the conclusion (administration-contingent, not a fixed "type"),
  it doesn't rescue the original claim as stated.
- **China**: NOT fixable by more of the same genre. Needs a different kind
  of data -- Xi Jinping's own speeches on the same topic (to test if the
  pattern holds at HEAD level, not just OFFICIAL/spokesperson), and/or
  MFA responses to non-historical disputes (to test if it's a general
  institutional-communication-style artifact vs. history-specific).

## Revised scale target (2026-09-22): ~20/country, not 30 or 50

After estimating effort for 50/country (Japan: achievable via existing
736-backlog coding; Korea: ~1% hit rate scanning the Moon-era archive by
title keywords, Yoon-era press conferences not yet sourced at all; China:
similarly low hit rate per targeted week, plus needs the Xi-speech genre
diversification above) and finding that even Japan's "easy" backlog has a
much lower true-positive rate than the raw 736 count suggested (a
proximity-keyword sweep across all 736 backlog rows for
comfort-women/forced-labor/colonial/Yasukuni/textbook-type language,
excluding the already-coded 10, found only **6** new genuinely on-topic
candidates -- most of the backlog is "war"-keyword false positives from
COVID-era press conferences, Diet policy speeches mentioning Ukraine, a
domestic political-funding "apology," etc., exactly as
`pilot_coverage_report.md` already warned), the user and I agreed to
retarget at **~20/country** rather than 30 or 50.

Progress toward that revised target: the 6 new Japan candidates found
(all genuinely on-topic, no more false-positive spending) have been coded
and merged, bringing Japan's main axis to **16**. They also happen to
double as evidence for the genre-confound check above (J6, the Okinawa
memorial press conference, replicates agency_explicit=0 in a
PRESS_CONFERENCE, not just the SPEECH-genre ceremony) and form a small
temporal series on the forced-labor issue across five dates
(2021-10-15 -> 2022-03-11 -> 2022-06-10 -> 2022-11-13 -> 2025-06-09)
tracking how substantively Kishida/Ishiba engage with it over time and
across two different ROK presidents (Yoon, Lee) -- see coder_notes on
each row.

Current tallies: Japan 16, Korea 10, China 8 (34 main-axis total). Korea
and China still need new discovery work (per the diagnosis above) to
reach ~20; Japan needs more backlog sweeps of the same
proximity-keyword kind (has headroom in `pilot_manual_review.csv`,
now 731 rows after removing the 6 promoted ones, but expect a similarly
low hit rate, not a straight path to +4 more).

## Target reset to 30/country and final push (2026-09-22, later same session)

The ~20/country retarget above was the user's call at the time, made when
Japan's real backlog hit-rate turned out much lower than the raw 736-row
count suggested. Later the same session the user reviewed Japan's progress
and explicitly reset the target back up: **"30件を目標 日本→韓国→中国の順に"**
(target 30, in the order Japan → Korea → China). The ~20/country section
above is kept as a historical record of that intermediate decision and the
effort-estimation reasoning behind it, not as the final target.

Executed in that order, across several discovery rounds:

- **Japan**: 16 → **30**. The 12-record Hiroshima/Nagasaki Peace Memorial
  Ceremony batch (2020-2025, Abe/Suga/Kishida/Ishiba) filled most of the
  gap via the same proximity-keyword sweep method as the earlier 6-record
  batch. The 30th record, Kishida's July 2024 Sado Island Gold Mines
  UNESCO message, was included as a deliberate *silence* data point: the
  message omits any mention of the wartime forced-Korean-labor dispute
  that was the actual diplomatic story behind the inscription (see its
  `coder_notes`) — an intentional test of the codebook's non-hallucination
  rule (code what the text says, not what the surrounding controversy
  implies) rather than a coding oversight.
- **Korea**: 10 → **30**. New sources beyond the original pilot's
  Briefing Room/current-admin listing: the `eng.president.go.kr/speeches/*`
  path (previously untried, distinct from `/briefing/*`, found via Wayback
  CDX), a 6-year (2021-2026) annual series of MOFA Spokesperson protest
  statements on Japan's textbook authorizations (found via web search
  identifying the `mofa.go.kr` press-release board's `seq=` numbering
  scheme, then fetched directly from the live site rather than Wayback),
  a MOFA Yasukuni statement, two March First Independence Day addresses, a
  Keio University lecture, and several Lee Jae Myung-era records (a
  Yomiuri Shimbun interview via `korea.net`, two Comfort Women Memorial
  Day messages, Tokyo-summit remarks). The Sado Island Gold Mines dispute
  ended up as a three-point, two-country trace across time (Korea's Jan
  2024 pre-inscription protest, Japan's own July 2024 silence, Korea's
  July 2026 UNESCO follow-up assessment) — one of the more complete
  single-dispute threads in the corpus.
- **China**: 8 → **30**. New annual-commemoration genres beyond the
  existing Yasukuni-response series: Dec 13 Nanjing Massacre National
  Memorial Day (2021-2024, filling out the series alongside the existing
  2025 record), Sept 18 (Mukden/September 18 Incident) sirens ceremony
  (2020, 2023, 2024), and July 7 (Lugou/Marco Polo Bridge Incident)
  commemoration (2021, 2023, 2024) — found via targeted web search per
  year rather than the `english.www.gov.cn/news/page_N.html` archive's own
  page-number index, since attempting to calibrate a date-to-page-number
  mapping for that archive this session found the rate highly non-linear
  (a naive linear extrapolation from known anchor points missed target
  dates by 30-100+ pages in both directions; recovered via iterative
  probing instead — see the corresponding batch scripts' commit messages
  for the anchor points used, if this needs to be redone). Also added the
  corpus's first HEAD-level China records outside the Sept 3, 2025 Xi
  speeches: three Xi Jinping-Japan PM APEC-sidelines summit readouts
  (2022 Kishida/Bangkok, 2023 Kishida/San Francisco, 2024 Ishiba/Lima),
  each raising history alongside Taiwan as a "major issue of principle" in
  near-identical language regardless of which PM Xi is meeting — a
  genuinely different register from the sharper MOFA spokesperson
  Yasukuni/Nanjing-genre language, itself a notable finding for the
  genre-confound question below.

**Final tallies: Japan 30, Korea 30, China 30 (90 main-axis records
total)**, up from 34 (16/10/8) at the point the ~20/country section above
was written. `pilot_japan_2020_2025.csv` was kept in sync with the main
file throughout (including fixing a pre-existing 1-record undercount
found during the Japan batch). `pilot_manual_review.csv` (the Japan
keyword-filtered backlog) is now 718 rows, down from 731, after removing
the 13 promoted URLs (12 Hiroshima/Nagasaki + 1 Sado message). A full
enum-validation pass against `codebook.md`'s controlled vocabularies was
added partway through this push and run after every batch from then on —
it caught and fixed a few invalid values introduced in early drafts
(an out-of-vocabulary `document_type`, an invalid `issue_primary`, and
similar) before they were committed; none of the resulting fixes changed
a record's substantive coding, only its literal field value.

Provenance note that applies to several Korea and China records added in
this final push: where a direct fetch of the official government page
failed repeatedly (connection resets, an unindexed or unguessable
`seq=`/page-number scheme) but a reliable wire-service report (Xinhua,
Yonhap via Korea Times/Korea Herald) quoted the official statement
directly and at length, that wire report was used as `source_url` instead
of the primary page, with `classification_confidence` downgraded to
MEDIUM and the limitation stated explicitly in `coder_notes`. This is a
deliberate, flagged departure from the primary-source-only sourcing this
corpus otherwise follows, not a silent substitution — see individual
records' `coder_notes` and this file's batch-script commit messages for
which records this applies to.

## Revisiting the genre/confound question with the expanded sample

The methodology stress-test above (28-row sample) found Japan's finding
"relatively well supported" (agency_explicit=0 held across both SPEECH and
PRESS_CONFERENCE genres), Korea's "60%" figure administration-contingent
rather than a stable trait (Moon/Lee vs. Yoon), and China's finding "not
decomposable" because 7 of 8 records were the same genre (spokesperson
press conference). With 90 records and substantially more genre/speaker-
level diversity per country (see the per-country `document_type` and
`speaker_level` breakdowns obtainable from `pilot_east_asia_2020_2025.csv`
directly), this stress-test should be re-run before finalizing the paper's
3-type conclusion — it has **not** been re-run as part of this push
(scope was data collection only, per the user's "a" instruction to
continue toward 30/country). In particular:

- China now has HEAD-level records (the 3 APEC summit readouts) alongside
  the OFFICIAL-level MOFA series, which directly addresses the earlier
  "cannot rule out this is just how MFA briefings talk" concern — the
  summit readouts show a *different*, softer register at HEAD level
  ("draw lessons from history," agency_explicit=0) than the OFFICIAL-level
  Yasukuni/Nanjing genre's sharper, agency_explicit=1 language, which is
  itself a finding, not a null result.
- Korea now has a much larger OFFICIAL-level (MOFA spokesperson) sub-
  sample (11 records) that did not exist in the 28-row analysis at all,
  which should be checked against the HEAD-level (presidential) records
  for the same kind of genre/level decomposition already done for Japan.
- Japan's 30th-record silence-by-omission case (Sado) and the Hiroshima/
  Nagasaki batch's confirmation that Ishiba's Aug 15 "remorse" pattern-
  break does not carry over to the Hiroshima/Nagasaki genre are both
  directly relevant to how confidently the paper can generalize from any
  single Japan genre to a country-level claim.

## Remaining before this phase is publication-ready

- Refresh `pilot_coverage_report.md`'s per-country tables and narrative,
  and `README.md`'s "Current status" section, for the 34 -> 90 change
  (in progress in this same session, alongside this file's update).
- Re-run the genre/speaker-level/administration confound stress-test
  above against the full 90-record sample before finalizing the paper's
  "3-type" conclusion wording — not yet done (see previous section).
- The remaining ~718-item Japan `pilot_manual_review.csv` backlog is
  still mostly untouched -- out of scope per the user's "low priority,
  not full-scale" framing, not an oversight.
- Recompute the paper's quantitative tables (keyness analysis, apology/
  responsibility vocabulary table) against the full 90-record corpus —
  the existing tables in `draft_paper_ja.md` and `draft_paper_ja.docx`
  still reflect the earlier 28-record state.

This file is a working tracker, not a publication output — delete or fold its
content into `pilot_coverage_report.md` once phase 2 is complete.
