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

## Confound stress-test re-run on the full 90-record sample (2026-09-22, after the 30/30/30 push)

The original stress-test (28-row sample, above) found Japan's finding
"relatively well supported," Korea's "60%" figure administration-
contingent rather than a stable trait, and China's near-uniform pattern
"not decomposable" because 7 of 8 records were the same genre
(spokesperson press conference). Re-running the same
`agency_explicit` cross-tab against the full 90-record sample (code: a
short pandas/csv snippet grouping by `country`, `document_type`,
`speaker_level`, and `speaker_name`; not saved as a script since it is
three lines and easy to regenerate) gives a substantially clearer, and in
one case reversed, picture. Headline rates (`apology`/`remorse`/
`reflection`/`remedy`/`agency_explicit`, share of `1` among non-`NA`
responses, n=30 each):

| | apology | remorse | reflection | remedy | agency_explicit |
|---|---|---|---|---|---|
| Japan | 0.00 | 0.13 | 0.67 | 0.70 | 0.00 |
| Korea | 0.00 | 0.00 | 0.40 | 0.20 | 0.71 |
| China | 0.00 | 0.00 | 0.17 | 0.00 | 0.87 |

At the country level this is, if anything, a *cleaner* fit to the
"policy-management / victimhood-politics / sovereignty-legitimacy" framing
than the 28-row sample was: Japan pairs zero agency_explicit with the
corpus's highest remedy (0.70) and reflection (0.67) rates (concrete
relief/policy measures and self-referential "never again" framing, never
a named responsible actor); Korea and China both run high on
agency_explicit (directed at Japan) and near-zero on remedy/remorse/
apology (neither is apologizing for anything in this corpus — they are
criticizing Japan). But the country-level numbers hide very different
internal structure once decomposed by genre and speaker_level, and that
internal structure is the more important finding for the paper's method
section:

**Japan — now fully robust, not just "relatively" supported.**
`agency_explicit=0` holds in **all 30 of 30 records**, across every
`document_type` (SPEECH n=18, PRESS_CONFERENCE n=11, STATEMENT n=1) and
every one of the four sampled prime ministers (Abe, Suga, Kishida,
Ishiba) individually. With three times the sample and a genre the 28-row
version didn't have (the Hiroshima/Nagasaki addresses) confirming the
same pattern, this is no longer a "probably genre-robust" claim — it is a
clean, exceptionless finding across genre and administration, for the
HEAD-level main-axis sample specifically (see the Sado silence record
and phase-2's forced-labor temporal series for the caveats already noted
about within-genre variation in *other* fields like remorse/reflection).

**Korea — the "60% administration-contingent" finding sharpens into a
level-contingent one.** The 28-row sample had zero OFFICIAL-level Korea
records; this push added 11 (the MOFA textbook/Yasukuni/Sado statement
series). Splitting by `speaker_level`:

- HEAD (presidential, n=19; 17 non-NA): overall 0.59, but a clear
  administration gradient — **Moon 1.00 (4/4) → Yoon 0.50 (3/6, 2 NA
  cases are his 2023/2024 Aug 15 addresses, which do not mention Japan at
  all) → Lee 0.43 (3/7)**. This replicates and extends the original
  finding: not a fixed national trait, and now showing continued decline
  under Lee rather than a rebound, with three administrations' worth of
  data instead of two-and-a-fraction.
- OFFICIAL (MOFA spokesperson, n=11): **0.91**, and — unlike the
  presidential level — essentially flat across all three administrations'
  terms in office (Moon-era statements 2/2, Yoon-era 5/6, Lee-era 4/4;
  the single 0 is the deliberately-included Yoon "dinner" null-engagement
  record, not a genuine counterexample). This is the push's clearest new
  finding for Korea: the "sharp, actor-naming" register the original
  28-row sample's aggregate 60% figure gestured at is concentrated in and
  driven by the *bureaucratic* level, which does not shift with
  administration change, while the *political/presidential* level is
  exactly where the administration-contingent variation lives. A
  "被害政治型" characterization fits the MOFA-spokesperson register far
  better than it fits any single president's addresses.

**China — reverses from "not decomposable" to "decomposable, and the
apparent uniformity was a genre artifact after all."** The 28-row
sample's near-100% figure came from a sample that was 7/8 the same genre
(spokesperson press conference); this push added the corpus's first
HEAD-level China data (5 records: the 2025-09-03 Xi speeches, already
present, plus three new Xi-Japan-PM APEC summit readouts). Splitting by
`speaker_level`:

- OFFICIAL (MOFA spokesperson, n=13) and UNKNOWN (third-person Xinhua/
  State Council wire narration of ceremonies — Nanjing, Sept 18, July 7,
  n=12): **1.00 each**. Both genres explicitly name "Japanese
  militarists," specific Class-A war criminals, or "Japanese troops" as
  the actor, in near-formulaic language.
