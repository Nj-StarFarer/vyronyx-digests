# Manifest 2026-10-03 (#3): CAL Kepler Test v0.2, the gated run (before any sealed row exists)

Prepared on 3 Oct 2026 at about 14:05 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, addresses, versions and SHA-256 fingerprints only. No data, code or results are stored here.

## What is being registered
The code and rules for the one gated run of the CAL Kepler Test v0.2 (spec fingerprint d02d5c94180b6f2daa66bac5be2a5d484d4116fb4386d7f6633acd76ea6d9b25, registered 1 Oct; build registered in manifest #2). The gated run searches for a formula on the training planets only, makes that formula public in the repository, and only then downloads the sealed planets (discovered 2019 or later) and the moons of Jupiter and Saturn, and scores it once.

## Fingerprints (SHA-256) of files in the private repo Nj-StarFarer/SkyNet
| File | Bytes | SHA-256 |
|---|---|---|
| .github/workflows/cal-kepler-gated.yml | 20167 | ab682e3038e7ee85b6b52313b7f1b9e16bbb931a27e63bbabe8ed1a6b63a258c |
| cal_tests/kepler_v0.2/build/kepler_gated.py | 32249 | 8412e2fdf560069bece6a7034e100ce4092fe3db6b49d7b714360ad4d5f66da8 |
| cal_tests/kepler_v0.2/build/kepler_moons.py | 26770 | a3dafe3fcf0c897c743ca7f212ede4c61be410f663fe69a017236f55fa79449a |
| cal_tests/kepler_v0.2/build/kepler_gated_selftest.py | 44218 | ea6c8bc637fac7f103c4d7bd3da98894e6c2c8dbbf7798a9c86451ae510fe329 |
| cal_tests/kepler_v0.2/build/GATED_RUN_NOTES.md | 13133 | 483d58d1d19274008865346071915359320802e21d0da0bb7f251dc10ffea97d |
| cal_tests/kepler_v0.2/build/OPUS_GATED_RULINGS_2026-10-03.md | 6844 | 6ef2875fd547225b79e2072f6f2c3988396a37a0a2dc6c2829c07a562cb68ee6 |
| cal_tests/kepler_v0.2/build/GATED_BUILD_SHA256SUMS.txt | 526 | c332fe7b31c40cb9b012997d005280db4836a013924b0bf2323580dd01650c98 |
| cal_tests/kepler_v0.2/build/BUILD_SHA256SUMS.txt (unchanged since manifest #2) | 961 | 5adab60a324c2f34f9ea9f0e9c8680896d4e824cd21d0bd32cedd78194be7023 |

Private-repo commits: bf06353708158d32de2d6a280a0b8a407e11c0d5 (build files, 3 Oct 2026 13:58:38 IST), 1071d2e69130956bb7235ef4ea35e62b7a448b5c (workflow, 13:59:09 IST). All 8 fingerprints were recomputed from the files as stored on GitHub after the commits and match.

## Pinned before the run
- **Sealed-planet query** (exists only inside the workflow): SHA-256 e1b28dff4968ad21bbd90c4fac33898274f6c6f28053796f29eacbad224ea540. It asks the NASA Exoplanet Archive `ps` table for default rows discovered in 2019 or later.
- **Moons page addresses**, tried in this order (JPL Solar System Dynamics, Planetary Satellite Mean Elements). Nobody at VyroNyx has opened them for this test, by rule:
  1. https://ssd.jpl.nasa.gov/sats/elem/
  2. https://ssd.jpl.nasa.gov/sats/elem/sat_elem.html
- **Training table** (downloaded 3 Oct 2026, GitHub Actions run 37104841415): canonical file SHA-256 1664b741f52d79751c6304a87746e2cf3b557a3cbcd362970d9a7380a59420c9; 1396 planets, 313 with every column filled.
- **Software pins** (recorded by the PySR self-test, run 37105223011, all 11 tests passed): PySR 2.6.0, juliacall 0.9.36, Julia 1.11.9, SymbolicRegression.jl 2.5.1, Python 3.11. Any difference in the first four is a named stop before a search is paid for.

## The order that protects the test
1. Job 1 sees the training table only; it never sees the sealed query, the moons address, or any earlier stop folder. PySR searches twice with the frozen settings; the two chosen formulas must be identical.
2. Job 2 commits the chosen formula and its SHA-256 to the repository's main branch and checks it is there.
3. Only then does job 3 start: the moons page first (if it cannot be read, the run stops before any sealed planet is downloaded), then the sealed planets, then scoring with pass bars P1-P6 and a second, independently written checker.
4. Job 4 commits the result, pass or fail, or the named stop.
A run needs the typed phrase `NJ APPROVES THE KEPLER RUN` and runs only from the main branch.

## Rules fixed before any sealed row exists (OPUS_GATED_RULINGS_2026-10-03.md)
- A retry may continue only with a formula byte-identical to the one already committed. If an earlier attempt stopped after sealed planets were downloaded, the scoring code and pass bars may not change; otherwise the test is reported VOID.
- If the moons page cannot be read, the reader may be fixed only in how it reads the page, never in which moons count; the full kept/dropped list is published before the retry, and no moon prediction is computed.
- A planet in both the training and sealed sets is removed from the sealed set before scoring, and listed.
- If the independent checker disagrees, the result is published as "DISPUTED — under Opus review"; no PASS is claimed until it is resolved in writing.
- "None of the above" is a valid named outcome.

## Forecasts (written before the run, never edited)
- Moons page stops the first attempt: 40%. Version drift stops the first attempt: 10%. Reaches scoring within 3 attempts: 85%.
- Overall PASS, given it reaches scoring: about 55% (unchanged since the frozen spec).
- A PASS proves the search machinery works on unseen data. It does not show new physics; Kepler's third law is 400 years old.

## Approval trail
NJ said "Yes" at 13:57 IST to committing the files and "Yes" at 14:00 IST to publishing this manifest. These are statements in private chat and are claims until this manifest exists. The run itself has not been started; it will be started by NJ.

## How to verify
Ask VyroNyx for any file listed. Compute its SHA-256 and look for the same string in the table. Check that this file's commit is dated before the gated run's GitHub Actions run, and that the run's formula commit comes before its sealed download in the run log.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
