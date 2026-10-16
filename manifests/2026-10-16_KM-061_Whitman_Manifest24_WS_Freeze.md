# Manifest 2026-10-16 (KM-061 Whitman #24): WS freeze — what is wrong with the pump loop; the one run follows

Prepared by Opus, 16 Oct 2026. Private repository `Nj-StarFarer/SkyNet`, commit `e4b7d81`.

- **Data:** SKAB, the Skoltech water-circulation testbed (a pump, motor, flow, pressure, temperatures and vibration), at commit `b2c0d46c29` (census run 38848201862, names only). No WS data value has been seen.
- **Exam:** 34 blind fault runs. Whitman names the fault kind:
  - suction valve: 16;
  - fluid amount: 6;
  - rotor imbalance: 5;
  - discharge valve: 4;
  - cavitation: 2;
  - hot fluid: 1.

  The fault-free file is the reference. Each run is judged against its own start.
- **Gates:**
  - G1: named right on ≥ 60% of what it names, with ≥ 10 named.
  - G2: better than the simple rival.
  - G3: no healthy piece named a fault (medium or high).
  - G4: every run answered.
  - **G5 (new, after the WH lesson): more right than always guessing the commonest kind (16).**
- **Independent audit before the freeze:** 3 blockers and 5 should-fix items. All were fixed and tested.
- **Assumption, written before the data:** the pressure gauge sits between the pump and the outlet valve.
- **Build hash:** `d2d72c90c84b098ad52583ee2195a833b018993adb31ce941a6e2798d2d4b6df`.
- **Forecast (before the run):**

  | Outcome | Chance |
  |---|---|
  | All gates pass | about 20% |
  | G1 | about 35% |
  | G2 | about 50% |
  | G3 | about 70% |
  | G5 | about 30% |

  The biggest risks: fluid-amount runs taken for valves, and the gauge-position assumption.

*Opus · 16 Oct 2026*
