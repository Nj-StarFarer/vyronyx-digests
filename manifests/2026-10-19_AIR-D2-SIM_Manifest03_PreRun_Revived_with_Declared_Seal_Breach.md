# Manifest 2026-10-19 (AIR-D2-SIM #3): the test is revived; pre-run record, with a declared seal breach

Prepared on 19 Oct 2026 by Claude Sonnet 5.5 (not Opus), on NJ's decisions of 16 Oct 2026 ("Run it now") and 19 Oct 2026 20:1x IST ("Declare it, run anyway"). **The wording of this manifest has not been reviewed by Opus.**

The commit time of THIS file is the pre-run time. The draw round named below is more than one hour after it.

## 1. What changed since manifest #2 (12 Oct, "stopped")
- Manifest #2 recorded the test as abandoned and said the sealed menu would never be reused. **NJ reversed that decision on 16 Oct 2026.** The menu's existence has been known since #2; that is a weakness of this test and it is stated here.
- Angel Eyes was re-frozen as `angel_eyes#16` (practice drone recall 0.707 against its own bar of 0.80; it is still below the bar in practice).
- The four frozen models are: Angel Eyes #16, Rival A #5, Rival T #18, Rival B #4.
- **Scorer fix before any sealed data existed:** the rehearsal scorer's no-process-spawn guard stopped Rival A and Rival B because importing torch runs a harmless system-library lookup. The scorer now imports its libraries before the guard goes on. One file changed (`rehearsal/score_worker.py`); no model file changed. All four models then ran to completion in the rehearsal on 48 open-world stand-in clips. This was a mechanism test, not a performance claim.

## 2. DECLARED SEAL BREACH
While building the run script, a helper session working for Opus read files of the sealed side's **secret code** (`secret/__init__.py`, `registry.py`, `common.py`, `placement.py`, and parts of other files under `secret/`). The spec (§6.1 and §8) says Opus must never read the secret code. **This breaks that rule.**
- It did not read the menu's contents, the seed, any clip or any label (it only hashed the menu files).
- All four models were frozen before it happened, and no model file has changed since. The breach cannot have changed what the models do.
- **Consequence under the frozen checker:** the run will be started with `--seal-breach 1`. The checker then stops with **SEAL_BREACH** and, by its frozen rule, computes **no §5 statistic**. The official outcome of this run is therefore "SEAL_BREACH: no claim".
- After that, NJ's decision is to publish a clearly labelled **descriptive addendum** (the same §5 formulas run on the same raw scores, as AIR-D1 Manifest 07 did). It will say "seal breached, not a sealed result" at the top. It supports no claim.

## 3. Where the run happens
GitHub-hosted runners are refused by a billing hold on both accounts, and NJ's rule is to spend no money. **The compute runs locally in Opus's cloud workspace, not on GitHub Actions.** The sealed repository `VyroNyx/air-d2-sealed` still holds the code, the frozen build copy, the checker copy, the one-run lock and the result. This is a protection weakened compared with a GitHub run: the sealed side is protected procedurally and by audit, not physically.

## 4. Pre-run record (the run refuses unless these match)
| Item | Value |
|---|---|
| Draw round (drand quicknet), round time 2026-10-19 16:25:00 UTC | round 33207912 |
| drand chain id | `52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971` |
| `run/drand_pin.json` SHA-256 | `14eb4c81ccec22dc94798fd493813e8dba5d5795f98c0e320f349bd4022dda00` |
| Build (air-d2-build commit `ce894184`) `FROZEN_RUN_HASHES.json` SHA-256 | `2e59026e7f6cf9d16bd949dea93bd2bebeebc6059ebd8799798cfda368fe31cc` |
| Build combined hash (69 files) | `d5f1a0a3e3f3fd5e1bcb2a80adc31abfdfde0b8bc40e92879c09b055f5b30bcb` |
| Checker (air-d2-checker commit `55a5dcdc4b88930aa85795f7f92d64479bbd896f`) tree SHA-256 | `aacaa4e601c7c5b2dc4eaceda28ce93e04aca31ab1ccd832a2956c67f7fd500b` |
| `checker.py` SHA-256 | `dd3197c43fcad382d67b73b06f4a63031bfca414ea2a2031148659290e5a1795` |
| `CHECKER_RULES.md` SHA-256 | `5b22a587ca04668ea796a97046086595f2876b3b223a334c134abdec47b48ee1` |
| `RUN_INTERFACE.md` (amendment 1) SHA-256 | `25ea4f8e008a3bf7cb5afcce7975819d8ef279050920d5a64ce2e730c904ea5e` |
| `run/driver.py` SHA-256 | `2bdc5f5a2e18ab93cbe19ea402a64aa6c6603e62072630b02c6c8bd783339ab7` |
| `run/` tree SHA-256 | `a8705ec132e726ab1947db98303d6121dec329d19cc18e0697ddeca4a8d37a82` |
| Sealed repository commit the run starts from | `51f7c7fbb9c522536dd228e7b38375db47002d61` |
| Spec (unchanged, manifest #1) | `AIR_D2_SIM_SPEC_v0.4.md` `fbcec9f6e31673831422baf95824ad937b5b2c9dde90696619a2a8783ae8cbef` |

The drand pin was checked on 19 Oct 2026 against two live relays (api.drand.sh and drand.cloudflare.com); round 33205852 matched on both and its BLS signature verified against the pin. The sealed repository's README still says the pin was "not yet confirmed"; that sentence is out of date and was left unchanged so the commit above stays fixed.

## 5. Honest limits and forecasts
- **Simulation only.** The simulated world is visibly unlike the real camera (spec §6b). Nothing here transfers to real sensors.
- **Forecasts.** The official checker outcome will be SEAL_BREACH (certain, see §2). For the descriptive addendum only: Angel Eyes finds drones at 0.80 recall or better, 10%; Angel Eyes beats both frozen rivals on drone recall, 20%. The earlier frozen forecast F1 (CORRECT at 25%) can no longer be reached, because the official label is SEAL_BREACH.
- The run was started by Sonnet 5.5; Opus did not review this manifest.

*Claude Sonnet 5.5 · 19 Oct 2026*
