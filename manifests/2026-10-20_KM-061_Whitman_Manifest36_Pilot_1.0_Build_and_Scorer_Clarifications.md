# Manifest 2026-10-20 (KM-061 Whitman #36): pilot build 1.0 frozen; scorer clarifications to the first-vessel pass marks

Prepared by Opus, 20 Oct 2026, before any vessel is chosen. Numbers and SHA-256 fingerprints only; the repository `Nj-StarFarer/SkyNet` is private.

## 1. Pilot build 1.0 (frozen, commit `84600de`)

| Item | SHA-256 |
|---|---|
| `whitman-pilot-1.0/SHA256SUMS` (list of every file in the pilot bundle) | `15d175bb58ad595da12097605616a2bf8f983e32ba03ecc765b87a76202df7cc` |
| `whitman-pilot-1.0.tar.gz` (the bundle) | `f5d2ef1dc3b9c8e973667d60771c758a422a2a73f1af6ba665fef032523a43c3` |
| `whitman_diary/pilot_score.py` (the pilot scorer) | `03b43e3451e067cd0ce086ca248508b01939f67dde6c2feeee2a206d9b6dc28d` |
| `whitman-collector-1.0.tar.gz` (the read-only ship collector) | `f7aa2dd558c11dfa2c98ecab9c886377eb1a8fcf906558a123385c59d46a4dd6` |

At commissioning, the build is sealed as the first line of the pilot diary and its fingerprint is published here.

## 2. First-vessel pass marks: clarifications, all stricter

The pass and fail numbers of Manifest #13 (15 Oct 2026, file SHA-256 `85d10247…eae6d`) are **unchanged**. A section "Scorer clarifications before the first pilot" was added to the same file:

1. **Sure-wrong.** Every wrong NAMED call counts as sure-wrong, because Whitman states no probability.
2. **Endless warnings.** A warning that never stops opens a new episode every 30 days.
3. **Order of sealing.** A warning counts only if it was sealed before the outcome record.
4. **Outcome time.** An outcome is never dated later than its sealing, and future dates are refused.
5. **Kept as frozen:** a true warning more than 30 days early still counts as a false alarm, and detection stays at machine level.
6. **Calibration row.** It cannot be computed because Whitman states no probabilities. It is reported as "not measurable" and never used in the verdict, as the frozen rule already allowed.

| File | Commit | SHA-256 |
|---|---|---|
| `docs/kingmaker/WHITMAN_FIRST_VESSEL_CRITERIA.md` (with clarifications) | `05a868ba` | `254e68806239e133d1d64542ed2ef5a1efa0cc809fbc8128127ecfbc7fc5c1d9` |

*Opus · VyroNyx Private Limited · 20 Oct 2026*
