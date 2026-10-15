# Manifest 2026-10-15 (KM-061 Whitman #14): WG result — FAIL (all three gates)

Prepared by Opus, 15 Oct 2026. The one attempt of the ARC Gloria quiet test (build `d45d797c…`, Manifest #11b) ran as run 38727096347. Result file `whitman_wg/sealed_results/run_38727096347/WG_RESULT.json` in the private repository `Nj-StarFarer/SkyNet` (commit `9c45c19`), SHA-256 `2a25824c6639650343320c9f57a7f8326d7e28f8f109f1cf0880b7770a150d11`.

## The result, as it came out
| Engine | Machine warnings per 1,000 h (gate ≤ 1.0) | Machine warnings | Ship's own rule alarms | Warnings starting in an hour with a bad reading (gate 0) |
|---|---|---|---|---|
| Main engine | 0.53 | 3 | 46 | 0 |
| Port generator | **8.17** | 36 | 1 | **1** |
| Starboard generator | 0.86 | 2 | **0** | **1** |

- **WG1 FAIL** (port generator 8.17 per 1,000 h). **WG2 FAIL** (port generator 36 against the rule's 1; starboard 2 against the rule's 0). **WG3 FAIL** (one each on the two generators).
- **Our forecast** (Manifest #11): about 50% for all three to pass. The biggest risk we named was a lasting change in the logs with a fixed learning year. That is what happened: 22 of the port generator's 36 warnings are led by one gauge (air temperature) in Oct – Dec 2023.
- **What passed:** on the main engine, 3 warnings in 5,650 judged hours against the ship's 46 rule alarms, and no typo ever started a warning.
- **The claim allowed by a pass is NOT made.** The data is now spent for this test; anything learned from it is development, and any fix must be proved on other data.

*Opus · 15 Oct 2026*
