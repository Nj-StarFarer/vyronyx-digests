# Manifest 2026-10-15 (KM-012 #11): E9, predict-then-reveal on radio hop sequences. INCONCLUSIVE

Prepared by Opus, under NJ's standing delegation. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `c2f306f9`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/E9_SPEC.md` (frozen spec and the result) | `9eec33b2e16d9f841d5a9b91189524eb4fce91dfb3feae9e922c18584ec7a3bc` | 6027 |
| `angel_eyes/air_e9/sealed_38685474350/result.json` | `7c1b2f6299c5698c910b956af87f4ddc55693f1edce5bdf6234f52dd4848c4f0` | 4018 |
| `angel_eyes/air_e9/sealed_38685474350/predictions.json` | `4a225e45fac54986b2803dc2aebe45c041c35b04c81b1e6cb97e33989f329b6f` | 9807 |

- **Test:** for each of 12 drone radio recordings (Tampere, CC BY 4.0), explain how the link hops from the first half
  second only, then predict each next burst of the second half before it is revealed; rivals: histogram and Markov.
  Spec frozen at `d5ae20fb` before any recording was opened; run `38685474350`.
- **INCONCLUSIVE:** only 3 recordings showed a hop structure; the frozen rule needs 4.
- **Phantom 4 Pro Plus:** a repeating cycle of 22 bursts found; predicted 0.667 of sealed bursts vs 0.514 for both
  rivals; 0.636 stated beforehand.
- **Missed:** Parrot Mambo control — called "steady", but a Markov learner found order (0.49 vs 0.19).

*Opus · 15 Oct 2026*
