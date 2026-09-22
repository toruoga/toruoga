# Pilot Coverage Report — Japan, Korea, China, 2020–2025

## Status (2026-09-22): 101 records fully contextually coded (main axis: Japan
## 41 [30 HEAD + 4 MINISTER + 7 newly promoted from a full backlog review],
## Korea 30, China 30) + 1 pre-2020 landmark anchor. The 718-row Japan
## backlog (`pilot_manual_review.csv`) has now been fully reviewed and
## dispositioned (7 promoted, 711 excluded with a recorded reason each) —
## see "Full backlog review" below.

This report is the single working record for the corpus's discovery
methodology, coding decisions, methodological stress-tests, and open items.
It supersedes the separate `phase2_plan.md` working-log file, which has been
folded in here and removed (this file plays the role that file's own final
line asked for: "delete or fold its content into `pilot_coverage_report.md`
once phase 2 is complete" — done now, even though a few discovery items
below remain open, since the fold itself is a housekeeping task independent
of finishing every remaining item). Where this report says "this session" or
gives a date, it is describing when that specific finding or decision was
made, not necessarily today.

## Scope agreement

The 法政論叢 invited paper stays **low-priority and non-full-scale**: it does
**not** attempt Japan-scale exhaustive archive crawling for Korea/China, and
does **not** attempt uniform 1990–2025 coverage (that would require ~324
documents and re-solving URL discovery for all three countries in the
pre-2016 era, where Korea's older MOFA-hosted material is already known to be
~0% recoverable per `political_apology_vol4_url_liveness_check.csv`).

Instead the corpus follows two tracks:

- **Main axis**: 2020–2025, matching the original pilot design. Scaled over
  several rounds (see "History of the scaling target" below) to the current
  30 records per country.
- **Landmark anchors** (`landmark_anchors.csv`): a small, purposively-selected
  set of pre-2020 historical-recognition flashpoints, added as qualitative
  reference points rather than a dense annual time series. Planned set: 1995
  Murayama Danwa (done), 2001–2006 Koizumi Yasukuni Shrine visits, the 2005
  history-textbook controversy, the 2015 Japan-Korea "comfort women"
  agreement, and the 2018 Korea Supreme Court forced-labor ruling (all four
  still open — see "Remaining open items" below).

All sourcing follows `codebook.md` Section 2: official government domains
only; Wayback Machine snapshots of an official domain are an acceptable
fallback (same precedent as the vol.4 liveness check and the Korea
`webarchives.pa.go.kr` sourcing already in this repo), but third-party
mirrors (academic databases, news, Wikipedia) are not. A small number of
Korea/China records substitute a wire-service report (Xinhua, or Yonhap via
Korea Times/Korea Herald) that quotes an official statement directly, where
the primary government page could not be reached after repeated attempts;
each such record is flagged in its own `coder_notes` with
`classification_confidence` downgraded to MEDIUM — a deliberate, flagged
departure from primary-source-only sourcing, not a silent substitution.

## Current coverage table

| Country | Fully coded (main axis) | Backlog pending | Landmark anchors |
|---------|--------------------------|------------------|-------------------|
| Japan   | 41 (30 HEAD + 4 MINISTER + 7 backlog-promoted) | 0 (718 reviewed, all dispositioned — see below) | — |
| Korea   | 30 | 0 (candidate pools hand/search-verified, not archive-crawled at Japan's scale) | — |
| China   | 30 | 0 (same as Korea) | — |
| **Total** | **101** | **0** | **1** (1995 Murayama Danwa) |

Per-country `issue_primary` and `speaker_level`/`document_type` distributions
at this tally can be recomputed directly from
`pilot_east_asia_2020_2025.csv` (e.g. `python3 -c "import csv, collections;
print(collections.Counter(r['issue_primary'] for r in csv.DictReader(open('pilot_east_asia_2020_2025.csv')) if r['country']=='japan'))"`)
rather than hand-copied into prose here, since the distribution will shift
again if the corpus is scaled further.

Underlying discovery-pipeline table (original pilot, pre-scaling; kept for
its "how each country's candidate pool was built" detail):

| Country | URLs discovered | Downloaded | Kept after keyword filter | Fully coded (original pilot) |
|---------|------------------|------------|------------------------------|-------------------------|
| Japan   | 1096 | 1081 | 746 | 10 |
| Korea   | 10 | 10 | 10 | 10 |
| China   | 8 | 8 | 8 (1 stale placeholder excluded, see `inaccessible_sources.csv`) | 8 |
| **Total** | **1114** | **1099** | **764** | **28** |

Japan used the full archive-crawl mechanism
(`scripts/01_discover_urls.py --seed-index-urls` over 78 resolved monthly
statement archives). Korea/China's original candidates were seeded with
hand-verified search results instead, since Korea's live-site pagination
looked JS-only and China's State Council "news" index turned out to be a
portal page, not an article archive. Later scaling rounds (below) partly
closed that gap for both countries but their candidate pools remain **not**
exhaustive, representative samples of everything available on those sites
the way Japan's is.

## History of the scaling target

The corpus went through three explicit target changes, each a user decision
made after reviewing actual discovery effort, not a default plan followed
mechanically:

1. **Original pilot**: 28 records (Japan 10, Korea 10, China 8).
2. **~20/country** (interim): after finding that Japan's raw 736-row keyword-
   filtered backlog had a much lower true-positive rate than its size
   suggested (a proximity-keyword sweep for comfort-women/forced-labor/
   colonial/Yasukuni/textbook-type language, excluding the already-coded 10,
   found only 6 new genuinely on-topic candidates — most of the backlog is
   "war"-keyword false positives from COVID-era press conferences, Diet
   policy speeches mentioning Ukraine, a domestic political-funding
   "apology," etc.) and that Korea/China would both need genuinely new
   discovery work (not just more hand search) to scale further, the user and
   the assistant agreed to retarget at ~20/country rather than 30 or 50.
   Reached: Japan 16, Korea 10, China 8 (34 total).
3. **30/country, final** (2026-09-22, "30件を目標 日本→韓国→中国の順に"): after
   reviewing Japan's progress at 16, the user reset the target back up to 30
   and specified the discovery order (Japan → Korea → China). All three
   countries reached exactly 30, for **90 main-axis records**. A fourth,
   smaller round (below) then added 4 Japan MINISTER-level records, bringing
   the corpus to its current 94.

### Round 2→3 discovery methods (16/10/8 → 30/30/30)

- **Japan** (16 → 30): a 12-record Hiroshima/Nagasaki Peace Memorial
  Ceremony batch (2020–2025, Abe/Suga/Kishida/Ishiba), found via the same
  proximity-keyword backlog sweep as the earlier 6-record batch. The 30th
  record, Kishida's July 2024 Sado Island Gold Mines UNESCO message, was
  included as a deliberate *silence* data point: the message omits any
  mention of the wartime forced-Korean-labor dispute that was the actual
  diplomatic story behind the inscription — an intentional test of the
  codebook's non-hallucination rule (code what the text says, not what the
  surrounding controversy implies), not a coding oversight.
