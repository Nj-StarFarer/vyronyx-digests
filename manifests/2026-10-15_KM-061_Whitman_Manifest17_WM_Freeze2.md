# Manifest 2026-10-15 (KM-061 Whitman #17): WM freeze 2 — role map; the one run follows

Prepared by Opus, 15 Oct 2026. Private repository `Nj-StarFarer/SkyNet`, commit `ebbdc3b`.

- **Blind preparation** (run 38777618665): 16 data files became 1 reference file and 15 blind files under random IDs. The key stays on NJ's Mac (SHA-256 `f702f2bbd19b576538cc163fbe206129f35a60a1e66300b19c3b1c5db85db259`).
- **Correction to Manifest #16:** it said 16 fault files; there are **15** fault files and 1 reference file.
- **Role map:** the fixed marine rules mapped this engine's gauge names badly (`wm_role_map_RULES_REPORT.json`). So the map was written by hand from the gauge NAMES and the dataset's own variable dictionary, with no data value seen. It is disclosed in full in `docs/kingmaker/WHITMAN_WM_FREEZE2.md`. Gauges with no role in the frozen catalogue (for example, the air-filter pressure drop) are left out.
- **Build hash (freeze 2):** `4bf69e2d9ace67c95c6d44010380230ee505293ccf981f0801e680359b26df7c`. It covers freeze 1 plus the role map, the blind summary and the variable dictionary.
- **Forecast unchanged:** about 10% that all gates pass.

*Opus · 15 Oct 2026*
