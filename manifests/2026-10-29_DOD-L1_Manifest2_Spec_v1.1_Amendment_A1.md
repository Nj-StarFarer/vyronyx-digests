# Manifest 2026-10-29 (2): Dodona DOD-L1 Spec v1.1, Amendment A1 (pre-registration)

Prepared on 29 Oct 2026. The commit time of THIS file in this repository is the authoritative publication time. It supersedes Manifest 1 for the run that follows.

This manifest holds names and SHA-256 fingerprints only.

## Why there is a second manifest
- **The crash:** the first search under Spec v1 crashed before any formula existed. PySR refuses a variable named `fps`.
- **The loophole:** a short test search on public validation data then showed that the constant frame rate let the search slip a hidden constant with units past the units check.
- **The fix (Amendment A1):** the frame rate is removed from the search's inputs.
- **What did not happen:** no formula was ever committed and no sealed row was ever created.
- **The pass marks:** unchanged, after re-measuring them.

## Fingerprints (SHA-256)
| File (in the private repo VyroNyx/dodona) | Bytes | SHA-256 |
|---|---|---|
| sealed/DOD-L1/DOD-L1_Spec_v1.md | 14719 | 3209ef444e0f5cb7fca1a7083536ce29760d24de988316af1013a29a79fc7b90 |
| sealed/DOD-L1/thresholds.json | 729 | 9020d800baf947991b9ad7e974b8eeed9ada62e30f45ebe96ae78273e334722d |
| sealed/DOD-L1/MANIFEST.sha256 | 1685 | 3fe832a29b89b9e80e4f6b0358bbfc69d0e8584c9c28be6c56235fb2680d9f00 |

Private-repo commit that holds all of these files: 82ce5c6005bde839f5f93189778e5c198dc0363a (commit date Thu, 29 Oct 2026 15:08:54 +0530).

## State at publication
- **CAL:** no formula exists. CAL has not searched under v1.1.
- **Sealed rows:** none exists. They are created only after CAL's formulas are committed, from a seed derived from that commit's ID.