- **Korea** (10 → 30): `en.president.go.kr`'s listing turned out to load via
  an AJAX POST to `/ajaxf/frBoard/bbsViewGalleryList.do` (params from the
  page's `#sendForm`), not a plain `?page=N` GET — a single `pagePerCnt=100`
  POST returns the current administration's full listing in one call.
  Separately, `webarchives.pa.go.kr`'s Moon-era (19th) listing supports
  genuine `?page=N` pagination (confirmed back to ~April 2021); the Yoon-era
  (20th) listing does not — its archived snapshot only ever captured page 1
  of each category, a hard, unfixable limit of the National Archives'
  snapshot itself (see "Korea's Yoon-era gap" below for the full
  investigation). New sources found this way: the previously-untried
  `eng.president.go.kr/speeches/*` path (distinct from `/briefing/*`, found
  via Wayback CDX); a 6-year (2021–2026) annual MOFA Spokesperson
  protest-statement series on Japan's textbook authorizations (found via web
  search identifying the `mofa.go.kr` press-release board's `seq=` numbering
  scheme, then fetched live rather than via Wayback); a MOFA Yasukuni
  statement; two March First Independence Day addresses; a Keio University
  lecture; and several Lee Jae Myung-era records (a Yomiuri Shimbun
  interview via `korea.net`, two Comfort Women Memorial Day messages,
  Tokyo-summit remarks). The Sado Island Gold Mines dispute became a
  three-point, two-country trace across time (Korea's Jan 2024
  pre-inscription protest, Japan's own July 2024 silence, Korea's July 2026
  UNESCO follow-up assessment).
- **China** (8 → 30): `mfa.gov.cn/eng/xw/fyrbt/lxjzh/index_N.html` is a real,
  date-ordered press-conference archive, but with a hard lower bound around
  `index_145` (≈ July 2022) — pre-mid-2022 content is not reachable through
  this path at all, archive or no archive. No working site search exists
  (`search.fmprc.gov.cn` has a TLS cert mismatch) and article titles are
  never topical, so finding relevant content means downloading and grepping
  full daily transcripts around known high-salience weeks (Yasukuni's
  biannual shrine festivals, Nanjing Memorial Day, PM transitions) rather
  than keyword search. New genres added this way: Dec 13 Nanjing Massacre
  National Memorial Day wire reports (2021–2024, via
  `english.www.gov.cn`'s Xinhua/State Council news archive, a different
  source from the MFA daily transcripts — third-person wire narration,
  `speaker_level=UNKNOWN`), Sept 18 (Mukden Incident) sirens ceremony
  (2020, 2023, 2024), July 7 (Lugou/Marco Polo Bridge Incident) commemoration
  (2021, 2023, 2024), an Apr 30, 2025 response invoking Japan's WWII
  "aggression"/"colonial rule" over the Philippines, and an Aug 2022
  Yasukuni response. Also added the corpus's first HEAD-level China records
  outside the Sept 3, 2025 Xi speeches: three Xi Jinping–Japan-PM
  APEC-sidelines summit readouts (2022 Kishida/Bangkok, 2023
  Kishida/San Francisco, 2024 Ishiba/Lima), each raising history alongside
  Taiwan as a "major issue of principle" in near-identical language
  regardless of which PM Xi is meeting — directly relevant to the
  speaker-level confound analysis below. An attempt to calibrate
  `english.www.gov.cn/news/page_N.html`'s own date-to-page-number mapping
  proved unreliable (a naive linear extrapolation from known anchor points
  missed target dates by 30–100+ pages in both directions); recovered via
  targeted web search per year and iterative probing instead.

A full enum-validation pass against `codebook.md`'s controlled vocabularies
was added partway through the 30/30/30 push and run after every batch from
then on — it caught and fixed a few invalid values introduced in early
drafts (an out-of-vocabulary `document_type`, an invalid `issue_primary`, and
similar) before they were committed; none of the fixes changed a record's
substantive coding, only its literal field value. `pilot_japan_2020_2025.csv`
was kept in sync with the main file throughout (including fixing a
pre-existing 1-record undercount found during the Japan batch), as was a
speaker-name inconsistency (`"Lee Jae-myung"` vs. `"Lee Jae Myung"` across
different rows, normalized to the latter so the confound analysis below
groups his administration correctly).

### Round 4: Japan MINISTER-level records (2026-09-22, after 30/30/30)

The confound stress-test below (run against the 90-record 30/30/30 sample)
found that Korea's and China's headline `agency_explicit` rates are each
concentrated at a specific `speaker_level` rather than holding uniformly
across the whole national apparatus — but Japan's sample was **HEAD-level
only**, so the corpus could not test whether Japan's own policy-management
register is head-of-state-specific (like Korea's and China's registers turn
out to be level-specific) or holds at the bureaucratic/ministerial level
too. Four Foreign Minister (Cabinet rank, per `codebook.md`'s
`speaker_level=MINISTER` definition) records were added via Wayback Machine
snapshots of `www.mofa.go.jp` (live-blocked in this environment; see
"Network access notes" below):

- **MOTEGI Toshimitsu, May 19, 2020** regular press conference: declines to
  comment on ROK-internal criticism of the comfort-women survivor
  foundation, restates the 2015 agreement's "final and irreversible
  resolution" as Japan's standing position (apology/remorse/reflection/
  remedy all 0).
- **HAYASHI Yoshimasa, Aug 10, 2022** press conference (on reappointment in
  the reshuffled second Kishida Cabinet): asked about the forced-labor
  asset-liquidation crisis and comfort women issue, calls the situation
  "very difficult" and says it "cannot be left as it is" (`reflection=1`)
  but commits only to communication on Japan's existing position — no
  remedy, no explicit agency attribution.
- **HAYASHI Yoshimasa, May 10, 2022** extraordinary press conference (Seoul,
  after attending President Yoon's inauguration as PM Kishida's Special
  Envoy): same "cannot leave this as it is" framing (`reflection=1`),
  emphasis on process/communication over substance. The near-duplicate May
  9, 2022 pre-departure press conference (same event, nearly identical
  wording) was deliberately excluded to avoid double-counting.
- **KAMIKAWA Yoko, July 27, 2024** MOFA statement on the Sado Island Gold
  Mines' UNESCO inscription: a direct same-day MINISTER-level companion to
  the already-coded Kishida (HEAD) message on the same event — frames the
  site purely as pre-modern mining heritage, no mention of Korea or forced
  labor at all (deliberate null/silence data point, all content fields
  0/NA).

