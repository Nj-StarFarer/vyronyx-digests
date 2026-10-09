# Manifest 2026-10-09 (#15): Angel Eyes AIR-U1 v1.4 — sealed outcome: MISS

Prepared on 9 Oct 2026 by Opus, after the sealed run ended. An Inspector (a fresh session that did not write it) checked it against the evidence on 9 Oct 2026: every number, hash, the label and the artifact digests agree; its 8 wording and completeness corrections are applied. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, numbers and SHA-256 fingerprints only. It stores no data, no code and no secret.

## 1. The result in one paragraph
On 40 sealed days of 2026 CONUS traffic (3,108,613 tracks), Angel Eyes found **1 of 83** hidden 7700 emergency tracks within an alert budget of 0.5% of all tracks (K = 15,543). The better baseline (B1) found **5 of 83**. The bar, set in advance from 2025 data (manifest #14), was a recall of 20%. **Label: MISS**, as committed by the scorer and confirmed by the independent checker. Nobody relabels it.

## 2. The run
- **Workflow:** `air-u1-sealed.yml` (SHA-256 `c04bf2b3…cd5a5`, manifest #12), run `37817812688`, attempt 1, in `VyroNyx/angel-eyes-air-u1`, from `main` at commit `c7bd56a`.
- **Started** by NJ's typed phrase at 17:35:58 UTC on 8 Oct 2026, after manifest #14 was public. **Ended** at 18:55:12 UTC. All 13 jobs succeeded on their first attempt. No stop was recorded.
- **Result commit:** `0916777` ("AIR-U1 sealed result"). Run record: `9e81583`.
- **Build check before reading:** every build file was compared with manifest #12 and they match. The build sums file is `fd77c465…b9599`, and all 82 entries check OK. The interface, requirements, `keycheck.py`, workflow, checker (`8da2bcde…d7d7e`) and scorer public key (`d4e6d9ec…0a40`) are unchanged. No build, checker, key or workflow file changed between `c7bd56a` and the result. The SEAL plan sums are `68b098df…e4645a6`, as in manifest #14.
- **Actions minutes:** about **442 min**, against the projection N × c′ + 60 = 40 × 10.0 + 60 = **460 min** (Spec v1.4 Change 4; the start condition needed 1.25 × 460 = 575 min left). This is the per-job time from the Actions API, each job rounded up to the next minute. NJ's billing page has not been read for this run.
- **Artifact storage:** 141,561,861 bytes in 17 artifacts (Actions API), against N × s′ = 162.4 MB.

## 3. Reading, in the order of the binding reading plan (`acc3bf40…`)
1. **The ending:** one committed `sealed_result.json` with a label. No stop.
2. **Placebo** (n = 83, `min_hits_to_fire` = 5): Angel Eyes 0/83, B0 1/83, B1 1/83. All are ≤ 0.05, so there is no PLACEBO_LEAK.
3. **Checker:** independent, **agrees** on all 357 checks across 40 days. Its notes say it did not check the merge-commit list hash (how the lists are written before hashing is not in the spec or the interface), the provenance, or the run lifecycle (the guard's job).
4. **Label:** **MISS**.
5. **P-U2:** does **not** fire. Angel Eyes' recall of 1/83 = 0.0120 is not below B\*_seal − 0.05 = 5/83 − 0.05 = 0.0102. The committed headline is "Angel Eyes". It was close, and B1 found more.

## 4. The fixed table
| | Value |
|---|---|
| N (sealed days) | 40 |
| T (tracks) / K (list length, 5 per 1,000) | 3,108,613 / 15,543 |
| n (7700 key events after the 7500 drop) | 83 |
| 7500 tracks dropped | 1 |
| 7600 events | 113 |
| B\* (fixed at CAL) / B\*_cal | B1 / 2/42 |
| B\*_seal | 5/83 = 6.0% |
| P-U1 bar = max(0.20, B\*_cal + 0.10) | 1/5 = 20% |

| Method | Hits / n | Recall | Wilson 95% | Precision | Lift over base rate | 7600 recall | List length used |
|---|---|---|---|---|---|---|---|
| **Angel Eyes** | **1 / 83** | **1.2%** | 0.2% – 6.5% | 0.012% | 4.6 | 0.0% (0/113) | 8,114 of 15,543 |
| B0 | 3 / 83 | 3.6% | 1.2% – 10.1% | 0.019% | 7.2 | 0.0% (0/113) | 15,543 |
| B1 | 5 / 83 | 6.0% | 2.6% – 13.3% | 0.032% | 12.0 | 0.9% (1/113) | 15,543 |

- **"Right time"** (alert window overlaps [t_E − 15 min, track end]): 1 of Angel Eyes' 1 hit, so 100%. With one hit, this says very little.
- **P-U3:** 0.0% of events are UNRESOLVED. 0.6% of Angel Eyes' alerts are H7 ("none of our explanations fit") and 99.4% are H1 (every survivor is H1 or H7, v1 §5). H7 means unknown, never discovery.
- **Survivors before the budget cut:** 2.61 per 1,000 tracks. So Angel Eyes filled only 8,114 of its 15,543 alert slots (52%), while the baselines filled all of them.

## 5. What this does and does not say
- It says: on this question, at this budget, Angel Eyes did **not** beat the simple baselines, and it was far below the bar set in advance.
- It does not say anything about detecting drones, silent drones or radar targets. AIR-U1 tests one narrow question on cooperative ADS-B tracks.
- **Prior art:** Manoranjan 2026, *"Before 7700: Detecting Persistent Trajectory Precursors in OpenSky Data"* (Zenodo 23073781). Their question is early warning in matched cohorts. Ours is blind retrieval from all traffic at a fixed alert budget. The numbers are not comparable.
- Any hits are likely to come mostly from motion **after** the declaration. The question allows that (reading plan §3, prior-art note).
- The 14 honest limits of Spec v1 §11 (`air_u1/spec/AIR_U1_SPEC_v1.md`) apply.

## 6. Forecasts on file, scored (none edited)
| Source | Forecast | P | Happened? |
|---|---|---|---|
| v1 §10 | TOO_FEW after CAL | 15% | No |
| v1 §10 | VMAX_RANGE | 15% | **Yes** (raw 7,500 fpm, clamped to 7,000; manifest #10) |
| v1 §10 | BUDGET stop after CAL | 35% | No (the rule was removed in v1.4, before any v1.4 CAL) |
| v1 §10 | NO_HEADROOM | 5% | No |
| v1 §10 | PIPELINE_SUSPECT | 20% | No |
| v1 §10 | B\*_cal between 0.10 and 0.40 | 50% | No (0.048) |
| v1 §10 | P-U1 met (CORRECT) | 30% | No |
| v1 §10 | P-U2 fires | 20% | No |
| v1 §10 | 7600 recall below 0.10 | 70% | Yes (0.0%) |
| v1 §10 | More than a third of 7700 events look ordinary | 60% | **Not scored.** No committed number measures it; it needs a per-event look, allowed only after this manifest is public, and it would be post hoc. |
| v1.1 | BUDGET stop after CAL | 25% | No |
| v1.2 | NOT_REPRODUCIBLE | 3% | No |
| v1.3 | SEAL_INCOMPLETE | 4% | No |
| v1.4 | Probe passes first time | 75% | Yes (one re-run of failed jobs was part of the probe's design; manifest #13) |
| v1.4 | Secret reaches the scorer on `main` | 50% | Yes |
| v1.4 | CAL v1.4 ends with a committed result | 75% | Yes |
| v1.4 | CHECKER_MISMATCH again in CAL | 5% | No |
| v1.4 | TOO_FEW after CAL v1.4 | 20% | No (k = 42) |
| v1.4 | N_max = 102 binds | 25% | No (N = 40) |
| v1.4 | A sealed run starts before 31 Oct 2026 | 45% | Yes (8 Oct) |
| Reading plan §6 | Named stop | 15% | No |
| Reading plan §6 | CORRECT | 25% | No |
| Reading plan §6 | INTERESTING | 15% | No |
| Reading plan §6 | **MISS** | 45% | **Yes** |
| Reading plan §6 | P-U2 fires | 20% | No |
| Reading plan §6 | More than half of hits are "right time" | 70% | Yes (1 of 1) |
| Prior-art note | Most hits come from motion after the declaration | 70% | **Not scored yet.** It needs a per-event look, allowed only after this manifest is public. |
| DEV manifest #10 | Only k = 5–9 risks a BUDGET stop | — | Held (k = 42, outside the 5–9 band; BUDGET itself was retired in v1.4 Change 4) |

v1 §10 says v0's forecasts stay on record. They are not in this repository or in vyronyx-digests, so they are not scored here.

**Brier score over the 25 scored yes/no forecasts: 0.111** (0 is perfect; always saying 50% gives 0.25). The reading-plan set alone scores 0.090. The biggest misses were VMAX_RANGE (said 15%, it happened) and the four forecasts at 45–50%.

## 7. What happens next
- **The parking rule (v1 §13):** this is the first MISS. AIR-U1 gets **one amendment cycle**: a new spec version and a new sealed period, each published before its run. A second MISS parks AIR-U1 until NJ reopens it.
- **No tuning:** no v1.4 code, rule, threshold or bar changes for this test. The KM-001 "No-tune" cell is ticked only if no AIR-U1 build or spec commit follows, other than the new spec version for a new period.
- **Single-event looks** happen only after this manifest is public, and are labelled "post hoc, exploratory". They can never change this label or any number above.

## 8. Fingerprints (SHA-256)
| File (in `VyroNyx/angel-eyes-air-u1`, commit `0916777`) | SHA-256 |
|---|---|
| air_u1/v1.4/sealed/results/run_37817812688/sealed_result.json | `c0708c69a449daed80cf3420aa9f2659de62c922f3a3a27a652de2cda53d5999` |
| air_u1/v1.4/sealed/results/run_37817812688/checker_report.json | `ca4f0b2386233779ced2d80932eed3799c21a6e23e3dcd52c29b5c1ed49d96e8` |
| air_u1/reading/AIR_U1_READING_PLAN.md (binding, unchanged) | `acc3bf4026a43afe77c7f7e5e496c835e9696cd1fab405fdcd0e1649bf023371` |
| air_u1/build/AIR_U1_BUILD_SHA256SUMS.txt (unchanged since #12) | `fd77c46548521773a313cba9175490c83f4dfb28f92ba475133b4e41cadb9599` |
| air_u1/sealed/AIR_U1_SEAL_PLAN_SHA256SUMS.txt (unchanged since #14) | `68b098dff9cdc433a4d4037d1a5ad5f9ca93f30b34e5605b6226a2930e4645a6` |

| Run artifact (GitHub digest) | SHA-256 |
|---|---|
| air-u1-seal-result | `4b9db2e1b5cd6a95079857d75f2661d6835bc43be43bfe0f944c3e5d2955e78e` |
| air-u1-merge | `a423bf886b51356a7a39286b9180a1ce3cbd072cb5c17077559450a7da6f65bd` |
| air-u1-merge-public | `36d54155f61db359227499d22df54b03f69d7d5647135b30f15cc2b56ba9681c` |
| air-u1-seal-job-0 … 6 | `2a4bdb8b…e387`, `2942ec31…b28b`, `b17ddac5…c38c5e`, `60daacca…c376073`, `79c31568…a41681`, `850a8217…866b68`, `b6fdfec1…37809` |
| air-u1-done-0 … 6 | `1128f48f…99370`, `408ee0c4…f99b8`, `f5528752…efa9a`, `f227c384…fce98`, `eae9b252…63688`, `45fd3789…83346`, `f237c892…e6893` |

## How to verify
1. Ask VyroNyx for any file listed. Compute its SHA-256 and compare it with the table.
2. Check that manifest #14 was committed before run `37817812688` started, and that this file was committed after it ended.

## Pending
No OpenTimestamps proof exists yet for this or any earlier manifest. One will be added in a later commit if it can be made, and this file will not be edited.

*Opus · VyroNyx Private Limited · 9 Oct 2026*
