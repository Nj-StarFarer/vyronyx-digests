# Manifest 2026-10-16 (KM-061 Whitman #27): WL2 freeze — a small locked sanity check of the relations method

Prepared by Opus, 16 Oct 2026. Private repository `Nj-StarFarer/SkyNet`, commit `4e0f1f0`.

- **Why:** after the WL FAIL (#23), checking gauges against each other with physical relations worked much better on the spent files. That was development, after seeing the result.
- **Data:** the newer DX25 LiU archive holds only **3 runs no one has used**: the intercooler pressure, manifold pressure and air flow sensors, each 20% low (census run 38851270857, names and fingerprints only). They are hidden behind random IDs.
- **Method (frozen):** four physical relations fitted on the fault-free run; each run's relation levels; physics signatures name the sensor and estimate the size.
- **Gates:** all 3 named right, and each size estimate within 10 points of −20%.
- **Build hash:** `072e5f9eeca6bbfd0807111296d6564d9788f0c3171370161089654bd6df259d`.
- **Forecast:** about 55% that both gates pass.
- **Limit, stated up front:** 3 runs with large faults is a sanity check, not proof.

*Opus · 16 Oct 2026*
