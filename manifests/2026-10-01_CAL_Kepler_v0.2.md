# Manifest 2026-10-01: CAL Kepler Test v0.2 (pre-registration)

Prepared on 1 Oct 2026 (clock tool read 23:26 IST). The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names and SHA-256 fingerprints only. No data, code or results are stored here.

## What is being registered
The CAL Kepler Test v0.2, part of VyroNyx's KingMaker Protocol. The test asks whether an equation-finding system (PySR) can find an orbit law from a table of real planets, with the answer hidden, and then carry the same formula unchanged to moons. The spec fixes the data, the split, the pass bars, the rival methods, the named stops and the forecasts before any data is downloaded.

## Fingerprints (SHA-256)
| File (in the private repo Nj-StarFarer/SkyNet) | Bytes | SHA-256 |
|---|---|---|
| cal_tests/kepler_v0.2/CAL_Kepler_Test_Spec_v0.2_FROZEN.md | 15873 | d02d5c94180b6f2daa66bac5be2a5d484d4116fb4386d7f6633acd76ea6d9b25 |
| cal_tests/kepler_v0.2/CAL_Kepler_Answer_Key_v0.2.md | 764 | d245536ea7b5e79b9ddcc9d1253810e99eb00de8d4b4aa57e7255c1fb838f6e0 |
| cal_tests/kepler_v0.2/SHA256SUMS.txt | 198 | 7c30f41fdc38876e8820d8d913f9a4799399e894ae46665e23a510da1090519d |

Private-repo commit that holds all three files: 4d917cd772601173bdb8a4692e1eb5c1b0fb1305 (git author date Thu, 1 Oct 2026 17:30:34 +0530). Spec freeze, as recorded in the spec itself: Thu 1 Oct 2026, 16:18 IST. All three fingerprints were recomputed from the files in that commit at 23:25 IST and match the commit message.

## State at publication
- No Kepler data (training or sealed) has been downloaded anywhere. The spec seals the test rows physically: they are not fetched until the gated run.
- The build code, the self-tests, the checker, the training-set fingerprint and the chosen formula do not exist yet. Each will be fingerprinted in a later manifest published before the step it governs (before the training download, and before the sealed rows are fetched).

## What this manifest proves, and what it does not
- It proves that files with exactly these fingerprints existed no later than the commit time of this file, and that the answer key was fixed before any data download.
- It does NOT prove that the files existed earlier than that. The 16:18 freeze and the 17:30 git date were recorded in private places and are claims until this manifest exists. Anything earlier than this commit is on trust.
- It says nothing about whether the test will pass. The spec's forecasts are inside the registered file.

## How to verify
Ask VyroNyx for the spec file. Compute its SHA-256 (for example `shasum -a 256 CAL_Kepler_Test_Spec_v0.2_FROZEN.md`) and look for the same string in the table above. Then check that this file's commit in this repository is dated before the test was run.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
