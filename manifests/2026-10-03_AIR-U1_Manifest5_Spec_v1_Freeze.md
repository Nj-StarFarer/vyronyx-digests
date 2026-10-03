# Manifest 2026-10-03 (#5): Angel Eyes AIR-U1 Specification v1, frozen (before any labelled data is used)

Prepared on 3 Oct 2026 at about 21:57 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, versions and SHA-256 fingerprints only. It stores no data, code or results.

## What is being registered
**AIR-U1 Specification v1**: a pre-registered test of whether Angel Eyes can find real aircraft emergencies (squawk 7700) in public ADS-B tracks over the continental US.
- The emergency code and every identifying field are hidden from the system.
- It is compared with two baselines given the same alert budget.
- It must explain why each alert is not an ordinary event: a data glitch, a gap, a normal manoeuvre, a holding pattern, a go-around or an identity mix-up.

The answer key is the code the aircrew set, recorded by the public archive before this test existed.

Status of the periods at freeze:
- **CAL (2025) and SEAL (Jan–Jun 2026) data have never been downloaded.**
- Only one DEV (2024) day has been read, and only as counts: the census registered in manifest #4.

## Fingerprints (SHA-256) of files in the private repo Nj-StarFarer/SkyNet
| File | Bytes | SHA-256 |
|---|---|---|
| air_u1/spec/AIR_U1_SPEC_v1.md | 28312 | f07212d293c41537f8cbdb086087532cb4124835293b657d1f765daacf481359 |
| air_u1/spec/AIR_U1_DAY_PERMUTATIONS.json | 14782 | 7101aa37cb16a262e3b41b5df8ec4bcc29c760147755c1b1e19bc323498de084 |
| air_u1/spec/AIR_U1_FREEZE_PINS.md | 1599 | 42cff1a9a104496b46711eca500c407b70693da108884606bf886cfa4d813ce6 |

- Private-repo commit: cca2fe84b368aa76621d81d75e613a4fe972ddb8 (3 Oct 2026, 21:54:51 IST).
- All 3 fingerprints were recomputed from the files as stored on GitHub after the commit, and they match.

## Pinned at freeze
- **Day order:** `numpy.random.default_rng(20261002 + period)` permutations (numpy 2.2.6), for DEV (2024), CAL (2025) and SEAL (Jan–Jun 2026). The DEV order begins with 2024-03-24, the census day.
- **Airport list:** OurAirports, `davidmegginson/ourairports-data` commit d954b7be2f09a3357d92399592e8c0224ee0f43d. `airports.csv` has SHA-256 ff5143921ef72d767402c299a5d868f79166c5c589267aca13dce957c41bd2a2 (12,734,638 bytes; Public Domain).
- **Region:** CONUS. It was chosen by the rule published in manifest #4, before the census result existed: 64,467 tracks starting in CONUS against 24,212 in Europe.
- **Sizing:**
  - CAL is 28 days;
  - the sealed size is N = min(181, max(28, ⌈60·D_cal/k⌉)) days, where k is the number of CAL emergencies;
  - the test stops with TOO_FEW if 181·k < 30·D_cal.
- **Bars, as formulas:**
  - main bar: Angel Eyes recall@K ≥ max(0.20, best baseline's CAL recall + 0.10);
  - CORRECT also requires beating the best baseline on the sealed data;
  - placebo and independent-checker stops apply.

## Rules that protect the test (from the spec)
- Numbers tuned on DEV, and the build fingerprints, are published **before** the calibration run. Any later change is a new spec version.
- The answer key is encrypted and deleted from the machine before Angel Eyes runs. If the sealed run is split across machines, no key is opened until the merged alert lists are fingerprinted and committed.
- Fewer than 30 emergencies in the sealed data is reported, and never voids the run. Confidence intervals never change a label.

## Forecasts written in the spec (never edited)
| Forecast | Probability |
|---|---|
| CORRECT | 30% |
| Stopped by the budget rule after calibration | 35% |
| TOO_FEW | 15% |
| PIPELINE_SUSPECT | 20% |

## Approval trail
NJ said "freeze. if yoy are confident." at 21:53 IST. Opus confirmed that it was confident: the spec had two independent reviews and no open blockers. These are statements in private chat, and they are claims until this manifest exists. No AIR-U1 test run has started. The build waits for November's Actions quota.

## How to verify
1. Ask VyroNyx for any file listed, compute its SHA-256, and look for the same string in the table.
2. Check that this file's commit is dated before any AIR-U1 DEV, headroom or sealed run in the GitHub Actions history.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
