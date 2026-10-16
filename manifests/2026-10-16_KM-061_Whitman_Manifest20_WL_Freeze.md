# Manifest 2026-10-16 (KM-061 Whitman #20): WL freeze — a lying sensor or a real leak; the one run follows

Prepared by Opus, 16 Oct 2026. Private repository `Nj-StarFarer/SkyNet`, commit `ca936b2`.

- **Data:** the LiU-ICE engine air-path training archive (Linköping University): a real turbocharged engine on a test bench. Archive SHA-256 `5b6ecfcad96a…` (census run 38845873798, names only).
- **Exam:**
  - The WLTP fault-free run is the reference.
  - **40 blind runs:**
    - 36 sensor faults (intercooler pressure, manifold pressure or air flow, each scaled by −15% to +15%, on two drive cycles: WLTP and FTP75);
    - 2 intake leaks (4 and 6 mm);
    - 2 more fault-free runs (right answer: nothing wrong).
  - All FTP75 runs are judged by a model that learned only on WLTP.
  - The FTP75 fault-time file is never read. No WL data value has been seen.
  - (The commit message says 41 blind runs; the right count is 40.)
- **Method:**
  - Each checked sensor is predicted from the engine's commands and ambient readings (fuel left out, because the controller sets it from the measured air flow).
  - The noise bar comes from out-of-sample predictions.
  - One sensor moving alone means a lying sensor. Air flow up with manifold pressure down means a leak.
- **Gates:**
  - G1: sensor-or-leak right on at least 80% of the 38 faulty runs.
  - G2: the lying sensor named exactly on at least 2 of 3 sensor-fault runs.
  - G3: at most 1 in 10 faulty runs called "nothing wrong".
  - G4: more exactly right than the simple rival.
  - G5: the healthy check and both fault-free blind runs called "nothing wrong".
- **Build hash:** `55c5ad30bc5cc1cb3f24dd1669800214cf7cbd7684b814b7daa34a23eead4ac7`.
- **Forecast (before the run):**

  | Outcome | Chance |
  |---|---|
  | All gates pass | about 5% |
  | G1 | about 25% |
  | G2 | about 30% |
  | G3 | about 15% |
  | G4 | about 50% |
  | G5 | about 40% |

  Most likely: the ±10–15% sensor faults are named, the ±5% ones are called "nothing wrong" (12 of the 38), and the FTP75 runs are harder than WLTP.

*Opus · 16 Oct 2026*
