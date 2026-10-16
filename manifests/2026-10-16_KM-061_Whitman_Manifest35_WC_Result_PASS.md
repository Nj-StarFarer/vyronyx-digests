# Manifest 2026-10-16 (KM-061 Whitman #35): WC result — PASS (5 of 5 gates)

Sealed run 38877032286 on the frozen build `7ab4e250…` (Manifest #34, forecast 35%).

- **Machine:** a real 90-ton centrifugal chiller with real imposed faults (ASHRAE RP-1043), which Whitman had never seen.
- **Passed all five gates:**
  - **G1:** beat the simple one-gauge rule, 289 to 249, and 149 to 142 on fouling, leak and overcharge alone.
  - **G2:** 188 hard-fault names, 182 right (97%).
  - **G3:** beat the best constant answer.
  - **G4:** 0 false alarms in 107 healthy states.
  - **G5:** every state answered.
- **Best:** air in the system, 46 of 81 states and all 3 days (the simple rule called it fouling). Condenser fouling: 29 against 19.
- **Weaker:**
  - the simple rule was better on refrigerant leak (47 vs 38) and overcharge (76 vs 69);
  - both missed the small faults;
  - excess oil was never found.
- **Limits:** one lab chiller (1999), 8 reference days. The result came after a disclosed safe stop and one rule change.

*Opus · 16 Oct 2026*
