# Manifest 2026-11-03 (24): AQ-S6 "Far eyes for big lulls", spec v1 freeze

The commit time of THIS file is the authoritative publication time.

- **The question:** a Floaty-like soaring body has a slow backup thruster (1 s spin-up, up to 40% of its weight). A far upwind sensor, read with SkyNet's DOD-G1-A1 travel law, warns it of big lulls. Does the warning keep the body up better than reacting to the air it feels, for the same thruster energy?
- **PASS if all three hold:**
  - **P1:** with the warning, time dropped ≤ 0.8× that of energy-matched reacting.
  - **P2:** with the warning, energy ≤ 1.05× that of energy-matched reacting.
  - **P3:** with the warning, time dropped ≤ 0.7× that of default reacting.
- **Disclosed before the freeze:** on the tuning air, the ratios were 0.92 (P1) and 0.78 (P3). Both would fail there. The marks are unchanged.
- **Sealed seeds:** made from the commit below.

| File | SHA-256 |
|---|---|
| sealed/AQ-S6/AQ-S6_Spec_v1.md | a3eb45f97235c6b644e053606d917c6d0c09e73e1bdfd6d523113629e4d3fcb5 |
| sealed/AQ-S6/tuning.json | 4e60574c3f870ae6d50d07d819a803f97a370cb7856d30be73afa635ab9954a5 |
| sealed/AQ-S6/MANIFEST.sha256 | d532b865336ebca725e80893b033ceb084ee9fee826d997fc39f9dc645425a77 |

**Commit:** c422c5a40a925f8fd32db4995d5c11fd4daf843a (Tue, 3 Nov 2026 14:13:11 +0530), in VyroNyx/dodona.

- **State:** no sealed episode exists.
