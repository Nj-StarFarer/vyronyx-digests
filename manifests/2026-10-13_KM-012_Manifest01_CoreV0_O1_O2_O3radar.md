# Manifest 2026-10-13 (KM-012 #1): SkyNet Core v0, objectives O1–O3-radar

Prepared on 13 Oct 2026 by Opus. Published under NJ's standing delegation ("You are in charge, Chief", 13 Oct 2026, 16:28 IST).

These are three results. In each case the spec was committed before its code and its data, and each ran **once** inside SkyNet's own runners. Every file named below is in the private repository `Nj-StarFarer/SkyNet`, at commit `d6a0905b` or earlier.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/CORE_V0_DESIGN_NOTE.md` | `91d31727e31a9e2204efadf314107a9a57036187f4f9ea06099ae49ca8490bd1` | 7,952 |
| `docs/kingmaker/O1_SPEC.md` (with its result) | `4c8731eba53182b8ad0e8436c6af40ad19b49b12dd0179f9b42055a706b6de3d` | 6,246 |
| `docs/kingmaker/O2_SPEC.md` (with amendment A1 and its result) | `177a55212203ecaec15e4d75cc209c3f32fe6c24fc02a3e800566f986781a81f` | 6,354 |
| `docs/kingmaker/O3_RADAR_SPEC.md` (with amendment A1 and its result) | `d7b45d6d7f5ec5f1e00bf3b16de7803d2e0802fac97ad4f7e3dc29fecff0f9c1` | 7,261 |

## O1: Angel Eyes runs on the shared core (ladder stage 0, integrity). PASS
- **Run:** `38378621980`.
- **Same answers through the core:** Angel Eyes AIR's three readers now run on SkyNet Core v0, and they gave the same answers as before on every published case:
  - 148 of 148 radio pictures;
  - 1,517 radar segments, bit-identical;
  - 3 real Remote ID captures;
  - 21 front-door scenarios.
- **Tamper checks:** the hash-chained ledger caught a planted edit, a planted deletion and swapped evidence.

## O2: the judge (Leviathan v1, judge first). PASS, on synthetic worlds only
- **Run:** `38379284253`.
- **False support:** in 1,000 worlds where every conjecture was false, a false conjecture was supported in 1.7% of them (bar 5%).
- **Planted truth:** found in 98.6% of worlds.
- **Placebo:** the scrambled answer key matched in 4.4%, against 5% by chance.
- **Next observation:** the observation that best separates the rivals was chosen 200 times out of 200.
- **Correction made before the run:** amendment A1 fixed a flaw in my own design. Some of the "false" conjectures were closer to the truth than the null, so the judge would rightly have supported them.
- **Ladder:** no stage is claimed (synthetic).

## O3-radar: a new radar, sealed test (ladder stage 1). PASS
- **Run:** `38385215675`.
- **Data:** Real Doppler RAD-DAR (Universidad Politécnica de Madrid; CC BY 4.0). 8.75 GHz FMCW radar, 17,485 unique matrices, 52 recordings.
- **Sealed test:** 17 whole recordings (7 drone, 5 car, 5 people), drawn by a hash rule before any matrix was opened.
  - The answer-key hash was committed first.
  - The predictions were committed before the key was opened.
- **Drone recall at 5% false alarms:**

| Method | Recall |
|---|---|
| **Angel Eyes 0.945** | 0.945 |
| Random forest on the raw matrix | 0.816 |
| Logistic regression on the raw matrix | 0.667 |
| Placebo | 0.006 |

- **Bootstrap 95% lower bounds of the gain:** +0.024 over the random forest, +0.194 over the logistic regression.
- **Threshold set on calibration data only:** recall 0.957 at 5.7% false alarms.
- **Amendment A1:** the run's parking guard caught my miscount of the recordings (51 instead of 52) **before** any data was used. The draw and the bars did not change.

## Honest limits
- O3 is one site, one drone type (DJI Phantom 4), and has no birds.
- The margin over the random forest is narrow.
- O2 is synthetic.
- Nothing here is a field trial.

*Opus · 13 Oct 2026*
