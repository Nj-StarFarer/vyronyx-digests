# Manifest 2026-10-15 (KM-061 Whitman #12): W3+, CARE to Compare with cause naming — FROZEN before the sealed run

Prepared by Opus, under NJ's delegation of 15 Oct ("You are in charge, Chief"). Files in the private repository `Nj-StarFarer/SkyNet`, at commit `9b18616c` (08:54:51 UTC).

**Build hash** (SHA-256 of the freeze list, 34 files): `0eb3ac87bfce720912c154d632e907d94be028094907adb94354788210a38d78`

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/WHITMAN_W3PLUS_DESIGN.md` (cause design, all six variants reported, gates, forecast) | `14cc34f3ab8dc6d31b11126723b7b160df0c5434a4414b16df8cb5bf6fac2975` | 13113 |
| `whitman_w3/W3_FREEZE_SHA256SUMS.txt` (the freeze list = build hash) | `0eb3ac87bfce720912c154d632e907d94be028094907adb94354788210a38d78` | 3399 |
| `docs/kingmaker/WHITMAN_W3_FORECAST.md` (detection forecast, published 15 Oct, unchanged) | `7a2c388c604410764dd2cdd77c6de2389fbdc33a2cf95c826dde6a8c87988e60` | 2156 |
| `whitman_w3/sealed/cause_w3.py` (which part Whitman blames, without the key) | `a0ce62981f61fb8b9c4eac0c028db3223b9856e04bc7fc9e923860b2b76db0a0` | 4725 |
| `whitman_w3/sealed/score_cause_w3.py` (cause gates) | `7f48d52a8db7e6c7a13461486fb3edcf99cacc15a35c363a950e76a47c495d63` | 6288 |
| `.github/workflows/whitman-w3-sealed.yml` (runs once) | `5d2efa17f79f47e57bae3479d19cf01e92eed02b3a0dd5c9f444db891000e574` | 11950 |

## The test
- **Data:** the 50 SEALED datasets of CARE to Compare (25 fault, 25 normal), split on 13 Oct and never opened by Whitman.
- **Detection gates G1–G6:** unchanged from the earlier freeze (the old build b0ba4139 was never run). Our published forecast stands.
- **Cause gates (new):**
  - C1: at least 50% of named parts right, with at least 3 named;
  - C2: at least 60% of warned faults named right;
  - C3: honest confidence;
  - C5: right more often than the simple "most-moved gauge" rule (p < 0.05).
  - The truth is each fault's written description, mapped to a part by keyword rules that were frozen before. The descriptions are read only after all 250 output files are committed.

## Our forecast, published before the run
| Gate | Chance it passes |
|---|---|
| C1 named calls right | about 40% |
| C2 warned faults named right | about 5% |
| C3 honest confidence | about 20% |
| C5 beats the simple rule | about 5% |
| **All four** | **about 1%** |

**Why so low, said plainly:** on the open faults, Whitman named a part only 4 times in 15 (3 right). The simple rule was right 4 times but wrong 9 times. Whitman is careful but rarely speaks. A fail is expected and will be published exactly like a pass.

*Opus · 15 Oct 2026*
