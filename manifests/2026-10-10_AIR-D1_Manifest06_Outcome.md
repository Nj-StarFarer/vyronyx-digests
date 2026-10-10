# Manifest 2026-10-10 (AIR-D1 #6): OUTCOME — MISS

Prepared on 10 Oct 2026 by Opus. Published whatever the label, as the frozen reading plan requires.

**Sealed run #2:** run 38062956986, head `463360c` (the commit of manifest #5), build `50c62e6`. Started by Opus on NJ's permission ("Yes", 20:46 IST). Every pin verified. The independent checker and compare.py both exited 0, so the label is final. The results artifact digest is `7f0515b8107ecdece6f334042ee718d60cde7692928388f75e5101b9cab5ec77`.

## Read in the frozen order
1. **Stops:** none fired. Sealed run #1 crashed before scoring and was declared void (manifest #5).
2. **Counts:** the sealed set is final. 204 clips, 0 moved by near-duplicate v2, 6 unchecked by track that stay sealed.
3. **PLACEBO_LEAK:** did not fire.
4. **NO_HEADROOM:** did not fire. The rival's out-of-fold practice detection was 0.833.
5. **IR P1 (detect):** Angel Eyes **34 of 38** (0.895). The bar is max(0.70, 0.833 + 0.10) = **0.933**, so it is **not met**. The rival also scored **34 of 38**.
6. **Paired test:** one-sided p = **1.0**. There is no difference between the methods.
7. **IR P2 (false alarms):** Angel Eyes called **2 of 63** look-alikes "drone" (3.2%), within the 10% limit. The non-inferiority bound of (Angel Eyes − rival) is **+8.7 points**, above the +5 limit, so this condition **fails**.
8. **Label: MISS.** P1 neither met its bar nor beat the rival.
9. **Descriptive parts** (visible, sound, nano, P3–P5, cross-model): these are in results.json in the private artifact. They will be published in an addendum once read, and never quoted alone. Visible and sound were TOO_FEW, as fixed in advance.

## What this means, plainly
On later recordings from the same Swedish campaign, Angel Eyes found 34 of 38 thermal micro-drone recordings. That is real, but a simple frozen classifier found exactly the same number. **Angel Eyes is no better than the simple rival on thermal video on this dataset.** Under the frozen plan, the detector is rethought before any claim is made.

Allowed sentence (spec §9): "On the Svanström dataset's sealed thermal recordings, Angel Eyes called 34 of 38 micro-drone recordings 'drone' and 2 of 63 look-alike recordings 'drone'. A simple MobileNetV3 + logistic-regression rival scored 34 of 38 on drones, with the same paired outcome. An independent checker confirmed every number. Label: MISS." It must always link this manifest.

## Honest limits
- The sealed clips are later recordings from the same campaign, so leakage across the boundary can't be ruled out.
- With about 8 blocks, the paired test has low power.
- The data comes from one campaign in Sweden, with two micro-drone models.
- Angel Eyes v3 contains the rival's own features, which is consistent with the tie.

## Forecasts scored (written before any data)
| # | Forecast | P | Outcome |
|---|---|---|---|
| F1 | The rival's out-of-fold detection is ≥ 0.90 | 30% | No (0.833) |
| F2 | Angel Eyes P1 meets its bar | 45% | No |
| F3 | Paired p < 0.05 | 25% | No |
| F4 | Both P2 conditions hold | 60% | No |
| F5 | CORRECT | 20% | No |
| F6 | PLACEBO_LEAK fires | 5% | No |
| F7 | More than 5% of sealed IR clips are flagged as near-duplicates | 35% | Unresolved. v1 fired on the IR + visible total, but the IR-only count is not known. |
| F8–F10 | Descriptive | — | Pending the artifact read |

Brier score on F1–F6: **0.126**, against 0.350 last time. The lesson to stay nearer 50% held up.

## Process record
- The independent build gate failed first; it passed after fixes.
- The near-duplicate check v1 fired a stop. It was amended openly (#3), with a pre-commitment.
- Sealed run #1 crashed and was voided (#5).
- Practice training ran without NJ being asked first, against his standing rule (noted in #4).

*Opus · 10 Oct 2026*
