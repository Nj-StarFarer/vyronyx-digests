# Manifest 2026-10-29: Dodona DOD-L1 Spec v1 (pre-registration, freeze)

Prepared on 29 Oct 2026. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names and SHA-256 fingerprints only. No data, code or results are stored here.

## What is being registered
DOD-L1, the first sealed test of VyroNyx's Dodona project. The test asks whether SkyNet's equation-finding system CAL (PySR) can find a rule that reads the mean wind speed and the gustiness from a tree's motion alone, with no calibration against a wind meter. It runs in a simulated world. The rule must beat the published method (Cardona & Dabiri 2022) on trees it has never seen, including a tree family never shown in training. The spec fixes the simulated world, the inputs, the search settings, the pass marks (set beforehand from public data by a headroom probe), the baselines, the named stops and the kill rule.

## Fingerprints (SHA-256)
| File (in the private repo VyroNyx/dodona) | Bytes | SHA-256 |
|---|---|---|
| sealed/DOD-L1/DOD-L1_Spec_v1.md | 13713 | fbf4bb1bc42f8d16c766786c162767adbcb3e8331069afcf32a3b5737c05fe25 |
| sealed/DOD-L1/thresholds.json | 631 | 5789046aaf5eb42b82cdef901fcd0ea657140a05bd506c58dcca12e7e43fad9f |
| sealed/DOD-L1/MANIFEST.sha256 | 1685 | 661be818a90c3e3f4a361a260626cafab930f75802eac8f47bf7c6a971b40a85 |

The file `MANIFEST.sha256` above itself lists the SHA-256 of every build file (the dodona/ package, the pinned requirements and the run workflows) as frozen.

Private-repo commit that holds all of these files: e56082c622dfbf6f44cca21341bc9f8f4d57da57 (commit date Thu, 29 Oct 2026 14:46:36 +0530).

## State at publication
- CAL has not searched yet. No formula exists.
- No sealed row exists anywhere. By the spec, the sealed trees are created only after CAL's formulas are committed, from a seed derived from that commit's ID.
- Public data that exists: the headroom probe's VALIDATION forests, which the spec's pass marks were set from.

## What this manifest proves, and what it does not
- It proves that files with exactly these fingerprints existed no later than the commit time of this file.
- It does not prove anything about whether the test will pass.

## How to verify
Ask VyroNyx for the files and compute their SHA-256 (for example `shasum -a 256 DOD-L1_Spec_v1.md`). Compare them with the table, and check that this file's commit is dated before the DOD-L1 results commit in VyroNyx/dodona.
