# Manifest 2026-10-03 (#6): Angel Eyes AIR-U1 Specification v1.1, an open amendment (before any AIR-U1 data is processed)

Prepared on 3 Oct 2026 at about 22:15 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, versions and SHA-256 fingerprints only. It stores no data, code or results.

## What is being registered
**AIR-U1 Specification v1.1** = Spec v1 (manifest #5, unchanged) plus one amendment file. It changes one thing: how baseline B0 is computed.

- **Why.** A build benchmark on synthetic data measured the pinned toolkit, Stone Soup 1.9.1, at about 3,200 points/s per core. That is too slow for the frozen budget at any allowed number of days: about 3,000 Actions minutes against a limit of 1,300.
- **What changes.** B0 remains the Stone Soup constant-velocity Kalman filter, with the same model, noise rule and score. A batched numpy copy of that filter now computes its scores, under three guards:
  1. a build fuzz test that requires equality with Stone Soup to 1e-9;
  2. a daily live check: Stone Soup itself re-scores 256 seeded real tracks, and they must match to 1e-6. A mismatch fires a new named stop, B0_MISMATCH;
  3. a rule on which configurations the fast copy may use.
- **Gaps closed.** It also fixes, in advance, how B0 treats points with no altitude, and that the baselines run only while no answer key is on the runner.
- **What has been seen.** This change depends on speed alone. **No AIR-U1 DEV, CAL or SEAL data has been processed.** The only real data read so far is the census counts in manifest #4. CAL (2025) and SEAL (Jan–Jun 2026) data have never been downloaded.

## Fingerprint (SHA-256) of the file in the private repo Nj-StarFarer/SkyNet
| File | Bytes | SHA-256 |
|---|---|---|
| air_u1/spec/AIR_U1_SPEC_v1.1_AMENDMENT.md | 6905 | e977d5d35b2085bc820b085927deaff6c297ca912b6ff8e7e8049dd34ef4afd4 |

- Private-repo commit: 7d65293424bdfb11bacfc7f43737b7c186ff89ee (3 Oct 2026, 22:13:20 IST).
- The fingerprint was recomputed from the file as stored on GitHub after the commit, and it matches.
- The three v1 files of manifest #5 are unchanged.

## What does not change
- The budget (1,300 minutes), the sizing rules, the bars, the placebo, the split sealed run and the answer-key handling.
- **The v1 forecasts are not edited.** The amendment adds one new forecast with today's date: a BUDGET stop after calibration at 25%. The v1 forecast of 35% still stands as written.

## Approval trail
- Opus asked NJ: "may I commit the v1.1 amendment … and publish manifest #6?" NJ answered "You are in charge" at 22:08 IST.
- Before the commit, an independent review found 9 wording and definition gaps (no blockers). All 9 were applied.
- These are statements in private chat, and they remain claims until this manifest exists. No AIR-U1 run has started.

## How to verify
1. Ask VyroNyx for the amendment file, compute its SHA-256, and compare it with the table.
2. Check that this file's commit is dated before any AIR-U1 DEV, headroom or sealed run in the GitHub Actions history.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
