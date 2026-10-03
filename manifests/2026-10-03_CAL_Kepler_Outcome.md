# Outcome 2026-10-03: CAL Kepler Test v0.2, gated run — CORRECT (all six pass bars met)

This note records the result of the test registered in manifest #3 (`manifests/2026-10-03_CAL_Kepler_Manifest3_GatedRun.md`, published 3 Oct 2026 14:02:20 IST). The spec was registered 1 Oct and the build in manifest #2. No data, code or results are stored here; the result files are in the private repo Nj-StarFarer/SkyNet under `cal_tests/kepler_v0.2/gated/`.

## The run
GitHub Actions run 37110160033, started by NJ on 3 Oct 2026 at about 14:04 IST, first attempt, no named stop. Software versions equalled the pinned ones.

| Time (IST) | Event | Private-repo evidence |
|---|---|---|
| 14:11:51 | Formula chosen from the training planets only (two identical PySR searches) | `formula/formula_committed.json` |
| 14:12:19 | Formula public on the main branch | commit c470239 |
| 14:13:10 | Sealed-planet query sent (sha256 e1b28dff…a540, as registered) | `results/score_report.json` |
| 14:13:36 | Result committed | commit d5b93e8 |

## The formula (SHA-256 of formula.txt: 28a4e439d259447c757e47ac89fa37fd61cfc0380b0aa3ac9d094dc7583cd423)
`pl_orbsmax / sqrt((st_mass / pl_orbsmax) / 0.07782194)`, which is P = 0.27897 · a^1.5 · M^-0.5 (P in days, a in gigametres, M in units of 10^30 kg). The textbook constant is 0.28149; the found one is 0.9% lower.

## Scores
| Bar | Result |
|---|---|
| P1 accuracy, 1450 sealed planets (discovered 2019 or later) | median error 0.0039 dex (bar 0.03); 90th percentile 0.018 (bar 0.10); no prediction 0% (bar 5%) — PASS |
| P2 right inputs | uses only orbit size and star mass; none of 9 decoy columns — PASS |
| P3 right form | exponents 1.5000 and −0.5000; constant within 5% — PASS |
| P4 transfer to 31 moons of Jupiter (8) and Saturn (23), no refit | median 0.0035 dex, worst 0.0050 — PASS |
| P5 attack | no decoy correlates with the errors (largest abs. Spearman 0.17, bar 0.2); extreme star masses pass — PASS |
| P6 against the engineer's baseline | 0.0039 vs limit 0.0059 on the 597 rows where both predict — PASS |

Rivals on the sealed planets (median error): no-data 0.61 dex; distance-only 0.054 dex; engineer's baseline 0.0054 dex but no prediction for 58.8% of planets. The independently written checker agrees on all six bars, the label and the rival medians. No planet was in both the training and sealed sets.

## Forecasts registered before the run, against the outcome
Overall PASS about 55% → PASS. Moons page stops the first attempt 40% → did not stop. Version drift 10% → none.

## What this shows, and what it does not (as registered in spec section 3)
- It shows that CAL's search, given 11 shuffled columns and no hint which matter, found the right two inputs and the exact power law from the training planets alone, and that the law predicted planets and moons it had never seen.
- It does not show new physics: Kepler's third law is 400 years old. Humans chose the question (predict the period), supplied the measured columns, and chose the operators the search may use.
- Circularity, named before the test: many published planet orbit sizes were themselves calculated from the period with Kepler's law, which makes the planet accuracy easier. The moons are the cleaner check: their orbit sizes and periods come from JPL's mean elements and the planet masses from JPL's GM values, and the formula transferred with no refit. It is cleaner, not perfectly independent: GM values are themselves measured from orbital motion (spacecraft and moons).

## Pending
An independent timestamp proof (for example OpenTimestamps) over manifests #2, #3 and this note will be added in a later commit; this file will not be edited.
