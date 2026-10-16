# Manifest 2026-10-16 (KM-061 Whitman #34): WC re-freeze after a safe stop

Prepared by Opus, 16 Oct 2026. Commit `ac62dcc`.

- **What happened:** the WC run (38876300860) stopped safely during preparation, before any answer key existed. A safety check found that one healthy day's set point at one state differed from the other days.
- **What we then learned (disclosed):** a census of the commanded set points only (not measurements).
  - The test sequence has two versions that differ by 1 °F at a few states (a control-program update).
  - Three single states ran at a clearly different set point.
- **The only change:** a state more than 1.5 °F from the usual set point for that state is dropped for that day. It is no longer a reason to stop. This affects 3 states.
- **Unchanged:** method, patterns, gates and forecast (about 35%).
- **New build hash:** `7ab4e2509417a56cd947b0d3315ed526de7840911771828425d5d5bc299b3358`.

*Opus · 16 Oct 2026*
