# Manifest 2026-10-14 (KM-012 #6): E5, hearing a drone (sound), sealed Halmstad clips. MISS

Prepared by Opus during the night run, under NJ's standing delegation. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `da5c2b8e`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/E5_SPEC.md` (frozen spec, note N1 and the result) | `5e467ddf947f5dd515dfcd96ec7dd34acaab74ddd265d22144654c09b13dc4a1` | 5071 |
| `angel_eyes/air_e5/sealed_38601210198/result.json` | `2bd81692b9dce4a8b80cf1634fd7a585f664f309735e42ab8609210ea64d2751` | 702 |

## The test (ladder stage 1 for sound)
- **Data:** 45 sealed ten-second clips from the Halmstad multi-sensor set (CC0): 15 drone, 15 helicopter, 15 background, from recording sessions never heard in development.
- **Run:** `38601210198`, on NJ's Mac. The spec was frozen at commit `e01e093c` before any sealed clip was opened. The key hash was committed first; predictions and the drone threshold (fixed on development clips only) were committed before the key was opened.

| | Clip accuracy |
|---|---|
| Angel Eyes reader | 0.822 |
| Textbook rival (logistic regression on band energies) | 0.844 |
| Same learner, band energies only | 0.844 |
| Placebo (labels permuted between whole groups) | 0.067 |

- Drone call at the development threshold: 14 of 15 drones heard (0.933), but 5 of 30 non-drone clips called drone (0.167; bar 0.15).
- **Passed:** accuracy at least 0.70; placebo not void.
- **Failed:** beating the textbook rival (−0.022, lower bound −0.133); false drone calls (by one clip).
- **Verdict: MISS.** The test was valid. Sound is not claimed. This sealed set is spent.

## What it teaches
The reader hears drones, but it mistakes some helicopters and background for drones, and its extra measurements did not add anything over plain band energies on this test.

*Opus · 14 Oct 2026*
