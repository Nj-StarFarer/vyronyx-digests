# Manifest 2026-10-03: Angel Eyes ZERO, task ZERO-001, frozen specification v1.2 (manifest #1b)

Prepared on 3 Oct 2026 (clock tool read 06:46 IST at the freeze). The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names and SHA-256 fingerprints only. No Space-Track data, no operator-log (IDS) data and no answer-key content is stored here. The specification text sits in the private repository.

## Why a new version exists
Manifest #1 (file `2026-10-02_ZERO-001_Manifest1_Spec_v1.1.md`) registered specification v1.1. After the build, ZERO failed the build gate written into v1.1 (section 8.9): 1,549 false BURN flags on development and calibration data from quiet satellites, against a limit of 18. The stop was named in advance (S_GUARD_BUILD). Nothing was run on 2024-25 orbit data and no operator log from 2024 or later has been read by anyone. v1.2 changes only the items X1 to X8 in its Appendix C. The data, windows, seeds, baseline B1 and its threshold, the pass rules and the gate limit are unchanged. v1.1 stays registered as history.

v1.2 allows exactly one attempt at the build gate. If ZERO fails it again, task ZERO-001 closes with the result "ZERO not ready; B1 stands".

NJ froze the specification on Sat 3 Oct 2026 at 06:46 IST.

## Fingerprint of the committed file (SHA-256)
Private repository Nj-StarFarer/SkyNet, commit 32b12166e0197c4e332a9358c0bee620560c06d2 (GitHub commit time 3 Oct 2026, 06:48:26 IST). The file was read back from GitHub after the commit and its fingerprint matches the copy on NJ's computer.

| File (in the private repo) | Bytes | SHA-256 |
|---|---|---|
| angel_eyes/zero/zero001_v1.2_freeze/ZERO-001_Specification_v1.2_FROZEN.md | 53324 | 8074d1ff8f0e33532c7f975cc261f2e0f9ed7a5fbfda0c04d24636a91f2746b0 |

The freeze changed only the banner and the status line. Without them the text hashes to 2e97ee5d484cc96424cffa518f91ade71e462a0edf240510c2357f756d7af60e (52883 bytes), which is the text the independent reviewer checked.

The v1.1 specification remains `a5a759873bd64dce2da0fa8b1e12d7f76e6188e243896c042b90227c7290225f` (manifest #1, private commit 8bd9b5ba75b036368708b65564851c9f32fc2b0b, public digest commit 15daab6).

## Data and tools
No data file and no script from manifest #1 changed. Their fingerprints stay as listed in manifest #1 and in Appendix A of the specification.

## Still to come
The code hashes for the two v1.2 changes, the training-data hash and the gate result will be published in later commits (spec section 8.9, item X3), before the gate is run. Manifest #2 (final code, pinned packages, model numbers, checker) follows only if the gate passes. An OpenTimestamps proof for this file has not been added yet.
