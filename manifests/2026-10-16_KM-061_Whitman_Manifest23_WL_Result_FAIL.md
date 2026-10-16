# Manifest 2026-10-16 (KM-061 Whitman #23): WL result — FAIL

Prepared by Opus, 16 Oct 2026. Private repository `Nj-StarFarer/SkyNet`. The run was 38847471197, on build `6e5d3818` (Manifests #20 and #22, forecast "about 5%"). The statements were committed (`dd3397a`) before the key was opened (`46f947e`).

- **Gates:**
  - G1: sensor-or-leak right on 17 of 38 faulty runs. FAIL.
  - G2: lying sensor named on 14 of 36. FAIL.
  - G3: 13 faulty runs called "nothing wrong". FAIL.
  - G4: 14 exactly right against the simple rival's 13. PASS.
  - G5: both fault-free blind runs were quiet, but the healthy check was a shortlist. FAIL.
- **By sensor:**
  - intercooler pressure: 6 of 12;
  - air flow: 8 of 12;
  - manifold pressure: 0 of 12;
  - leaks: 0 of 2.
- **Why:**
  - the models were too weak for transient driving (their own error was 10–18%, against 5–15% faults);
  - the manifold pressure sensor sits inside the engine's throttle control loop, so its error showed up in the air flow;
  - the leak rule had the wrong sign for this engine.
- Full write-up: `docs/kingmaker/WHITMAN_WL_RESULT.md`.

*Opus · 16 Oct 2026*
