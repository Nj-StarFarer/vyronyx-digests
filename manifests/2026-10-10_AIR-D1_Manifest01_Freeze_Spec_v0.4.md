# Manifest 2026-10-10 (AIR-D1 #1): Angel Eyes drone detection on real recordings, FREEZE of spec v0.4

Prepared on 10 Oct 2026 by Opus. Published on NJ's instruction ("Lock Air D1", 10 Oct 2026, 14:52 IST).

The commit time of THIS file is the authoritative freeze time. This manifest holds names, numbers and SHA-256 fingerprints only. It stores no data, no code and no secret. The repository the hashes refer to is private.

## 1. What is frozen
Repository `Nj-StarFarer/SkyNet`, commit `18e61a2`:

| File | SHA-256 | Bytes |
|---|---|---|
| `angel_eyes/air_d1/AIR_D1_SPEC_v0.4.md` | `975bb51cedddbbd1fc0c0dc6da6330a474f036b25d07e1589cd245013aba7045` | 24,023 |
| `angel_eyes/air_d1/AIR_D1_FORECASTS_AND_READING_PLAN.md` | `792ec37ee753984e3dd8325521497351fce9a26aecf645318881249a8c81b8f6` | 2,789 |

## 2. The test in brief
- **Question:** on public, real recordings, does Angel Eyes tell small drones from look-alikes (birds, aeroplanes, helicopters) better than a simple frozen classifier, with honest confidence and a correct "unknown"?
- **Dataset:** Svanström et al., multi-sensor drone detection, v1.0.0 (Zenodo 10.5281/zenodo.5500576). The Zenodo licence reads "Other (Open)"; the archive's own `LICENSE` is CC0 1.0 (checked at tag v1.0.0).
- **Seal:** the last 30% of each sensor × class × drone-type stratum, by clip number, after a 10-clip buffer. Two-drone and internet clips are practice only.
  - The split can be worked out from the public description sheet by design. The protection is that the build environment downloads only practice files, through an allowlist.
- **Expected sealed counts:**
  - thermal: 38 micro-drone and 63 look-alike recordings;
  - visible: 29 and 36;
  - sound: descriptive only.
- **One confirmatory test, on thermal video only:**
  - detection (P1) at least max(0.70, the rival's out-of-fold practice detection + 0.10);
  - a block sign-flip test p < 0.05 against the rival;
  - false alarms (P2) at most 10%, and not more than 5 points worse than the rival.
- **Rival:** frozen MobileNetV3-Small ImageNet features with logistic regression (video); band energies with logistic regression (sound). Each side gets the same budget of 20 tuning runs per sensor.

## 3. Honest limits, written before any data
- The dataset has no session information, and long same-type runs show that **leakage across the boundary cannot be ruled out.** The claim will say "later recordings from the same campaign", never "new sessions".
- With about 8 blocks of thermal drone clips, the paired test has little power.
- The data is one campaign in Sweden, with two micro-drone models. It says nothing about other places, drones or sensors.

## 4. What has been touched
Only the dataset's `LICENSE`, `README.md` and description sheet (metadata) have been fetched, by Opus on 10 Oct 2026. No video, audio, label or demo file has been fetched, no model has been trained, and the exposure audit across all seven VyroNyx repositories is clean.

## 5. How it was reviewed
An independent reviewer checked v0.2 and v0.3. It found 5 blockers in v0.2, and 1 new blocker plus partial fixes in v0.3. All were applied in v0.3 and v0.4. Opus checked the final hashes and byte counts by script.

## 6. Next
A separate session writes the pinned split code and the allowlist download, and makes the seal. Then come the build (Angel Eyes and the rival), the build gate, a fresh checker, the rehearsal and the pre-run manifest. Then one sealed run on NJ's typed phrase.

*Opus · 10 Oct 2026*
