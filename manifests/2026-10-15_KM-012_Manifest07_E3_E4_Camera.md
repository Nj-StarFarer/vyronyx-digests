# Manifest 2026-10-15 (KM-012 #7): E3 / E4, drones on visible and heat camera, sealed Halmstad clips. Visible MISS; heat PASS by the bars, with a scene-shortcut warning

Prepared by Opus, under NJ's standing delegation. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `51e53bdd`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/E3_SPEC.md` (frozen spec and the result) | `8d9f0073adf0ccb415bd39fc012d210b483cd7cda16c4436116588f50f7bca35` | 6735 |
| `angel_eyes/air_e3/sealed_38664915181/result.json` | `9865137e620bdd14791df1b7a1d5e2ccad27c127eba8f6022e943e4b7f25e8e8` | 2050 |

## The test (ladder stage 1 for each camera)
- **Data:** the sealed groups of the Halmstad multi-sensor set (CC0), recording sessions never seen in development: 160 visible clips (65 drones) and 212 heat-camera clips (92 drones), with birds, aeroplanes and helicopters.
- **Run:** `38664915181`, on NJ's Mac. Spec frozen at `e0d5cfd9` before any sealed clip was opened; key hash first, predictions and drone thresholds (development only) committed before the key was opened.

| | Visible: drones caught at 5% false calls | Heat: drones caught at 5% false calls |
|---|---|---|
| Angel Eyes reader | 0.585 | 1.000 |
| Rival (thumbnail logistic regression) | 0.631 | 0.511 |
| Scene-only check (frame brightness only) | 0.569 | **1.000** |
| Placebo | 0.015 | 0.011 |

- **Visible: MISS.** 58.5% of drones caught at the development threshold (bar 80%); did not beat the rival.
- **Heat: PASS by the frozen bars** (100% of drones, 5.8% false drone calls, beats the rival with lower bound +0.045, 4-class 0.759).
- **Warning, published with the result:** the scene-only check also caught every heat-camera drone. In this data set the heat drone clips can be separated by how the scenes were recorded, not necessarily by the drone. **No claim is made that Angel Eyes recognises drones on a heat camera** until a test where scene brightness cannot separate the classes.

*Opus · 15 Oct 2026*
