# Manifest 2026-10-08 (#14): Angel Eyes AIR-U1 v1.4 — the CAL result, the sealed-run plan, and the pre-run readings (before the sealed run)

Prepared on 8 Oct 2026; the clock tool read 23:05 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, numbers and SHA-256 fingerprints only. It stores no data, no code and no secret.

**No 2026 (SEAL) data has been read.** No sealed-run workflow has run. Everything below is fixed and public before the sealed run starts.

## 1. The CAL v1.4 result (committed by the scorer job of run `37578951157`, 7 Oct 2026)
- **How the run went:** the CAL headroom run started with NJ's typed phrase on 7 Oct 2026 at 05:57:52 UTC. All four day jobs succeeded on their first attempt. The scorer job opened the answer keys, the independent checker **agreed** on all 43 numbers, and the result was committed on `main` at **07:01:50 UTC** (commit `b4faecd`). No stop was recorded.
- **The numbers:**

| | Value |
|---|---|
| D_cal (days) | 28 |
| T (tracks) / K (list length, 5 per 1,000) | 2,270,920 / 11,354 |
| k (7700 key events after the 7500 drop) | 42 |
| B0_cal | 1 / 42 |
| B1_cal | 2 / 42 |
| B\* | **B1**, B\*_cal = 2 / 42 |
| P-U1 bar = max(1/5, B\*_cal + 1/10) | **1/5** (0.20) |
| Stop | none (TOO_FEW needs k ≤ 8; NO_HEADROOM needs B\*_cal ≥ 0.85; PIPELINE_SUSPECT needs B\*_cal ≤ 0.01) |
| **N (SEAL days)** = min(102, max(28, ⌈60 × 28 / 42⌉)) | **40** |

- **What it means:** the simple baselines found very little. To be labelled CORRECT, Angel Eyes must reach a recall of at least 20% on the sealed days, and the other v1 §7 conditions must hold.

