# Manifest 2026-10-09 (#16): Angel Eyes AIR-U1 v2, Step 0 diagnosis: outcome (the retry was closed at Step 0 by decision)

Prepared on 9 Oct 2026 by Opus, after Step 0 ended. Published on NJ's instruction ("Publish it. And tell me the CRUX of the problem. We will fix it.", 9 Oct 2026, 20:34 IST).

An Inspector (a fresh session that did not write it) checked it against the evidence before publication. Every hash, commit, time, digest, interval and the gate odds agree, and its 19 corrections are applied.

The commit time of THIS file in this repository is the authoritative publication time. This manifest holds names, numbers and SHA-256 fingerprints only. It stores no data, no code and no secret.

## 1. The result in one paragraph
After the v1.4 sealed MISS (manifest #15), AIR-U1 was allowed **one** retry that could change only two things: the explanation filters and the order of the alert list. Before any sealed run, **three retry variants, all written before any data**, were tested on 14 of the 28 already-used 2025 CAL days (18 hidden 7700 emergency events, 1,136,300 tracks).

**The best variant (V2) put 1 of 18 events (5.6%; Wilson 95% 1.0%–25.8%) in the top 0.5% list, and that one hit is a SOFT alert:** it was explained by H2 and H5 and kept only because V2 keeps explained candidates. No hit was a SURVIVOR. V1 and V3 put 0 of 18. The sealed bar is 20%.

Of the 18 events:
- 2 had no anomalous window;
- 9 had anomalous windows but did not meet the candidate (persistence) rule;
- 7 became candidates and were explained away;
- none survived the filters.

Under this detector (a constant-velocity Kalman residual test), emergency flights are **at most slightly more unusual than everyday traffic**, far too little to reach a top-0.5% list:
- 7 of 18 events (39%) became candidates, against 35.9% of all design-half tracks and 40.8% of DEV tracks;
- of the 16 events with an anomalous window, 9 have a median NIS above the DEV median (about 8 expected by chance), 4 are above the DEV 90th percentile (about 1.6 expected), and none is above the DEV 99th percentile.

**These three pre-written variants of the allowed changes reached 1/18 at best.** Opus judges that no change allowed in the retry is likely to reach 20%. Half the events never became candidates, and the ceiling check's score-only order found 1 of 42. That is a judgement, not a proof.

## 2. The run
- **Workflow:** `air-u1-step0.yml` at commit `ca22d24` (SHA-256 `0f786f39…bb676`). Run `37940384334`, started by NJ's typed phrase at 13:55:43 UTC and ended at 14:40:49 UTC on 9 Oct 2026. About **182 Actions minutes** (per-job times, rounded up).
- **Data:**
  - 14 design CAL days (2025);
  - the 7 DEV days (2024, unlabelled, no answer key made).
  
  **The 14 holdout CAL days and every 2026 day were never touched.** All 21 days are present.
- **Reproduction check:** on all 7 DEV days, T, the candidate count, and the "explains any" count for each of H2–H6 equal the committed DEV run (`air_u1/dev_final/dev_summary.json`).
  - **Evidence:** both DEV jobs' day steps succeeded, and `step0.py` at `ca22d24` exits with code 3 on any stop, including NOT_REPRODUCED.
  - The aggregate's per-day T and candidate counts also equal `dev_summary.json`.
- **Job status:**
  - **The plan job succeeded. The 6 day jobs and the aggregate job are marked "failure", and so is the run.**
  - **Cause:** a post-run bytecode check written by Opus counted `.pyc` files. 31 are tracked in the build since commit `0fe93b0`, so that check always fails.
  - **Aggregate job:** the failing step contains only that check, so its failure is fully explained.
  - **Day jobs:** that check is the last of four post-run checks in one step. **Whether the earlier after-run checks passed (the SHA-256 re-check of the build and the git-status check) is not shown.** The run logs could not be read from Opus's session. For the design jobs, nothing else covers the after-run state.
  - Every day step succeeded. The build was checked by SHA-256 before each day job's work.
- **Fix:** a fix was committed in `3e07648` (14:17:59 UTC, while the run was in progress). It counts only new or changed `.pyc` files. No run has used it yet.
- **Artifacts** (Actions API digests):
  - summary `61eb0116…f829`
  - design-0 `ae362892…ec78`, design-1 `e414bf70…0e83`, design-2 `85a5cf26…69bf`, design-3 `d19ddb2b…8c8e`
  - dev-0 `5c084661…e58f`, dev-1 `9acefa47…f3f5`

## 3. Documents (SHA-256)
| Document | SHA-256 | Committed |
|---|---|---|
| Step 0 method `tools/km001/step0/METHOD.md` (identical at `ca22d24` and now) | `98936ffe4837e5f1c4ac7c95200b844f4caf4724cea1fb3258f6b351d203a6f3` | `ca22d24`, 13:30:20 UTC, before the run |
| `step0.py` as run | `b71902ba46d7e61b146db682c43d39a19678f8bc9a92f9056d88a20f6b8bd1b2` | `ca22d24` |
| `aggregate.py` as run | `5e002c68af212ae83d0b77e68d457ed4ba6d496980e2af942185739e25fbc81a` | `ca22d24` |
| `step0_days.py` as run | `ff954fc60ecc1a7bc5ae32ed9c9a8e0e6265d472081496ab248f16f9806a5b07` | `ca22d24` |
| `plan.py` as run | `fd3622a146747966e9d63b6308b6712f1a84e0ec880c9c7940e8c5a3c515844e` | `ca22d24` |
| Forecasts `FORECASTS.md` | `a2ca81743b8f0bc441ae26e3a4ced5f2fcb227e9317f5e241f8b108f4d500318` | `b72ae57`, 14:05:57 UTC: after the run started, and before any job finished (the first at 14:14:06) or any artifact or annotation existed. The proof is the git commit time. |
| v2 spec draft (mechanical variant pick) | `a1175148d3dceb649fa8edbfcfc9ef81d632b2581c71b1b711bc8d4426120f28` | `9f530e7`, 14:06:55 UTC, before any result |
| Result `RESULT.md` | `64f2500be51eed94c8313a00daa1bcd8d476b9e0b64c19581b0a8218667a14ab` | `4ccc840`, 14:42:10 UTC |

- The four code files were changed after the run started, in `5c4f32a` (14:05:40 UTC, which added the holdout-gate tool). **To check them, hash them with `git show ca22d24:<path>`.**
- An independent fresh-eyes reviewer reviewed the method before the run. Its findings (METHOD §8b) were applied before the run.

## 4. The fixed table (design half, pooled K = 5,681 over 1,136,300 tracks; worst case for ties at K)
| Variant (fixed before data) | Filters | List order | Hits / 18 | Wilson 95% |
|---|---|---|---|---|
| V1 | build's; explained candidates kept as SOFT | persistence first | 0 | 0%–17.6% |
| **V2** (mechanical pick) | build's; explained candidates kept as SOFT | how unusual for its altitude band and flight phase | **1 (SOFT)** | 1.0%–25.8% |
| V3 | tighter explanations (F1 + F3 + F4); kept as SOFT | as V2 | 0 | 0%–17.6% |

- **Ranks under V2:**
  - the hit ranks 5,178 (worst case 5,179) of K = 5,681;
  - of the other 17 events, 15 are ranked, from about 30,000 to about 874,000 (worst case);
  - 2 have no anomalous window and cannot be ranked.
- **Holdout gate odds:** the gate needs at least 5 of the 24 holdout events.
  - If the true rate were 1/18, the chance is about **1%**.
  - At 15%, about **29%**.
  - At the Wilson upper bound of 26%, about **78%**.
  - 1/18 is the best of three variants on the same days, so it is an optimistic point estimate.

## 5. Forecasts on file, scored (none edited)
| # | Forecast | P | Happened? |
|---|---|---|---|
| 1 | NOT_REPRODUCED stop | 5% | No |
| 2 | 15–27 design events | 80% | Yes (18) |
| 3 | H4 explains ≥ 90% of event candidates | 85% | No (6 of 7 = 86%) |
| 4 | H2 first explanation for at least half of them | 60% | Yes (4 of 7) |
| 5 | Best variant ≥ 20% | 25% | No |
| 6 | Best variant ≥ 30% | 12% | No |
| 7 | Best is V1 / V2 / V3 | 40 / 30 / 30% | V2 |
| 8 | Keeping explained candidates adds > 50 SOFT per 1,000 (DEV) | 75% | Yes (405.5 SOFT per 1,000 DEV tracks) |
| 9 | Opus ends by recommending park (after the holdout gate) | 70% | Yes, but **without** the gate: RESULT.md recommended parking straight after Step 0 |

## 6. Decision and what comes next
- **What the pre-registered plan required:** pick, then FREEZE.json, then the holdout gate (METHOD §7, v2 spec §2–3). **It was stopped by decision after Step 0.**
  - No FREEZE.json was written.
  - The holdout gate was not run.
  - No sealed 2026 day was opened.
- **Outcome for the record:** *AIR-U1 v2 retry closed at Step 0 by decision. Not frozen, no gate, no sealed run.*
- **Opus's own document recommended this** (RESULT.md: park AIR-U1 by choice, path C).
- **AIR-U1's labels stand:** v1.4 sealed MISS (#15), and this outcome.
- **Opus's reading (n = 18; a reading, not a finding):**
  - The cause is the detector's signal: unusual motion against a straight-line model barely separates emergencies from everyday traffic.
  - Half the events were lost at the candidate (persistence) rule, which is a detection stage outside the retry's allowed changes.
- **NJ's decision** (quoted above): fix the cause. Changing the signal is outside what the retry was allowed to change. So it will be a **new, separately pre-registered test**, with its own spec, its own fresh calibration days and its own sealed period, published here before it runs. It is **not** a third attempt at AIR-U1.
- **What this does not say:** anything about drones, radar or non-cooperative targets. AIR-U1 is one narrow question on ADS-B tracks.