Also ruled out as a source this round: Japan's Chief Cabinet Secretary press
conference archive (`japan.kantei.go.jp/tyoukanpress/`), confirmed (after
checking both a 2023 date and a current 2026 date, and ruling out
JS-rendering via a Playwright fetch with a custom User-Agent — the site's WAF
serves a themed fake "page not found" to a bare/default UA, the same
behavior already documented below for `japan.kantei.go.jp`'s statement
pages) to be **video-only with no English text transcripts** for any date
tested.

**Confound stress-test re-run against the full 94-record sample
(2026-09-22, after Round 4):** re-running the same `agency_explicit`/
`apology`/`remorse`/`reflection`/`remedy` cross-tab (see the dedicated
section below) with Japan's speaker_level split gives, by level:

| Japan | apology | remorse | reflection | remedy | agency_explicit |
|---|---|---|---|---|---|
| HEAD (n=30) | 0.00 | 0.13 | 0.67 | 0.70 | 0.00 |
| MINISTER (n=4) | 0.00 | 0.00 | 0.50 | 0.00 | 0.00 |

`agency_explicit=0` now holds in **all 34 of 34** Japan records regardless
of speaker_level — the single most direct confirmation available in this
corpus that Japan's "no named responsible actor" pattern is not
head-of-state-specific, unlike Korea's and China's register gaps (both
sharply level-specific — see below). Country-level `apology`/`remorse` also
stay at 0 across both levels. The two fields that do move are `reflection`
(0.67 HEAD → 0.50 MINISTER — both Hayashi MINISTER records code
`reflection=1` for "cannot be left as it is," but Motegi's and Kamikawa's
do not) and, more sharply, `remedy` (0.70 HEAD → 0.00 MINISTER): none of
the 4 MINISTER records commit to or describe a concrete relief/policy
measure the way roughly seven in ten HEAD-level records do (the Hiroshima/
Nagasaki addresses' peace-fund/hibakusha-support references, Kishida's
forced-labor and shuttle-diplomacy records, etc.) — the MINISTER-level
genre sampled here (routine press-conference Q&A, one UNESCO statement) may
simply not be the genre where Japan states remedies, rather than a
level-based difference in willingness to state them. n=4 remains a small
sample for `reflection`/`remedy`, but `agency_explicit`'s 0/34 result is
about as clean a finding as the corpus can currently produce.

## Round 5: full backlog review of `pilot_manual_review.csv` (2026-09-22)

Per explicit user request ("718件バックログの本格コーディング"), every one of
the 718 Japan rows in `pilot_manual_review.csv` was individually
dispositioned this round — not just skimmed for a few more wins, but given
an actual EXCLUDED/PROMOTED verdict and a recorded reason, so the file is
now fully auditable rather than an open-ended backlog. Method:

1. **Triage by existing signal columns.** The file already carries
   per-row keyword-proximity flags (`apology_signal`, `remorse_signal`,
   `reflection_signal`, `remedy_signal`, `pardon_or_forgiveness_signal`,
   `explanation_signal`) computed by the original pipeline. The 62 rows
   with `apology_signal`, `remorse_signal`, or `pardon_or_forgiveness_signal`
   = 1 (the highest-precision subset) were read individually first (title +
   full `relevant_excerpt`).
2. **Content-pattern exclusion for the rest.** A regex classifier was run
   over every row's title/question/response/excerpt text, sorting matches
   into named categories (COVID-19/pandemic, natural disaster, domestic
   political scandal, Ukraine/Russia or unrelated geopolitics, North Korea
   missile launches, condolence messages for unrelated deaths, generic
   diplomatic messages/speeches to third countries, routine unrelated press
   conferences, index/navigation pages). This left 173 rows (after removing
   the already-read 62) genuinely unclassified by any pattern, which were
   then read individually the same way as the high-signal 62.
3. **Full-text verification for ambiguous cases.** A handful of titles
   that could plausibly contain real content despite not matching an
   obvious exclusion pattern — a Jan 2022 press conference on the Sado
   Mines UNESCO nomination timeline, two Sept 2024 Japan-ROK/Japan-China
   press conferences, a July 2021 press conference on a Hiroshima High
   Court ruling, a March 2025 Japan-U.S. Iwo-To ceremony address, and a
   handful of titles left over after full classification (Nobel Prize
   comments, a UNESCO sake-brewing inscription message, appointment/New
   Year statements) — were fetched from `japan.kantei.go.jp` directly (all
   reachable without Wayback) and read in full before disposition, per the
   codebook's non-hallucination rule.

**Result: 7 promoted, 711 excluded**, each with a `full_review_status`
(PROMOTED/EXCLUDED) and `full_review_reason` column now added to
`pilot_manual_review.csv` (no rows deleted — the full 718-row file, with
disposition, remains as the audit trail). Exclusion reasons, by volume:
COVID-19/pandemic (239), Ukraine/Russia or unrelated geopolitics (165),
natural disaster or accident (122), generic diplomatic message/speech to a
third country (105), routine unrelated press conference (29), condolence
message for an unrelated death (11), North Korea missile-launch response
(10), individually-read-and-confirmed-irrelevant (8), domestic political
scandal/personnel matter (8), Japan-ROK/Japan-PRC summit press conference
with no substantive historical content beyond generic references (6),
index/navigation page (5), National Foundation Day/Marine Day message (2),
atomic-bomb-survivor domestic welfare policy — ruled out as a domestic
health/certification matter (the "black rain" lawsuit) rather than an
international historical-recognition dispute (2). This confirms, at full
scale, the low true-positive rate already documented from the two earlier
partial sweeps (6 then 12 promoted out of ~730): roughly 1% of this
particular backlog was genuinely on-topic.

The 7 newly-promoted records (all `speaker_level=HEAD`, added to
`pilot_east_asia_2020_2025.csv`/`pilot_japan_2020_2025.csv`):

- **The Battle of Okinawa Memorial Ceremony Address series** (June 23,
  2020/2021/2023/2024/2025 — Abe, Suga, Kishida ×2, Ishiba), a fourth
  annual WWII ceremonial genre alongside Aug 15 and Hiroshima/Nagasaki,
  previously entirely missing from the corpus (only a same-date 2025
  PRESS_CONFERENCE about the ceremony was already coded; the ceremonial
  Address itself, a separate document each year, was not). Same pattern as
  the rest of Japan's HEAD-level sample: `apology=0`, `remorse=0`,
  `reflection=1` (self-referential "never repeat the horrors of war"),
  `remedy=1` (concrete, recurring U.S.-base-burden-reduction commitments,
  coded on the same logic as the Hiroshima/Nagasaki batch's
  atomic-bomb-survivor relief measures), `agency_explicit=0` throughout.
  2022 (77th anniversary) could not be located in the backlog and was not
  separately searched for this round.
