# Manifest 2026-10-13 (KM-012 #3): O5, CAL explains causes on sealed AOT objects. PASS (stage-3 test)

Prepared on 13 Oct 2026 by Opus. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `35b2f33f` or earlier.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/O5_SPEC.md` (frozen spec, note N1, result) | `c6ad9c033b7720bc87e345be19a23db24ccb542901ebbb12d6b12a8e932c8706` | 7,447 |
| `docs/kingmaker/O5_DATA_CHOICE.md` (data choice, dev pools, development log) | `9cb6c2c8ad68163844f5ead1b46fd3942eff7bddf74d78d2ef765cefd721b5ec` | 4,321 |

## The test
Given a flying object's path in a camera view, Angel Eyes must name its cause (aeroplane, helicopter, bird or flock) only when one rival clearly wins, and otherwise keep the rivals open.
- **How it decides:** CAL registers each rival with its predictions before the frames are read. The Leviathan judge weighs the evidence frame by frame.
- **Data:** Amazon AOT (CDLA-Permissive-1.0). 120 sealed objects from 73 fresh flights: 40 aeroplanes, 40 helicopters, 40 birds. No flocks were left in the pool.
- **Run:** `38424096206`.
  - The cause-key hash was committed first.
  - The decisions were committed before the key was opened.
  - 0 frames failed.

| Measure | Result | Bar |
|---|---|---|
| Accuracy when it names a cause | **0.869** (53 of 61), lower bound 0.776 | >= 0.80 / 0.70 |
| Share named | 50.8% | >= 35% |
| Wrong names after 5 frames | 0 | <= 2% |
| Gain over the forced answer (always answers: 0.742) | +0.127, lower bound +0.055 | >= +0.10 / > 0 |
| Placebo right names | 0.8% | void if > 5% |

**Verdict: PASS (stage-3 test).** Stage 2 (O4) is still a MISS, so the AIR ladder is not claimed past stage 1 until O4 passes.

## Honest limits
- The labelled box path stands in for a tracker.
- No flocks or drones were tested.
- Birds were mostly left with rivals open (8 of 40 named, all 8 right).
- The camera is on an aircraft.
- The evidence weight has no formal guarantee: the error rates were measured, not proven.

*Opus · 13 Oct 2026*
