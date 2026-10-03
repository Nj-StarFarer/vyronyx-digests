# Manifest 2026-10-03 (#2): CAL Kepler Test v0.2 build

Prepared on 3 Oct 2026 (clock tool read 10:22 IST). The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names and SHA-256 fingerprints only. No data, code or results are stored here.

## What is being registered
The build for the CAL Kepler Test v0.2 (frozen 1 Oct 2026, spec fingerprint d02d5c94180b6f2daa66bac5be2a5d484d4116fb4386d7f6633acd76ea6d9b25, registered in the manifest of 1 Oct): the pipeline, the self-tests, the independent checker (written in a separate session from the spec text alone, sharing no code with the build), the train-set query, the Opus rulings of 3 Oct 2026 (Amendment A1), and the two GitHub Actions workflows that will run the train download and the PySR self-tests.

## Fingerprints (SHA-256) of files in the private repo Nj-StarFarer/SkyNet
| File | Bytes | SHA-256 |
|---|---|---|
| cal_tests/kepler_v0.2/build/BUILD_SHA256SUMS.txt | 961 | 5adab60a324c2f34f9ea9f0e9c8680896d4e824cd21d0bd32cedd78194be7023 |
| cal_tests/kepler_v0.2/build/OPUS_RULINGS_2026-10-03.md | 5815 | ca0a45481fe217134b1a6dacda7c716256636ca4ef56d3c3b096d096e6c3cea9 |
| cal_tests/kepler_v0.2/build/RULINGS_NEEDED.md | 6461 | 57f4896615b0734c632bba5cfa47b5eea1f8f2b3247c2d631ec43c0f52830463 |
| cal_tests/kepler_v0.2/build/kepler_core.py | 23750 | a0d2ee5081152ac20fba2e09c4ef939666fa6598a01e60e8ba7c46ce0c72ed7e |
| cal_tests/kepler_v0.2/build/kepler_fetch_train.py | 5554 | d403d76849548960fbe06c3a5813a05c0de5fbf9e8ab4c7cace2c6d2326b1db4 |
| cal_tests/kepler_v0.2/build/kepler_search.py | 5337 | c2a9f2dbe18971430707075ad14113e95bc17b8f6ddcf710e004dacb41e3dc1a |
| cal_tests/kepler_v0.2/build/kepler_selftest.py | 20443 | ada09a25c106bf822fd97f9af59d47b9a52c64b47e50aeee170ae954de256837 |
| cal_tests/kepler_v0.2/build/kepler_synth.py | 3580 | d8c13c30e01476f6b2b0d582a042f2da394f39fca0c2891429b0046a7d94dae2 |
| cal_tests/kepler_v0.2/build/train_query.adql | 283 | 5b83ddb70181064ee18b27a6fd4d0b7da980243a4b7d8344928b4d2fdaf6eabd |
| cal_tests/kepler_v0.2/build/independent/AMBIGUITIES.md | 5847 | f6b156962655af2eb115d9eeb46fb9925ee2c9cbe625a9ebf55fe20d421d62ea |
| cal_tests/kepler_v0.2/build/independent/indep_check.py | 14026 | 8a8f0cf99b838705ff42b49197262adfd5fc30ea442803ae098f6d74e2a0793d |
| cal_tests/kepler_v0.2/build/independent/selftest_indep.py | 6143 | 850ce21712b273c60676448e5a01aa32d7333af291a8297d7d822d38f156e7e2 |
| .github/workflows/cal-kepler-selftest.yml | 4979 | 5361a3244d692342c65a02d476f08570514e60d0c392ccb69bcfeb6e5b8e7932 |
| .github/workflows/cal-kepler-train.yml | 4670 | 997a89edde9d26aed6659f089096e6dbb397403b9d163cccda585604b34987dd |

Private-repo commits: 4956fe69bda43bf9b9a15a8b4a15f56876387bf0 (build files, 3 Oct 2026 10:17:11 IST), 1a71874c92eb549f162f86eaa80b06ae24f50164 (independent checker, 10:17:56 IST), 26f4d61e434f23e48b1d88e03909b629871a37c2 (workflows, 10:18:35 IST). All 14 fingerprints were recomputed from the files as stored on GitHub after the commits and match the local files.

## What was decided before this manifest (Amendment A1, in OPUS_RULINGS_2026-10-03.md)
- Opus accepted nine readings where the frozen spec was silent, and set the rule for the columns PySR sees: if fewer than 300 train rows have every column filled, the distractor column with the most blank cells is dropped, one at a time, never below 5 distractors; if 300 complete rows are still not reached, the named stop S2b ends the test. Only blank counts are used, never values. This was fixed before any data was seen.
- P6 compares CAL with the engineer's baseline (R2) on the same sealed rows.
- The gated run will search twice on the train set (stop S3 if the two chosen formulas differ).
- Typed phrases, in this order: `NJ APPROVES THE KEPLER TRAIN DOWNLOAD`, then `NJ APPROVES THE KEPLER SELFTEST`, then (later) `NJ APPROVES THE KEPLER RUN`.
- Approval trail: Opus approved A1 on 3 Oct 2026 at about 10:05 IST under NJ's delegation ("You are in command"); NJ said "Yes" at 10:15 IST to committing the build and publishing this manifest. These are statements in private chat and are claims until this manifest exists.

## State at publication
- No Kepler data (training or sealed) has been downloaded anywhere. The sealed planets and all moons have no query anywhere in the build; their queries will exist only in the gated-run workflow, which needs its own typed phrase.
- PySR has not run yet, anywhere. Julia cannot be installed in the build workspaces. Self-tests 1, 2 and 5 (planted law, planted wrong law, determinism) ran only with a clearly labelled stand-in solver and are not results. The other eight self-tests pass on synthetic data. The Julia, juliacall and SymbolicRegression.jl versions will be pinned and recorded at the first install, in the self-test workflow, as the spec requires.
- A defect found and fixed during the build: the check that a formula is an exact power law wrongly failed a clean formula with decimal exponents (rounding residue from the symbolic step). Both the build and the independent checker were fixed, and a regression test was added.

## What this manifest proves, and what it does not
- It proves that files with exactly these fingerprints existed no later than the commit time of this file, and that the rules above were fixed before any Kepler data download.
- It does NOT prove they existed earlier. The SkyNet commit times above are recorded by GitHub in a private repository and are claims until this manifest exists.
- It says nothing about whether the test will pass. The forecasts are inside the registered spec (overall PASS about 55%) and in the Opus rulings (shortage rule used about 55%, test stops even after it about 15%).

## How to verify
Ask VyroNyx for any file listed. Compute its SHA-256 (for example `shasum -a 256 kepler_core.py`) and look for the same string in the table. Then check that this file's commit in this repository is dated before the train download.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
