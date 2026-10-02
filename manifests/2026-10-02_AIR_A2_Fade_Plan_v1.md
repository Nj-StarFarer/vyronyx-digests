# Manifest 2026-10-02: Angel Eyes AIR A2 Fade Test, plan v1 (practice test)

Prepared on 2 Oct 2026 (clock tool read 11:54 IST). The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names and SHA-256 fingerprints only. No data, code or results are stored here.

## What is being registered
The plan for the A2 Fade Test, part of VyroNyx's KingMaker Protocol (Angel Eyes AIR). It is a **practice test, not a sealed test**: it re-uses public radar recordings whose sealed set was already opened on 1 Oct 2026. The plan fixes, before any fade code exists: the fade steps, what is measured, what counts as "lost", the reproduction gate, the placebo reading, the forecasts, the named stops and the reading plan. Nothing here earns a stage on the capability ladder.

## Fingerprint (SHA-256)
| File (in the private repo Nj-StarFarer/SkyNet) | Bytes | SHA-256 |
|---|---|---|
| angel_eyes/air_v2/fade/A2_Fade_Test_Plan_v1.md | 16269 | 057d017a429efc7d7292687ba1c7aa716db143c1165ba81122fabb059244fcf6 |

Private-repo commit that holds the file: 2105fbac03b039f1912b8682e17af143fa49b06c (GitHub commit time Fri, 2 Oct 2026, 11:54:28 +0530). The file's fingerprint was recomputed from the committed copy at 11:54 IST and matches.

## State at publication (updated 2 Oct 2026, about 12:45 IST, before publishing)
- The plan was committed to the private repository at 11:54:28 IST, before any fade code was written.
- Since then the fade tool, its self-tests and an independent checker were written and tested on synthetic data only. They are not yet committed and have not been run on any real data. They will be fingerprinted in a later manifest.
- No fade result exists. No new data has been downloaded. The test will re-use the public KTH 77 GHz radar recordings (Zenodo 5845259, CC BY 4.0) used by the 1 Oct 2026 Arm A test.

## What this manifest proves, and what it does not
- It proves that a file with exactly this fingerprint existed no later than the commit time of this file, and therefore before any fade result exists.
- It does NOT by itself prove the earlier private commit time (11:54:28 IST). VyroNyx can show that commit on request.
- It says nothing about what the fade test will find. The plan's forecasts are inside the registered file.

## How to verify
Ask VyroNyx for the plan file. Compute its SHA-256 (for example `shasum -a 256 A2_Fade_Test_Plan_v1.md`) and look for the same string in the table above. Then check that this file's commit in this repository is dated before the test was run.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
