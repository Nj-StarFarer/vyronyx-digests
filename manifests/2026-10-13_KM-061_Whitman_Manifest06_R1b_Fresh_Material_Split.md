# Manifest 2026-10-13 (KM-061 #6): Whitman Rung 1b, fresh material and the open/sealed split, named before opening

- **Prepared:** 13 Oct 2026 by Opus.
- **Published on NJ's instruction:** "Do everything yourself".
- **Contents:** names, numbers and SHA-256 fingerprints only. No data, code or secret. The repository is private (`Nj-StarFarer/whitman-km061`).
- **What this is:** Rung 1 is spent (Manifest #5, FAIL). Spec v1.0 §8 allows a retest only on fresh sealed material named before it is opened. This manifest names that material and fixes the split. So far only a structure-only census has touched it (run `38347157570`): file names, hashes, headers, row counts and timestamps. It read no sensor value, no label and no operation-log content.

## The split document

| File | SHA-256 | Commit |
|---|---|---|
| `r1b/spec/RUNG1B_DATA_SPLIT.md` | `54bfb5325a55521ece0f2fc2497209103805ff7c3e27a9809f193ec7bd993cd4` | `ebf1dedb2bd07d5c8375c3b3b3738ae743498af1` |

## The pinned sources

| Source | File | SHA-256 |
|---|---|---|
| ARC Gloria (Zenodo 18330661), a real ship | `main_machinery_sensored.zip` | `b0d800d753a985396804ca136633c2e944f36573634bd4f36da2b2c5b644897a` |
| PRONTO (Zenodo 1341583), a multiphase-flow facility with induced faults | `PRONTO benchmark case study.zip` | `6879563fb7df5a71984c52157774f58b3f4725bd7ab0c717f7fcd57313f08961` |

## The split, in short

- **ARC Gloria** (main engine and two generators, 1 Hz):
  - **open:** timestamps before `2025-11-01 00:00:00`;
  - **sealed:** everything on or after that time.
  - The sealed part tests false alarms at sea (every alert counts as false) and planted sensor faults, drawn with a seed made at run time.
- **PRONTO:**
  - **open:** the folder `C0 Normal and Slugging conditions/` (12 Sep 2017 and 26 Jun 2018) and the operation-log rows for those two days;
  - **sealed:** the folders `C1 Air Blockage/`, `C2 Air Leakage/` and `C3 Diverted flow/`, the whole `Pre-processed data/` folder, and every other operation-log row.
  - The sealed part tests catching induced faults on a new plant.
- **Not used:** MetroPT2 `dataset_train.csv`. Part of it overlaps data already used, and its earlier months have no failure record.

## What happens next, in this order

1. Pack the open parts only, with an independent leak check.
2. Design on the open parts and on the spent Rung 1 data.
3. Freeze the Rung 1b spec (gates and marks) **before any sealed part is opened**, and publish its fingerprint.
4. Run once, sealed, and publish the result whatever it is.

*Opus · VyroNyx Private Limited · 13 Oct 2026*
