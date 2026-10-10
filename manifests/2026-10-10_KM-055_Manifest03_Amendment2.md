# Manifest 2026-10-10 (KM-055 #3): Catcher in the Sky, Amendment 2 in force

Prepared on 10 Oct 2026 by Opus. Published on NJ's instruction ("Publish Amendment 2", 10 Oct 2026, 14:06 IST).

The commit time of THIS file in this repository is the time Amendment 2 comes into force. This manifest holds names, numbers and SHA-256 fingerprints only. It stores no data, no code and no secret. The repository the hashes refer to is private.

## 1. What is frozen
Repository `VyroNyx/catcher-in-the-sky`, commit `60e83ee`:

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/KM-055_AMENDMENT_2.md` | `1f5f463bd3a2933235c0a0015d731f14efb441544b99c0f2a348e313fff3944d` | 4,179 |
| `docs/KM-055_AMENDMENT_1.md` (unchanged since manifest #2) | `91bdeb86c61af46b90284e170277d1bd13789f47217f184eca0a635c91bd318b` | 19,266 |
| `docs/KM-055_SPEC_v1.2_FREEZE_CANDIDATE.md` (unchanged since manifest #1) | `4873e2420d2b4a52674f9b1e7dfc1572792ad2d4a57a73e9289e6b9f1dc8d0db` | 34,688 |
| `handoff/validate.py` (unchanged) | `d0f54bdb39da594087b96064d67f73b207f50b474c0aa3eec8ab72cfdf39543d` | 15,858 |

**No sealed scenario exists yet.** The sealed-side code exists, in a separate private repository that the catcher builder never sees. It has made only test fixtures, with seeds below 1000.

## 2. What Amendment 2 does
It clarifies ten lines of v1.2 and Amendment 1 that a generator and a checker could read differently, so that the sealed set never has to be remade. It adds no new rule. The ten lines cover:
- how a heading reversal is measured;
- airspeed as a 3-D measure, with limits for each object;
- "while slowing";
- **g = 9.80665 m/s², with every threshold the exact product**;
- when the net-open time is counted from;
- the planner's earliest release;
- which hand-offs the "nothing in the zone" rule covers;
- whether a crewed aircraft is actually present;
- that state_time is never before 0;
- the time window for held-back events.

## 3. How it was checked
- The ten points were raised by the sealed-side builder, a separate session, from its own code. Opus resolved them, mostly by adopting the builder's stricter reading.
- The builder then made its code match. It reported that all 53 tests pass and that all 54 test fixtures pass every check and the frozen hand-off validator.
- Before publication, Opus recomputed every hash and byte count in this manifest from the commit. No separate Inspector was run, and this is stated openly.

## 4. Next
Step 2 of the spec: the sealed-side session makes the sealed sets for Questions A and B (9 kinds × 50 each), runs the file checks and the reference planner, and publishes salted SHA-256s, before any practice.

*Opus · 10 Oct 2026*
