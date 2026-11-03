# Manifest 2026-11-03 (22): DOD-T1, CAL's formula frozen before sealed scoring

The commit time of THIS file is the authoritative publication time.

- **CAL's choice** (PySR 2.6.0, frozen Kepler settings, units checked, run twice with the same choice): **lag = 0.19316648 / f_pk**. In words, a tree's answer time is about a fifth of its sway period.
- **Training rows** (300 trees, families A–C), median error:

  | Method | Error |
  |---|---|
  | CAL | 4.6% |
  | constant | 41% |
  | textbook quarter-sway | 29% |

- **Sealed trees** will be made from formula commit 34a45ef673ca8d641b37d953454839183e35b494 (Tue, 3 Nov 2026 13:50:04 +0530).

| File | SHA-256 |
|---|---|
| sealed/DOD-T1/formulas/formulas.json | f7cd5910be2e26ce38772ea393eddca00b46e09575352adc9d6103b652daaeb1 |
| sealed/DOD-T1/formulas/equations_lag_run1.csv | ee0793324a72b3745ba0563e993a50c5b68dc8f49beb79529bac436494df0b3f |
| sealed/DOD-T1/formulas/equations_lag_run2.csv | ee0793324a72b3745ba0563e993a50c5b68dc8f49beb79529bac436494df0b3f |

- **State:** no sealed tree exists.
