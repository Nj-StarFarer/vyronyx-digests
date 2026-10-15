# Manifest 2026-10-15 (KM-061 Whitman #15): W3+ result — FAIL (detection gates G2, G4; all cause gates)

Prepared by Opus, 15 Oct 2026. The one attempt of the CARE wind-turbine sealed exam (build `0eb3ac87…`, Manifest #12) ran as run 38714002584 on 50 sealed datasets (25 with a recorded fault, 25 normal). Results in the private repository `Nj-StarFarer/SkyNet` (commit `4ef0b23`): `score_report.json` SHA-256 `b510dd5729db1de8ce275afe508ff44f4558dd50648b6a01bd7de7f94e9472ae`, `cause_report.json` SHA-256 `2976c9edeac21682a8d553548ad9187d5278c6292da59b8194fe46424b39fbba`.

## Detection (primary scorer; the second scorer agrees on every gate)
| Detector | CARE score | Faults caught (of 25) | Normal datasets alarmed (of 25) |
|---|---|---|---|
| **Whitman** | **0.591** | 14 | 11 |
| Authors' model (efd) | 0.561 | 12 | 14 |
| Isolation forest | 0.597 | 13 | 11 |
| Alarm panel | 0.523 | 15 | 17 |

- G1 beats the authors' model: **pass**. G3 beats the alarm panel: **pass**. G5 not silent: **pass**.
- G2 beats the isolation forest: **FAIL** (0.591 against 0.597; in bootstrap draws Whitman beats it 25% of the time).
- G4 few false alarms (at most 5 of 25 normal datasets): **FAIL** (11).

## Naming the faulty part (W3+)
- 15 scored fault events. Whitman named a part once, and it was wrong (C1 fail). Of 8 warned faults it named none right (C2 fail). C3 and C5 fail. The simple rival (most-moved gauge) was right twice.
- Our forecast (Manifest #12): about 1% for all cause gates to pass. They did not.

**No claim is made.** The sealed set is spent.

*Opus · 15 Oct 2026*
