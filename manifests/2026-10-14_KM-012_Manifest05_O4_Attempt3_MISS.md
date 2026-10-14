# Manifest 2026-10-14 (KM-012 #5): O4 attempt 3, camera persistence on fresh sealed AOT flights. MISS

Prepared by Opus during the day run, under NJ's standing delegation. File in the private repository `Nj-StarFarer/SkyNet`, at commit `4b532e78`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/O4C_SPEC.md` (frozen spec, note N1 and the result) | `282ce04b795dc3e3351a73ec3d4037cd92de1e1de11491ce215f9797c0c6854a` | 5,411 |

## The test (ladder stage 2, third attempt)
- **What changed after the attempt-2 VOID:** a new placebo (another flight's blips, so still objects cannot line up by chance) and 10 blips per frame. The bars were unchanged.
- **Data:** 32 fresh flights (new salt), 16 minutes of video, 40 sky objects.
- **Run:** `38514292075`, on NJ's Mac.
  - The key hash was committed first.
  - The predictions were committed before the key was opened.
  - 0 frames failed.

| | Recall | False objects per hour |
|---|---|---|
| Angel Eyes | 0.45 | 6,315 |
| Same detector, every blip | 0.65 | 80,621 |
| Old threshold, every blip (B4) | 0.65 | 23,186 |
| Placebo (another flight's blips) | 0.075 | 6,454 |

- **Passed:** false objects cut 12.8-fold (lower bound 9.0); recall floor met (0.45); false-object rate under 10,000 per hour; placebo not void.
- **Failed:** recall kept (−0.20, bar −0.15) and matching B4 (−0.20, bar −0.10).
- **Verdict: MISS.** The test was valid. No stage is claimed.

## What it teaches
The eye saw the objects; the promotion rule dropped 8 of them. The next attempt must keep more objects without letting false ones back in.

*Opus · 14 Oct 2026*
