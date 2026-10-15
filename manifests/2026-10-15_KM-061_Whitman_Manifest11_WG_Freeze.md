# Manifest 2026-10-15 (KM-061 Whitman #11): WG, the ARC Gloria quiet test — FROZEN before the data is opened

Prepared by Opus, under NJ's standing delegation. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `80610f5f` (07:58:41 UTC).

**Build hash** (SHA-256 of the freeze list): `1ad2073fad8dc171a88a10f0ba5fb1bbc8db0e8e600833bcee2d6971563a0773`

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/WHITMAN_WG_SPEC.md` (frozen spec, gates and forecast) | `aee92550ecb9db9716cb6024105dc3a4641fa5abe537fdc08f829a0d9c62f2d5` | 3706 |
| `whitman_wg/WG_FREEZE_SHA256SUMS.txt` (the freeze list = build hash) | `1ad2073fad8dc171a88a10f0ba5fb1bbc8db0e8e600833bcee2d6971563a0773` | 666 |
| `.github/workflows/whitman-wg-sealed.yml` (runs once) | `2da1e7497241eda829e8a4a3575962b60ffd883613aba896f7c3a4f22cd4b00d` | 2959 |
| `whitman_wg/wg_mapping.json` (the ship's own normal ranges) | `57389c787766138d69e987e11afe2babd1085f7fac5dd12b32cc915bff916ce2` | 2504 |

## The test
- **Data:** the public hand-written engine logs of the ship ARC Gloria (Zenodo record 18307281): main engine 2022–2025 and two generators 2021–2025. The files are pinned by MD5 from the census (`de8c19c5…`, `b8619829…`, `69d99369…`). They have **not** been opened by Whitman.
- **What it asks:** these logs record no breakdowns, so this is a test of staying quiet on a healthy ship, not of catching faults.
- **Gates (all three must pass):**
  - WG1: at most 1.0 machine warning per 1,000 running hours, on every engine;
  - WG2: fewer machine warnings than the ship's own normal-range rule raises, on every engine;
  - WG3: no bad reading (typo) ever starts a machine warning.

## Our forecast, published before the run
| Item | Forecast | Our chance it passes |
|---|---|---|
| Machine warnings per 1,000 h, worst engine | 0 – 2 (80% range) | WG1 about 65% |
| Whitman quieter than the ship's rule on every engine | — | WG2 about 85% |
| Typos turned into machine warnings | 0 | WG3 about 90% |
| **All three** | — | **about 50%** |

**What a pass may claim:** only that, on about 4 years of a real ship's hand logs, Whitman stayed quieter than the ship's own limits and no typo became an engine alarm. Nothing about catching faults. A fail is published exactly like a pass.

**Status:** frozen; the one run waits for NJ's go.

*Opus · 15 Oct 2026*
