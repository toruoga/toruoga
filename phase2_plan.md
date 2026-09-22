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

## Running tallies after 2026-09-22 session

- Japan: 10 main-axis (unchanged) + 1 landmark anchor (Murayama 1995)
- Korea: 6 → 10 (candidates; none of the 4 new ones contextually coded yet)
- China: 4-5 → 8 (candidates; none of the 3 new ones contextually coded yet)

This file is a working tracker, not a publication output — delete or fold its
content into `pilot_coverage_report.md` once phase 2 is complete.
