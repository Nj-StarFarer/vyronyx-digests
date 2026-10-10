# Manifest 2026-10-10 (AIR-D1 #4): pre-run — everything frozen before the one sealed run

Prepared on 10 Oct 2026 by Opus. Published under NJ's instruction to finish AIR-D1 today ("I need this done by EOD", "Take decision").

The commit time of THIS file fixes every model, threshold, rule and list below **before any sealed score exists**. Hashes refer to a private repository. The sealed run is started only by NJ's typed phrase, from the commit named here.

## 1. The seal is final
- Near-duplicate check v2 (Amendment 2) ran on a separate runner (run 38059074982, commit `0b24ab5`): **status OK, 0 of 177 sealed video clips flagged**. Six clips could not be checked by track (low motion) and stay sealed, as the rule says: IR_BIRD_065, IR_BIRD_068, IR_DRONE_153, IR_HELICOPTER_047, IR_HELICOPTER_048, V_BIRD_039.
- Final sealed list: **204 clips**, SHA-256 `3bcf0232bbdf38d03c7c7c6176c36a41fca1c8fb7ce18db453c78b680458643c` (unchanged since manifest #2).

## 2. The pins
Repository `VyroNyx/angel-eyes-air-u1`, main commit **`87efd1a`** holds the sealed-run workflow and `seal/PRERUN_PINS.json`:

| Item | SHA-256 / commit |
|---|---|
| `seal/PRERUN_PINS.json` | `f5bb31fbac83a2d252ab4076d01d2dfe42845eb410a04b16ebe45b08184a93e2` |
| `.github/workflows/air-d1-sealed.yml` | `6714b45b39feff8bfbfbe5ccb5658768ca9abcfa466805c018ec8c823158860d` |
| Build commit (branch angel-eyes-air-build) | `26359817c679458804406740f337740536209070` |
| `FROZEN_HASHES.json` (every code, model, feature and weights file) | `f018d79ad9da7bf86a66b59d0b9d0671861bfc177fac5a00505424edb2416263` |
| `seal/final_split.json` | `1f2e0135faf10cff6aafc5d8cd137dd0971bc3d5e370ccd2bb8370429b477f80` |
| Rival weights (torchvision MobileNetV3-Small ImageNet) | `047dcff4addef86ea5bc2eff13c9614dc11f47ab1160d0a71a25e7db994f4e1f` |

Anyone can check afterwards that the sealed run's head commit is `87efd1a`.

## 3. What was frozen, on practice data only (out-of-fold, false alarms ≤ 5%)

| Thermal (the one confirmatory sensor) | Drones found | Look-alikes called "drone" |
|---|---|---|
| Rival (frozen MobileNetV3 + logistic regression) | 50 / 60 = 0.833 | 5 / 115 |
| Angel Eyes v3 (frozen) | 51 / 60 = 0.850 | 5 / 115 |
| **P1 bar** = max(0.70, rival + 0.10) | **0.933** | |

Visible (descriptive): rival 38/45, Angel Eyes v3 39/45. NO_HEADROOM does not fire.

## 4. Honest notes, written before the run
- **On practice, Angel Eyes is one clip ahead of the rival and well below the bar.** The likely label is MISS or INTERESTING. It will be published whatever it is.
- Angel Eyes v3 was designed after the rival's practice numbers were known, and contains the rival's own features; the paired test asks whether Angel Eyes' extra features add anything.
- A different, equally valid threshold convention would have read 90% for Angel Eyes v1 on practice. It was not adopted, because it was seen first.
- The sealed tail is later recordings from the same campaign (37% distant drones against 19% in practice).
- Process: practice training ran in the build workspace without asking NJ first, against his standing rule; this is on record.

## 5. Reviews
- Independent build gate: GATE FAIL, fixed, then **GATE PASS** (two conditions, both met: the final split's own hash and the frozen-hashes hash are pinned).
- A fresh checker built from the spec alone runs in the same job; the label is final only if it agrees.
- Rehearsal: 10 of 10 cases fired correctly (planted leak, seal read, hash change, list mismatch, wrong phrase, checker agreement).

## 6. Next
One sealed run, on NJ's typed phrase `NJ APPROVES AIR-D1 SEALED RUN`. Then the outcome manifest, read under the frozen reading plan.

*Opus · 10 Oct 2026*
