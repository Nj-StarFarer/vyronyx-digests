# Manifest 2026-10-13 (KM-061 #7): Whitman Rung 1b, frozen spec and build, published before the sealed part is opened

- **Prepared:** 13 Oct 2026 by Opus.
- **Published on NJ's instruction:** "Do everything yourself".
- **Contents:** names, numbers and SHA-256 fingerprints only. No data, code or secret. The repository is private (`Nj-StarFarer/whitman-km061`).
- **What this is:** the Rung 1b test rules and the detector build, frozen. Nothing listed here changes after this point. The sealed part of the ship data (Manifest #6) has not been opened. The sealed run checks the build hash below first and stops if it differs.

## The build hash (typed into the sealed run)

| Item | SHA-256 | Commit |
|---|---|---|
| `r1b/FREEZE_SHA256SUMS.txt` (55 files) | **`474e37e6b01d757808b8e56725d9d3d04b7416b755a697d5d6ddefa9249802cb`** | `01bf23825e8bc6cca9e8b5ebea7577508d55910b` |

## Key files inside it

| File | SHA-256 |
|---|---|
| `r1b/spec/WHITMAN_R1B_SPEC_v1.0.md` (the rules) | `6aa5980f5639d5d8880de087957f0fd028dd90fdae849fa541210f4566018a99` |
| `r1b/spec/RUNG1B_DATA_SPLIT.md` (Manifest #6) | `54bfb5325a55521ece0f2fc2497209103805ff7c3e27a9809f193ec7bd993cd4` |
| `r1b/build/INTERFACE_R1B.md` | `f7cf524e22cee64e44ccabeed7fcfba1921ebfb6793fdc66806a8aa2983c7708` |
| `r1b/build/models_r1b/MODELS_SHA256SUMS.txt` (detector and baseline models, fitted on the open part only) | `dbcdfb7312430d97f82cecdf4a9e2544a740080524536ebdf5fbffbcd8c89e91` |
| `r1b/build/models_r1b/MACHINE_SPREAD.json` (planted machine-fault sizes) | `fef87d8ddfd4cc84f953eecf3c2491a27bd0039755de74b63e14c35247474171` |
| `r1b/plant/plant_r1b.py` (written independently, from the spec only) | `9ca16d37bc78946e66323309126c44a7ef33dd860525b0a9d354298dd1789ea2` |
| `r1b/reader/reader_r1b.py` (written independently, from the spec only) | `6cddb0277d18aac7a93f9f9da1ba6720c750d1db08bba48f56e3c44934c92e30` |
| `r1b/sealed_run/opus_check_r1b.py` (second scorer) | `73cc9fe3224ee831d1caf5134f5ffc420f9b1368addce846318bd4e9a7ca4b36` |
| `.github/workflows/whitman-r1b-sealed.yml` | `597af30bef5ca565efbfab77cac03b958a0c88892ad6ac59cda07eb2f994db97` |

## The test, in short

- **Data:** ARC Gloria (a real ship): main engine (ME), port generator (GP), starboard generator (GS).
  - Whitman is fitted on 8 Sep – 31 Oct 2025.
  - It is tested on 1 Nov – 19 Dec 2025, which nobody has opened yet.
- **Three copies per machine, under neutral names:**
  - clean;
  - with up to 20 planted gauge faults: stuck, drift, spikes, dropout;
  - with up to 6 planted machine faults: cooling and lube.

  The seed is drawn inside the run, and its hash is committed before Whitman starts.
- **Order of commits:** Whitman's outputs are committed before the planting key is read. An independent reader scores them, and a second scorer must agree with it.

| Gate | Mark | Development value (open-part check) |
|---|---|---|
| G1 False alarms per machine (clean) | at most 1 on each | 0, 0, 0 in 16 days |
| G2 Fewer than the alarm panel | Whitman total < panel total, or both 0 | 0 vs 13 |
| G3 No hiding | UNKNOWN ≤ 10%, SENSOR_FAULT ≤ 2% of running time | at most 0.8% |
| G4 Gauge faults told apart | at least 30% | 46% |
| G5 Machine alarm on a lying gauge | at most 10% | 1 of 68 |
| G6 Planted machine faults caught | at least 30% | 44% |

- **Not used, with reasons stated in the spec:**
  - **PRONTO:** only about 25 minutes of healthy open data at the fault set points, too little to set a fair mark.
  - **MetroPT2 `dataset_train.csv`:** as Manifest #6 says.
- **Limits stated in the spec:**
  - There are no labelled real faults, so every alert on clean data counts as a false alarm.
  - The machine faults are synthetic.
  - The data covers one ship and one season.
- **Checks done before freezing:**
  - an independent author's rehearsal: 108/108 checks pass;
  - a fresh-session inspection: all blockers fixed and re-inspected;
  - end-to-end rehearsals on open data, locally and in CI: the reader and second scorer agree.
- The result will be published as measured, whatever the label.

*Opus · VyroNyx Private Limited · 13 Oct 2026*
