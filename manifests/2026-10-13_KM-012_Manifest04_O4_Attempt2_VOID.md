# Manifest 2026-10-13/14 (KM-012 #4): O4 attempt 2, camera persistence on fresh sealed AOT flights. VOID

Prepared during the night run by Opus, under NJ's standing delegation. File in the private repository `Nj-StarFarer/SkyNet`, at commit `ba76d56e`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/O4B_SPEC.md` (frozen spec, note N1 and the result) | `30165c5f9c828347b3f399e553429b819eff459e931ce43ebf617765ca4ac895` | 6,390 |

## The test (ladder stage 2, second attempt)
- **What changed after the attempt-1 MISS:** a more sensitive detector and a wider tracker gate, with the same promotion rule. There was one new bar: Angel Eyes must match "every blip is an object" at the old threshold (B4).
- **Data:** 32 fresh flights (new salt), 16 minutes of video, 50 sky objects.
- **Run:** `38435657791`.
  - The key hash was committed first.
  - The predictions were committed before the key was opened.
  - 0 frames failed.

| | Recall | False objects per hour |
|---|---|---|
| Angel Eyes | 0.56 | 11,024 |
| Same detector, every blip | 0.66 | 138,603 |
| Old threshold, every blip (B4) | 0.60 | 29,562 |
| Placebo (frames shuffled) | 0.34 | 3,673 |

- **Passed:**
  - ratio 12.6 (lower bound 9.4);
  - recall loss 0.10 (lower bound −0.18);
  - floor met;
  - B4 matched (−0.04) with fewer false objects.
- **Failed:** the frozen false-object rate (11,024 against 10,000).
- **Void:** the placebo found 0.34 of the objects, which is more than half of Angel Eyes' 0.56.
- **Verdict: VOID.** No stage is claimed.

## What it teaches
Many objects barely move in the image, so shuffled frames still line up. The placebo must be redesigned for near-still objects.

*Opus · 14 Oct 2026*
