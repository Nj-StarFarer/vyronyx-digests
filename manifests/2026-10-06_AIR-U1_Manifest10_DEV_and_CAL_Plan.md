# Manifest 2026-10-06 (#10): Angel Eyes AIR-U1 DEV numbers, runner probe and CAL plan (before the CAL headroom run)

Prepared on 6 Oct 2026; finished at 13:43 IST (clock tool). The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, versions, numbers and SHA-256 fingerprints only. It stores no data and no code.

## What is being registered
The numbers that Spec v1.3 says are set on the DEV days and then frozen, before any labelled day is read:
- the DEV-RULE numbers;
- the fitted B1 model;
- the measured cost per day;
- the number of CAL days.

It also registers the runner probe, and the plan file that the CAL headroom run checks before it starts.

**What has been seen:**
- 7 development days of 2024 (adsb.lol `globe_history_2024`).
- No answer key exists for DEV, and none was built.
- No 2025 (CAL) or 2026 (SEAL) data has been read.

## Earlier DEV runs that failed (DEV holds no labels, so it may be repeated in full: v1 §13, v1.2)
None of these made a result, a stop record or a commit on `main`. Each one was started by NJ with the typed phrase.

| Run | Started (IST, 6 Oct) | What failed | Fix |
|---|---|---|---|
| `37400725098` | 07:15 | the disk filled while the days were prepared (`OSError: [Errno 28]`) | D1 |
| `37407668107` | 08:39 | the runner ran out of memory while sampling tracks for the B0 noise calibration | D2, D3, D4 |
| `37416798326` | 10:35 | a crash on real data: tracks with no track-angle at all (`IndexError` in `moving_slope`) | D5 |

## Build changes after manifest #9 (D1–D5)
Manifest #9 froze the build at sums `dd53cc1d6c305ed19eccd02e88b12a137bba3b5025ded9454a3d761e9867dece` (76 files).
- **Why it changed:** each change fixes a failure seen on an unlabelled DEV run, or on the runner itself. No label, key or score existed or was read for any of them.
- **The changes:**
  - **D1** (SkyNet `28b2a0a`): frees disk space before the DEV run.
  - **D2 + D3** (`30059c3`): the same disk clean-up in the CAL and SEAL day jobs, a 6 GB swap file, a resource monitor, and the B0 noise sample drawn in two passes. A test shows the two-pass version gives **exactly** the same sample as the first version.
  - **D4** (`e46a423`): fixes from an independent review. Real copies in the sample, and the free-space check now runs after the swap, on both disks.
  - **D5** (`b2cc638`): an empty sub-track at the end of a view no longer crashes `moving_slope`. A test shows the numbers for every other track are byte-identical.
- **Not changed:**
  - any detector rule, threshold, feature, model or scorer;
  - the checker;
  - the scorer key;
  - `requirements.txt`;
  - the airports pin;
  - the probe workflow.
- **The build now:** sums `5da8f245ef4ecbcb2c4c41c01c85f4205846d557c01cfced032a3c5371aba5e5` (78 files; two new test files). Tests: 18 of 18 pass.
- **Build gate for D1–D5:** **PASS**, at about 13:37 IST on 6 Oct 2026. An independent reviewer that had not seen the work read the diff from `64f9ff8` to `b2cc638` and ran the tests in a copy.
  - D3 gave byte-identical output to the old version on 63 adversarial cases (empty, half-empty and reordered chunks; sizes 1 to 10⁷; three seeds).
  - D5 gave byte-identical output on 2,073 random views with empty tracks. The other 927 views were exactly the cases where the old code crashed.
  - Suite: 18 of 18 pass. The sums file verifies. The workflow files equal their build copies.
  - The clean-up, swap and monitor run before sudo is removed and before any attempt marker. They weaken no guard.
  - Two small items were accepted as notes, because neither can happen with the code as it stands:
    - an empty free-space reading would skip the free-space check, but a failing `df` already stops the step;
    - the new sums value had to be recorded somewhere public, and this manifest records it.