- **A Jan 28, 2022 Kishida press conference on the Sado Mines UNESCO
  nomination timeline** — a fourth, and chronologically earliest, point in
  the Sado Island Gold Mines dispute thread already traced in this corpus
  (Korea's Jan 2024 protest, Japan's July 2024 silence message, Korea's
  July 2026 follow-up). Kishida acknowledges the nomination "has been met
  with various arguments and opinions" and pledges a task force to
  "respond to various arguments, including those concerning historical
  background" — an oblique, unnamed reference to the wartime forced-labor
  controversy, without naming Korea or forced labor. `explanation=1` for
  the process rationale; all other content fields 0, consistent with the
  same avoidance pattern later seen in the July 2024 record.
- **A March 29, 2025 Ishiba address at the Japan-U.S. Iwo-To Reunion of
  Honor Ceremony** — a new comparison case: an explicit Japan-U.S.
  reconciliation framing ("Japan and the United States, which once fought
  against each other, have reconciled... now becoming trusted allies")
  that has no equivalent in this corpus's Korea- or China-facing records.
  `reflection=1` ("humbly and sincerely facing history"), `remedy=1` (an
  ongoing war-dead remains repatriation project), `agency_explicit=0`.

Also individually verified and excluded rather than assumed irrelevant:
the two Sept 2024 Japan-ROK/Japan-China press conferences use "history" and
"aggression" only in generic, non-substantive ways (record-pace people-to-
people exchange "in history," routine diplomatic language) with no
apology/remorse/responsibility content; the July 2021 Hiroshima High Court
press conference is about extending Atomic Bomb Survivors' Assistance Act
certification to "black rain" plaintiffs, a domestic health/welfare
administrative matter distinct from the international historical-
recognition disputes this corpus tracks, so it was not coded despite
matching keywords.

## Fully coded records by country

### Japan (41) — see `pilot_japan_2020_2025.csv`

HEAD level (37): the six annual August 15 National Memorial Ceremony for the
War Dead addresses (2020–2025, Abe/Suga/Kishida/Ishiba); Ishiba's same-day
press conference reintroducing "remorse" language after 13 years (Aug 15,
2025); Suga's January 2021 press conference on the comfort-women court case;
Kishida's March 2023 forced-labor-issue press conference and the
Kishida-Yoon joint press conference restarting "shuttle diplomacy"; the
12-record Hiroshima/Nagasaki Peace Memorial Ceremony batch (2020–2025);
Kishida's July 2024 Sado Island Gold Mines silence message; the 5-record
Battle of Okinawa Memorial Ceremony Address series (2020/2021/2023/2024/
2025); Kishida's Jan 2022 Sado Mines UNESCO-nomination press conference;
Ishiba's March 2025 Japan-U.S. Iwo-To Reunion of Honor address (the last 7
promoted from a full review of the `pilot_manual_review.csv` backlog — see
"Round 5" above).

MINISTER level (4): see "Round 4" above (Motegi 2020, Hayashi ×2 2022,
Kamikawa 2024).

Issue distribution across all 41 skews toward `WAR_GENERAL` (the Aug 15/
Hiroshima/Nagasaki ceremonial genre) with `FORCED_LABOR` and `COMFORT_WOMEN`
as the main substantive-dispute categories; see the CSV for the exact
recomputed counts.

