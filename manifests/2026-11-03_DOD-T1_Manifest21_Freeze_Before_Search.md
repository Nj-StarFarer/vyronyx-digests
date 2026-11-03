# Manifest 2026-11-03 (21): DOD-T1 "How quickly does a tree answer the wind?", frozen before CAL's search

The commit time of THIS file is the authoritative publication time.

- **The question:** can SkyNet's CAL find a tree's answer time to a gust (how far its sway trails the wind) from what a camera sees? The inputs are the sway rhythm, the tree's height, the mean wind and a decoy.
- **Why it matters:** a tree can warn a soaring body downwind only if a gust takes longer to travel to the body than the tree takes to answer it. AQ-S5's probes found that a tree 2 m upwind answers too late.
- **PASS:** median error of CAL's law
  - on 200 sealed trees of families A–C:
    - at most 0.5× the error of a constant;
    - at most 15%;
  - on 100 sealed palm-like trees never trained on: at most 20%.
- **Disclosed:** a 40-tree exploration had already shown lag ≈ 0.19 / sway rhythm, palms included, before the marks were written.

| File | SHA-256 |
|---|---|
| sealed/DOD-T1/DOD-T1_Spec_v1.md | 13ed557b60fbcc62cc344c23fd25ef101e2d4d44c00076d0fc0f040415ceccc9 |
| sealed/DOD-T1/train_rows.csv | d1c4d41415993b65e01b99b65bd75105b8b74a642aff838d4f00596ad2c12129 |
| sealed/DOD-T1/MANIFEST.sha256 | d56bdc4d2c65a1b9142a081dc5a40be70d205f2e7ef4a1ca568a752e73bd1694 |

Commit: 5285c7b65cb571ce43dce89f38fc6c253fbde381 (Tue, 3 Nov 2026 13:42:36 +0530), in VyroNyx/dodona.

- **State:** CAL has not searched. No sealed tree exists.
