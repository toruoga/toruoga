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
| **Korea main axis (2020-2025+)** | **+3 downloaded (raw+cleaned)** | Solved the JS-pagination problem for real: `en.president.go.kr`'s listing is an AJAX POST to `/ajaxf/frBoard/bbsViewGalleryList.do` (params in the page's `#sendForm`), not unreachable — just not a plain GET. A `pagePerCnt=100` POST returned the full 48-item listing for the current (Lee Jae Myung) administration in one call. 3 of the 48 are on-topic: 81st Liberation Day address (2026, `MK8xT9SG`), 80th Liberation Day address (2025, `96ecUYVL`), Korea-Japan summit joint statement with PM Takaichi (`VWkmhWnq`, mentions Chosei coal mine forced-labor remains repatriation). Not yet contextually coded. Yoon/Moon-era gaps still open via webarchives.pa.go.kr with the same trick, not yet attempted. |
| **China main axis (2020-2025)** | in progress | `mfa.gov.cn/eng/xw/fyrbt/lxjzh/index_N.html` confirmed crawlable (paginated by date, ~7 entries/page, index_1 = most recent). No site search endpoint found (`search.fmprc.gov.cn` TLS cert mismatch). Given the volume of pages back to 2020, next step is to jump toward known high-salience dates (Aug 15, Dec 13 Nanjing memorial, spring/autumn Yasukuni festival weeks) rather than paging through every week. |

This file is a working tracker, not a publication output — delete or fold its
content into `pilot_coverage_report.md` once phase 2 is complete.
