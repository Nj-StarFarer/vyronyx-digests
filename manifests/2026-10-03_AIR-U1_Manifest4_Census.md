# Manifest 2026-10-03 (#4): Angel Eyes AIR-U1 census job and its pre-registered rulings (before the census is run)

Prepared on 3 Oct 2026 at about 15:53 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, versions and SHA-256 fingerprints only. No data, code or results are stored here.

## What is being registered
The AIR-U1 census: a one-off GitHub Actions job that reads ONE development day of 2024 public ADS-B history (adsb.lol `globe_history_2024`, ODbL) and writes counts only. It records the file layout, how often each field is present, how many tracks start in each of two region boxes (CONUS, Europe), and how many tracks world-wide carry the emergency codes 7700 / 7600 / 7500. It writes no positions, codes, callsigns or aircraft addresses. The 2025 (CAL) and 2026 (SEAL) periods are not touched.

The census decides which region box AIR-U1 will use. The rule for that choice, and what happens on every other outcome, was written and fingerprinted before the census exists (`AIR_U1_CENSUS_RULINGS.md` below).

## Fingerprints (SHA-256) of files in the private repo Nj-StarFarer/SkyNet
| File | Bytes | SHA-256 |
|---|---|---|
| .github/workflows/air-u1-census.yml | 6981 | 16e50779c6941b2d484703c9220c19f5af4111d519738b81b3caa7c665de6f15 |
| air_u1/census/build/air_u1_census.py | 71799 | ac7d08b5c5f8fa1d7c4e602d8c0e81e83810c456fadad88b880de27105830794 |
| air_u1/census/build/air_u1_census_selftest.py | 53292 | bd790c2a9c1b4c8ab3cdf9f5e896b42a43313f0c6c412140d1f5f89552644f7d |
| air_u1/census/build/air_u1_census_fuzz.py | 4914 | 774e1b14563c1b8969ded5871c342825ab359cb64b444a162e59b9867340ba00 |
| air_u1/census/build/AIR_U1_CENSUS_NOTES.md | 9327 | 23e2cbc280e6db68f50a86493636e9879b1cf31ef6a7cb09e321cf38a4a539ac |
| air_u1/census/build/AIR_U1_CENSUS_RULINGS.md | 4572 | 253639964ef39c3fe9a4980d1e3216fb4c5f40eef158d9c25ec5cd54a7999c36 |
| air_u1/census/build/AIR_U1_CENSUS_SHA256SUMS.txt | 443 | 55ace742586f59e099089d38efdfac9af05f1a800295316112aeea670b6ee614 |

Private-repo commits: cecf5ed633cd6f72118ba275578c7d00e46ae7d3 (build files, 3 Oct 2026 15:50:35 IST), 710e04530770152c3027d47efd678db72a47f718 (workflow, 15:51:32 IST). All 7 fingerprints were recomputed from the files as stored on GitHub after the commits and match. The job itself refuses to run if any build file differs from `AIR_U1_CENSUS_SHA256SUMS.txt`.

## Pinned before the run
- **Day choice:** `numpy.random.default_rng(20261002).permutation(the 366 dates of 2024)`, numpy 2.2.6; the first of the first 30 dates that has a release. Release variants tried in the order prod-0, prod-1, staging-0; one variant per day.
- **Track rule:** airborne points with time and position, per aircraft per day; split at gaps over 10 minutes; keep tracks of at least 10 minutes and 60 points.
- **Key event:** a squawk code seen at two or more times at least 30 s apart within a kept track (squawk field only).

## Rules fixed before the census exists (AIR_U1_CENSUS_RULINGS.md)
- **Region choice:** the box with more kept tracks that START inside it. Tie: more airborne points inside kept tracks; still tied: CONUS. Emergency, squawk and key-event counts play no part and are never split by region.
- **Partial census:** the choice is still made if at least 50% of trace files were read; otherwise the census is run again.
- **Schema check fails** (squawk on under 1% of airborne points, or a kept field missing entirely): AIR-U1 is paused and its answer key is redesigned before any further specification.
- **World-wide emergency counts:** never a stop, including zero; used only to size how many days AIR-U1 needs. Nothing is tuned on them.
- **New gap G7:** the GitHub Actions in this job are pinned by version tag, not by commit fingerprint. That is accepted for this metadata-only census and is required to change before any CAL or SEAL run.

## Approval trail
NJ said "Yes" at 15:48 IST to committing the files and "Yes" (same message) to publishing this manifest. These are statements in private chat and are claims until this manifest exists. The census has not been started; it will be started by NJ, who types the phrase `NJ APPROVES THE AIR-U1 CENSUS` himself.

## How to verify
Ask VyroNyx for any file listed. Compute its SHA-256 and look for the same string in the table. Check that this file's commit is dated before the census's GitHub Actions run, and that the run's result folder (`air_u1/census/results/run_<id>/`) is dated after it.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
