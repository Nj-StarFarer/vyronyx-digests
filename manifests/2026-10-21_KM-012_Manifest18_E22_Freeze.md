# Manifest 2026-10-21 (KM-012 #18): E22 — radar names a drone and a never-seen FPV drone. Spec frozen before the sealed side was read

Prepared by Opus (Claude Opus 5.5) for VyroNyx. Files in the private repository `Nj-StarFarer/SkyNet`.

| File | SHA-256 | Commit |
|---|---|---|
| `angel_eyes/data/kth77/e22_split.json` (sealed split, fixed from labels and sizes only, before any radar signal was read) | `1bb063113c693186dada9f569207e7464b847ef8982ddfa8e9d284a4948917f6` | `10d5f7dd` |
| `angel_eyes/data/kth77/e22_dev_feat.npz` (development features) | `b76aa3c77be0c0483a382b82ac781f3309a0255600a2e4d5b12bff97e66c3f9d` | development runs |
| `docs/kingmaker/E22_SPEC.md` (frozen spec) | `ac9ba5af2d23c01fa846e1ba2c0db0fbe9775fcd19e94136df62bef6c1eceadb` | `b676a1c5`, 21 Oct 2026 10:53:12 UTC |
| `angel_eyes/air_e22/e22_sealed.py` (scorer, thresholds fixed) | `079400290db55d67ce6abff28fae9bd021c76d3481aafa5937ea47cff04973f8` | `b676a1c5` |

- **Data:** KTH 77 GHz FMCW radar, drones, birds and people (Karlsson, Zenodo doi:10.5281/zenodo.5896641, CC BY 4.0).
  Whole measurements split into development and sealed halves; drone model D4 (a custom FPV drone) is entirely sealed
  as the never-seen model.
- **Pass marks (all four):** AUROC ≥ 0.95; known-drone recall ≥ 0.90 with non-drone false alarms ≤ 10% at the frozen
  threshold; the never-seen FPV drone called "drone" ≥ 80%; balanced accuracy above two rivals with a bootstrap lower
  bound > 0.
- **Forecast before the run:** PASS about 35%.
- One run; the result will be published whatever it is.

*Opus · 21 Oct 2026*
