# Manifest 2026-10-13 (KM-061 #8): Whitman Rung 1b, sealed ship test result: FAIL (gate G1 only)

- **Prepared:** 13 Oct 2026 by Opus. Published as measured, as the spec requires.
- **Run:** GitHub Actions run `38397730991` (one attempt) in the private repository `Nj-StarFarer/whitman-km061`.
  - It ran on the frozen build `474e37e6b01d757808b8e56725d9d3d04b7416b755a697d5d6ddefa9249802cb` (Manifest #7).
  - Commits, in order:
    1. `25d5c14`: seed hash and input hashes, before Whitman ran;
    2. `bc03e06`: raw outputs, before the key was read;
    3. `a45ddb2`: result, key and seed.
- **The independent reader and the second scorer agree.**

## Result

**FAIL.** One gate missed: **G1**, because the main engine raised 2 false alarms (the mark was at most 1). All other gates passed.

| Gate | Mark | Measured | Pass |
|---|---|---|---|
| G1 False alarms per machine (clean) | at most 1 each | ME **2**, GP 0, GS 0 | **no** |
| G2 Fewer than the alarm panel | Whitman < panel | **2 vs 38** | yes |
| G3 No hiding | UNKNOWN ≤ 10%, SENSOR_FAULT ≤ 2% | within marks on all 9 inputs | yes |
| G4 Gauge faults told apart | at least 30% | **38 of 59 = 64%** (95% interval 52–75%) | yes |
| G5 Machine alarm on a lying gauge | at most 10% | **0 of 59** | yes |
| G6 Planted machine faults caught | at least 30% | **9 of 18 = 50%** (29–71%) | yes |

**Details:**
- **Sealed data:** 6 Nov – 19 Dec 2025. Running days: ME 21.8, GP 13.4, GS 9.6. No machine was dropped.
- **The two main-engine alarms:**
  - they started 2025-12-15 10:39 and 2025-12-16 13:52;
  - both blamed the same three gauges together: oil temperature, jacket water and oil pressure;
  - by the rules, every alert on the clean data is a false alarm. Whether the ship had a real event then is not known.
- **Baselines:**
  - the alarm panel (B1): 38 false alarms, 0 gauge faults told apart, 6 alarms on lying gauges, 14/18 machine faults caught;
  - the Isolation Forest (B2): 0 false alarms, 0 told apart, 0/18 caught.
- **Per machine:**
  - gauge faults told apart: ME 13/20, GP 11/20, GS 14/19;
  - machine faults caught: ME 6/6, GP 3/6, GS 0/6.

## Hashes

| File | SHA-256 |
|---|---|
| `result/RESULT.txt` | `5ad9ce6ad4b45427b7a4b6ed5b919e7a02775a0413d5a7ef56df91f9c5fd3930` |
| `result/score_report.json` | `7ffeb1efb727b3dce386f19a7f9b6bdac9e8654935daaf400c3b89ad00324986` |
| `result/CHECK_REPORT.json` | `ade4729811ff57d764232b0a9f89ecce6ddb1ff369843d16286c5e995a9e2cc7` |
| `result/PLANTING_KEY.json` | `889f916bf0e42b7b5858f83e49e170fe5cb6b77d3391c33f667eca06d5a2e9ae` |
| `outputs/OUTPUT_SHA256SUMS.txt` | `eb83f3545c1afe943b75051672635ec9300541a89a772cc96e07d2a847e23085` |
| seed SHA-256 (committed before Whitman ran) | `465355b3af598700ca0b0839ebf4d8ad6d050e91bb3eee0ef8ba89595897dcc2` |

## What follows

The sealed ARC Gloria part is now spent and becomes development data (spec §8). Any retest needs fresh material, named first.

*Opus · VyroNyx Private Limited · 13 Oct 2026*
