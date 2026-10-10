# Manifest 2026-10-10 (AIR-D1 #5): sealed run #1 crashed before scoring; wiring fix; new pins

Prepared on 10 Oct 2026 by Opus. Published to keep the record complete before any further sealed run.

## 1. What happened
Sealed run #1 (run 38061040812, NJ's phrase, head `87efd1a`, build `2635981`) passed every pin and hash check, then **crashed in the scoring step** with `IndexError: index 175 is out of bounds for axis 1 with size 175`. The independent checker did not run, and **no label exists**. The run's results artifact (digest `52fa1eff…b427`) has not been opened by anyone and is declared **void**. It will not be read.

## 2. Cause
The sealed path read each model's feature version from a metadata key that the placebo models do not carry, so it defaulted to the old version. The IR placebo, trained on 1,327 columns, was handed 175. The earlier rehearsal used synthetic data, which always carried that key, so it never exercised this path. This is a pipeline fault, not a result.

## 3. The fix, code only
- The feature version is now taken from each model's training setting, and every model's input width and feature names are checked **before any data is read**. All 15 models were audited.
- **No model, feature, weights, threshold, checker or practice file changed.** Their hashes in FROZEN_HASHES.json are byte-identical between builds `2635981` and `50c62e6`. Only five code and test files changed: `run_sealed.py`, `rehearsal.py`, `rehearsal_real.py`, `synthetic.py` and `test_model_inputs.py`. This was checked separately from the builder's report.
- **A new permanent rehearsal case** runs the full sealed path on 20 real **practice** clips. Features match the frozen files exactly, every model's scores match its training-time fold scores (max difference 0.0, tolerance 1e-9), and the real checker agrees.
- 85 tests pass, and the rehearsal passes 11 of 11 cases.

## 4. New pins
Repository `VyroNyx/angel-eyes-air-u1`, main commit **`463360c`**:

| Item | SHA-256 / commit |
|---|---|
| `seal/PRERUN_PINS.json` | `7033ce68d8de5eccb4829a9bdfa33907ec814aa1c5ade24aa72f14da5eb6dd02` |
| `.github/workflows/air-d1-sealed.yml` | `165e8bf48ccf697f2e11c63abcf9d9ba2a059be3738868c10194b2c1ff9ca5ec` |
| Build commit | `50c62e6e5ec5eb6fa15dfbc3b8021729887d4e04` |
| `FROZEN_HASHES.json` | `4e16f14ca73b90c197b94ff746134412293c1215d801fbddc1783d631990294a` |
| Final sealed list (unchanged) | `3bcf0232bbdf38d03c7c7c6176c36a41fca1c8fb7ce18db453c78b680458643c` |

Everything else in manifest #4 stands, including the practice numbers and the honest notes.

## 5. Next
Sealed run #2 from commit `463360c`, started after NJ's permission. That is the one sealed run that counts.

*Opus · 10 Oct 2026*
