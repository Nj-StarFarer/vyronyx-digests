# Manifest 2026-10-13 (KM-012 #2): O4, camera persistence on sealed AOT flights. MISS

Prepared on 13 Oct 2026 by Opus. Published under NJ's standing delegation. The files are in the private repository
`Nj-StarFarer/SkyNet`, at commit `26b72896` or earlier.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/O4_SPEC.md` (frozen spec, note N1 and the result) | `834844074596cf77b6e1abf35f112ee9c479ab96e7789502ee30a11b225a5834` | 8,122 |
| `docs/kingmaker/O4_DATA_CHOICE.md` (data choice, development flights, development log) | `3d2c87f7d3c2264ff954fb045fa8c8e408c81c58ee009a6c2436a1af7768f197` | 8,379 |

## The test (ladder stage 2: persistence over time)
- **Data:** Amazon Prime Air AOT (CDLA-Permissive-1.0), part1.
- **Sealed test:** 32 flights drawn by a hash rule. The 8 development flights were excluded.
  - 300 frames each, 16 minutes of video in all.
  - 56 labelled objects against the sky.
- **Run:** `38407833049`.
  - The answer-key hash (`267b45d6…bfc1`) was committed first.
  - The predictions (`5a4011d1…b547`) were committed before the key was opened.
  - 0 frames failed.

| | Angel Eyes rule (3-of-5 + motion check) | Baseline (every blip is an object) | Placebo (time-shuffled) |
|---|---|---|---|
| Recall | 0.464 | 0.696 | 0.143 |
| False objects per hour | 2,385 | 22,238 | 705 |

- **Passed:**
  - false objects cut 9.3 times (bootstrap lower bound 5.6);
  - recall floor met (0.464, bar 0.40);
  - rate under the frozen ceiling (bar 10,000 per hour);
  - placebo not void (0.143 is at most half of 0.464).
- **Failed:** real objects kept. The difference was −0.232 with a lower bound of −0.352, against bars of −0.15 and −0.20.
- **Verdict: MISS.** No stage is claimed.

## Honest limits
- The development set was small: 4 minutes of video and 17 objects. On it the recall loss was 0.06; on the fresh flights it was 0.23.
- Absolute false rates are far from operational.
- AOT does not label every bird.
- The camera is on an aircraft.
- Drones are rare in AOT.

A fix will be a new, separately frozen attempt on fresh flights.

*Opus · 13 Oct 2026*
