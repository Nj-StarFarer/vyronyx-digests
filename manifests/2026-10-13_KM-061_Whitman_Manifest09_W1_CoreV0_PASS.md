# Manifest 2026-10-13 (KM-061 #9): Whitman on SkyNet Core v0, objective W1 (stage 0, integrity): PASS

- **Prepared:** 13 Oct 2026 by Opus.
- **What changed:** after NJ's instruction "Find an alternative. Also just like Angel Eyes, build Whitman as per KingMaker", Whitman was moved onto SkyNet Core v0, the same core as Angel Eyes. It gets Leviathan as memory and judge, and CAL as explainer.
- **The plan:** a ladder of objectives W1–W8, each with its spec frozen before its code.
- **Fresh real-fault data for detection (W3):** CARE to Compare (Zenodo 15846963, CC BY-SA 4.0). These are wind-turbine recordings with 44–45 real recorded fault events, never opened by VyroNyx.

## Documents fingerprinted (all in the private repository `Nj-StarFarer/SkyNet`)

| Document | Commit | SHA-256 |
|---|---|---|
| `docs/kingmaker/WHITMAN_CORE_DESIGN_NOTE.md` (design, frozen) | `e197bd4` | `df7435f11e9cc5b534aa6134b289083f9418216dd3e361c1d58feb34c2ac097e` |
| `docs/kingmaker/WHITMAN_W3_DATA_CHOICE.md` (decided before any W3 download) | `e197bd4` | `44e36205662f4e8f4dd3fb20af5461f138ade62bf8c399534eb919ba9dce63ee` |
| `docs/kingmaker/WHITMAN_W1_SPEC.md` (spec frozen in `e197bd4`, before code; RESULT section added after the run) | `36b7281` | `34f9e192086c31810a19f8cf77192a692d099fdb7223c83cdb5b0403ad2ad200` |

## W1 result: PASS

- **Run:** GitHub Actions run `38404071482` (one attempt).
- **Code:** commit `0654e71`, written after the spec.
- **Results:** committed by the run in `1847886`.

| # | Check | Measured |
|---|---|---|
| V | Copied Whitman files equal the Rung 1b freeze list (build `474e37e6…`, Manifest #7) | 31 of 31 |
| R1 | Sealed ship inputs re-made from the public ARC Gloria zip and the committed seed | all hashes equal |
| R2 | Whitman's raw decision files, run directly and through the core | 18 of 18 byte-identical to the published run (Manifest #8) |
| R3 | Evidence trail | verifies; a planted edit and a planted deletion are both caught at the right line; two replays end on the same final hash |
| R4 | Placebo trail (evidence swapped between machines) | rejected |
| R5 | One evidence item per alert episode, each resting on its own input | no problems |

**Earned:** stage 0 (integrity) for the Whitman reader on Core v0.

**Not earned:** no detection claim. Rung 1b stays FAIL (Manifest #8). Detection is objective W3.

## Hashes of the result files (`skynet_core/results/w1_38404071482/`)

| File | SHA-256 |
|---|---|
| `W1_RESULT.json` | `7e188fc4151ad5b2ce7115ecb0591ab070b48e2f68e05c1b6b2e61434756366d` |
| `w1_ledger.jsonl` (final chain hash `fc5a7149a86dbf90a643a5e61be001ee0540c86a4beb441a1d01d51850de3d6e`) | `98619c93e40bade61b0464fbd5b5e2aa8eddb54b45896efe45d86342d70950af` |
| code `skynet_core/w1_replay.py` | `951c46ddceb92c58227ec900f66b33eac679da866d37dbe305365ca54e7a014d` |
| code `skynet_core/whitman.py` | `cbacfc840b4e9524dd5411cbed6315f45bc0eb0556e51c9a2d6b048e99647d50` |
| code `skynet_core/readers/whitman_machine.py` | `d088047435e2780d78b1adb96ce1db507b71a75b4c79aa85e6ededf78f8d566d` |

## What follows

W3 step 1: a structure-only census of CARE to Compare. It reads no sensor values and no event times or text. The W3 spec is frozen next, before any sealed dataset is opened.

*Opus · VyroNyx Private Limited · 13 Oct 2026*
