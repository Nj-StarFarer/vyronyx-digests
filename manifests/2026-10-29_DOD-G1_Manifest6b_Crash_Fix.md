# Manifest 2026-10-29 (6b): DOD-G1, crash fix before the search

The commit time of THIS file is the authoritative publication time.

- **What happened:** the first frozen search run crashed while building the public R0 data, before any CAL search. It was a Python unpacking bug in `dodona/g1/run_g1.py`.
- **The fix:** code only. No rule, mark, seed, CAL setting or spec text changed.
- **State:** no formula and no sealed field exists.

| File | SHA-256 |
|---|---|
| dodona/g1/run_g1.py (fixed) | c2f4f482ab7542dc729e4b7a22140fae79f581111cf5cc4e4e88fe94ed48e267 |
| sealed/DOD-G1/MANIFEST.sha256 (all code files) | 74b7c0f6e2134f2a06127147f7cfe3d0ea74c028e918855924e21ffd601706ab |
| sealed/DOD-G1/DOD-G1_Spec_v1.md (unchanged) | 66548b63eca8c5f49daa6ac7251ef6470bcbc5e0b187b525e1fab3dcf0e58c6d |
| sealed/DOD-G1/thresholds.json (unchanged) | 2cb99f8f041248d3ddb85f0b2700cde788b50cca53e9ce10869340eb66d6d0fd |

Commit: 1e2b5ff750fd5cbd940487b5a61ad0197358f441 (commit date Thu, 29 Oct 2026 16:51:24 +0530).