**Notable substantive finding**: the six original Aug 15 addresses show a
consistent pattern across Abe (2020), Suga (2021), and Kishida (2022–2024):
domestically-oriented mourning for Japan's own war dead, no apology, no
remorse language, no reference to foreign victims — contrasting with
landmark statements (Murayama 1995, Abe's 70th-anniversary statement 2015).
Ishiba's 80th address (Aug 15, 2025) breaks this pattern, reintroducing
"remorse" for the first time in 13 years, framed in the same-day press
conference as continuity with, not departure from, prior administrations'
position. The forced-labor issue also forms a small temporal series across
five HEAD-level dates (2021-10-15 → 2022-03-11 → 2022-06-10 → 2022-11-13 →
2025-06-09) tracking how substantively Kishida/Ishiba engage with it over
time and across two different ROK presidents (Yoon, Lee) — see `coder_notes`
on each row.

### Korea (30)

Moon Jae-in: 75th (2020) and 76th (2021) Liberation Day addresses, his
August 2020 message on the National Day to Honor Japanese Military Comfort
Women Victims, his 2022 March First Independence Movement Day address.
Yoon Suk Yeol: 77th (2022), 78th (2023), 79th (2024) Liberation Day
addresses, plus OFFICIAL-level MOFA statements from his term. Lee Jae Myung:
80th (2025) and 81st (2026) Liberation Day addresses, the 2026-05-19
Korea-Japan summit joint statement with PM Takaichi (Chosei coal mine
forced-labor remains DNA analysis), two Comfort Women Memorial Day messages,
Tokyo-summit remarks, a Yomiuri Shimbun interview. Across all three
administrations: a 6-year annual MOFA Spokesperson protest-statement series
on Japan's textbook authorizations, a MOFA Yasukuni statement, a Keio
University lecture. All `speaker_level=HEAD` (n=19) or `OFFICIAL` (MOFA
spokesperson, n=11).

**Notable substantive finding**: Moon's addresses engage substantively with
colonial-era history (forced labor court rulings, comfort women, explicit
non-retaliation framing, "Japan must squarely face history and be humble
before it"), while Yoon's addresses show *declining* engagement year over
year — 2022 explicitly invokes the 1998 Kim Dae-jung–Obuchi Declaration to
frame "historical problems" as resolvable, 2023 mentions Japan only as a
trilateral security partner with zero historical content, 2024 mentions
Japan only in passing. Lee Jae Myung's addresses partly *revive* engagement
relative to late-Yoon, re-invoking "unresolved historical issues" and
re-citing the 1998 Declaration, though by reference rather than restating
specific grievances. See the confound stress-test below for how this
HEAD-level administration gradient sits alongside a flat, high
OFFICIAL-level rate.

### China (30)

Five MFA spokesperson responses to Japanese leaders' Yasukuni Shrine ritual
offerings (Wang Wenbin Aug 2022, Mao Ning Oct 2023, Wang Wenbin Apr 2024, Mao
Ning Oct 2024, Lin Jian Oct 2025); Lin Jian's separate Oct 17, 2025 response
on the death of former PM Murayama Tomiichi; Guo Jiakun's Apr 30, 2025
response invoking Japan's WWII "aggression"/"colonial rule" over the
Philippines (the only China record naming a historical victim other than
China/Korea); a Munich Consul General's Sept 2025 Nanjing-referencing
keynote; Dec 13 Nanjing Massacre National Memorial Day wire reports
(2021–2025); Sept 18 (Mukden Incident) sirens ceremony reports (2020, 2023,
2024); July 7 (Lugou Bridge Incident) commemoration reports (2021, 2023,
2024); three Xi Jinping–Japan-PM APEC summit readouts (2022, 2023, 2024);
two 2025-09-03 80th-anniversary-of-victory Xi speeches. `speaker_level`:
OFFICIAL (MOFA spokesperson, n=13), UNKNOWN (third-person wire narration of
ceremonies, n=12), HEAD (Xi Jinping, n=5).

**Notable substantive finding**: the Yasukuni responses use near-identical
formulaic language each time ("spiritual tool and symbol of Japanese
militarists' war of aggression," "14 convicted Class-A war criminals"),
suggesting a standing institutional script; the Aug 2022 instance is the
most elaborate version found, additionally invoking the 1943 Cairo
Declaration, suggesting the formula has been trimmed over time. The
Philippines record shows the same aggression/colonial-rule framing applied
to a third country's victimhood, suggesting the "face up to history" script
is general-purpose, not China/Korea-specific. See the confound stress-test
below for how this OFFICIAL/UNKNOWN-level pattern diverges sharply from
Xi's own HEAD-level language.

## Confound stress-test: is the "3-type" claim actually supported?

The paper's original claim — "日本=政策管理型、韓国=被害政治型、中国=主権・
正統性型" (Japan=policy-management, Korea=victim-politics, China=sovereignty-
legitimacy) — was directly stress-tested twice: once against the 28-row
sample, once against the full 90-row (30/30/30) sample, by cross-tabulating
`agency_explicit` (and the other apology-vocabulary fields) against
`country`, `document_type`, `speaker_level`, and `speaker_name`/
administration.

### First pass (28-row sample)

- **Japan**: `agency_explicit=0` held across both `document_type=SPEECH`
  (the annual ceremony) and `document_type=PRESS_CONFERENCE` — relatively
  well supported, not purely a ceremonial-genre artifact.
- **Korea**: the aggregate "60%" figure hid a sharp split by
  *administration*, not genre: Moon (4/4 `agency_explicit=1`) and Lee (2/3)
  clustered opposite Yoon (0/3, 2 NA) — "被害政治型" described Moon/Lee-era
  discourse, not a stable Korean national trait.
- **China**: 7 of 8 records were the same genre (spokesperson press
  conference), so the near-100% finding was **not decomposable** from that
  sample alone — could not rule out "this is just how MFA briefings talk
  about anything" vs. a memory-regime-specific finding. Weakest-supported
  leg of the three.

Diagnosis at the time: Korea's gap is fixable by more data of the same
kind (more Yoon-era press conferences, more per-administration N) but the
fix changes the conclusion rather than rescuing it as originally stated;
China's gap is **not** fixable by more of the same genre — it needs Xi
Jinping's own speeches on the same topic, to test whether the pattern holds
at HEAD level too.

### Second pass (full 90-row sample, after the 30/30/30 push)

Headline rates (`apology`/`remorse`/`reflection`/`remedy`/`agency_explicit`,
share of `1` among non-`NA` responses, n=30 each):

| | apology | remorse | reflection | remedy | agency_explicit |
|---|---|---|---|---|---|
| Japan | 0.00 | 0.13 | 0.67 | 0.70 | 0.00 |
| Korea | 0.00 | 0.00 | 0.40 | 0.20 | 0.71 |
| China | 0.00 | 0.00 | 0.17 | 0.00 | 0.87 |

At the country level this is, if anything, a *cleaner* fit to the
policy-management/victimhood-politics/sovereignty-legitimacy framing than
the 28-row sample: Japan pairs zero `agency_explicit` with the corpus's
highest remedy (0.70) and reflection (0.67) rates (concrete relief/policy
measures and self-referential "never again" framing, never a named
responsible actor); Korea and China both run high on `agency_explicit`
(directed at Japan) and near-zero on remedy/remorse/apology (neither is
apologizing for anything in this corpus — they are criticizing Japan). But
the country-level numbers hide very different internal structure once
decomposed by genre and `speaker_level`, which is the more important finding
for the paper's method section:

**Japan — now fully robust, not just "relatively" supported.**
`agency_explicit=0` holds in **all 30 of 30** HEAD-level records, across
every `document_type` (SPEECH n=18, PRESS_CONFERENCE n=11, STATEMENT n=1)
and every one of the four sampled prime ministers (Abe, Suga, Kishida,
Ishiba) individually — a clean, exceptionless finding across genre and
administration, for the HEAD-level main-axis sample specifically (see the
Sado silence record and the forced-labor temporal series for caveats about
within-genre variation in *other* fields like remorse/reflection). The
Round-4 MINISTER-level addition (n=4) is preliminarily consistent with this
extending to the bureaucratic level too — see "Round 4" above.

**Korea — the "60% administration-contingent" finding sharpens into a
level-contingent one.** The 28-row sample had zero OFFICIAL-level Korea
records; the 30/30/30 push added 11 (the MOFA textbook/Yasukuni/Sado
statement series). Splitting by `speaker_level`:

- HEAD (presidential, n=19; 17 non-NA): overall 0.59, with a clear
  administration gradient — **Moon 1.00 (4/4) → Yoon 0.50 (3/6, 2 NA are his
  2023/2024 Aug 15 addresses, which do not mention Japan at all) → Lee 0.43
  (3/7)**. Not a fixed national trait; continued decline under Lee rather
  than a rebound.
- OFFICIAL (MOFA spokesperson, n=11): **0.91**, essentially flat across all
  three administrations' terms (Moon-era 2/2, Yoon-era 5/6, Lee-era 4/4; the
  single 0 is the deliberately-included Yoon "dinner" null-engagement
  record, not a genuine counterexample). The "sharp, actor-naming" register
  the aggregate figure gestured at is concentrated in and driven by the
  *bureaucratic* level, which does not shift with administration change,
  while the *political/presidential* level is exactly where the
  administration-contingent variation lives. "被害政治型" fits the
  MOFA-spokesperson register far better than any single president's
  addresses.

**China — reverses from "not decomposable" to "decomposable, and the
apparent uniformity was a genre artifact after all."** The 30/30/30 push
added the corpus's first HEAD-level China data (5 records: the 2025-09-03 Xi
speeches plus three new Xi–Japan-PM APEC summit readouts). Splitting by
`speaker_level`:

