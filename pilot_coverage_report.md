# Pilot Coverage Report — Japan, Korea, China, 2020–2025

## Status (2026-09-22): 94 records fully contextually coded (main axis: Japan
## 34 [30 HEAD + 4 MINISTER], Korea 30, China 30) + 1 pre-2020 landmark
## anchor, 718 Japan candidates still pending

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
| Japan   | 34 (30 HEAD + 4 MINISTER) | 718 | — |
| Korea   | 30 | 0 (candidate pools hand/search-verified, not archive-crawled at Japan's scale) | — |
| China   | 30 | 0 (same as Korea) | — |
| **Total** | **94** | **718** | **1** (1995 Murayama Danwa) |

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

**Preliminary read (n=4, not yet folded into the paper):** Japan's MINISTER
level shows 0/4 apology, 0/4 remorse, and 0/4 `agency_explicit` — matching
HEAD level's 0.00 exactly — but 2/4 reflection (both Hayashi records, both
"cannot be left as it is") vs. HEAD level's 0.67 reflection rate. This is
consistent with, but on 4 records cannot yet confirm, the hypothesis that
Japan's policy-management register is a genuinely national/institutional
trait held across both HEAD and MINISTER levels, unlike Korea's and China's
register gaps, which are sharply level-specific. n=4 is too small to update
the paper's speaker-level claims on; noted here for a future analysis pass.

## Fully coded records by country

### Japan (34) — see `pilot_japan_2020_2025.csv`

HEAD level (30): the six annual August 15 National Memorial Ceremony for the
War Dead addresses (2020–2025, Abe/Suga/Kishida/Ishiba); Ishiba's same-day
press conference reintroducing "remorse" language after 13 years (Aug 15,
2025); Suga's January 2021 press conference on the comfort-women court case;
Kishida's March 2023 forced-labor-issue press conference and the
Kishida-Yoon joint press conference restarting "shuttle diplomacy"; the
12-record Hiroshima/Nagasaki Peace Memorial Ceremony batch (2020–2025);
Kishida's July 2024 Sado Island Gold Mines silence message.

MINISTER level (4): see "Round 4" above (Motegi 2020, Hayashi ×2 2022,
Kamikawa 2024).

Issue distribution across all 34 skews toward `WAR_GENERAL` (the Aug 15/
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

**Not yet done**: re-running this stress-test against the current 94-record
sample (i.e., incorporating the 4 Round-4 MINISTER records) — the
preliminary n=4 read in "Round 4" above is suggestive but was explicitly
not treated as sufficient to revise the paper's speaker-level claims.

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

## Remaining open items

1. Continue the contextual-coding pass over `pilot_manual_review.csv` (718
   Japan rows) — still out of scope for this phase, not attempted beyond the
   two targeted proximity-keyword sweeps already done.
2. Periodically re-test `www.mofa.go.jp` / `www.mofa.go.kr` direct access —
   both still blocked as of 2026-09-22 (see "Network access notes").
3. Find a working discovery mechanism for China's State Council
   `english.www.gov.cn/news/` portal-page problem — unresolved;
   `mfa.gov.cn`'s press-conference archive was confirmed real and crawlable
   but has a hard ~July-2022 lower bound, so it cannot substitute for a
   State Council source reaching further back.
4. Extend `landmark_anchors.csv` with the remaining four planned pre-2020
   flashpoints (Koizumi's 2001–2006 Yasukuni visits, the 2005 textbook
   controversy, the 2015 Japan-Korea comfort women agreement, the 2018
   Korea Supreme Court forced-labor ruling) — blocked earlier in this
   project's history by a site-wide Internet Archive outage; not yet
   retried since, and still out of scope for the 2020-2025-main-axis-focused
   rounds completed so far.
5. Re-run the genre/speaker-level/administration confound stress-test above
   against the current 94-record sample (incorporating the 4 Round-4
   MINISTER records) before treating the register-level finding as settled
   for Japan — the current n=4 MINISTER sample is suggestive but was
   explicitly not treated as sufficient on its own.
6. Fix LibreOffice's headless conversion (or find an alternative renderer)
   so `.docx` outputs can get a rendered visual check, not just XSD schema
   validation — diagnosed as an environment-level break (see "Network
   access notes"), not something resolved this session.
