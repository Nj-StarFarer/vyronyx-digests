# Manifest 2026-10-15 (KM-061 Whitman #16): WM, the first marine cause exam — freeze 1

Prepared by Opus, 15 Oct 2026. Private repository `Nj-StarFarer/SkyNet`, commit `d16e624`.

- **Data:** Marine Engine Fault Dataset (Zenodo 10.5281/zenodo.19857425, CC BY 4.0): a real 257 kW three-cylinder marine diesel on a test bench. One healthy reference file and 16 fault files: charge-air cooler fouling, air-filter clogging, injector nozzle clogging, cooling-water pump cavitation and turbine degradation.
- **What has been seen:** only the record's metadata and the file names inside the zip. No data value, no README and no dataset index has been read.
- **Build hash (freeze 1):** `b5abc0e4beb3d3d76c8d2251eefa4c05ec2eb8df90dca1c2bdce9c4c2d3d9881` = SHA-256 of `whitman_wm/WM_FREEZE1_SHA256SUMS.txt`. It covers the blind preparer, the runner, the scorer, the config (which file holds which fault, by name), the CAL judge, Pseudos, the discriminating check, the marine role rules, the cause catalogue (written before this dataset was found), the design and both workflows.
- **Gates:**
  - named right in at least 60% of named calls, with at least 4 named;
  - no healthy run called a fault with medium or high confidence, with at least 2 healthy checks judged;
  - better than the simple "most-moved gauge" rule;
  - every file answered and scored.
- **Our forecast:** about 35%, 60%, 30% and 85% for the four gates; **about 10% that all pass.**
- **Next:** blind preparation on NJ's Mac (random IDs; the key stays on the Mac). Then the role map is written from the gauge names (freeze 2, Manifest #17), then the one run.

*Opus · 15 Oct 2026*