- OFFICIAL (MOFA spokesperson, n=13) and UNKNOWN (third-person Xinhua/State
  Council wire narration — Nanjing, Sept 18, July 7, n=12): **1.00 each**.
  Both genres explicitly name "Japanese militarists," specific Class-A war
  criminals, or "Japanese troops" as the actor, in near-formulaic language.
- HEAD (Xi Jinping himself, n=5): **0.20** (1 of 5) — the opposite pattern.
  All three APEC summit readouts code `agency_explicit=0`: Xi's language is
  "draw lessons from history"/"face history squarely," abstract and
  unaddressed to a named actor, paired with an explicit pivot to
  present-day cooperation — structurally the closest thing in the whole
  corpus to Japan's own register. Only one of the two 2025-09-03
  war-anniversary speeches names Japan explicitly.

  This is exactly the test the first-pass diagnosis called for ("Xi
  Jinping's own speeches on the same topic, to test if the pattern holds at
  HEAD level"), and the answer is **no, it does not hold** — China's
  near-uniform `agency_explicit=1` finding is a property of the
  OFFICIAL-level MOFA-spokesperson-and-state-media commemorative register
  specifically, not a China-wide "sovereignty/legitimacy" trait that also
  describes how its head of state actually talks to Japan's leaders in
  person. `document_type` alone does not cleanly separate this (the three
  summit readouts and the Xinhua wire narration are both coded
  `document_type=OTHER`); `speaker_level` is the variable doing the work.

### Implication, and how the paper responded

All three countries show their headline `agency_explicit` rate concentrated
at a specific `speaker_level` rather than holding uniformly across the whole
national apparatus: Japan's 0% is level-independent within what the corpus
covers (only HEAD data existed at the time of this analysis; see Round 4
above); Korea's aggregate 71% is really "OFFICIAL ~90%, flat across
administrations" plus "HEAD ~50–100% declining by administration"; China's
aggregate 87% is really "OFFICIAL/media ~100%" plus "HEAD ~20%."

`draft_paper_ja.md` was revised accordingly (same day, as an explicit
follow-up requested by the user): the abstract (Japanese, English, and the
Japanese restatement), Section 4 (theoretical framework), Section 7
(discussion), and Section 8 (conclusion) were rewritten to reformulate the
three types as two discourse registers rather than three fixed national
characters — a **bureaucratic/media register** (stable across
administrations — Korea's MOFA spokesperson ~91%, China's MOFA/state-media
~100%) and a **head-of-state register** (highly variable — Japan uniformly
0% across four PMs, Korea 43–100% depending on administration, China's Xi
only 20% in APEC summit meetings). The revised conclusion argues the
persistent gap between these two registers, not either alone, is what keeps
historical-recognition disputes structurally available for renewed friction
even as head-of-state dialogue grows more conciliatory. The three-type
labels themselves (政策管理型/被害政治型/主権・正統性型) were kept, per the
user's framing of this as a wording revision rather than a request for
entirely new labels; the title/subtitle were left untouched (marked
provisional in the draft's own editorial memo). `draft_paper_ja.md`/`.docx`'s
quantitative tables (keyness analysis, apology/responsibility vocabulary
table) were also recomputed against the full 90-record corpus as part of
this pass.

**Done, 2026-09-22**: re-run against the current 94-record sample,
incorporating the 4 Round-4 MINISTER records — see "Round 4"'s "Confound
stress-test re-run against the full 94-record sample" subsection above for
the Japan HEAD-vs-MINISTER breakdown. Headline result: `agency_explicit=0`
now holds across all 34 Japan records (both speaker_levels), strengthening
rather than qualifying Japan's existing finding; `reflection` and
`remedy` both drop at MINISTER level relative to HEAD, though n=4 is too
small to treat that gap as more than suggestive. **Not yet reflected in
`draft_paper_ja.md`/`.docx`** — updating the paper's speaker-level claims
and quantitative tables for this is a separate drafting task, not done as
part of this analysis pass.

## Network access notes

An earlier session in this repository's history reported the pilot fully
blocked by an org-level egress policy denying every government domain
(`mofa.go.jp`, `kantei.go.jp`, `mofa.go.kr`, and even `en.wikipedia.org` as a
control). A later session re-tested and found that policy no longer in
effect; see `README.md`'s own "Network access notes" section for the
per-domain diagnosis used during discovery. Re-tested again on 2026-09-22
with both a default and a full browser-like User-Agent string, and by
inspecting the agent-proxy's own relay diagnostics:

- **Japan** — `japan.kantei.go.jp` reachable (earlier 404s were the site
  rejecting a bare default User-Agent, not a genuine block; browser-like UAs
  work, as does a custom research-bot UA against sub-sites with their own
  stricter WAF, e.g. `japan.kantei.go.jp/tyoukanpress/`). `www.mofa.go.jp` is
  genuinely blocked site-wide: an Akamai edge server itself returns
  `403 Access Denied` (`errors.edgesuite.net` reference ID in the body),
  independent of User-Agent — confirmed again 2026-09-22, not a fixable
  client-side issue. Wayback Machine snapshots of `www.mofa.go.jp` remain
  the working fallback (used for the Murayama Danwa landmark anchor and all
  4 Round-4 MINISTER records); `curl --compressed` is required to correctly
  decode some Wayback snapshot responses.
- **Korea** — `en.president.go.kr` (current administration) and
  `webarchives.pa.go.kr` (National Archives of Korea's official web archive,
  covering the retired Moon Jae-in/Yoon Suk Yeol eras) both reachable.
  `www.mofa.go.kr` and its embassy subdomains reset the TLS connection
  mid-handshake regardless of headers — the same class of block as MOFA
  Japan, but manifesting as a connection reset rather than an HTTP-level
  403. Confirmed again 2026-09-22 via the agent-proxy's relay diagnostics
  (`__agentproxy/status`): the proxy successfully opens a tunnel to
  `www.mofa.go.kr:443` but the remote end closes it mid-TLS-exchange after
  ~12s, consistently, across multiple attempts — a remote-side block, not a
  local proxy misconfiguration.
- **China** — `www.mfa.gov.cn` reachable directly (with intermittent,
  retriable connection resets — not a hard block). `english.www.gov.cn`
  reachable but its `/news/` page is a general links/portal page, not a news
  archive (see "What didn't work" below).

**LibreOffice headless PDF conversion remains broken** in this environment,
confirmed again on 2026-09-22 with additional diagnosis beyond earlier
sessions: `soffice --headless --convert-to pdf` fails with
`Error: source file could not be loaded` for **any** input file, including a
freshly-created minimal `.docx`, a plain `.txt` file, and even the
simplest-possible `soffice --cat` (load-only, no conversion) invocation, with
a completely fresh user profile (`-env:UserInstallation=file:///...`) and
under verbose logging (`SAL_LOG`). Disk space and profile-lock issues were
ruled out. This points to a fundamental filter/startup failure in the
LibreOffice installation itself, not a `.docx`-specific or file-specific
problem, and is outside what can be fixed from userland in this session —
`.docx` outputs continue to be validated via XSD schema check
(`/mnt/skills/public/docx/scripts/office/validate.py`) instead of a rendered
PDF preview.

## What worked

- The full 9-stage pipeline ran end-to-end across three countries and two
  discovery methods (archive crawl for Japan, hand-verified/AJAX-discovered
  search-seeded URLs for Korea/China).
- `scripts/01_discover_urls.py --seed-index-urls` for Japan's resolved
  administration-slug/month archives.
- `scripts/common.py`'s institution map covers Korea's National Archives
  web-archive mirror (`webarchives.pa.go.kr`) and multiple retired
  presidential-site domain variants.
- All 94 coded records were read in full context (not keyword-matched) —
  see `coder_notes` on each row for the specific textual basis of every
  field, including explicitly-flagged borderline calls.
- The Wayback Machine (`archive.org/wayback/available` JSON API +
  `web.archive.org/web/<timestamp>id_/<url>` direct-content fetch) as a
  reliable fallback for every live-blocked official domain encountered.

## What didn't work / open items still worth noting

- **MOFA Japan, MOFA Korea (all subdomains)** — both blocked at the network
  level (Akamai WAF for `.go.jp`; TLS ClientHello/mid-handshake reset for
  `.go.kr`), independent of headers/UA — see "Network access notes" above
  for the 2026-09-22 re-confirmation. Neither contributes documents directly
  (Wayback Machine substitutes for `.go.jp`; `.go.kr` content has so far
  been found on other reachable Korean government domains instead).
- **`eng.president.go.kr` / `english1.president.go.kr` / `english.president.go.kr`**
  (Korea's pre-Lee-administration English presidential domains) are DNS-dead
  — retired when the administration changed, not blocked. Their content
  survives verbatim on `webarchives.pa.go.kr` and was used instead.
- **China's State Council `english.www.gov.cn/news/`** section is a general
  links/portal page (links to ~200 unrelated provincial government offices),
  not a news article archive as originally assumed — its auto-crawled
  results were discarded as noise. `english.www.gov.cn/policies/` or a State
  Council Information Office-specific section might be a better target for
  future discovery, not yet tried.
- **Korea's live site (`en.president.go.kr`) pagination** was originally
  thought JS-rendered; later found to be a discoverable AJAX POST endpoint
  (see "Round 2→3" above) — resolved, not an open item, kept here for
  context on why the original pilot missed it.
- **Korea's Yoon-era (20th administration) archive gap** — a real, final
  limit, not a solvable crawl problem. Beyond the AJAX/CDX methods above,
  `?pageIndex=N`, `/speeches/list?page=N` (503), and the sibling `/briefing`
  and `/visits` listings under `webarchives.pa.go.kr/20th/eng.president.go.kr/`
  were all tried: `/briefing` has the same 5-item cap (its one Japan-adjacent
  item, a Nov 2024 Japan-ROK-US trilateral statement, turned out to be
  security/economic only, matching the existing non-engagement pattern
  rather than adding new content); `/visits` returned no parseable items.
  The National Archives of Korea's snapshot of the Yoon-era site only
  preserved page 1 of each listing category — there is no way to page
  further back through this source. Reaching further into Yoon-era
  Japan-relevant content would need a different source entirely (e.g.
  targeted web search for specific known events).
- **A stale China MFA URL**
  (`.../xwfw_665399/s2510_665401/2511_665403/202103/...`, a March 2021
  comfort-women remarks page found via search) now serves a generic "系统
  维护" (system maintenance) placeholder with HTTP 200 — a soft-404 from a
  pre-2023 URL structure the site never redirected. Logged to
  `inaccessible_sources.csv` with the correct reason rather than fabricating
  content or mis-filing it as "not relevant."
- **Two pipeline bugs found and fixed** during the original pilot:
  `04_filter_history_documents.py` and `05`/`06`'s per-stage scripts had no
  "already processed" check, so re-running them after adding new countries
  silently reprocessed and duplicated every prior row (Japan's 756→1502
  candidate rows, 757→2251 passages, before being caught and fixed); all
  three scripts now skip already-seen URLs. `common.py`'s
  `is_allowed_by_robots()` declared a `timeout` parameter but never applied
  it to the network call, so `RobotFileParser.read()` could hang
  indefinitely against a flaky host (observed against `mfa.gov.cn`) — fixed
  with an explicit `urlopen(..., timeout=...)`.
- **Japan's Chief Cabinet Secretary press conference archive**
  (`japan.kantei.go.jp/tyoukanpress/`) — confirmed video-only, no text
  transcripts, for any date tested; ruled out as a source (see "Round 4"
  above).
- **LibreOffice headless PDF conversion** — see "Network access notes"
  above; a genuine, re-confirmed environment-level break, not fixable from
  userland this session.
- 718 real, downloaded, keyword-filtered Japan candidates remain uncoded
  (`pilot_manual_review.csv`, `classification_confidence=LOW`) — out of
  scope for this phase's non-full-scale framing, not an oversight.

## China State Council discovery, and landmark anchors: 2026-09-22 follow-up

Two more open items were attempted this session: finding a working discovery
mechanism for China's State Council `english.www.gov.cn/news/` portal-page
problem, and extending `landmark_anchors.csv` with the remaining four
planned pre-2020 flashpoints.

**China discovery method — partially resolved.** `english.www.gov.cn`'s own
site search does not help: its homepage search form points to a separate
`search.english.www.gov.cn` subdomain that is a JS single-page app with no
discoverable backend API (its bundled `search.js` was inspected directly;
no API endpoint string could be found in it), and the Chinese-language
`sousuo.www.gov.cn/search-gov/data` API that does work is scoped to the
State Council's policy-document library (`zhengcelibrary`, e.g. 国发/国办发
notices), not news articles — a different content type entirely, unable to
find e.g. Nanjing Memorial Day or Yasukuni-response wire reports. However,
a **working substitute was found**: Google-style `site:english.www.gov.cn`
web search (via this session's WebSearch tool) does index the portal's news
content and can be keyword-searched directly, unlike the site's own broken
in-site search — e.g. `site:english.www.gov.cn "Nanjing Massacre" memorial
2020` immediately surfaced
`https://english.www.gov.cn/news/photos/202012/14/content_WS5fd6bf48c6d0f72576941d63.html`,
a Dec 13, 2020 Nanjing Massacre memorial ceremony report **not currently in
the corpus** (the existing series starts at 2021). This confirms the
targeted-search method already used to build the corpus's annual-
commemoration series can be made systematic (keyword search across all
years at once, not one manually-guessed year at a time) rather than staying
manual guesswork. **Not yet acted on**: fetching that specific 2020 URL (and
any other gaps this method would surface) failed — the live URL now 302-
redirects to the homepage (site restructured since 2020, as with Kantei's
pre-redesign URLs) and its Wayback Machine snapshot could not be retrieved
because of a site-wide `web.archive.org` outage encountered this session
(see below) — to be retried once that clears.

**Landmark anchors — blocked, not extended this session.** All four
remaining planned anchors (Koizumi's 2001–2006 Yasukuni visits, the 2005
textbook controversy, the 2015 Japan-Korea comfort women agreement, the
2018 Korea Supreme Court forced-labor ruling) were investigated but none
could be sourced to a primary government document this session:

- A site-wide `web.archive.org` outage was encountered partway through this
  attempt: the Wayback Machine's content-serving path
  (`web.archive.org/web/<timestamp>id_/...`) returned `Recv failure:
  Connection reset by peer` for **every** URL tried, including one that had
  worked earlier this same session (the Motegi 2020 MOFA record) and even a
  snapshot of `example.com` — while `archive.org`'s own homepage and its
  `wayback/available` JSON API (a different subdomain/path) stayed up
  throughout. This matches a previously-documented outage pattern in this
  project's history ("archive.org went fully offline site-wide" earlier in
  the session that produced the original landmark-anchor plan) recurring
  again today. Since most of these four anchors' Japan-side documents live
  on the permanently-blocked `www.mofa.go.jp` (Akamai `403`), Wayback is
  their only viable path, so this outage blocks them directly.
- Tried as non-Wayback alternatives, without success: `japan.kantei.go.jp`'s
  live "statement" archive (PM's own formal statements/speeches) is
  reachable without Wayback and does extend back to Nov 2017 (the 98th Abe
  Cabinet; confirmed by fetching `/98_abe/statement/201811/index.html`
  directly), but none of the four events' Japan-side response was a formal
  PM statement in this archive — the 2015 comfort women agreement was
  announced via a Foreign Ministers' joint press conference (Kishida
  speaking on Abe's behalf, a MOFA event) and the 2018 ruling reaction was
  a Chief Cabinet Secretary press-conference response (the same video-only,
  no-transcript archive already ruled out as a source this session for
  other purposes) — neither genre is in Kantei's statement archive, and
  pre-2017 content (Koizumi 2001–2006, the 2005 textbook controversy) is
  not on the live Kantei site at all (old `koizumispeech`-path URLs
  identified via web search all 404 on both `www.kantei.go.jp` and
  `japan.kantei.go.jp`). Korea's Supreme Court website (`eng.scourt.go.kr`,
  `engnew.scourt.go.kr`) is also currently unreachable through this
  environment's network path (connection reset / proxy policy rejection),
  ruling out the ruling's own text as an alternative primary source for
  now. A wire-service fallback (the precedent used elsewhere in this
  corpus for Korea/China records, downgrading `classification_confidence`
  to MEDIUM) was considered for the 2018 ruling but no source was found
  quoting Japan's official statement verbatim in full — only paraphrased
  news coverage and a private company's (Nippon Steel's) own press
  release, which is not a government source and would not satisfy
  `codebook.md`'s sourcing rule even as a quoted-statement fallback.

None of the four anchors were added. Retry once `web.archive.org` recovers;
Koizumi/2005-textbook in particular have no viable path other than Wayback
snapshots of MOFA (and, for Korea/China reactions, the equivalent blocked
`www.mofa.go.kr`/possibly-reachable `mfa.gov.cn`).

## Remaining open items

1. ~~Continue the contextual-coding pass over `pilot_manual_review.csv`
   (718 Japan rows)~~ — **done 2026-09-22**: every row now individually
   dispositioned (7 promoted, 711 excluded with a recorded reason) — see
   "Round 5: full backlog review" above. The backlog is closed, not merely
   further sampled; nothing remains pending in `pilot_manual_review.csv`.
2. Periodically re-test `www.mofa.go.jp` / `www.mofa.go.kr` direct access —
   both still blocked as of 2026-09-22 (see "Network access notes").
3. ~~Find a working discovery mechanism for China's State Council
   `english.www.gov.cn/news/` portal-page problem~~ — **partially done
   2026-09-22**: `site:english.www.gov.cn` web search substitutes for the
   site's own broken/wrong-content-type in-site search and already
   surfaced one new candidate (a 2020-12-13 Nanjing Memorial Day record not
   currently in the corpus) — see "China State Council discovery, and
   landmark anchors" above. Fetching that candidate (and using the method
   to find further gaps) is blocked by the `web.archive.org` outage noted
   there; retry once it clears. `mfa.gov.cn`'s press-conference archive
   still has its hard ~July-2022 lower bound, unaffected by this finding.
