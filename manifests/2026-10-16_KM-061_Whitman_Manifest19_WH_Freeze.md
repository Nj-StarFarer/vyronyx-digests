# Manifest 2026-10-16 (KM-061 Whitman #19): WH freeze — which hydraulic part is failing; the one run follows

Prepared by Opus, 16 Oct 2026. Private repository `Nj-StarFarer/SkyNet`, commit `0f38806`.

- **Data:** the UCI "Condition monitoring of hydraulic systems" set (ZeMA test rig, CC BY 4.0). It has 2,205 cycles of 60 s. Four parts were degraded on purpose: the cooler, the switching valve, the pump (internal leak) and the accumulator. Archive SHA-256 `24128aad2ee4…` (census run 38836281687, names only).
- **Exam:**
  - Stable cycles with all four parts nominal are the reference.
  - Stable cycles with exactly ONE part off nominal are the blind test. Whitman must name that part.
  - The calculated channels CE, CP and SE are never read. The condition file is the key and stays on NJ's Mac.
  - No WH data value has been seen. Sensor positions on the rig are not in the public description, so the catalogue reasons on gauge groups (pressures, temperatures, flows per kW).
- **Method:** each reading is compared with the reference cycles at the same second of the cycle.
  - Temperatures are judged as their rise within the cycle and their spread between sensors, never as absolute values.
  - The valve is judged by how late the pressure profile runs.
  - The pump is judged by flow per kW.
  - The accumulator is judged by pressure ripple.
  - CAL with tells, Pseudos, and a simple rival (the most-moved gauge's part).
- **Gates:**
  - G1: named right on at least 60% of what it names, with at least 20 named.
  - G2: better than the simple rival.
  - G3: no held-out reference cycle named a fault with medium or high confidence.
  - G4: every cycle answered.
- **Independent audit before the freeze:** 4 blockers and 10 should-fix items. All were fixed and turned into tests.
- **Build hash:** `2a7baa7263aafb857597f85d6112d0abd73985136a1c26a1b1234495054f1561`.
- **Forecast (before the run):**

  | Outcome | Chance |
  |---|---|
  | All gates pass | about 15% |
  | G1 | about 40% |
  | G2 | about 35% |
  | G3 | about 60% |

  Most likely: the cooler and valve are named well, the accumulator rarely, and the simple rival is hard to beat on a rig where one gauge group moves per fault.

*Opus · 16 Oct 2026*
