# Manifest 2026-10-20 (KM-012 #17): E21 outcome — VOID. The radar referee failed its own check, so there is no verdict

Prepared by Opus (Claude Opus 5.5) for VyroNyx. Files in the private repository `Nj-StarFarer/SkyNet`. Follows manifest #16
(spec frozen and 450 predictions committed before any sealed radar map was read).

| File | SHA-256 | Bytes | Commit |
|---|---|---|---|
| `angel_eyes/data/e21/radar_features.json` (450 sealed radar maps read, 0 errors) | `73be36220c1ebb6fa784f2ed2a27e2334204ea8a37d5752b19ac82f524a71d16` | 140136 | reveal runs, last 20 Oct ~17:35 UTC |
| `docs/kingmaker/E21_NOTES.md` (N1 count correction; N2 scorer bar set to the frozen spec's 40%, before scoring) | `6b35a48e23c503ba7f7de4ae6b7087636932cedf20c607ad1b39bddc5e980124` | 1200 | `f2fcf8d1` |
| `angel_eyes/air_e21/e21_sealed.py` (as scored) | `01e7f6445d5f844a0d3f57caf80cd2d9662693a3309aba29971fdbf2454e31ce` | 9875 | `f2fcf8d1` |
| `angel_eyes/data/e21/e21_result.json` | `a056c2c38438bda2de69d62fee3f2f66fba00f7db125e0c05baffe4cafba2d74` | 664 | `a262213f` (score run 39467995403) |
| `docs/kingmaker/E21_RESULT.md` | `489054e3858f9db5f518056af7c16685f6a681fff795a6c54c8d72c06b7e2c9a` | 2730 | `c4ddd595` |

- **Outcome: VOID_REFEREE.** The frozen referee check needed the radar to read "rotors" on ≤ 5% of corner-reflector maps.
  It read rotors on **6 of 90 (6.7%)**, at 6 m and 8 m. Drone maps: 360 of 360. By the frozen rules, no pass or miss
  is declared, and these sessions are not re-run.
- **Descriptive only:** Angel Eyes made 184 rotor predictions from radio alone; **all 184 were confirmed** by the radar
  and **none were on the corner reflector**; it spoke on 51% of drone pairs. Mean loss: Angel Eyes 0.404, rival
  "strong transmitter means rotors" 0.329, rival "always rotors" 1.867. So even with a clean referee, the first pass mark
  (loss below both rivals) **would have failed**.
- **Correction disclosed:** before scoring, the scorer's coverage bar (0.50) was found to differ from the frozen spec
  (40%) and was set to the spec (note N2). Coverage was 0.51, so it did not change anything.
- **Lessons:** a referee needs clear margin from its limit before freezing (development showed 3.3% against a 5% limit);
  the loss must be set from how often strangers occur in real use, stated before the run.

*Opus · 20 Oct 2026*
