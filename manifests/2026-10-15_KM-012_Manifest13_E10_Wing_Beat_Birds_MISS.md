# Manifest 2026-10-15 (KM-012 #13): E10, birds named by wing-beat physics with no bird labels. MISS

Prepared by Opus, under NJ's standing delegation. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `87d80fce`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/E10_SPEC.md` (frozen spec and the result) | `8ddcd79a12cb612aed18c99b28a649f75837bb987d459ae6851aba97a93bb1f1` | 7503 |
| `angel_eyes/air_e10/sealed_38687415654/result.json` | `99d7c0ccc4f568981e3c7e2d343de1ed1ef135ec8550835c7f5c463f8962ea0e` | 1044 |
| `angel_eyes/air_e10/sealed_38687415654/predictions.json` | `88775ae097516644b9ae7c115d72f8bfc27a4fc808133899c66b012162e3e1b1` | 98233 |
| `angel_eyes/air_e10/sealed_38687415654/key.json` | `f12f1cd30729aa7d80589bb5079abe6332a1984ad95a02227a78ba1874ecc8d2` | 65075 |
| `angel_eyes/air_e10/sealed_38687415654/split.json` | `9196466c1ef026a10482f9d61815877bebc15505a4bb369a0b7a53ce429ed465` | 5933 |

- **Test:** Halmstad drone/bird/aircraft/helicopter video (CC0), visible and infrared: with no bird example or label,
  measure a wing beat from the target's size flicker and explain the object as a flapping-wing flier — never putting
  wings on a drone, aeroplane or helicopter. Rival: a classifier trained on the labels. Run `38687415654`; 372 sealed
  clips (71 bird).
- **MISS:** wings on 7% of bird clips (bar 35%; rival 51%); wings on 8% of non-bird clips (bar 5%).
- **Held:** the order-shuffled placebo produced no wing beat on any bird clip.
- **Diagnosis:** non-bird clips flicker in size too (the infrared gate from development non-birds came out at 68.9);
  on small, far targets a size flicker is not specific to wings.

*Opus · 15 Oct 2026*
