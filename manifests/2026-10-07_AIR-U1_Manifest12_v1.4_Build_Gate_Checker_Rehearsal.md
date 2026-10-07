# Manifest 2026-10-07 (#12): Angel Eyes AIR-U1 v1.4 — build, independent gate, checker and dress rehearsal (before any v1.4 data)

Prepared on 7 Oct 2026; the clock tool read 11:09 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, numbers and SHA-256 fingerprints only. It stores no data, no code and no secret.

**No v1.4 data has been read.** No v1.4 workflow has run. Nothing below depends on any answer key. Spec v1.4 requires all of it to be public before the CAL v1.4 run.

## 1. The v1.4 build
- **Commit:** `91e8a0a` in `VyroNyx/angel-eyes-air-u1`.
- **What it changes:** only the nine items that Spec v1.4 Change 6 lists:
  - the undefined-score rule (`n_baro`);
  - the frozen CAL list;
  - N_max = 102 and the frozen SEAL list;
  - BUDGET removed;
  - the repository-identity check and the probe key check;
  - the new terminal stops;
  - the moved v1.3 CAL sums;
  - new sums files;
  - the edits these force.
- **No detector, rule, threshold, feature, model or baseline changed.** The DEV results of manifest #10 stay binding byte for byte.
- **Build group hashes.** These change, because shared source files carry the listed edits. They are recomputed by the build's own `buildinfo`:

| Group | Manifest #10 | v1.4 |
|---|---|---|
| angel_eyes | `8e5a5f097e15…` | `f9e43a08d23ad73985afe3415225857bc8fd3c9b902aed1bb5d0696995dddd33` |
| b0_batched | `2136bbbfa63c…` | `22de9bf0fc79533b4d07ac48025c9c93c82f63e71c9a55e8f5cba1a50827ae49` |
| b0_stonesoup_harness | `fe919bc9c29c…` | `fe919bc9c29c6cafac92707a669ebdb8c521894be0bb3c3222fcd6cd4b9aa8a5` (unchanged) |
| b1 | `cf99c3807361…` | `702f40236d28331281a57153c76ba6e88ac0bf4cba7a41a486e60d1600285668` |
| data_prep | `eb958741ffc5…` | `e3ff78f6308af5ef2b2bb5e6ea8b09b31eeb1a09513c83830424669bd9ff2c02` |
| run_scripts | `b5de36dec2aa…` | `6e8a803f9b3f419f5eb020a8c49c067053993e4ddde3b4534fa2b6afc362dbe7` |

`batched_b0_code_sha256` `9aa617c15bfee8f7cdcec5496af70af36c1cd3b1c42e229ad40b388b679d4609` and `stonesoup_harness_sha256` `851842ad40f587c78fb88b1c4a6f22b2707489016b1a4f838e82bf939ca1f790` are unchanged.

## 2. The independent build gate: PASS
- **Who reviewed it:** a fresh session that had not seen the build.
- **What it found:**
  - every changed line maps to one of the nine items, and the FAIL list is empty;
  - the diff replays byte for byte;
  - the build sums are 82/82 OK;
  - the generated workflows equal the running copies;
  - the tests pass 21/21 (Python 3.11, hash-pinned packages).
- **Its nine "arguable" points** were ruled on by Opus. All are accepted, and none changes behaviour outside the items.
- **The gate diff** (`git diff 87b7991 91e8a0a`), SHA-256 **`8d3d7af24b95a48b77eef45e87c4292083ccf83a73ff0d57400b20c6ce6d3adc`** (40 files). Against `0fe93b0`, the only extra changes are the spec files of manifest #11.

## 3. The independent checker (v1.4)
- **How it was updated:** by a fresh session, from the spec text and the interface file only, without seeing build code.
- **What it now does:**
  - it checks the undefined-score rule on every row before anything else;
  - a breach exits **4** ("non_finite"), which is never a disagreement;
  - it drops NaN before each top-K;
  - it uses N_max = 102.
- **Tests:** 138 pass.
- **The CAL plan sums** have the same three entries as v1.3 (the checker, the DEV sums and the scorer public key), with the new checker hash. The plan job's checker gate passes on them.

## 4. The dress rehearsal before CAL (Change 7): 27 of 27 agree
- **The harness:** frozen as code in `tools/km001/rehearse/` and committed before this manifest. Its hashes are below.
- **What it ran on:** the label-free outputs of the v1.3 CAL run (28 days, 2,257,288 tracks), with **synthetic** answer keys sealed by a throwaway key pair. The scorer secret and the real answer keys were never used. `n_baro` was set from the NaN pattern only to exercise the code: 1,383 tracks, with B0 and B1 NaN on exactly the same rows.
- **Scenarios:**
  - S1 to S7 (CAL path): random events, 7700+7500 tracks, keys outside the population, events on top-ranked tracks, all combined, events on `n_baro < 2` tracks, and five-way ties at rank K;
  - S8 (SEAL path): a placebo with n < 20;
  - S9 (SEAL path): bookkeeping with synthetic Angel Eyes alerts.

  Each ran with seeds 1, 2 and 3.