4. Extend `landmark_anchors.csv` with the remaining four planned pre-2020
   flashpoints (Koizumi's 2001–2006 Yasukuni visits, the 2005 textbook
   controversy, the 2015 Japan-Korea comfort women agreement, the 2018
   Korea Supreme Court forced-labor ruling) — **attempted again 2026-09-22,
   still blocked**: see "China State Council discovery, and landmark
   anchors" above for the full investigation (a site-wide `web.archive.org`
   outage, which these anchors depend on for their MOFA-hosted Japan-side
   documents; Kantei's own live statement archive does not cover the
   relevant event types even where it reaches back far enough in time;
   Korea's Supreme Court website is separately unreachable; no
   codebook-compliant wire-service fallback was found for the one anchor
   where that precedent might otherwise have applied). Retry once
   `web.archive.org` recovers.
5. ~~Re-run the genre/speaker-level/administration confound stress-test
   above against the current 94-record sample~~ — **done 2026-09-22**, see
   "Round 4"'s "Confound stress-test re-run against the full 94-record
   sample" subsection above. Headline result: `agency_explicit=0` now holds
   across all 34 Japan records regardless of speaker_level; `reflection`
   and `remedy` both drop at MINISTER level relative to HEAD (n=4, still
   too small to treat as more than suggestive). Not yet reflected in
   `draft_paper_ja.md`/`.docx` — a separate drafting task.
6. Fix LibreOffice's headless conversion (or find an alternative renderer)
   so `.docx` outputs can get a rendered visual check, not just XSD schema
   validation — diagnosed as an environment-level break (see "Network
   access notes"), not something resolved this session.
7. **New, 2026-09-22**: retry the `web.archive.org` outage-blocked items
   above once the Wayback Machine's content-serving path is confirmed
   working again — both item 3's new China candidate and all four of item
   4's landmark anchors are otherwise ready to pursue with a known method
   and, for item 4's 2015/2018 anchors, known specific event details, just
   blocked on this one external dependency.