| File | Size (bytes) | SHA-256 (manifest #9 → now) |
|---|---|---|
| air_u1/build/AIR_U1_BUILD_SHA256SUMS.txt | 6716 | dd53cc1d… → `5da8f245ef4ecbcb2c4c41c01c85f4205846d557c01cfced032a3c5371aba5e5` |
| .github/workflows/air-u1-dev.yml | 15643 | 503007f0… → `46057404defb6af540ae2a7b4029efcad76c9d5250c726ec46434d7561782055` |
| .github/workflows/air-u1-headroom.yml | 27151 | c7b6640b… → `63dc2115c2a954a0b1a8183e779ee01ac10aeaae92ae852e02dd4e7bceaf2787` |
| .github/workflows/air-u1-sealed.yml | 37341 | bdfcfdad… → `8af0548d7b9c4797695e598d8d28aeece9c41ce6dd48e3e975c24d0339938335` |
| .github/workflows/air-u1-probe.yml | 14294 | unchanged `e6e940516d794217cb92c68dd354899b4fd041e7ac8afbabacf155ef89136ee3` |
| air_u1/build/requirements.txt | 5035 | unchanged `a1d8f07c7c378f669f6c211f18d1f35ca5c65bcb57da642a96841f246e1570f6` |
| air_u1/checker/evaluate.py | 55107 | unchanged `4b859336d707cebbd5249793f0b1b7168350f27667019bb8fbcb616442906609` |
| air_u1/checker/SHA256SUMS.txt | 244 | unchanged `e99c2602dae4e18550f49073435edb0bc7f45db68264914501436be0d1773b6c` |
| air_u1/keys/scorer_public.pem | 800 | unchanged `d4e6d9ec1bb565c919c39b305a43802228a97320e73ac4c5d045ac27dd750a40` |

## The DEV run
- **Run:** `37422096339` of `air-u1-dev.yml`, started 11:38 IST on 6 Oct 2026 by NJ with the typed phrase `NJ APPROVES THE AIR-U1 DEV RUN`. Its commit is `f3fdf9e2481fde42a7ce3ff0db54b9f7bb338703`: an automatic Leviathan state commit on top of `b2cc638` that changes only `leviathan_engine/leviathan_state.json`. The AIR-U1 files are identical to `b2cc638`.
- **Result:** green. All jobs succeeded (plan, dev, commit_results, record). The DEV step took 47.6 min, and the whole run took 50.8 min as measured by the job clock.
- **Committed by the workflow** to `air_u1/v1.3/dev/results/run_37422096339/` in commit `7c9d3a3591e412eb95908dfd931d305c39f64c6f` (12:30 IST). The run record is in `8e6a2091c0cc1a5b88e842b815cb7d626fa1c04e` (12:30 IST).
- **The 7 DEV days (2024):** 24 Mar, 31 Jul, 4 Jul, 25 Apr, 16 Jul, 28 Oct, 20 Sep, in permutation order. They are the first 7 dates of the frozen DEV permutation that have a release.

## The DEV-RULE numbers (now frozen; any change is a new spec version)
| Number | Rule (spec) | Value |
|---|---|---|
| N_p | smallest in 2..5 with at most 2% of DEV CONUS tracks as candidates (v1 §5) | **5** |
| V_max | 99.9th percentile of vertical rate, rounded up to 500 fpm; expected 4,000–7,000 (v1 §5) | **7,000 fpm**, **clamped** from a raw 7,500 fpm. The job reported VMAX_RANGE, and the clamp is recorded here as v1 §5 and v1.2 require. |
| J_max | 99.99th percentile, rounded up to 1,000 fpm, never below 15,000 (v1 §5) | **18,000 fpm** |
| B0 process noise | calibrated on DEV (v1 §5) | qh 0.15423235586407424 · qv 0.0027163002012641547 · rh 900.0 · rv 100.0 · v0h 300.0 · v0v 30.0 |
| Longest DEV track (used by the CAL and SEAL fuzz) | v1.2 Change 1 | **27,330** points |
| Cost per day c | v1.2 Change 5 (fetch + prep + detect + live check, plus shared set-up and fuzz) | mean **5.991** min, max **6.929** min (set-up 4.96 min shared) |
| CAL days | 28, or 14 if 28 × c > 400 min (v1 §13) | **28** (28 × 5.991 = 168 min) |

## Fingerprints (SHA-256)
| File | SHA-256 |
|---|---|
| air_u1/dev_final/dev_rules.json | `1cc330588915ae5647e625cecb265175fa7cfc394cfbde0fc8f6c764a9837755` |
| air_u1/dev_final/dev_summary.json | `a9c1ba9696afcf13bd0d747a27cf4c1aa2fd2c0374b6b313ad6fcafa2feffb05` |
| air_u1/dev_final/b1_model.pkl (pickle hash) | `23613bb749f461654035047c41b67e9040d253db88916bfd9c066a83b156247a` |
| B1 model, canonical tree hash | `f750e17a9212903ab32f4184d1b3b58070f10f21b74745c9add9191dac5de498` |
| air_u1/dev_final/AIR_U1_DEV_SHA256SUMS.txt | `0cdc0d9bd462ed4fc817bbaa12897461793b3fc02a1969fd24509eeb65625235` |
| air_u1/cal/AIR_U1_CAL_PLAN_SHA256SUMS.txt (lists the checker, the DEV sums and the scorer public key) | `537ca3aacd705fff31e2fd5e1c5af4af134bee099c67339ca0e7f8de2bae4599` |
| Build groups | angel_eyes `8e5a5f097e153ecb854ed39f0aa76f46871dd29a3aeb62fb2cfcfc350575325b` · b0_batched `2136bbbfa63c43ac5e0ccf9eb18239b36bfc18e27bb7150d1e0d211c181e6842` · b0_stonesoup_harness `fe919bc9c29c6cafac92707a669ebdb8c521894be0bb3c3222fcd6cd4b9aa8a5` · b1 `cf99c380736147f91fac5a0e5d2a390c7330b2cb24a18309a991f04c392f78ca` · data_prep `eb958741ffc5ee223ab681e84111644ee32e054afcc571e5c4b63c2f3f540d3c` · run_scripts `b5de36dec2aabc8fb42b6210912b060b0d41c5efbf9d19908b321d8f4e3f9227` |
| Batched B0 code | `9aa617c15bfee8f7cdcec5496af70af36c1cd3b1c42e229ad40b388b679d4609` |
| Stone Soup reference harness | `851842ad40f587c78fb88b1c4a6f22b2707489016b1a4f838e82bf939ca1f790` |

- **What `dev_final/` is:** byte-for-byte copies of the files the DEV run committed under `run_37422096339/` (checked with `cmp`).
- **Commit:** `7a551ea27eadc2b441d6ce28e39cf1d0b583e510` (13:14 IST, 6 Oct 2026), made with NJ's yes.
- **Checks still in force:** the checker (`4b859336…6609`) and the scorer public key (`d4e6d9ec…0a40`) are unchanged since manifest #9. The build is the D1–D5 build above.

## Budget, for information (v1 §13)
- **Worst case**, N = 181 sealed days: projected DEV + CAL + SEAL = **1,302.8 min**, against the limit of 1,300.
- The real projection is made after CAL, with the measured CAL minutes and the actual N.
- With the costs measured here, only the lowest band of CAL emergencies (k = 5–9, so N = 181) is at risk of a BUDGET stop. Every band from k = 10 up projects under 1,300.

## Self-checks of the DEV run
- **Build fuzz of B0, largest difference:** 6.74 × 10⁻¹¹, against a bar of 1 × 10⁻⁷. That is 128,917 points over track lengths up to 86,400, including the longest DEV track of 27,330.
- **Stone Soup live check, maximum relative difference per DEV day:**

| Day | Max relative difference |
|---|---|
| 2024-03-24 | 2.41 × 10⁻¹¹ |
| 2024-07-31 | 2.11 × 10⁻¹¹ |
| 2024-07-04 | 3.76 × 10⁻¹² |
| 2024-04-25 | 4.12 × 10⁻¹² |
| 2024-07-16 | 5.93 × 10⁻¹¹ |
| 2024-10-28 | 8.47 × 10⁻¹² |
| 2024-09-20 | 1.85 × 10⁻¹¹ |

## Runner probe (`air-u1-probe.yml`, no AIR-U1 data, no secret)
- **Runs:** probe `37338679463` (two attempts; "Re-run failed jobs") and cancel `37339327789`, started by NJ on 5 Oct with `NJ APPROVES THE AIR-U1 PROBE RUN`.
- **Checks** (from `read_probe.py`, reading the GitHub API's job steps, artifacts and annotations): **18 of 18 pass.**
  - sudo and docker are removed before any marker: PASS;
  - attempt 2 reads attempt 1's artifact: PASS;
  - `overwrite: true` replaces an artifact: PASS;
  - `overwrite: false` refuses a duplicate: PASS (annotation "409 Conflict: an artifact with this name already exists");
  - the fail-stop form `failure() || cancelled()` runs after a job timeout: PASS, and after a cancel: PASS.
- **What the runner was:** one 72 GB disk (with /mnt on the same disk), about 14 GB free at the start, about 7 GB RAM, 2 vCPU, Ubuntu 24.04.5.
- **One note:** upload-artifact at the pinned commit targets Node 20, and GitHub runs it on Node 24. It works.

## G7: action pins re-checked
The four action SHA pins were re-checked on 6 Oct 2026 at about 11:42 IST with `git ls-remote --tags` against the public action repos. **All 4 pass:**
- checkout `11d5960a…` = v4.4.0;
- download-artifact `d3f86a10…` = v4.3.0;
- setup-python `a26af69b…` = v5.6.0;
- upload-artifact `ea165f8d…` = v4.6.2. This is at least 4.2, so `overwrite` is supported.

## Corrections and notes on earlier manifests (Inspector run 1, 6 Oct 2026)
- **Manifest #9's times.** #9's text says it was "prepared on 5 Oct at about 17:40", and a private tracker entry put the gate decision at 17:45. **The commit times are authoritative:**
  - SkyNet `64f9ff8` (build, checker, workflows, public key) at 17:34 IST;
  - #9 at 17:35 IST.

  The build gate had passed before the commit, as `64f9ff8`'s message states ("build gate PASSED"). The "17:40" and "17:45" were not readings from a clock. #9 is not edited.
- **"Runs wait for November".** Manifests #5 to #9 say this. On 5 Oct the Actions minutes were checked again, and the runs began in October: probe 5 Oct, DEV 6 Oct. The CAL headroom run may also run in October. When the sealed run happens depends on the CAL count and the minutes left. The budget rule (v1 §13) is unchanged.
- **The order of the CAL plan file.** `AIR_U1_CAL_PLAN_SHA256SUMS.txt` lists the DEV sums. It was committed privately (`7a551ea`, 13:14 IST) after the DEV run and before this manifest. **This manifest registers it before any CAL run.** No CAL run has started.
- **Private evidence.** SkyNet is a private repository. Every SkyNet commit and Actions run ID in this manifest is private evidence. It is listed so it can be checked later, and it counts as public only through this manifest.

## Approval trail
- NJ approved the `dev_final/` commit: "Keep going, Chief." (13:13 IST, 6 Oct 2026), in reply to the request for a yes to commit.
- NJ approved this manifest: "Yes and Yes." (13:42 IST, 6 Oct 2026), in reply to the request to publish manifest #10.
- These are statements in private chat, and they remain claims until this manifest exists.
- **Next:** the CAL headroom run, with NJ's typed phrase. Its plan job refuses to start unless the CAL plan sums above verify.

## How to verify
1. Ask VyroNyx for any file listed. Compute its SHA-256 and compare it with the table.
2. Check that this file's commit is dated after the DEV run and before any `air-u1-headroom.yml` run in the GitHub Actions history.

## Pending
An independent timestamp proof (for example OpenTimestamps) has not been added for this manifest. It also has not been added for the earlier manifests, though each one promised it. Until it is, publication times rest on GitHub commit times alone. Any proof will be added in a later commit, and this file will not be edited.
