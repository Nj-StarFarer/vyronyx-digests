# Manifest 2026-10-21 (KM-012 #20): CORRECTION — E22 was not a valid sealed test

Prepared by Opus (Claude Opus 5.5) for VyroNyx. Corrects manifests #18 and #19.

| File | SHA-256 | Commit |
|---|---|---|
| `docs/kingmaker/E22_NOTES.md` (note N1) | `3311164be254a807af4ba40dc62fda3498ec1ccdc515badefe080fa03ef0448f` | `64e9fbfa` |

- The KTH 77 GHz radar dataset used by E22 had **already been used** by an earlier Angel Eyes test (AIR v2 Arm A,
  sealed run opened 1 Oct 2026), which trained on it and tested every drone model, including the FPV drone, as the
  never-seen model. Our own data registry marked it development-only. E22 was chosen without checking that registry.
- **E22 is therefore development evidence only, not a sealed result.** Its MISS stays recorded as published; its
  passes (separation 0.981; FPV drone called "drone" 97.9%) must not be cited as sealed results.
- New rule: every sealed test now checks its dataset against the data registry, in writing, before freezing.

*Opus · 21 Oct 2026*
