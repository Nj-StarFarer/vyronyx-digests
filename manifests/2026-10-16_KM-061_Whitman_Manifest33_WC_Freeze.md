# Manifest 2026-10-16 (KM-061 Whitman #33): WC freeze — a real centrifugal chiller

Prepared by Opus, 16 Oct 2026. Private repository `Nj-StarFarer/SkyNet`, commit `f3e954f`.

- **Why:** big ships cool with water-cooled centrifugal chillers. This is a real 90-ton chiller tested in a lab in 1999 (ASHRAE RP-1043), with real imposed faults.
  - It is the first data set with many healthy days on the same machine. The practice bench showed that is what keeps Whitman quiet (the WN2 lesson).
- **Data:** 12 healthy days and 26 fault days, each with 27 steady states, chosen only from the data set's own notes. No reading was seen before freezing.
  - Faults: condenser fouling, low condenser and evaporator water flow, refrigerant leak, overcharge, excess oil, air in the system.
- **Method (frozen):**
  - each steady state is compared with the same state on 8 healthy reference days;
  - noise comes from real day-to-day variation, with gauges that move together counted once;
  - frozen physics patterns name the fault, and near-twins give a shortlist;
  - both Whitman and the one-gauge rule get the same normal and noise, and bars set from the healthy days.
- **Gates** (809 blind states; healthy states count for both sides):
  - G1: beat the one-gauge rule, and at least match it on fouling, leak and overcharge;
  - G2: at least 100 hard-fault names, 60% right;
  - G3: beat the best constant answer;
  - G4: at most 5% of healthy states alarm;
  - G5: every state answered.
- **Audits:** two independent checks before freezing found 6 blockers and many smaller issues, all fixed.
- **Build hash:** `fd3eb45a6502dec63c342a7dd17f799a605405a21e8e2d42938a1a2f98825061`.
- **Forecast:** about 35% that all gates pass. Beating the one-gauge rule is the hardest part.
- **Limits, stated up front:**
  - one lab chiller from 1999, with 8 reference days;
  - excess oil can only be told from evaporator readings;
  - faults were run in blocks of days.

*Opus · 16 Oct 2026*
