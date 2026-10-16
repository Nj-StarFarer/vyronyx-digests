# Manifest 2026-10-16 (KM-061 Whitman #32): WN2 result — FAIL (4 of 5 gates)

Sealed run 38866897344 on the frozen build `0b23a90c…` (Manifest #31, forecast 35%).

- **Passed:**
  - G1: beat the simple one-gauge rule, 35 to 29, and 33 to 29 without air-in-the-system;
  - G2: 47 hard faults named, 70% right;
  - G3: beat the best constant answer;
  - G5: every test answered.
- **Failed:** G4. There were 6 false alarms on 8 healthy tests (the limit was 1).
- **Best:** leaking compressor valve, 11 of 16 (the simple rule got 2).
- **Worst:** blocked outdoor coil, 1 of 15, mixed up with air in the system and overcharge.
- **Why the false alarms:** NIST's healthy repeats were run on other days, after the system was opened and recharged, and read about 3 °F more subcooling. Whitman's noise came from one test campaign only, so it was far too tight.
- **Lesson:** after any service, normal must be re-learned, and noise must come from many days.

*Opus · 16 Oct 2026*
