# Manifest 2026-10-15 (KM-012 #8): E12 / E13, keeping identity straight in crowded skies (simulated). E12 MISS; E13 PASS

Prepared by Opus, under NJ's standing delegation. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `ab34b0bd`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/E12_E13_SPEC.md` (frozen spec, note E12-N1, and the result) | `adc241856d089a4367dceaf68c01108bd88b8ef251e1b1423d354506c59e3082` | 7272 |
| `angel_eyes/identity/sealed_e12_e13/result.json` | `fc95101164bf1883a13127ea0a0da915b9d0fddd8f58deb25a8bca7b5909d06a` | 5923 |
| `angel_eyes/identity/sealed_e12_e13/seeds.json` (sealed scene seeds; hash committed before the run) | `e9478db149d9955f8d536b61080660cd3664cd3b7f9ca7703d977f01c330d26f` | 699 |

## The test
- **Simulated scenes** with exact truth (crossings, gaps, clutter, identical twins): crowds of 10, 100 and 1,000 objects
  (E12) and 40 scenes of 30 objects with one object pointed out once (E13; half with a decoy twin and a
  land-and-relaunch twin). Not real sensors, not real flight.
- **Angel Eyes' identity ledger** keeps possible swaps open with odds, corrects them only with evidence (fingerprints
  rule out, never confirm against an unheard twin), and logs every change in a hash-chained record. Odds pass through
  a calibration map fitted on development scenes only.
- **Rivals:** a standard tracker (every claim certain), the same with re-linking, and the same stating its own
  development accuracy as its confidence.
- **Score:** sure-and-right minus ten times sure-and-wrong per claim; calibration error; real time at 1,000.
- Spec frozen at `fe8d6d5b` (07:19:48 UTC); seeds drawn at 07:18:23 UTC, values never displayed, only their hash
  committed (note E12-N1).

| Crowd | Sure-wrong: Angel Eyes / standard | Identity right | Calibration error | Verdict per size |
|---|---|---|---|---|
| 10 | 2.3% / 26.8% | 0.824 / 0.733 | 0.129 | MISS (utility lower bound −0.09; calibration over 0.10) |
| 100 | 2.7% / 30.8% | 0.725 / 0.693 | 0.047 | MISS (utility lower bound −0.01) |
| 1,000 | 2.2% / 16.2% | 0.839 / 0.838 | 0.014 | PASS (87 ms per frame; stated whole-scene integrity 1.73%, actual 1.72%) |

- **E12: MISS** — every bar passes at 1,000 objects; at 100 and 10 one scene each pushed the lower bound below zero, and
  at 10 the odds were too cautious.
- **E13: PASS** — the chosen one: Angel Eyes 24 right and 1 sure-wrong of 40; the standard tracker 16 right and 24
  sure-wrong. With the traps: 17 right, 0 sure-wrong (standard: 7 right, 13 sure-wrong).

*Opus · 15 Oct 2026*
