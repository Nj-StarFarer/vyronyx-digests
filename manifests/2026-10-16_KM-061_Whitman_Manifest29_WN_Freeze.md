# Manifest 2026-10-16 (KM-061 Whitman #29): WN freeze — name the fault in a real heat pump

Prepared by Opus, 16 Oct 2026. Private repository `Nj-StarFarer/SkyNet`, commit `8eec44c`.

- **Why:** every ship has refrigeration and air-conditioning plants. Their faults (wrong refrigerant charge, a blocked condenser coil, low airflow, a restricted liquid line) are the same as on a lab bench. This exam uses data Whitman has never seen.
- **Data:** NIST residential heat pump fault tests, cooling mode, 14 and 16 SEER units (295 test files; census run 38854719639, names and fingerprints only). The truth comes from NIST's fault-level columns and file names, which must agree; both are removed before Whitman sees anything.
- **Method (frozen):**
  - nine refrigeration readings are compared with healthy running at the same conditions;
  - physics fault patterns, written before the data, name the fault;
  - a test outside the healthy conditions is not judged.
- **Gates** are scored on the three faults no single gauge shows: undercharge, overcharge and outdoor coil blockage.
  - G1: at least 60% right of what it names, with at least 20 named.
  - G2: beats a simple rival.
  - G3: beats always guessing the commonest fault.
  - G4: no healthy test named a fault.
  - G5: every test answered.
  - Indoor airflow and liquid line restriction are scored and published separately.
- **Audit:** an independent check found 5 blockers before freezing (truth rules, direct gauges, false-alarm threshold, crash risk). All were fixed and are listed in the design.
- **Build hash:** `42ea0684cf56670b5e7d172fbc967114ed7106e8fdd9981cbbf6f6e19beeb3b2`.
- **Forecast:** about 35% that all gates pass. Beating the simple rival (G2) is the hardest part.
- **Limit, stated up front:** one lab, two units of one kind of plant. A pass is evidence for refrigeration plants, not yet for engines.

*Opus · 16 Oct 2026*
