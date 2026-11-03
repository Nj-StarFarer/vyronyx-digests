# Manifest 2026-11-03 (19): AQ-S4 "Feel the air vs see it coming", spec v1 freeze

The commit time of THIS file is the authoritative publication time.

- **The question:** for a Floaty-like soaring body, does seeing the air ahead (an upwind tree, read with SkyNet's committed DOD-G1-A1 travel law) add anything to feeling the air where the body is (an on-body air sensor)? Every controller flies the same air.
- **PASS if all hold:**
  - P1: the on-body sensor alone gives ≤ 0.80× the height error of feedback only.
  - P2: on-body sensor + tree gives ≤ 0.985× the height error of the on-body sensor alone.
  - P3: on-body sensor + tree is better in ≥ 75% of episodes.
  - P4: its flap rate is ≤ 1.1× feedback only.
- **Prediction on file (not judged):** no tree alone beats the on-body sensor.
- **Disclosed before the freeze:**
  - The tuning rule was amended once, so that each controller picks its own gains within the flap budget. The marks did not change.
  - Tuning-air results: on-body sensor 0.623× feedback only; on-body sensor + 2 m tree 0.933× the on-body sensor; tree alone 1.017× the on-body sensor.
- **Sealed seeds:** made from the commit below.

| File | SHA-256 |
|---|---|
| sealed/AQ-S4/AQ-S4_Spec_v1.md | 3df970d2c734e3cdb9e1f10ca24012b2e9fc9784323f2f8130ed7eae347fa4bc |
| sealed/AQ-S4/tuning.json | 0fa88dd8ed4cee3000824e57197b82b910cd89dd216f022f1883f6392e2bada7 |
| sealed/AQ-S4/MANIFEST.sha256 | b73e31ad4e7fb5346190b2d09c72be7a8f53310766bfd97ca1e14d777d5b4ea2 |

Commit: 45f30cead672d31288de79e035185662444dae89 (Tue, 3 Nov 2026 13:23:29 +0530), in VyroNyx/dodona.

- **State:** no sealed episode exists.
