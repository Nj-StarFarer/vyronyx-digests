# Manifest 2026-10-15 (KM-012 #10): E14, the flight challenge — which of 100 drones is ours, with every radio silent (simulated). PASS

Prepared by Opus, under NJ's standing delegation. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `2e45eac4`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/E14_SPEC.md` (frozen spec, note E14-N1, and the result) | `c24723ad3e03f1dc1b55430979afd461587cab13d720663113a31aa0f41ebea4` | 4761 |
| `angel_eyes/identity/sealed_e14/result.json` | `ea2e2ab718548b9c448c6ff6e0c7883645cc2117f56cf602379ac341d9f44d2f` | 8162 |
| `angel_eyes/identity/sealed_e14/seeds.json` (drawn after the freeze; hash recorded before the run) | `9d390308ebc490cc366153e81b411e2ecfbc8d6897c8aa171f8dfdc69c08f8f2` | 500 |

## The test
- **Simulated** crowds of 100 drones. Our drone flies a secret one-time 12-bit pattern as speed changes (36 s),
  sent over our own control link. Angel Eyes only watches the tracks and says which one flew it.
- **Strong secrets only** (514 patterns: balanced, several changes, far from any natural speed change), so an
  informed adversary who knows the method is accepted with a stated chance of 1/514.
- 40 scenes; in 20 of them, 10 informed adversaries fly random strong patterns at the same time.
- Spec frozen at `9a1f3a26` (07:56:53 UTC); seeds drawn after it (07:56:55 UTC).

| Measure | Result | Bar |
|---|---|---|
| Ours found | 28 / 40 (70%) | ≥ 60% |
| Ordinary drones wrongly accepted | 1 of 3,681 (0.027%) | ≤ 0.1% |
| Informed adversaries wrongly accepted | 1 of 200; stated 0.195%; p = 0.32 | not significantly above stated |

**PASS.** A miss is safe in use (no one accepted; a new challenge is sent). Not yet shown on real flights or real sensors.

*Opus · 15 Oct 2026*