## 2. The sealed-run plan
- **The SEAL days:** the first 40 dates of the frozen list `seal_a180.json` (manifest #11), in permutation order. SEAL ordinal 9 is skipped for good:
  2026-05-19, 2026-06-26, 2026-02-13, 2026-01-21, 2026-04-20, 2026-02-14, 2026-02-27, 2026-01-10, 2026-04-19, 2026-01-31, 2026-01-25, 2026-01-03, 2026-01-14, 2026-01-15, 2026-01-08, 2026-04-29, 2026-03-03, 2026-06-04, 2026-06-28, 2026-03-06, 2026-01-26, 2026-04-11, 2026-01-17, 2026-03-17, 2026-03-04, 2026-06-24, 2026-02-19, 2026-01-02, 2026-01-05, 2026-03-25, 2026-04-26, 2026-02-20, 2026-03-18, 2026-04-09, 2026-05-31, 2026-01-24, 2026-04-02, 2026-05-29, 2026-03-02, 2026-05-11.
- **How the plan files were made:** `promote_cal` made them with the build's own functions. The sealed run's own pre-checks pass on them: the CAL result is clean and consistent, `BARS.json` equals it, there are N days in permutation order, and the SHA-sums cover every plan file.
- **Latest start (Change 4):** the sealed run must start before **6 Dec 2026, 07:01:50 UTC** (12:31 IST), which is 60 days after the CAL result commit.

## 3. The dress rehearsal before the sealed run (Change 7): 27 of 27 agree
- **The copy:** Opus copied the label-free outputs of CAL run `37578951157` within their artifact life (7 Oct 2026). The artifact zips match GitHub's own digests:

| Artifact | SHA-256 |
|---|---|
| air-u1-cal-job-0 | `58f1b8b524b2c34c7fefa9aa68c550db42f4d3cd05489f68c37506813e625b51` |
| air-u1-cal-job-1 | `ceb399a66a4985e8d06ec27c859f1fbbaba93083147a01395412b85e57b13008` |
| air-u1-cal-job-2 | `6d304ba9f8303d44a6b3498e9dfd31ba1a8c591ead7c39ece260d6d88440dd3e` |
| air-u1-cal-job-3 | `8709e7625b098a2131fd59601d254435aba073ed6de22f667447669f5fd0e369` |
| air-u1-minutes-plan-1 / cal_0-1 / cal_1-1 / cal_2-1 / cal_3-1 | `a9d5a977…daf0a`, `7aae73f7…dd3bc`, `79c0cb26…dc7f3`, `e891ca9c…81b51`, `e9c2e2f5…09070` |

- **The data:** 1,284 tracks have `n_baro < 2`. B0 and B1 are NaN on exactly those rows and on no others.
- **The rehearsal:** S1 to S9 with seeds 1, 2 and 3, using synthetic keys and a throwaway key pair. **All 27 runs agree.** There is no REHEARSAL_MISMATCH.
- **A harness-only fix, recorded openly:** the first attempt of this rehearsal made no working copy in "post" mode, so every run stopped inside the harness before the scorer ran (27 HARNESS_ERROR, no scorer or checker run). Change 7 says a fault in the harness alone is not a disagreement: it is fixed in the harness only, with a new published hash, and the rehearsal is run again.
  - The fixed `rehearse.py` is `4792234a…b3fd3b`; `scenarios.py` is unchanged.
  - The pre-CAL rehearsal was also re-run with the fixed harness. It again gave 27 of 27, with numbers identical to the first run (manifest #12).

## 4. Costs and the start condition (Change 4)
- **Measured CAL costs:**
  - c_CAL = 226.833 min ÷ 28 = 8.101 min/day, so **c' = max(10.0, 1.1 × 8.101) = 10.0**. Every attempt succeeded, so all of the minutes count.
  - s_CAL = 96,356,609 bytes ÷ 28 = 3.441 MB/day, so **s' = max(3.9, 1.18 × 3.441) = 4.061 MB/day**.
- **TOO_COSTLY does not apply:**
  - 1.25 × (40 × 10.0 + 60) = **575 minutes**, which is at most 2,000;
  - 40 × 4.061 = **162.4 MB**, which is at most 450 MB.
- **The CAL artifacts:** NJ deleted them on 7 Oct 2026 at about 23:00 IST, after Opus's copy. The readings below were taken at least 24 hours later: the deletion was confirmed complete through the Actions API at 23:01:07 IST on 7 Oct, and the readings were taken from 23:01:35 IST on 8 Oct.
- **The readings:**

| Reading | NJ (billing page) | Opus (Actions API, every stored artifact) | Used |
|---|---|---|---|
| Actions minutes used this month (of 2,000) | 245 min used of 2,000 (NJ's own screenshot, 23:04 IST) | — | **1,755 min** left |
| Artifact and package storage in use, U | 0 GB used of 0.5 GB (NJ's own screenshot, 23:04 IST) | 850 bytes (5 probe artifacts; no CAL artifact left; 23:02 IST) | **under 50 MB** (the page shows GB to one decimal, so "0 GB" means under 0.05 GB) (the larger) |

- **Condition 1 (minutes):** at least 575 minutes left → **MET (1,755 ≥ 575)**.
- **Condition 2 (storage):** U ≤ 50 MB and U + 162.4 MB ≤ 450 MB → **MET (U < 50 MB, and U + 162.4 MB < 213 MB ≤ 450 MB)**.

- **The four G7 action pins** were re-checked against their release tags on 8 Oct 2026 at 23:02 IST, and all four match.

## 5. Fingerprints (SHA-256)
| File (in `VyroNyx/angel-eyes-air-u1`) | SHA-256 |
|---|---|
| air_u1/v1.4/cal/results/run_37578951157/cal_headroom.json | `9daf998bc182c0f26571c8f7441c59dd43ab14cff527045f01f3f1fc705d4ec2` |
| air_u1/v1.4/cal/results/run_37578951157/checker_report.json | `6efa535122ab02d7c0335b711de137a3f08a1ebc8b1c6948e83bd26b0dbef60a` |
| air_u1/v1.4/cal/results/run_37578951157/cal_job_reports.json | `83f681af8c4eb996a35d42c128bd24380b7a64478470a16aefece8c58af3652f` |
| air_u1/cal/BARS.json | `f7fda74f1be74fc59eb3699451cc87aee788039f838d8fd7caf0cba49c46917b` |
| air_u1/sealed/seal_days.json | `184275a0f2b9ae308237f3ee0bcfa4827afaca1a978bb8db55cc95b1be5f9f7e` |
| air_u1/sealed/AIR_U1_SEAL_PLAN_SHA256SUMS.txt | `68b098dff9cdc433a4d4037d1a5ad5f9ca93f30b34e5605b6226a2930e4645a6` |
| air_u1/reading/AIR_U1_READING_PLAN.md (unchanged; binding) | `acc3bf4026a43afe77c7f7e5e496c835e9696cd1fab405fdcd0e1649bf023371` |
| tools/km001/rehearse/rehearse.py (fixed harness) | `4792234ae3e8f16e5899630fdbdc2469ed37950f6109ff510d18f21930b3fd3b` |
| air_u1/rehearsal/v1.4/pre_seal_rehearsal_summary.json | `ee3140925c198bed8517017d447c094d77b371b2c3ca4a003324c75042e6858e` |
| air_u1/rehearsal/v1.4/pre_cal_rehearsal_summary_rerun_fixed_harness.json | `d64d054c81bf9f9267adb9cf8602f7d243144873f26001a0a71506d7bf2b5e1d` |

The build (`fd77c465…`), the checker (`8da2bcde…`), the scorer public key (`d4e6d9ec…`), the CAL plan sums and the workflows are unchanged since manifests #12 and #13.

## 6. The reading plan
The sealed result will be read under `AIR_U1_READING_PLAN.md` (`acc3bf40…`, committed before any CAL number existed), with the v1.4 readings from Spec v1.4:
- read "v1.3" as "v1.4";
- read "the BUDGET projection" as N × c' + 60;
- the named stops include REHEARSAL_MISMATCH and TOO_COSTLY;
- the build hashes of the sealed run are compared with manifest #12 before step 1.

The label decides, and nobody relabels. An outcome manifest is published whatever the label.

## 7. Next
The sealed run (`air-u1-sealed.yml`), started only by NJ's typed phrase. It runs once.

## Pending
No OpenTimestamps proof exists yet for this or any earlier manifest. One will be added in a later commit if it can be made, and this file will not be edited.
