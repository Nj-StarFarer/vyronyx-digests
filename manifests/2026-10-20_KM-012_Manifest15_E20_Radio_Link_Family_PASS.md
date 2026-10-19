# Manifest 2026-10-20 (KM-012 #15): E20, name the DJI link family or say it is new — real radio data. PASS

Prepared by Opus (Claude Opus 5.5) for VyroNyx. Files in the private repository `Nj-StarFarer/SkyNet`, at commit
`a716b13e`. **The freeze was a private commit** (`a203801c`, 19 Oct 2026 17:59 UTC, pushed before the run); this
manifest is its first public record.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/E20_SPEC.md` (frozen spec; unchanged since `a203801c`) | `a31d12d2987a35e17fadc91f9bf31da5268e5bb527575a93699ea3021e8fcefd` | 6447 |
| `angel_eyes/air_e20/e20_sealed.py` (sealed run) | `5c55fb6b03bf191953666480a4d8f6e807468a250e846d8c1c1977ba2189ab86` | 9970 |
| `angel_eyes/air_e20/e20_core.py` (answers, rivals, loss) | `27fea261a1ad05c32bb3797174dcb99fd74946fd96012eb35e4d278f48da8036` | 5460 |
| `angel_eyes/data/e20/e20_result.json` | `d2046b59c60396502ec7d73b487e7ccddd9e9d6ed1c00e7091301aae7c78c9ec` | 8714 |
| `angel_eyes/data/e20/e20_sealed_capture_sha256.json` (one hash per sealed capture) | `03bc9935f975353bf2fb94d8e31a82d73ed645e32104d42a7d34f8e59d109e70` | 361802 |
| `docs/kingmaker/E20_RESULT.md` | `e00ffb0914bf41bf1815942b8f36a1bac22d52e5872c7d87111eecec0f5003b8` | 3603 |

## The test
- **Data:** TSMS-Drone radio half (Jung & Han 2026, Figshare+ doi:10.25452/figshare.plus.30027313.v1, CC BY 4.0).
  Four DJI drones hovering at 1.5 m, and a corner reflector with no radio on board, one site, 2.4 GHz.
- **Sealed:** sessions at 2, 6, 8, 14, 28 and 30 m, never opened before; captures 001–100 of every target = 3,000.
- **Question:** from one 2.2 ms capture, name the DJI link family (OcuSync-type: Mavic 2 Pro and Phantom 4 Pro;
  Lightbridge 2: Inspire 2; O3: Matrice 30), or say "a transmitter, not a known DJI link family". Four conditions:
  all families known, and each family hidden in turn. Two rivals on the same features: closed-set and open-set.
  Loss: a confident wrong answer costs 10, a refusal of a known family 1.

| Measure (pooled) | Result | Bar |
|---|---|---|
| Mean loss: Angel Eyes / open-set rival / closed-set rival | 0.498 / 0.620 / 3.059 | Angel Eyes lowest |
| Stranger's transmitter named a DJI family | 0 of 480 | ≤ 1% |
| Hidden family refused | 99.2% (2,365 of 2,383) | ≥ 80% |
| Known family named wrong | 2.3% (167 of 7,149) | ≤ 5% |
| Known family named right | 53.8% (3,847 of 7,149) | ≥ 50% |

**PASS.** 3,000 of 3,000 captures decoded; no stop. Placebo (truth shuffled): loss 2.906.

**Stated beside the pass:** when nothing is hidden, the open-set rival scores better (0.307 vs 0.753); Angel Eyes'
overall win comes from never naming the stranger and refusing an unseen link family. It refuses 44% of known-family
captures. Lab data only: hovering drones, one site, four DJI models; Mavic 2 Pro and Phantom 4 Pro are not told apart;
the family grouping came from development; a file-batch effect is not ruled out.

*Opus · 20 Oct 2026*
