# Manifest 2026-10-19 (AIR-D2-SIM #4): outcome — SEAL_BREACH, no claim; descriptive addendum

Prepared on 19–20 Oct 2026 by Claude Opus 5.5 for VyroNyx. Follows manifest #3 (commit `cb627ee8`), which declared the
seal breach before the run.

## 1. Official outcome: **SEAL_BREACH — no claim**
- The run finished on 19 Oct 2026 at 22:34 UTC (6 h 06 min). Result commit in the sealed repository:
  `c3d3fef9e28658f77e4542ae1be915ad4ed97b61` (`results/real/R/`).
- The frozen checker (`checker.py` SHA-256 `dd3197c4…1795`) was run with `--seal-breach 1`, as manifest #3 said it
  would be. It stopped with **SEAL_BREACH** and, by its frozen rule, computed no statistic.
- Every other stop was checked and **none fired**: VOID, BUDGET, CHECKER_MISMATCH, NON_FINITE, NOT_REPRODUCIBLE,
  SIM_TELL, TOO_FEW. The frozen-hash check passed; the seed commitment matched; the draw needed 0 replacements.
- Draw: drand quicknet round 33207912 (randomness `ff41bec4…518d`). Inputs: `LABELS.jsonl` SHA-256 `9f96d7ee…44c2`;
  scores Angel Eyes `0cd2f183…7517`, Rival A `33d973a2…c5cc`, Rival T `c065cc83…cebb`, Rival B `c5e91d82…f619`.
- Simulation tell probes (run before any score): (a) AUROC 0.519 (upper 0.546), (b) 0.504 (upper 0.533), (c) class
  gap 0.001. All under their limits: the models could not tell the simulated world from its own statistics.

## 2. Descriptive addendum — **seal breached, NOT a sealed result, supports no claim**
The same frozen checker, unchanged, run on a copy of the same `R/` with `--seal-breach 0`. Nothing was re-run or
re-scored. The checker's own label would have been **INTERESTING** (not PASS).

| Measure (3,280 clips) | Angel Eyes | Rival T (temporal) | Rival B | Rival A (image) | Bar |
|---|---|---|---|---|---|
| Drones found (recall, 776 drone clips) | **0.740** | 0.841 | 0.082 | 0.001 | AE ≥ 0.80 |
| False alarms on empty sky (476) | 0.036 | 0.132 | 0.004 | 0.000 | AE ≤ 0.05 |
| False alarms on look-alikes (652) | 0.132 | 0.225 | 0.008 | 0.000 | AE ≤ 0.10 |
| Never-seen objects vs known non-drones (AUROC) | **0.753** | 0.705 | 0.569 | 0.532 | beat A and T |

- **Test 1 (find more drones than both A and T): not met.** Angel Eyes found 573 more drones than Rival A (p < 0.001)
  but 79 fewer than Rival T (p = 1.0). Rival T found more drones, with 1.7 to 3.7 times Angel Eyes' false alarms.
- **Test 2 (separate never-seen objects better): met.** Ahead of A by 0.221 and of T by 0.048 AUROC (both p < 0.001,
  Holm-corrected).
- **Safety: not met.** Look-alike false alarms 13.2% against a 10% limit.
- **Weak spots:** far targets (recall 0.60 vs T 0.76) and one of the four drawn world shifts (group 1: recall 0.41,
  look-alike false alarms 31%).
- **Forecasts in manifest #3, scored:** "recall 0.80 or better" was given 10% — it did not happen (0.740); "beats both frozen rivals on drone recall" was given 20% — it did not happen (Rival T found more). Brier score for the two: (0.10² + 0.20²) / 2 = 0.025.

## 3. What this means
- No claim from AIR-D2. Even without the breach, Angel Eyes would not have passed: it misses its own recall bar and
  its look-alike safety limit, and a temporal baseline finds more drones.
- What the addendum suggests (description only): Angel Eyes trades detections for fewer false alarms, and is better
  than every rival at saying "this is something I have not seen". That is the direction for the next, separately
  frozen test, not a result.
- Simulation only. No real-sensor claim of any kind.

*Opus · VyroNyx Private Limited · 20 Oct 2026*
