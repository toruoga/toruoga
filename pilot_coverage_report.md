# Pilot Coverage Report — Japan, Korea, China, 2020–2025

## Status: real data collected across all three countries; 20 records fully
## contextually coded, 737 pending

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
| Korea   | 6 (hand-verified, not archive-crawled — see below) | 6 | 6 | 6 | 0 |
| China   | 5 (hand-verified; 235 auto-crawled links discarded as noise) | 5 | 4 (1 was a stale "system maintenance" placeholder page, not a real 404 — see `inaccessible_sources.csv`) | 4 | 0 |
| **Total** | **1107** | **1092** | **756** | **20** | **736** |

Japan used the full archive-crawl mechanism (`--seed-index-urls` over 78
resolved monthly statement archives — see the Japan-only section below).
Korea and China did not: their site structures (JS-rendered pagination for
Korea's live site; a portal-style, not article-style, "news" index for
China's State Council source) made a full archive crawl impractical within
this pilot's scope, so both were seeded with hand-verified candidate URLs
found via targeted search instead — a legitimate but narrower discovery
method than Japan's, meaning Korea/China's candidate pools are **not**
representative samples of everything available on those sites, unlike
Japan's.

## Fully coded records (20 total)

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

### Korea (6)

- Moon Jae-in: 75th (2020) and 76th (2021) Liberation Day addresses, and
  his August 2020 message on the National Day to Honor Japanese Military
  Comfort Women Victims
- Yoon Suk Yeol: 77th (2022), 78th (2023), 79th (2024) Liberation Day
  addresses

Issue distribution: `COMFORT_WOMEN` 1, `FORCED_LABOR` 1, `COLONIAL_RULE` 1,
`HISTORICAL_RECOGNITION_GENERAL` 3. All `speaker_level=HEAD`.

### China (4)

- Three MFA spokesperson responses to Japanese PMs' Yasukuni Shrine ritual
  offerings (Mao Ning, Oct 2023; Wang Wenbin, Apr 2024; Mao Ning, Oct 2024)
- The Chinese Consul General in Munich's September 2025 keynote at a
  Bavaria event commemorating the 80th anniversary of victory over Japan,
  naming the Nanjing Massacre explicitly

Issue distribution: `YASUKUNI` 3, `NANJING` 1. `speaker_level=OFFICIAL` for
all 4 (spokesperson/consul general, not head of state/government — China's
routine reactions to Japan's historical-recognition-adjacent acts are
handled at the MFA spokesperson level, unlike Japan/Korea's head-of-state
addresses).

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
addresses (2020, 2021) and comfort-women message engage substantively with
colonial-era history (forced labor court rulings, comfort women, explicit
non-retaliation framing), while Yoon's addresses show *declining*
engagement year over year — 2022 explicitly invokes the 1998 Kim Dae-jung–
Obuchi Declaration to frame "historical problems" as resolvable, 2023
mentions Japan only as a trilateral security partner with zero historical
content, 2024 mentions Japan only in passing (economic comparison, a
liberation-framing aside). This progression is directly relevant to a
Kingdon "problem stream" analysis: the same annual genre, same country,
visibly dropping historical-recognition framing over three consecutive
years.

**China** — The three Yasukuni responses use near-identical formulaic
language each time ("spiritual tool and symbol of Japanese militarists'
war of aggression," "14 convicted Class-A war criminals"), suggesting a
standing institutional script rather than case-by-case drafting — itself a
finding worth noting for a genre/formula analysis.

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
   (736 Japan rows).
2. Periodically re-test `www.mofa.go.jp` / `www.mofa.go.kr` access.
3. Find a working discovery mechanism for China's State Council source and
   for Korea's live-site pagination (an API endpoint likely exists behind
   the JS pagination; worth a dedicated investigation), then run a proper
   archive crawl for both countries the way Japan's was done, rather than
   relying on hand-picked search results.
4. Locate and code Lee Jae Myung's 80th Liberation Day address (Aug 2025)
   and any of his other 2025 statements once a working discovery path for
   `en.president.go.kr` exists.
