# Manifest 2026-11-03 (20): AQ-S4 "Feel the air vs see it coming", outcome PASS

The commit time of THIS file is the authoritative publication time.

- **Run:** scored once from freeze commit `45f30ce` (Manifest 19); 40 sealed episodes × 300 s; sealed seed 11572869649006205491.
- **Verdict: PASS.**
  - P1: on-body sensor / feedback-only = 0.798 (mark ≤ 0.80). Passed by 0.002.
  - P2: on-body + tree / on-body = 0.948 (mark ≤ 0.985).
  - P3: on-body + tree better in 92.5% of episodes (mark ≥ 75%).
  - P4: flap rate 0.992× feedback-only (mark ≤ 1.1).
- **Written prediction FAILED:** the 2 m tree alone gave 0.948× the on-body sensor (prediction: ≥ 1.0). It was better in 52.5% of episodes.
- **Result commit:** 8812e8286e6bc395e2dbfb37052249fe6c991ccc in VyroNyx/dodona.

| File | SHA-256 |
|---|---|
| sealed/AQ-S4/results/score_report.json | 0ab0412d4cf212addb1a4333c6ec72c30d8411b2ca297467063fcfe2e6ac74ee |
| sealed/AQ-S4/results/episodes.json | 4e3d387d721e2a7326c12f5634892f00c5d5f0870a229579cfeba695bcd25593 |
| sealed/AQ-S4/results/READING.md | 26545e4620052cba0b03c7af3f62be3f33594b12bb131393b0db82075266ef79 |
