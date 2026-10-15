# Manifest 2026-10-15 (KM-012 #9): E8, radio from drones never seen in training (nano, fixed-wing, mini). MISS

Prepared by Opus, under NJ's standing delegation. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `eed39535`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/E8_SPEC.md` (frozen spec and the result) | `4c179fe7a2ca6b307f4d0992cc6c5ee61d4cb051eec1400cfdfaaac796888a51` | 6602 |
| `angel_eyes/air_e8/sealed_38671832034/result.json` | `4b2c7e98f9bca0e43226f0efb0d4194c43c63810a13356457b5dbeb8a8134fd4` | 3618 |
| `angel_eyes/air_e8/sealed_38671832034/predictions.json` | `7661b886a13c5c46d7d3099b59ddd2fa08c5a4494680291c2a6d0eff5ce2744d` | 71502 |
| `angel_eyes/air_e8/sealed_38671832034/key.json` | `c9f35aa9c993fd4d8d1fd22364a2d60befe0274ebf4c6c17de0d53c82178734f` | 64730 |

## The test
- **Data:** Tampere University drone radio recordings (Zenodo 4264467, CC BY 4.0), 2.44 GHz, anechoic chamber.
  Known: 7 models (8 files). Never seen in training: Parrot Mambo (nano; control and video links), Parrot Disco
  (fixed-wing), DJI Mavic Mini.
- **Run:** `38671832034` on NJ's Mac. Spec frozen at `cec00032` before any recording was opened; key hash, then
  predictions and both gate thresholds committed before the key was opened.
- **Angel Eyes:** gradient boosting with a distance gate ("unknown" when a window is far from everything known);
  **rival:** the same learner with the textbook maximum-probability gate; both gates reject 5% of seen windows.

| Unseen file | Angel Eyes says "unknown" | Rival says "unknown" |
|---|---|---|
| Parrot Disco (fixed-wing) | 0.69 | 0.02 |
| Parrot Mambo control (nano) | 0.58 | 0.26 |
| Parrot Mambo video (nano) | 0.57 | 0.66 |
| DJI Mavic Mini (reported) | 0.01 | 0.44 |

- Known drones named right: **99.3%**. Beats the rival on the unseen Parrots: **+0.30** (lower bound +0.17).
- **MISS:** each Parrot file needed "unknown" on at least 80% of its windows; they reached 57–69%.
- **Every wrong name in the test is one model, "Typhoon H"** — including the Mavic Mini on 99 of 100 windows (a
  wrong maker, not only a wrong model). One broad known class absorbs unfamiliar links.

*Opus · 15 Oct 2026*
