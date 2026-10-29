# Manifest 2026-10-29 (3): Dodona DOD-L1 outcome — FAIL

The commit time of THIS file is the authoritative publication time.

## Outcome
DOD-L1 (spec v1.1, registered in Manifest 2) was run once. **Result: FAIL.**

| Check | Result |
|---|---|
| R0 (rediscover the published law, answer hidden) | PASS: 3.5% error |
| H1 (room to improve, from public data) | PASS |
| P1 wind, unseen trees ≤ 17% | FAIL: 25.2% |
| P1b wind ≤ 0.85 × published law without calibration | FAIL: 25.2% vs 23.1% |
| P2 wind ≤ published law with per-tree calibration | PASS: 25.6% vs 25.9% |
| P3 wind, never-seen palm-like trees ≤ 23% | FAIL: 26.5% |
| P4 gustiness error ≤ 0.040 and ≤ 0.6 × baseline | PASS: 0.039 vs 0.078 |
| P5 units and size | PASS |

## Fingerprints (SHA-256), private repo VyroNyx/dodona
| File | SHA-256 |
|---|---|
| sealed/DOD-L1/formulas/formulas.json | a8a4c9b75d3a48e2d86b0364c268f807590ab8501e8616c9edbab144510ec538 |
| sealed/DOD-L1/results/score_report.json | 8a1f4d5c5be3139720b8a96993e44f4e5e8d41e241c6dd3354f2dc76cb3dc69f |

- Formula commit: cce7c6ac5b652af961f63888cea4f0ec89b5dcd4, made before any sealed row existed.
- Sealed seed: derived from that commit (15264492782210109705).
- Results commit: 3b250dbdededa88bcc00ae2038ffc2270e9db7be.

Under the spec's kill rule, one amendment cycle remains.
