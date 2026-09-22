# Pilot Coverage Report — Japan, Korea, China, 2020–2025

## Status: real data collected across all three countries; 28 records fully
## contextually coded (main axis) + 1 landmark anchor, 736 pending

**2026-09-22 phase 2 update** (Japan-journal, non-full-scale scope — see
`phase2_plan.md`): Korea's and China's discovery methods, previously
capped at hand-verified search results, were both genuinely improved this
session rather than just re-searched by hand:

- **Korea**: `en.president.go.kr`'s listing turned out to load via an AJAX
  POST to `/ajaxf/frBoard/bbsViewGalleryList.do` (params from the page's
  `#sendForm`), not a plain `?page=N` GET — a single `pagePerCnt=100` POST
  returns the current administration's full listing in one call. Separately,
  `webarchives.pa.go.kr`'s Moon-era (19th) listing supports genuine
  `?page=N` pagination (confirmed back to ~April 2021); the Yoon-era (20th)
  listing does not — its archived snapshot only ever captured page 1 of
  each category, a hard, unfixable limit of the National Archives'
  snapshot itself.
- **China**: `mfa.gov.cn/eng/xw/fyrbt/lxjzh/index_N.html` is a real,
  date-ordered press-conference archive, but with a hard lower bound
  around `index_145` (≈ July 2022) — pre-mid-2022 content is not reachable
  through this path at all. No working site search exists and titles are
  never topical, so finding relevant content means downloading and
  grepping full daily transcripts around known high-salience weeks
  (Yasukuni's biannual shrine festivals) rather than searching by keyword.

This added 4 new Korea records (Lee Jae Myung's 80th and 81st Liberation
Day addresses, the 2026-05-19 Korea-Japan summit joint statement, and
Moon's 2022 March First Independence Movement Day address) and 4 new China
records (two from the same Oct 17, 2025 press conference — a Yasukuni
response and a separate response on Murayama Tomiichi's death — plus an
Apr 30, 2025 response invoking Japan's WWII colonial rule over the
Philippines, and an Aug 15, 2022 Yasukuni response), all now in
`pilot_east_asia_2020_2025.csv`. It also added one pre-2020 landmark
anchor (the 1995 Murayama Danwa, retrieved via a Wayback Machine snapshot
of the blocked `mofa.go.jp`) in the separate `landmark_anchors.csv` — kept
out of this file because it is a different, purposive sampling design
(historical flashpoints, not the 2020-2025 window), not part of the same
analytical frame as the table below.

An earlier session in this repository's history reported the pilot fully
blocked by an org-level egress policy denying every government domain
(`mofa.go.jp`, `kantei.go.jp`, `mofa.go.kr`, and even `en.wikipedia.org` as
a control). A later session re-tested and found that policy no longer in
effect. See "Network access notes" in `README.md` for the full diagnosis
per domain; in short:

- **Japan** — `japan.kantei.go.jp` reachable (earlier 404s were the site
  rejecting curl's bare default User-Agent, not a block). `www.mofa.go.jp`
  genuinely blocked site-wide (Akamai WAF `403`, independent of headers).
- **Korea** — `en.president.go.kr` (current, Lee Jae Myung administration)
  and `webarchives.pa.go.kr` (National Archives of Korea's official web
  archive, covering the retired `eng.president.go.kr` / Moon Jae-in and
  Yoon Suk Yeol eras) both reachable. `www.mofa.go.kr` and its embassy
  subdomains reset the TLS connection at the ClientHello regardless of
  headers — the same class of block as MOFA Japan.
- **China** — `www.mfa.gov.cn` reachable directly (with intermittent,
  retriable connection resets — not a hard block). `english.www.gov.cn`
  reachable but its `/news/` page turned out to be a general links/portal
  page, not a news archive (see "What didn't work" below).

## Coverage table

| Country | URLs discovered | Downloaded | Kept after keyword filter | Fully coded (non-LOW) | Pending contextual coding |
|---------|------------------|------------|------------------------------|-------------------------|----------------------------|
| Japan   | 1096 | 1081 | 746 | 10 | 736 |
| Korea   | 10 (4 archive-crawled this session — see phase 2 note above — 6 hand-verified) | 10 | 10 | 10 | 0 |
| China   | 8 (4 found via targeted date search this session; 5 hand-verified originally, 1 inaccessible — see below) | 8 | 8 (1 stale "system maintenance" placeholder page not counted, see `inaccessible_sources.csv`) | 8 | 0 |
| **Total** | **1114** | **1099** | **764** | **28** | **736** |

(Plus 1 pre-2020 landmark anchor in `landmark_anchors.csv`, not counted in
this table — see the phase 2 note above.)

Japan used the full archive-crawl mechanism (`--seed-index-urls` over 78
resolved monthly statement archives — see the Japan-only section below).
The original pilot's Korea/China candidates were seeded with hand-verified
search results instead, since Korea's live-site pagination looked
JS-only and China's State Council "news" index turned out to be a portal
page, not an article archive. The 2026-09-22 phase 2 session partially
closed that gap for Korea (the live site's pagination is a discoverable
AJAX endpoint, not JS-only; the Moon-era National Archives listing supports
real pagination too) and for China (the MFA press-conference archive is
real and crawlable, just capped at ~mid-2022 and un-searchable by keyword).
Korea's Yoon-era listing and China's State Council source remain hand-
verified-only / unresolved respectively — see the phase 2 note above and
"Proposed next steps" below. Korea/China's candidate pools are still
**not** exhaustive, representative samples of everything available on
those sites the way Japan's is.

## Fully coded records (28 total, main axis)

### Japan (10) — see `pilot_japan_2020_2025.csv`

- The six annual August 15 National Memorial Ceremony for the War Dead
  addresses (2020–2025, Abe/Suga/Kishida/Ishiba)
- Ishiba's same-day press conference explaining his reintroduction of
  "remorse" language after 13 years (Aug 15, 2025)
- Suga's January 2021 press conference on the comfort-women court case
- Kishida's March 2023 forced-labor-issue press conference and the
  Kishida-Yoon joint press conference restarting "shuttle diplomacy"

Issue distribution: `WAR_GENERAL` 6, `FORCED_LABOR` 2, `COMFORT_WOMEN` 1,
`HISTORICAL_RECOGNITION_GENERAL` 1. All `speaker_level=HEAD`.

### Korea (10)

- Moon Jae-in: 75th (2020) and 76th (2021) Liberation Day addresses, his
  August 2020 message on the National Day to Honor Japanese Military
  Comfort Women Victims, and his 2022 March First Independence Movement
  Day address (a different commemorative genre — the founding of the
  Provisional Government, not Liberation Day)
- Yoon Suk Yeol: 77th (2022), 78th (2023), 79th (2024) Liberation Day
  addresses
- Lee Jae Myung: 80th (2025) and 81st (2026) Liberation Day addresses, and
  the 2026-05-19 Korea-Japan summit joint statement with PM Takaichi
  (Chosei coal mine forced-labor remains DNA analysis)

Issue distribution: `COMFORT_WOMEN` 1, `FORCED_LABOR` 2, `COLONIAL_RULE` 2,
`HISTORICAL_RECOGNITION_GENERAL` 5. All `speaker_level=HEAD`.

### China (8)

- Five MFA spokesperson responses to Japanese leaders' Yasukuni Shrine
  ritual offerings (Wang Wenbin, Aug 2022; Mao Ning, Oct 2023; Wang
  Wenbin, Apr 2024; Mao Ning, Oct 2024; Lin Jian, Oct 2025 — the Aug 2022
  and Oct 2025 records are new this session)
- Lin Jian's separate Oct 17, 2025 response on the death of former PM
  Murayama Tomiichi, extensively re-describing and endorsing the 1995
  Murayama Statement's content
- Guo Jiakun's Apr 30, 2025 response invoking Japan's WWII "aggression"
  and "colonial rule" over the Philippines (prompted by a Japan-Philippines
  summit question) — the only China record in this corpus naming a
  historical victim other than China/Korea
- The Chinese Consul General in Munich's September 2025 keynote at a
  Bavaria event commemorating the 80th anniversary of victory over Japan,
  naming the Nanjing Massacre explicitly

Issue distribution: `YASUKUNI` 5, `NANJING` 1, `APOLOGY_GENERAL` 1,
`COLONIAL_RULE` 1. `speaker_level=OFFICIAL` for all 8 (spokesperson/consul
general, not head of state/government — China's routine reactions to
Japan's historical-recognition-adjacent acts are handled at the MFA
spokesperson level, unlike Japan/Korea's head-of-state addresses).

## Notable substantive findings

**Japan** — The six Aug 15 addresses show a consistent pattern across Abe
(2020), Suga (2021), and Kishida (2022–2024): domestically-oriented
mourning for Japan's own war dead, no apology, no remorse language, no
reference to foreign victims — contrasting with landmark statements
(Murayama 1995, Abe's 70th-anniversary statement 2015). Ishiba's 80th
address (Aug 15, 2025) breaks this pattern, reintroducing "remorse" for
the first time in 13 years, which he frames in the same-day press
conference as continuity with, not departure from, prior administrations'
position.

**Korea** — A comparable pattern break, in the opposite direction: Moon's
addresses (2020, 2021, and his 2022 March First address) engage
substantively with colonial-era history (forced labor court rulings,
comfort women, explicit non-retaliation framing, "Japan must squarely face
history and be humble before it"), while Yoon's addresses show *declining*
engagement year over year — 2022 explicitly invokes the 1998 Kim Dae-jung–
Obuchi Declaration to frame "historical problems" as resolvable, 2023
mentions Japan only as a trilateral security partner with zero historical
content, 2024 mentions Japan only in passing (economic comparison, a
liberation-framing aside). Lee Jae Myung's 2025 and 2026 addresses partly
*revive* engagement relative to late-Yoon: both re-invoke "unresolved
historical issues"/"pain in the shadows of history" and re-cite the 1998
Declaration, though — like Yoon in 2022 — by reference rather than
restating specific grievances. The 2026-05-19 Korea-Japan summit statement
adds a concrete, if narrow, remedy-type data point: DNA analysis of
Chosei coal mine forced-labor remains, framed as "a small but meaningful
first step" on "historical issues" alongside otherwise purely economic/
security cooperation content. This progression is directly relevant to a
Kingdon "problem stream" analysis: the same annual genre, same country,
dropping and partially reviving historical-recognition framing across
three consecutive administrations.

**China** — The five Yasukuni responses (now spanning Aug 2022 to Oct
2025) use near-identical formulaic language each time ("spiritual tool and
symbol of Japanese militarists' war of aggression," "14 convicted Class-A
war criminals"), suggesting a standing institutional script rather than
case-by-case drafting — itself a finding worth noting for a genre/formula
analysis; the Aug 2022 instance is the most elaborate version found so
far, additionally invoking the 1943 Cairo Declaration and Taiwan's
restoration, suggesting the formula has been trimmed over time rather than
expanded. The two new non-Yasukuni records extend the range beyond that
single formula: the Oct 2025 response to Murayama Tomiichi's death treats
a Japanese apology statement (rather than a Japanese omission) as its
subject, praising and reaffirming it rather than protesting; the Apr 2025
Philippines record shows the same aggression/colonial-rule framing applied
to a third country's victimhood, not just China's or Korea's — suggesting
the "face up to history" script is a general-purpose one Japan's conduct
triggers, not a China/Korea-specific grievance formula.

## What worked

- The full 9-stage pipeline ran end-to-end across three countries and two
  discovery methods (archive crawl for Japan, hand-verified search-seeded
  URLs for Korea/China).
- `scripts/01_discover_urls.py --seed-index-urls` (added this pilot) for
  Japan's resolved administration-slug/month archives.
- `scripts/common.py`'s institution map now covers Korea's National
  Archives web-archive mirror (`webarchives.pa.go.kr`) and multiple retired
  presidential-site domain variants.
- All 20 coded records were read in full context (not keyword-matched) —
  see `coder_notes` on each row for the specific textual basis of every
  field, including explicitly-flagged borderline calls.

## What didn't work / open items

- **MOFA Japan, MOFA Korea (all subdomains)** — both blocked at the network
  level (Akamai WAF for `.go.jp`; TLS ClientHello reset for `.go.kr`),
  independent of headers/UA. Neither contributed any documents.
- **`eng.president.go.kr` / `english1.president.go.kr` / `english.president.go.kr`**
  (Korea's pre-Lee-administration English presidential domains) are DNS-dead
  — retired when the administration changed, not blocked. Their content
  survives verbatim on `webarchives.pa.go.kr` and was used instead.
- **China's State Council `english.www.gov.cn/news/`** section in
  `config.yaml` is a general links/portal page (links to ~200 unrelated
  provincial government offices), not a news article archive as assumed —
  its auto-crawled results were discarded as noise. No replacement URL was
  identified within this pilot's scope; `english.www.gov.cn/policies/` or
  a State Council Information Office-specific section might be a better
  target for a future session.
- **Korea's live site (`en.president.go.kr`) pagination** is JS-rendered
  (`?page=N` query strings return empty listings via plain HTTP GET), so
  it could not be archive-crawled the way Japan's Kantei was; only
  individually-verified URLs found via search were used. Lee Jae Myung's
  own 80th Liberation Day address (Aug 2025) could not be located this way
  and is not in this pilot despite being clearly relevant.
- **A stale China MFA URL** (`.../xwfw_665399/s2510_665401/2511_665403/202103/...`,
  a March 2021 comfort-women remarks page found via search) now serves a
  generic "系统维护" (system maintenance) placeholder with HTTP 200 — a
  soft-404 from a pre-2023 URL structure the site never redirected. Logged
  to `inaccessible_sources.csv` with the correct reason rather than
  fabricating content or mis-filing it as "not relevant."
- **A real pipeline bug was found and fixed this session**:
  `04_filter_history_documents.py` and `05/06`'s per-stage scripts had no
  "already processed" check, so re-running them after adding new
  countries silently reprocessed and duplicated every prior row (Japan's
  756→1502 candidate rows, 757→2251 passages, before being caught and
  fixed). All three scripts now skip already-seen URLs. A second bug —
  `common.py`'s `is_allowed_by_robots()` declared a `timeout` parameter but
  never applied it to the network call, so `RobotFileParser.read()` could
  hang indefinitely against a flaky host (observed against `mfa.gov.cn`) —
  was also fixed (explicit `urlopen(..., timeout=...)`).
- 736 real, downloaded, keyword-filtered Japan candidates remain
  uncoded (`pilot_manual_review.csv`, `classification_confidence=LOW`) —
  see the "What is still pending" discussion in earlier revisions of this
  report; unchanged by this session's Korea/China work.

## Proposed next steps

1. Continue the contextual-coding pass over `pilot_manual_review.csv`
   (736 Japan rows) — explicitly out of scope for the 2026-09-22 phase 2
   session (Japan-journal, non-full-scale framing), not attempted.
2. Periodically re-test `www.mofa.go.jp` / `www.mofa.go.kr` access —
   both still blocked as of 2026-09-22 (Akamai WAF / TLS reset
   respectively).
3. ~~Find a working discovery mechanism for ... Korea's live-site
   pagination~~ — **done 2026-09-22**: it's an AJAX POST to
   `/ajaxf/frBoard/bbsViewGalleryList.do`, not a dead end (see phase 2 note
   above). China's State Council `english.www.gov.cn/news/` portal-page
   problem remains unsolved; `mfa.gov.cn`'s press-conference archive was
   confirmed real and crawlable but has a hard ~July-2022 lower bound, so
   it cannot substitute for a State Council source reaching further back.
4. ~~Locate and code Lee Jae Myung's 80th Liberation Day address~~ —
   **done 2026-09-22**, along with his 81st address and a 2026-05-19
   Korea-Japan summit statement.
5. Korea's Yoon-era (20th administration) archive on `webarchives.pa.go.kr`
   is capped at whatever the National Archives snapshot captured (5 items
   per listing category) — confirmed **not further crawlable** this
   session (tried alternate pagination params and the sibling
   `/briefing`/`/visits` listings). Any further Yoon-era material would
   need hand-verified search discovery, the original (narrower) method.
6. China's Nanjing Memorial Day (Dec 13) does not reliably surface in the
   MFA's routine press conference — checked 2022 and 2023, neither had
   Yasukuni/Nanjing/comfort-women content in that day's Q&A. Nanjing-
   related remarks more likely come through a leader's own ceremony
   speech (as the existing Sept 2025 Munich consul-general record does)
   than the daily spokesperson briefing — a different discovery target
   than the press-conference archive.
7. Merge `landmark_anchors.csv` into a larger set as more pre-2020
   historical flashpoints are added (Koizumi's 2001-2006 Yasukuni visits,
   the 2005 textbook controversy, the 2015 Japan-Korea "comfort women"
   agreement, the 2018 Korea Supreme Court forced-labor ruling) — blocked
   as of 2026-09-22 by a site-wide Internet Archive outage encountered
   mid-session (`web.archive.org` returned a "Temporarily Offline"
   maintenance page); retry once that clears, since most of these depend
   on Wayback snapshots of blocked live domains (`mofa.go.jp`,
   `mofa.go.kr`).
