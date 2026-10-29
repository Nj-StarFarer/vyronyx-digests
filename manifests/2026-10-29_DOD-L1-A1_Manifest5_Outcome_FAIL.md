# Manifest 2026-10-29 (5): Dodona DOD-L1-A1 outcome — FAIL

The commit time of THIS file is the authoritative publication time.

The DOD-L1-A1 amendment (Manifest 4) was run once. **Result: FAIL.** Under the kill rule, the calibration-free wind-speed line of Dodona stops.

| Check | Result |
|---|---|
| R0 rediscovery | PASS: 2.2% |
| H1 room to improve | PASS |
| P1 wind ≤ 17% | FAIL: 22.1% |
| P1b ≤ 0.85 × published law, no calibration | FAIL: 22.1% vs 20.5% |
| P2 ≤ published law, calibrated | PASS: 22.2% vs 25.9% |
| P3 palm-like ≤ 23% | FAIL: 30.1% |
| P4 gustiness | PASS: 0.039 vs 0.086 baseline. This is the second independent sealed pass. |
| P5 units and size | PASS |

## Fingerprints (SHA-256), private repo VyroNyx/dodona
| File | SHA-256 |
|---|---|
| sealed/DOD-L1-A1/formulas/formulas.json | dddb7cdec0f253307fc8dcf61189118d4ff965baf6eac5d7b15a712ba09e2eff |
| sealed/DOD-L1-A1/results/score_report.json | 75741a2d729b58c7935c62aebafa419f584d2390d91cd2117caff5f39ef6e41c |

- Formula commit: 46dfab65df4bfcd2a4a94b16f5f3b920fc4b12b7. The sealed seed was derived from it.
- Results commit: a88e5d77af67f73b779356d5d5bd6792fff78c7b.
