# Manifest 2026-10-20 (KM-012 #16): E21 — radio predicts radar. Spec frozen and predictions committed before the radar was read

Prepared by Opus (Claude Opus 5.5) for VyroNyx. Files in the private repository `Nj-StarFarer/SkyNet`.

| File | SHA-256 | Bytes | Commit |
|---|---|---|---|
| `docs/kingmaker/E21_SPEC.md` (frozen spec) | `cce22810f27e726d37cb9cc12a8f1cb7e8c1027f564e388997f05d8a12a6ebe2` | 5442 | `06e044d6`, 20 Oct 2026 07:00:32 UTC |
| `angel_eyes/air_e21/e21_sealed.py` | `03b79232b90720c7a6e7c62e6170036f1bf689dd2eb8d0bd6c0c0e927b37cd65` | 9875 | same |
| `angel_eyes/air_e21/e21_radar_feat.py` | `108f5c9d6228f33f1da21a1447c308e5d8da711114a5484e9442cc8ca8a2f7b5` | 2253 | same |
| `angel_eyes/data/e21/predictions.json` (450 predictions from radio only; inner sha256 of the list `4919f459…aaa7`) | `9cda686c2351ff14f6edd15c7e55a63f2b00a316cb8ecb1542868205d0647868` | 67976 | `5deccae9`, 07:13:35 UTC |
| `docs/kingmaker/E21_NOTES.md` (note N1: a count corrected after the freeze; nothing in the test changed) | `126fa691c271a7c4e66ddc015caf89e94ea845e706487209094bd1b2d241348b` | 649 | `f91c97df` |

- **Question:** from one radio capture alone, write down whether the radar must show spinning-blade smear for the same
  object at the same moment (TSMS-Drone, CC BY 4.0), then open the radar. 450 sealed pairs: 4 DJI drones and a corner
  reflector, distances 2, 6, 8, 14, 28, 30 m, file numbers 001–015.
- **Pass marks:** Angel Eyes' loss below two rivals'; its rotor predictions confirmed by radar ≥ 95%; a prediction on ≥ 40%
  of drone pairs; none on the corner reflector. Referee check, else VOID: radar reads rotors on ≥ 90% of drone maps and
  ≤ 5% of corner maps.
- **Stated in the spec:** the radio side was already run in E20; the radar is the new, unopened evidence.
- The radar reveal started at 07:14 UTC, after both commits above. The result will be published whatever it is.

*Opus · 20 Oct 2026*
