# Codebook — East Asia Historical Recognition Corpus

Governs classification of official Japanese, South Korean, and Chinese
government statements on historical-recognition issues (2000-01-01 to
2025-12-31). All coders (human or LLM-assisted) must follow this document.
When in doubt, code `UNKNOWN` / `NA` and route the record to
`manual_review.csv`. **Never infer a value that is merely plausible.**

## 1. Unit of analysis

`Document -> Question/Answer or speech section -> relevant historical-recognition passage`

A single webpage (e.g. a press conference transcript) may yield zero, one,
or many records. Extract only the Q&A pairs or passages that concern a
historical-recognition issue; do not create a record for irrelevant
portions, but preserve the parent document's URL and metadata on every
record drawn from it.

## 2. Eligible sources

Official only: Japan (Kantei, MOFA Japan), South Korea (Office of the
President, MOFA Korea), China (State Council, MOFA/MFA China). No
Wikipedia, press, blogs, think tanks, secondary literature, or mirrors.
Search engines are for *discovery* only — a record requires the underlying
official page to have been opened and its text verified.

## 3. speaker_level

- `HEAD` — Prime Minister / President / equivalent head of government or state.
- `MINISTER` — Foreign Minister or other cabinet minister, when the statement is relevant.
- `OFFICIAL` — spokesperson, vice/deputy minister, senior official, press secretary, or other identifiable official below ministerial level.
- `UNKNOWN` — only when the source itself does not establish the speaker's level. Never inferred from context alone.

Also record `speaker_name`, `speaker_position`, `institution` verbatim from the source.

## 4. issue_primary (single value) / issue_secondary (list)

`WAR_GENERAL, AGGRESSION, COLONIAL_RULE, COMFORT_WOMEN, SEXUAL_SLAVERY,
NANJING, YASUKUNI, HISTORY_TEXTBOOK, FORCED_LABOR,
COMPENSATION_REPARATION, APOLOGY_GENERAL, HISTORICAL_RECOGNITION_GENERAL,
OTHER`

Pick the most specific `issue_primary` the passage actually supports; do
not force a narrow label onto a genuinely general statement — use
`HISTORICAL_RECOGNITION_GENERAL` in that case. Attach any additional
applicable codes as `issue_secondary` (e.g. `COMFORT_WOMEN` primary with
`[APOLOGY_GENERAL, COMPENSATION_REPARATION]` secondary).

## 5. Kingdon dimensions (multi-label, not mutually exclusive)

Three independent binary fields, each `1` / `0` / `NA` (cannot determine):

- `kingdon_problem` — the passage defines, describes, attributes, frames, or evaluates a historical issue as a public problem (victimization, aggression, injustice, responsibility, historical fact, suffering, unresolved issue, denial or recognition of wrongdoing).
- `kingdon_policy` — the passage discusses a concrete/potential solution, institutional response, agreement, compensation, apology measure, fund, education, legal arrangement, negotiation framework, or implementation mechanism.
- `kingdon_politics` — the passage concerns political negotiation, diplomatic pressure, mobilization, legitimacy, intergovernmental conflict, domestic contestation, sovereignty, national dignity, or strategic signaling.

A single passage may score `1` on all three. Also record
`kingdon_confidence` = `HIGH` / `MEDIUM` / `LOW`, reflecting how directly
the passage supports the codes assigned.

## 6. Apology / responsibility language (independent binaries)

- `apology` — explicit apology / apologizing language.
- `explanation` — description or explanation of past acts or the government's position.
- `remorse` — expressions of remorse, regret, sorrow, responsibility, or contrition.
- `reflection` — expressions of reflection, recognition, learning from the past, or self-examination.
- `remedy` — funds, compensation, reparations, institutional measures, assistance, corrective action, settlement, **regardless of who the beneficiary is**. This is the broad/raw measure; see `remedy_victim_directed` below for the narrower, analytically load-bearing version.
- `pardon_or_forgiveness` — request for forgiveness/pardon, or reconciliation explicitly framed as forgiveness.

Do not assume semantic equivalence merely because a related word appears
(e.g. "regret" about a procedural delay is not `remorse` about a historical
wrong) — read the surrounding passage.

