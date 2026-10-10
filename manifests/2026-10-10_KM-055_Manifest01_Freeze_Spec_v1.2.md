# Manifest 2026-10-10 (KM-055 #1): Catcher in the Sky, sealed catch-and-dock test in simulation: FREEZE of spec v1.2

Prepared on 10 Oct 2026 by Opus. Published on NJ's instruction ("Alright Publish.", 10 Oct 2026, 10:02 IST).

An Inspector (a fresh session that did not write it) checked every hash, number and table cell against the files before publication; its 2 corrections are applied.

The commit time of THIS file in this repository is the authoritative freeze time. This manifest holds names, numbers and SHA-256 fingerprints only. It stores no data, no code and no secret. The repository the hashes refer to is private.

## 1. What is frozen
KM-055 asks: on sealed simulated scenarios whose target movements it never practised, does Catcher in the Sky **catch** an approved micro camera drone more often than a frozen textbook chase method flying the same drone, **and dock after at least 90% of its catches**, without ever breaking a safety rule?

From this moment the text below changes only by a numbered amendment, published before any sealed data exists. **No sealed scenario, K9 policy, reference planner or practice scenario exists yet.**

Repository `VyroNyx/catcher-in-the-sky`, commit `35d60ef`:

| File | SHA-256 |
|---|---|
| `docs/KM-055_SPEC_v1.2_FREEZE_CANDIDATE.md` (the spec, 34,688 bytes) | `4873e2420d2b4a52674f9b1e7dfc1572792ad2d4a57a73e9289e6b9f1dc8d0db` |
| `handoff/validate.py` | `d0f54bdb39da594087b96064d67f73b207f50b474c0aa3eec8ab72cfdf39543d` |
| `handoff/test_validate.py` (36 tests, all pass) | `75ee2f0c51a7c51c3b866ad6aa238b5c28fc50c4417e42e5f6fdaaaa6601b772` |
| `docs/HANDOFF_FORMAT_v0.md` | `2f0d5068cbc1a59bd6f36442788a480dd1486ce11c4b201ad319983dacca3fb9` |
| `handoff/example_v0.json` | `829eff2232cca10c3bbbfbc9d81be8d9fb11e72578e291c29e78978cc61a31c9` |
| `handoff/example_v0_1.json` | `6efe3774135763708705b1b1b596c7aca1794638d959082ddac5a79c68e086b4` |

## 2. The key numbers in the frozen text
- **Labels:** CORRECT, INTERESTING or MISS. "Beats" means more catches than the rival **and** an exact two-sided McNemar test with p < 0.05, on the normal, winnable scenarios of the never-practised kinds (K5–K9). CORRECT also needs a gap of at least 10 points, a catch rate of at least 50%, docking after at least 90% of catches, and every should-abort scenario correctly aborted.
- **Stops:** SAFETY_FAIL, TOO_MANY_UNWINNABLE (more than 10%), MODEL_CHECK_FAIL, K9_FAULT, CHECKER_MISMATCH, SIM_FAULT.
- **Sealed set:** 9 movement kinds × 50 scenarios = 450, with exactly 5 should-abort scenarios per kind.
- **Practice:** horizontal acceleration at most 40% of a_max (2.75 m/s²) on every sample. **Held back:** at least 75% (5.15 m/s²) or 3.75 m/s² vertical. a_max = g × tan 35° = 6.87 m/s².
- **Margin:** the catcher has 1.33× the target's airspeed and 1.2× its climb speed.
- **Claims allowed:** about the catcher's software in this simulation only. Never real hardware, FPV or nano drones, or "interception proven".

## 3. Expected zone sizes (from `handoff/validate.py`)
Half-widths of the 99% zone in metres (along range / across range / vertical), with q = 8 / 8 / 4 m²/s³, for a hand-off with the spec's §6 errors, moved forward by Δt:

| Range from pad | Δt 0.5 s | Δt 1.5 s | Δt 4 s | Δt 7 s (cap) |
|---|---|---|---|---|
| 200 m | 10 / 12 / 25 | 15 / 16 / 27 | 47 / 47 / 42 | 105 / 105 / 80 |
| 400 m | 10 / 24 / 37 | 15 / 26 / 38 | 47 / 52 / 50 | 105 / 107 / 84 |
| 650 m | 10 / 38 / 52 | 15 / 40 / 52 | 47 / 60 / 62 | 105 / 111 / 92 |
| 900 m | 10 / 53 / 66 | 15 / 54 / 67 | 47 / 70 / 75 | 105 / 117 / 101 |

## 4. Cited manufacturer numbers (captured 10 Oct 2026, about 04:30 UTC)
| Page | Max horizontal speed | Max ascent / descent | Max pitch angle | Takeoff weight |
|---|---|---|---|---|
| https://dji.com/air-3/specs | 21 m/s (19 m/s in EU regions) | 10 / 10 m/s | 35° | 720 g |
| https://www.dji.com/mavic-3-pro/specs | 21 m/s | 8 / 6 m/s | 35° | 958 g |

**Honest limit:** the spec (§10 step 1) asks for archived copies of these pages. Opus's session could not reach an archive service, so this manifest records the cited values and the capture time instead. If the pages change later, these values are what the spec relied on.

## 5. How the text was reviewed
- Four independent reviews, by sessions that did not write the text:
  - a consistency review of v1.0 (8 blockers);
  - a re-review of v1.1 (2 blockers);
  - two checks of v1.2's own changes (3 blockers, then none).
- All findings are applied and listed in the spec's §14. The final verdict was "freezable after a text pass", and that pass is in commit `35d60ef`.

## 6. What comes next (spec §10)
1. **Step 2, before any practice:** a separate session writes the sealed generator, the secret kind K9, the hand-off maker and the reference planner, and makes the sealed set. Only salted SHA-256s are published.
2. Then the builder makes the world, the practice generator, the catcher and the rival.
3. Then the build hashes, a fresh checker, a dress rehearsal, the reading plan and forecasts, and the pre-run manifest.
4. Then one sealed run on NJ's typed phrase. Its outcome is published whatever the label.

*Opus · VyroNyx Private Limited · 10 Oct 2026*
