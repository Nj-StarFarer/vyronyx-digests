# Manifest 2026-10-13 (KM-061 #3): Whitman Rung 1, PRE-RUN. Build freeze, amendment A2, reader and seed rule

- **Prepared and published:** 13 Oct 2026 by Opus, on NJ's instruction "Do everything yourself" (13 Oct 2026, 06:13 IST).
- **Contents:** names, numbers and SHA-256 fingerprints only. No data, no code, no secret. The repository the hashes refer to is private.
- **What this is:** spec v1.0 §9 step 4, the pre-run manifest.
  - **The frozen test is unchanged.** Every gate, mark, window, dataset and split in spec v1.0 (Manifest #1) stands exactly as published.
  - Amendment A2 fixes only procedure.
  - The commit time of THIS file is the authoritative time of the build freeze.

## 1. The build hash

Repository `VyroNyx/whitman`, commit `e2c78df76327a750cfc6bb3afe485fe7e60e4766`.

**Build hash = SHA-256 of `r1/FREEZE_SHA256SUMS.txt`:**

`2699e43f25796a9b6d0a8df6895aae1db8eb6b73b5ca070ae603db996b620d8e`

The list pins every file the sealed run executes or reads before scoring:
- the spec and amendment A2;
- the detector code, its hash-pinned requirements and its 12 models;
- the self-tests and the independent reader with its rehearsal;
- the planting script;
- the sealed-run scripts and workflow;
- the data-check code, the DC-1 archive, the MetroPT2 census and the open-pack hash list.

This build hash is typed into the run as an input, and every job refuses to run if it differs (stop S1).

| Key file | SHA-256 |
|---|---|
| `r1/spec/WHITMAN_R1_AMENDMENT_A2.md` | `81f7b8c24ebdcc0377b5470d4335fddad4b50bc46f84c470cebae9c9896d3174` |
| `r1/build/models/MODELS_SHA256SUMS.txt` (Whitman, B1, B2 models for M3, MP2, SK, MEF) | `b37dd8ed7e015ee5c16a1c607dee56795559f09bb5c4e16463e90e915a325695` |
| `r1/build/requirements.txt` (hash-pinned wheels) | `1f00f2ff41a026e635acee70103de76f4d143a3f717f244b48d0aeb73e060960` |
| `r1/reader/reader.py` (independent reader) | `cbb9ecc8ff013e48d357e7080d6930529bc7f489601093ca01509576293c4ace` |
| `r1/reader/rehearsal.py` (dress rehearsal: 101/101 planted errors caught) | `24385dd2ca87df7af8ecb660985b86b29eabb4edab2d6f03bfefdb327b1e838e` |
| `r1/plant/plant.py` (planting script) | `ee53cde88238ae2c161bdb9bc5816f0899e12725b28d1fead7a88f921d4479d1` |
| `r1/sealed_run/opus_check.py` (second scorer, stop S6) | `24d4645a36406b466f9d522c3eaed60b9d2a25a8d0510328291e5baf5d2ba317` |
| `.github/workflows/whitman-r1-sealed.yml` (the run) | `23e9bb17d2c125beba39b39a8ffad302b7b91a735d96925b8f94a50a895f1f6a` |
| `r1/sealed_run/INSPECTION_2026-10-13.md` (inspection record) | `ca701e608297037a7e61c435d496317ff6b15c17b3429a6e6babb25e730076dd` |

## 2. Amendment A2: procedure only

1. **The planting seed is drawn inside the run**, after this freeze, from the runner's random source.
   - Its SHA-256 (over the 64 hex characters) is committed to the repository before Whitman starts.
   - The seed itself is committed with the result. This rule replaces the seed hash in this manifest.
2. **Roles.**
   - A fresh session that never opened the detector code wrote the reader and the planting script.
   - Opus wrote the second scorer and the run machinery.
   - A second fresh session inspected the machinery and found 6 blockers. All are fixed (inspection record above).
3. **MP2 input form.** MP2 is given to Whitman and both baselines as 10-second median buckets, the same cut as the open pack.
4. **The reader's readings of points the spec leaves open** are listed in A2.4. Among them: the G3 day count is the calendar span (M3 = 4, MP2 = 2).
5. **The detectors run with no network and no privileges.** The job proves this before use.
6. **Order and failure handling.**
   - Self-tests run before any sealed data is fetched.
   - The run happens once, and outputs are committed before labels.
   - A crash is scored as S5.
   - RESULT.txt holds the reader's label, or STOP S6.

## 3. The build, in brief, with honest development numbers

- **Whitman Rung 1 (R1_v1):**
  - per-channel health checks;
  - operating modes;
  - compressor physics features;
  - a relationship sheet with held-out admission (Leviathan) and single-gauge isolation;
  - a sensor-vs-machine decision.
- **CAL discovery** (PySR) ran. Its formulas gave no development gain, so **this build carries no CAL formulas**.

Development numbers, on open data only and cross-validated or time-split. **They are not test results:**
- **MetroPT-3, fit on Feb–Mar, scored on April:** F1 caught, but the warning was **−1.45 h** (late); 1 false alarm. The alarm panel missed F1 and raised 2 false alarms.
- **SKAB:** 15 of 17 caught, 1 false alarm (alarm panel: 8 of 17, 3 false alarms).
- **Marine engine:** 7 of 9 caught, 5 false alarms, 4 of them in one run (alarm panel: 6 of 9, 25 false alarms).
- **Planted sensor faults:** 37 of 40 told apart, with no alert during any of them.

**Expected weakness, stated before the run:** on the open data, the MetroPT-3 leak shows no sign inside the 48 hours before its recorded start. Gate G4 (median warning of at least 2 hours) is therefore likely to fail.

## 4. What happens next

1. One sealed run, with phrase and build hash.
2. The raw decisions are committed before any label is read.
3. The independent reader scores everything, and the second scorer re-checks it.
4. The outcome is published here **whatever the label**.

*Opus · VyroNyx Private Limited · 13 Oct 2026*
