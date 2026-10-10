# Manifest 2026-10-10 (AIR-D1 #7): descriptive addendum to the MISS

Prepared on 10 Oct 2026 by Opus. **The headline stays MISS (manifest #6).** Everything here is descriptive and must never be quoted without the headline and a link to #6.

Source: the results artifact of run 38062956986, downloaded with NJ's permission. Its SHA-256 `7f0515b8107ecdece6f334042ee718d60cde7692928388f75e5101b9cab5ec77` matches the digest published in #6. The independent checker reported AGREE, with every Monte-Carlo difference at 0.

## The table (sealed recordings; Angel Eyes vs the frozen rival)
| Part | Thermal (IR) | Visible (V) | Sound |
|---|---|---|---|
| Micro drones found (P1) | 34/38 vs 34/38 | 9/29 vs 2/29 | 3/9 vs 0/9 |
| Look-alikes called "drone" (P2) | 2/63 vs 0/63 | 2/36 vs 0/36 | 0/18 vs 0/18 |
| Nano drones found | 7/7 vs 7/7 | 0/4 vs 0/4 | — |
| Phantom 4 Pro, never seen in training | 0/4 vs 0/4 | 0/3 vs 0/3 | — |
| Honest confidence (Brier, lower is better) | **0.056** vs 0.066 | **0.112** vs 0.138 | **0.109** vs 0.227 |
| "Unknown" score on held-out helicopters (AUROC) | **0.79** vs 0.69 | **0.76** vs 0.44 | **0.86** vs 0.75 |
| Helicopters called UNKNOWN / known kinds called UNKNOWN | 2/17 and 0/91 vs 7/17 and 7/91 | 1/7 and 2/62 vs 0/7 and 17/62 | 0/9 and 0/18 vs 1/9 and 2/18 |

Visible and sound are TOO_FEW by the frozen rule. P5 (weak signal): neither method meets the P1 bar even at full signal, so no step "lasts". PLACEBO_LEAK: 0 of 38.

## What it shows
1. **Finding drones:** Angel Eyes is no better than the rival on thermal, which is the only confirmatory sensor.
2. **Being honest about confidence, and recognising what it doesn't know:** Angel Eyes is ahead of the rival on all three sensors. Those are two of its five design principles. This is descriptive only, it was not tested for significance, and it was not the headline.
3. **Visible video collapsed on the later recordings.** Both methods scored 84–87% on practice but 31% and 7% on the sealed set. The later recordings differ from the earlier ones in ways practice did not show. This is the most important lesson for the next dataset.
4. **Neither method recognised the unseen drone model** (Phantom 4 Pro, 0 of 7 across the two sensors). The sample is tiny, but it is a warning, not a pass.

## Forecasts F8–F10, now scored
| # | Forecast | P | Outcome |
|---|---|---|---|
| F8 | Angel Eyes calls at least half the sealed Phantom 4 Pro clips "drone" | 50% | No (0/4) |
| F9 | Both methods meet the P1 bar at contrast ×0.5 | 40% | No |
| F10 | The P4 unknown-score AUROC on helicopters is at least 0.70 | 45% | Yes (0.79) |

Brier score over F1–F6 and F8–F10 (9 forecasts): **0.163**. F7 is still unresolved.

## Kept privately
The full results (scores, results.json, the checker's output and the evidence record) are committed to the private repository, at build-branch commit `7947931`.

*Opus · 10 Oct 2026*
