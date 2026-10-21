# Manifest 2026-10-21 (KM-012 #19): E22 outcome — MISS (3 of 4 pass marks)

Prepared by Opus (Claude Opus 5.5) for VyroNyx. Follows manifest #18 (freeze). Files in the private repository
`Nj-StarFarer/SkyNet`.

| File | SHA-256 | Commit |
|---|---|---|
| `angel_eyes/data/kth77/e22_sealed_feat.npz` (65 sealed measurements, 43,782 segments) | `10cad7251a36da5f8cef7930704f3efff4db880f7ef09c1eda407097af278bc2` | `d0dd2ea7` (run 39587904030) |
| `angel_eyes/data/kth77/e22_result.json` | `b3932d3e4340c383065ce57a7e5363f6e92e66a5af159b2f9b543ab37a1b4510` | `d0dd2ea7` |
| `docs/kingmaker/E22_RESULT.md` | `02741eb517533e0215f7c8accfe57c0abdb724b5d73f3fe2c6f9c54c8ac40b74` | `291bf655` |

- **Outcome: MISS.** Passed: AUROC 0.981 (bar 0.95); known-drone recall 0.918 with 2.4% non-drone false alarms
  (bars 0.90 / 10%); a never-seen FPV drone called "drone" on 97.9% of tracks (bar 80%). Failed: beating both rivals —
  it beat the nearest-centroid rival, but not a plain model on the raw spectrum (balanced accuracy 0.955 vs 0.934,
  bootstrap lower bound −0.029; that rival's AUROC 0.987 was slightly higher).
- **Weak spot disclosed:** the DJI Matrice 200 was called a drone on only 41% of sealed tracks.
- One run; not re-run. Data: KTH 77 GHz radar (Karlsson, Zenodo doi:10.5281/zenodo.5896641, CC BY 4.0).

*Opus · 21 Oct 2026*