- **Result:** the scorer and the checker **agreed on all 27 runs**. There was no crash and no stop. The run went from 04:25:59 to 04:33:45 UTC on 7 Oct 2026 (Python 3.11.15, numpy 2.2.6, scipy 1.15.3, scikit-learn 1.7.2, stonesoup 1.9.1, cryptography 46.0.7).
- **Before the sealed run,** the same harness runs on the v1.4 CAL outputs. A disagreement there is the terminal stop REHEARSAL_MISMATCH, which counts as a MISS.

## 5. Fingerprints (SHA-256)
| File (in `VyroNyx/angel-eyes-air-u1`) | SHA-256 |
|---|---|
| air_u1/build/AIR_U1_BUILD_SHA256SUMS.txt (v1.4 build sums, `91e8a0a`) | `fd77c46548521773a313cba9175490c83f4dfb28f92ba475133b4e41cadb9599` |
| air_u1/build/AIR_U1_INTERFACE.md | `5bd45921bb6bc5faaeeb29729d102eb9ccd8d2d83271b3bd1d7ed821af55f12a` |
| air_u1/build/requirements.txt (unchanged) | `a1d8f07c7c378f669f6c211f18d1f35ca5c65bcb57da642a96841f246e1570f6` |
| air_u1/build/u1/keycheck.py | `ee22d8634afc315bc05e0959ccf49a786b9bda2e26f163ac096e57813c0ae2b6` |
| .github/workflows/air-u1-dev.yml | `cc998918dc0729513e6bff1b75b2b024c7550f80510659d6fb6883405cb2f6e6` |
| .github/workflows/air-u1-headroom.yml | `34415cc828dffa6d85de5465398c62e649ce2629f3c418021c83e351eadcb709` |
| .github/workflows/air-u1-probe.yml | `468bb958fcbbeaeeea5e1ebed070fac465f94f43deeda788b7ad0d44ec6ad0af` |
| .github/workflows/air-u1-sealed.yml | `c04bf2b3a309ea22c9157d027f698d83b1726b19d483148bd354ce3c690cd5a5` |
| air_u1/checker/evaluate.py (v1.4, `0cc3e0f`) | `8da2bcde6f03e602b6c8097f1893c0f17650eba7b8907af41a4a450c532d7d7e` |
| air_u1/checker/test_evaluate.py | `f3cb29e15bb3c2ce5de73b034de5c895158cc845b7ebe7f7849826942a5444ab` |
| air_u1/cal/AIR_U1_CAL_PLAN_SHA256SUMS.txt (v1.4) | `ef0c10efa1952e30357ee6725f44cdb1d0209f7b0d89578d0be802fefb5fa694` |
| air_u1/keys/scorer_public.pem (unchanged, manifest #9) | `d4e6d9ec1bb565c919c39b305a43802228a97320e73ac4c5d045ac27dd750a40` |
| tools/km001/rehearse/rehearse.py (`1ecc3b9`) | `c911a11bbe39ee4cf941ee39a64083a32875a7bd9f6309241ac1fb9e4f30d235` |
| tools/km001/rehearse/scenarios.py | `5c2510e0d7675d655022091c996c7b718cbfe515052877d5d252e836b77b0a76` |
| air_u1/gate/v1.4/GATE_REPORT.md (`225ddf7`) | `c35355cf81b0bc5f13ab6b7b46ce298cab6cbf68ac15bb5b1899d48cc6207b4c` |
| air_u1/gate/v1.4/OPUS_RULING.md | `0c09a93f9ca252294bd0fdc4c45fcdf32bd0d99002f46965672046f4c23378eb` |
| air_u1/rehearsal/v1.4/pre_cal_rehearsal_summary.json | `745fc0694b0e098317a13a189c0e9571f2348d38bffd9474ead3c17a7fc4b940` |
| Rehearsal inputs: v1.3 CAL job artifacts 0 to 3 (zip, kept outside every repository) | `5dd527b1…9e02`, `17ea0d59…95b2`, `e909a0b3…9149`, `1e43d360…460a` |

## 6. Rulings recorded here
- **REHEARSAL_MISMATCH, and a missed 60-day start (outside its three park exceptions), each count as a MISS.**
  - The build makes both terminal, so that every keyed workflow refuses to start.
  - The MISS itself is recorded and published by hand in a manifest. The code counts a MISS only after a SEAL marker.
- **The start condition of the sealed run** (organisation minutes and storage, Change 4) is a human reading published in the pre-run manifest. It is not code.

## 7. What happens next (in order)
1. **The runner probe** in the test repository, started only by NJ's typed phrase. It must:
   - pass every check;
   - show that the scorer key reaches the job and matches the public key above;
   - show free disk of at least 90% of what the v1.3 probe recorded.
2. **The CAL v1.4 run,** started only by NJ's typed phrase.
3. **If CAL commits a clean result:**
   - the SEAL day list (the first N of the frozen 180);
   - the dress rehearsal on the v1.4 CAL outputs;
   - the start-condition readings and a pre-run manifest;
   - the sealed run, within 60 days of the CAL result.

## How to verify
1. Ask VyroNyx for any file listed. Compute its SHA-256 and compare it with the table.
2. Check that this file's commit is dated before any v1.4 workflow run in the test repository's Actions history.

## Pending
No OpenTimestamps proof exists yet for this or any earlier manifest. One will be added in a later commit if it can be made, and this file will not be edited.
