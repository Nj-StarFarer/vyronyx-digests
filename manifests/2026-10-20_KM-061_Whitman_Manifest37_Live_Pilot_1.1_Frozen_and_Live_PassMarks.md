# Manifest 2026-10-20 (KM-061 Whitman #37): Whitman Live, pilot build 1.1, frozen; live-pilot pass marks, before any vessel

Prepared by Opus, 20 Oct 2026. Numbers and SHA-256 fingerprints only; the repository `Nj-StarFarer/SkyNet` is private.

## Why a live build

NJ, 20 Oct: the pilot must be the real thing, with Whitman connected to the ship and working by itself, not "send us data and we tell you what is wrong".

Whitman Live:
- **receives** signed hourly packets from the read-only ship collector;
- **judges** every machine every hour (the last 24 hours) and every complete day;
- **seals** every statement;
- **alerts** the chief engineer and Maritronix at once;
- **watches** the ship's link;
- **keeps** a live screen.

The crew answers every alert with what it found, and a person who is not from VyroNyx confirms each finding.

## The frozen build (commit `4dca93b`, tag `whitman-pilot-1.1-live`)

Before freezing, the build went through an independent attack review (round seven, 14 findings, all fixed).

| Item | SHA-256 |
|---|---|
| `whitman-pilot-1.1-live/SHA256SUMS` (the build's one fingerprint) | `a8462b0c34a06e03f58ca61858c92ddee4e62abb19cdbfa2c511e5807932ed72` |
| `whitman-pilot-1.1-live.tar.gz` | `05278467d95a3a96e68619fe9b7353a294c6dd054c5adea7f6528417e0a39ff6` |
| `whitman_live/live.py` | `4d1baa3442c05bb8871989670b34e0289ec57f346b0b04c4b25c8bd3f581ea29` |
| `whitman_live/live_score.py` (the live scorer) | `4ea7213a6be4fe34f5ff654b3ec79aceb85c10046d67535a9312d9ca5262d51a` |
| `whitman_edge/sig_watch.py` (with the live window) | `fa98d8283c5121ab3e999db6116cfcd1e39d639afdcff5fd69b03f22e4777e72` |

## Live-pilot pass marks (FROZEN): `docs/kingmaker/WHITMAN_LIVE_PILOT_CRITERIA.md`

SHA-256 `b0b1622c48ff438024d4fcc13eedafedaa1c1ee7a6101f4bc9d1ae79ec835c0f` (commit `4dca93b`).

| Measure | GREEN | AMBER | RED |
|---|---|---|---|
| Caught first (confirmed faults alerted about before the crew knew, out of all confirmed faults) | ≥ 50% | 30–50% | < 30% |
| Warnings right (answered alerts that found a real fault in the subsystem pointed at) | ≥ 50% | 30–50% | < 30% |
| False alarms (alerts answered "nothing found"), per vessel per month | ≤ 1 | 1–3 | > 3 |
| Right subsystem | ≥ 60% | 40–60% | < 40% |
| Wrong firm name | ≤ 5% | 5–15% | > 15% |
| Alerts within 2 hours of the newest data behind them | ≥ 95% | 80–95% | < 80% |
| Data coverage | ≥ 95% | 85–95% | < 85% |
| Evidence complete | 100% | ≥ 95% | < 95% |

**Verdict rules:**
- **GREEN:** no RED row and at most one AMBER row.
- **RED:** any RED in caught first, false alarms, wrong firm name or evidence.
- **AMBER:** anything else.
- **Minimum:** at least 8 confirmed faults, each fault counted once. The watch runs at least 90 days after learning and at most 12 months; with fewer faults the result is "too few events to score".

The silent-pilot marks of Manifest #13 (with the clarifications in #36) stay valid for a silent pilot.

*Opus · VyroNyx Private Limited · 20 Oct 2026*
