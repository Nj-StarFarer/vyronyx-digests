# Manifest 2026-10-10 (KM-055 #2): Catcher in the Sky, Amendment 1 in force

Prepared on 10 Oct 2026 by Opus. Published on NJ's instruction ("Publish Amendment 1", 10 Oct 2026, 11:48 IST).

The commit time of THIS file in this repository is the time Amendment 1 comes into force. This manifest holds names, numbers and SHA-256 fingerprints only. It stores no data, no code and no secret. The repository the hashes refer to is private.

## 1. What is frozen
Repository `VyroNyx/catcher-in-the-sky`, commit `35c0611`:

| File | SHA-256 |
|---|---|
| `docs/KM-055_AMENDMENT_1.md` (19,266 bytes) | `91bdeb86c61af46b90284e170277d1bd13789f47217f184eca0a635c91bd318b` |
| `docs/KM-055_SPEC_v1.2_FREEZE_CANDIDATE.md` (unchanged since manifest KM-055 #1) | `4873e2420d2b4a52674f9b1e7dfc1572792ad2d4a57a73e9289e6b9f1dc8d0db` |
| `handoff/validate.py` (unchanged) | `d0f54bdb39da594087b96064d67f73b207f50b474c0aa3eec8ab72cfdf39543d` |

**No sealed scenario, secret kind or reference planner exists yet.** An amendment is allowed only before sealed data exists.

## 2. What Amendment 1 changes
- **Question B added:** fast FPV-type drones on fixed, erratic routes into a protected zone.
  - Targets fly up to 39 m/s, with a 60° tilt (cited from DJI FPV).
  - The catcher has an "interceptor profile" of 45 m/s and 25 m/s², a margin of only 1.15× in airspeed.
  - The catcher plays goalkeeper, holding a net in the target's path.
  - Question B has its own sealed set (9 kinds × 50), its own label and its own claim wording.
- **Question A** (v1.2, micro camera drones) is unchanged except for Part R.
- **Part R, no target reacts to the catcher, in either question.** The secret kinds (K9 and BK9) become pre-scripted, fast, erratic routes. Each must meet fixed hardness rules:
  - at least one hard manoeuvre every 10 s;
  - sharp turns of 60° or more in at least half of the 6-s windows;
  - at least half the flight at 60% of top speed or more.

  **Reason:** a target that watches the catcher and steers around it to reach a point would amount to evasion guidance for an attack drone. VyroNyx will not build it.
- **Part S, self-protection:** the catcher may avoid objects, keep its distance and retreat. It never manoeuvres against another aircraft. This is not tested in this sealed run.
- **Part T, the trouble-finder:** an automatic search for pre-scripted routes the frozen catcher struggles with. It is a separate test after the sealed run, pre-registered on its own, and never part of KM-055's labels.

## 3. Expected 99% zone sizes for Question B (from `handoff/validate.py`, q = 46 / 46 / 10)
Half-widths in metres (along range / across range / vertical), for a hand-off with the spec's §6 errors, moved forward by Δt:

| Range from pad | Δt 0.5 s | Δt 1.5 s | Δt 4 s | Δt 7 s (cap) |
|---|---|---|---|---|
| 200 m | 11 / 13 / 25 | 27 / 27 / 28 | 107 / 107 / 57 | 246 / 246 / 119 |
| 400 m | 11 / 24 / 37 | 27 / 34 / 39 | 107 / 109 / 63 | 246 / 247 / 122 |
| 650 m | 11 / 39 / 52 | 27 / 46 / 53 | 107 / 113 / 73 | 246 / 248 / 127 |
| 900 m | 11 / 53 / 66 | 27 / 58 / 68 | 107 / 119 / 84 | 246 / 251 / 134 |

## 4. How it was reviewed
- An independent reviewer checked versions 0.1 to 0.4. Its findings were 5, 2 and 3 blockers, plus should-fix and minor items, all applied.
- The fourth review was stopped by NJ, so Opus checked v0.5 against the reviewer's last findings.
- Before publication, Opus checked every hash and table cell in this manifest by script. No separate Inspector was run, and this is stated openly.

## 5. Cited source
- DJI FPV specifications and FAQ: https://www.dji.com/support/product/dji-fpv. It was read on 10 Oct 2026 and gives: M mode 39 m/s; 60° maximum tilt; 0–100 km/h in 2 s; about 795 g; S mode climb 15 m/s and descent 10 m/s.

*Opus · VyroNyx Private Limited · 10 Oct 2026*