- `remedy_victim_directed`: `1` only if `remedy=1` AND the measure is the
  speaker's own government committing to or providing compensation/relief
  directed at the **other** country's historical victims (e.g. Japan
  compensating Korean forced-labor victims). `0` in every other case,
  including: the speaker's government caring for its own citizens/victims
  (Japan: hibakusha support, war-dead repatriation, Okinawa base-burden
  relief; Korea: Comfort Women Memorial Day measures, Korea's own
  third-party compensation plan for its own citizens); one country
  welcoming or commenting on the *other* country's own domestic measure;
  or one country demanding remedy *from* the other. This field exists
  because `remedy` alone conflates self-directed and victim-directed
  relief, which were found (2026-10-02 review pass) to look identical at
  the keyword level but to mean opposite things substantively — see
  `pilot_coverage_report.md`, "Attribution-direction split and remedy
  narrowing," for the full derivation and the three records whose
  `remedy` value was corrected as a result.

## 7. Responsibility / agency

- `responsibility_actor` in `{STATE, GOVERNMENT, LEADER, MILITARY, PEOPLE_NATION, UNSPECIFIED, OTHER}`. Note: this records only the *type* of actor named, not *which country*'s actor — see `attribution_direction` below for that.
- `agency_explicit`: `1` if the responsible actor is explicitly named; `0` if expressed through passive/impersonal/abstract/agentless language (e.g. "mistakes were made," "it is regrettable," "the events of the past," "suffering occurred"); `NA` if not applicable. Judge from context, not mechanically.
- `attribution_direction` in `{SELF, OTHER, NONE, NA}`, defined only when
  `agency_explicit` is not `NA`: `SELF` if the speaker's own government is
  named as the responsible actor; `OTHER` if the other country is named;
  `NONE` if `agency_explicit=0` (no actor named); `NA` mirrors
  `agency_explicit=NA`. Added because `agency_explicit` alone cannot
  distinguish "Japan names Japan as responsible" from "Korea names Japan
  as responsible" — both score `agency_explicit=1` despite being
  substantively opposite claims (self-attribution vs. other-attribution).
  Empirically (2026-10-02 review pass, full 102-record corpus), every
  Korea/China `agency_explicit=1` record is `OTHER` (names Japan); the
  only `SELF` record in the corpus is the 1995 Murayama Danwa landmark
  anchor.

## 8. document_type

`STATEMENT, PRESS_CONFERENCE, SPEECH, JOINT_STATEMENT, WRITTEN_RESPONSE, OTHER`.
For press conferences, keep `question_text` and `response_text` separate
where the source allows it.

## 9. audience_orientation

`DOMESTIC, INTERNATIONAL, MIXED, UNKNOWN`. Judge from the actual event/context
(venue, addressee, occasion) — an English-language page is not automatically
`INTERNATIONAL`.

## 10. Provenance / non-hallucination rules

- Every record requires a verified `source_url` that was actually opened.
- `raw_text`/quoted fields must be verbatim from the source; never paraphrase into `relevant_excerpt`.
- Do not infer speaker identity from administration/date alone.
- Do not infer an issue from a page title alone.
- Do not assume the contents of an inaccessible page.
- Do not manufacture dates.
- If unknown: write `UNKNOWN` / `NA`, never a best guess.
- `official_translation`: `1` if the source page is itself an official-government translation (e.g. MOFA's English rendering of a Japanese original), `0` if the retrieved text is the original-language official text, `NA` if unclear.
- `source_language`: ISO 639-1 code of the retrieved text's actual language (e.g. `en`, `ja`, `ko`, `zh`).

## 11. Deduplication

Two records are duplicates if they share (a) exact URL, (b) normalized
title + date, or (c) near-identical text (hash / high similarity) across
official mirrors (e.g. the same statement posted on both Kantei and MOFA).
Assign a shared `duplicate_group_id`; mark exactly one record per group
`canonical_record = 1` (prefer the primary institutional source — Kantei
for PM statements, MOFA for diplomatic statements) and `0` for the rest.
Do not delete duplicates.

## 12. classification_confidence

`HIGH` / `MEDIUM` / `LOW`, coder's own confidence in the full set of codes
assigned to the record. Any `LOW` record, any record with unclear speaker
identity, ambiguous issue coding, ambiguous Kingdon coding, conflicting
metadata, or extraction problems must be added to `manual_review.csv`.
