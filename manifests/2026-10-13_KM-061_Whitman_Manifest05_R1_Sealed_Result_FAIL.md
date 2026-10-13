# Manifest 2026-10-13 (KM-061 #5): Whitman Rung 1, SEALED RESULT: **FAIL**

- **Published:** 13 Oct 2026 by Opus, on NJ's instruction "Do everything yourself". Published as measured, as spec v1.0 §9 requires whatever the label.
- **Contents:** numbers and SHA-256 fingerprints only. The repository is private.

## 1. The run

GitHub Actions run `38344290057` in `VyroNyx/whitman`, with build hash `bffd61b23d5ac04b4606cf779cdb79d32f8cf18857f8697a10fc700dad87f47c` (Manifest #4). The order held:

| Step | Commit |
|---|---|
| Pins checked (28 of 28 OK) | — |
| Seed drawn and its hash committed | `ed985ee` |
| Whitman ran with no network, then raw decisions and output hashes committed before any label was read | `c1aafe5` |
| Independent reader scored, the second scorer agreed, and the result committed | `93fb806` |

| File (under `r1/sealed_run/results/run_38344290057/`) | SHA-256 |
|---|---|
| `SEED_SHA256.txt` (committed before Whitman ran) | `bde141cb4d016b7f1c3bbed0071b045000c4da0b0a6abc1bceaa410171f85a8e` |
| `outputs/OUTPUT_SHA256SUMS.txt` | `c378b1bdd98fb027c2916d9551fb071637c4538c64cd53ae9c5680e7b7c2743e` |
| `result/score_report.json` (the independent reader) | `28518d4098b95f34fa00ee72a4a2a27e884563785355f6f011952541f4026b9d` |
| `result/CHECK_REPORT.json` (second scorer: **AGREE**) | `9bbdeec99c29c4a8055e5e07ac8eb462163fbcedd4dcc776ca3f99ce1dc0bc6a` |
| `result/RESULT.txt` (**FAIL**) | `4f8e9e45f8a9e1843b81eaf3bdf52a6b778d415d23bf985774a9d34a43f69bd5` |

The revealed seed is `b6fcd7eacf4a17c2bfa418ce58bd75c36cc8b79f66564970d098620227911e68`. Its SHA-256 is `166ef9f9…ce732`, equal to the hash committed before the run.

## 2. Gates

| Gate | Mark | Measured | Result |
|---|---|---|---|
| G1 MetroPT-3 recall | ≥ 2 of 3 | **2 of 3** (F2, F3; F4 missed) | PASS |
| G2 MetroPT2 recall | ≥ 1 of 2 | **1 of 2** (Q1; Q2 oil leak missed) | PASS |
| G3 compressor false alarms | M3 ≤ 4, MP2 ≤ 2 | **M3 2, MP2 0** | PASS |
| G4 median warning | ≥ 2 h | **−0.86 h** (all three catches came 0.8–2.1 h *after* the recorded start) | **FAIL** |
| G5 SKAB recall | ≥ 70% | **7 of 17 (41%)** | **FAIL** |
| G6 SKAB false alarms | ≤ 3 | **0** | PASS |
| G7 marine engine recall | ≥ 3 of 4 | **3 of 4** (pump cavitation missed) | PASS |
| G8 marine engine false alarms | ≤ 1 per run | **0 in every run** | PASS |
| G9 planted sensor faults | ≥ 36 of 40, alert during ≤ 1 | **36 of 40, 1** | PASS |
| G10 no hiding | UNKNOWN ≤ 10%, SENSOR_FAULT ≤ 2% | M3: 5.4% / 0.4% (clean), 5.6% / 0.7% (planted). **MP2: SENSOR_FAULT 5.3%** | **FAIL** |
| G11 beats the alarm panel | more catches at ≤ false alarms | **Whitman 3 caught / 2 FA; alarm panel 4 caught / 22 FA** | **FAIL** |

**Label: FAIL.** Under spec §1 no claim is allowed. Under §8 any retest needs fresh sealed material, named in an amendment before the retest.

## 3. What the numbers say, plainly

- **Compressors.** Whitman caught 3 of 5 sealed failures with **2 false alarms**, against the alarm panel's 4 of 5 with **22** and the Isolation Forest's 2 of 5 with 6.
  - Every Whitman catch came 0.8–2.1 h after the recorded start. G4 failed, as Manifest #3 warned.
- **Marine engine.** Whitman caught 3 of 4 runs with **zero** false alarms. The alarm panel caught 4 with 6 false alarms.
- **SKAB water-pump rig.** Whitman caught 7 of 17 with zero false alarms (alarm panel 4 with 2).
  - Development had shown 15 of 17. **That gap is the measured cost of tuning on 17 open files.**
- **Planted sensor faults.** 36 of 40 were told apart.
- **MP2 "SENSOR_FAULT" share.** It was mostly one gauge (DV_pressure, about 62 hours), above the 2% cap.

*Opus · VyroNyx Private Limited · 13 Oct 2026*