- HEAD (Xi Jinping himself, n=5): **0.20** (1 of 5) — the opposite
  pattern. All three APEC summit readouts (2022 Kishida/Bangkok, 2023
  Kishida/San Francisco, 2024 Ishiba/Lima) code `agency_explicit=0`: Xi's
  language is "draw lessons from history" / "face history squarely,"
  abstract and unaddressed to a named actor, paired with an explicit pivot
  to present-day cooperation — structurally the closest thing in the
  whole corpus to Japan's own register. Only one of the two 2025-09-03
  war-anniversary speeches names Japan explicitly.

  This is exactly the test the original stress-test's diagnosis called
  for ("Xi Jinping's own speeches on the same topic, to test if the
  pattern holds at HEAD level") and the answer is **no, it does not
  hold** — China's near-uniform agency_explicit=1 finding is a property
  of the OFFICIAL-level MOFA-spokesperson-and-state-media commemorative
  register specifically, not a China-wide "sovereignty/legitimacy" trait
  that also describes how its head of state actually talks to Japan's
  leaders in person. Note that `document_type` alone does not cleanly
  separate this (the three summit readouts and the Xinhua wire narration
  are both coded `document_type=OTHER`); `speaker_level` is the variable
  that does the work here, not genre in the document-type sense.

**Implication for the paper's "3-type" wording.** All three countries now
show that their headline agency_explicit rate is concentrated at a
specific speaker_level rather than holding uniformly across the whole
national apparatus: Japan's 0% is genuinely level-independent (only HEAD
data exists in this corpus, and it's uniform within that level across
four administrations); Korea's aggregate 71% is really "OFFICIAL ~90%,
flat across administrations" plus "HEAD ~50-100% declining by
administration"; China's aggregate 87% is really "OFFICIAL/media ~100%"
plus "HEAD ~20%." A revised conclusion should probably name the
speaker_level the claim is actually about (e.g., "Korea's and China's
*bureaucratic/spokesperson* apparatus consistently names Japan as the
actor; their heads of state/government do not, and vary further by who
holds the office and, for China, by the diplomatic occasion") rather than
stating the 3-type claim as an undifferentiated national trait. This has
not been decided or written into `draft_paper_ja.md` yet — flagged here
as the concrete finding the next paper-drafting pass should work from.

## Remaining before this phase is publication-ready

- ~~Refresh `pilot_coverage_report.md`'s per-country tables and narrative,
  and `README.md`'s "Current status" section, for the 34 -> 90 change~~ —
  **done 2026-09-22**.
- ~~Re-run the genre/speaker-level/administration confound stress-test
  above against the full 90-record sample~~ — **done 2026-09-22**, see
  the "Confound stress-test re-run on the full 90-record sample" section
  above. Headline result: Japan's finding is now fully robust (0/30
  exceptions across genre and administration); Korea's and China's
  aggregate agency_explicit rates both turn out to be driven almost
  entirely by their OFFICIAL/bureaucratic-level records (~90-100%), while
  their HEAD-level records look quite different (Korea: administration-
  contingent, 43-100%; China: mostly agency_explicit=0, the opposite of
  the aggregate figure).
- ~~The paper's 3-type wording should be revised to name the
  speaker_level each claim actually describes~~ — **done 2026-09-22**
  (same day, later pass, explicitly requested by the user as a follow-up
  to the stress-test re-run above). `draft_paper_ja.md`'s abstract
  (Japanese, English, and the Japanese restatement), Section 4
  (theoretical framework), Section 7 (discussion), and Section 8
  (conclusion) were rewritten to reformulate the three types as two
  discourse registers rather than three fixed national characters: a
  **bureaucratic/media register** (stable across administrations —
  Korea's MOFA spokesperson ~91%, China's MOFA/state-media ~100% — which
  the original "victim-politics" and "sovereignty-legitimacy" labels
  describe well) and a **head-of-state register** (highly variable —
  Japan uniformly 0% across four PMs, Korea 43-100% depending on
  administration, China's Xi only 20% in APEC summit meetings — into
  which Japan's "policy-management" style extends without exception,
  while South Korea's and China's heads of state/government increasingly
  converge toward it). The paper's revised conclusion argues that the
  persistent gap between these two registers, not either alone, is what
  keeps historical-recognition disputes structurally available for
  renewed friction even as head-of-state dialogue grows more
  conciliatory. The three-type labels themselves (政策管理型/被害政治型/
  主権・正統性型) were kept, per the user's framing of this as a
  "wording" revision rather than a request for entirely new labels; the
  title/subtitle were left untouched (the subtitle is still marked
  provisional in the draft's own editorial memo, with a note that a
  register-themed subtitle could fit better if the author wants to
  revisit it).
- The remaining ~718-item Japan `pilot_manual_review.csv` backlog is
  still mostly untouched -- out of scope per the user's "low priority,
  not full-scale" framing, not an oversight.
- ~~Recompute the paper's quantitative tables (keyness analysis, apology/
  responsibility vocabulary table) against the full 90-record corpus~~ —
  **done 2026-09-22**; `draft_paper_ja.docx` (Japanese and English) has
  been regenerated twice this session (once for the table recomputation,
  once more for the 3-type reformulation above) and structurally
  validated (XSD schema check via the docx skill's validate.py), since
  LibreOffice headless PDF conversion remains broken in this environment.
- New follow-up opened by the reformulation above: Section 8 now names
  "collect Japan's own bureaucratic/spokesperson-level data" as the
  paper's first open item, since the current Japan sample is HEAD-level
  only and cannot yet confirm whether Japan's policy-management register
  is head-of-state-specific (as Korea's and China's registers turn out to
  be level-specific) or holds at the bureaucratic level too. Not
  attempted this session — a new discovery task, not a data-analysis one.

This file is a working tracker, not a publication output — delete or fold its
content into `pilot_coverage_report.md` once phase 2 is complete.
