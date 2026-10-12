# Manifest 2026-10-12 (KM-061 #1): Whitman Rung 1, sealed machinery-failure detection test: FREEZE of spec v1.0

- **Prepared:** 12 Oct 2026 by Opus.
- **Published on NJ's instruction:** "Yes and Yes" (12 Oct 2026, 22:28 IST), approving the freeze and its publication here.
- **Inspection:** a fresh Inspector session that did not write the spec checked every hash, file name, count and failure time against the data-check output and the public sources, in three rounds:
  - round 1: 8 blockers;
  - round 2: 4 blockers;
  - round 3: no blockers.

  Every finding is applied. The record is in spec §10.
- **Freeze time:** the commit time of THIS file in this repository is the authoritative freeze time.
- **Contents:** names, numbers and SHA-256 fingerprints only. No data, no code, no secret. The repository the hashes refer to is private.

## 1. What is frozen

Whitman is VyroNyx's autonomous intelligence layer for a ship's engine room. It reads data only and never controls the ship. Rung 1 asks one question:

**Can Whitman detect machinery failure early, on data it has never seen, without crying wolf?**

From this moment the spec changes only by a numbered amendment published here. **No Whitman detector exists yet.** Only the data check (census plus open-part statistics) has been run.

Repository `VyroNyx/whitman`, commit `aec34039e0170928ed7a09685c7fdad0b4d26d91`:

| File | SHA-256 |
|---|---|
| `r1/spec/WHITMAN_R1_SPEC_v1.0_FREEZE.md` (the spec, 24,401 bytes) | `7312b3bacf5b5c96365e3de2e963d546f112d81651fef51a8ea09d40d2e20288` |
| `r1/spec/WHITMAN_R1_DATACHECK_DC1.md` (the data-check spec, with amendment A1) | `13c232c7ad6bc86fb7d6305b357b482ca23d86e34acfe5d4a821fd3926790e4c` |
| `r1/datacheck/results/run_38280067666/DC1_REPORT.json` (the data-check output, archived from Actions run 38280067666) | `957db71f719813c8658df946defb65ce00e81c880c198282e4adffc55e713675` |

## 2. Public data pinned by the spec

| Data | Pin |
|---|---|
| MetroPT-3 (UCI 791), metro-train air compressor, 0.1 Hz | CSV SHA-256 `db30ccb4ea402e3c8bf2c99db06e288d4f2a772f6928f9dbe26a920d69793e24`. Sealed from 2020-05-01, with 3 failures. |
| MetroPT2 (Zenodo 7766691) | `MetroPT2.csv` MD5 `056e04fd1874eaef4697d6b6657502c3`, plus a SHA-256 to be published by the pre-build census. Sealed from 2022-05-25, with 2 failures from the record's own table. The paper's extra oil leak is an unscored zone. |
| SKAB (github.com/waico/SKAB) | Commit `b2c0d46c2971dcbfe71e26087b6d231998bb91c2`, seed 20261012. 17 open and 17 sealed fault files. Sealed list SHA-256 `d51507422716814028efd373bd59c02b043451c1ebb079c7ccce48b82b6527cf`. |
| Marine Engine Fault (Zenodo 19857425), a real marine diesel engine on a test bench | Zip SHA-256 `3fba7aa0c288ae1bc05383fb54bf67cbde209d61b26e3e811d4bc2f22f97442b`. The four 85%-load fault runs are sealed and scored; the injector-nozzle program run is sealed for Rung 2 only. |

## 3. The key numbers in the frozen text

- **Outputs:** one state per input row: NORMAL, WATCH, MACHINE_ALERT, SENSOR_FAULT or UNKNOWN. Only MACHINE_ALERT is scored as a detection.
- **Windows:** a failure window opens 48 h before a failure's recorded start. Repair grace is 48 h. A 7-day window is reported only.
- **Gates** (all must hold for PASS):
  - G1, MetroPT-3: catch at least 2 of 3 failures.
  - G2, MetroPT2: catch at least 1 of 2.
  - G3, compressor false alarms: at most floor(days ÷ 30) per dataset, which is 4 for MetroPT-3.
  - G4, warning: median warning of at least 2 h.
  - G5, SKAB recall: at least 70% of scored files.
  - G6, SKAB false alarms: at most 3.
  - G7, marine engine recall: at least 3 of 4 runs.
  - G8, marine engine false alarms: at most 1 per run.
  - G9, planted sensor faults: at least 36 of 40 told apart, and an alert starts during at most 1.
  - G10: UNKNOWN at most 10% and SENSOR_FAULT at most 2% of running time.
  - G11: Whitman must beat a fixed-limit alarm-panel baseline.
- **Stops:**
  - S1–S6 (hash mismatch, seal breach, not repeatable, peeked ahead, bad output, checker mismatch): no label is given.
  - S7 (MetroPT2 unusable) and S8 (too few scored SKAB files): reductions, not stops. The result is marked "without MP2" or "without SK".
- **Claim allowed if PASS:** detection only, on these public datasets, with Wilson intervals stated. No claim about causes, remaining life, repair planning, parts or ships.
- **Honest limit:** the failure times and labels of these public datasets are themselves public. They are kept out of the detector by locked storage, a no-network rule and hashed raw decisions written before any scoring. That is why every step is published here.

## 4. What comes next (spec §9)

1. A pre-build census of `MetroPT2.csv` (hashes, columns, time range; no sealed value read), published as Manifest #2.
2. The build on open data, with self-tests. The build hash is published.
3. A fresh session writes the independent reader. A dress rehearsal is run with planted errors.
4. The pre-run manifest: the seed hash, build hash and reader hash.
5. One sealed run on NJ's typed phrase. Its outcome is published here whatever the label.

*Opus · VyroNyx Private Limited · 12 Oct 2026*
