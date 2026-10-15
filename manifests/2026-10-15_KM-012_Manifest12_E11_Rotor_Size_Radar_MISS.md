# Manifest 2026-10-15 (KM-012 #12): E11, propeller size from radar physics on drones never seen. MISS

Prepared by Opus, under NJ's standing delegation. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `c2f306f9`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/E11_SPEC.md` (frozen spec and the result) | `68f0160a276127625bb0c7797967e9cabb6d4b4614abe1dfc77f040ba36e8266` | 7173 |
| `angel_eyes/air_e11/sealed_38694467389/result.json` | `10a5de212865a05b41e75eac338bc34ea32f4c11e65e90b4271b2496de9505bd` | 13264 |
| `angel_eyes/air_e11/sealed_38694467389/predictions.json` | `9281c5de006e432fe15e6452e6390a00a8b2cc992882cffa68a3379905791855` | 14949 |
| `angel_eyes/air_e11/sealed_38694467389/key.json` | `7f909f5b18b5d6a257d3594835e00ce5284310c7135bde1035b72df0dc8931ea` | 84440 |

- **Test:** TSMS-Drone continuous-wave radar (Korea Aerospace University, CC BY 4.0): measure each drone's propeller
  diameter and even/odd blade count from blade-tip Doppler and blade flashes, no training; leave-one-drone-out rival;
  a non-spinning corner reflector as control. Spec frozen at `bd7f09df` before any file was downloaded; run
  `38694467389`; first 20 files of each target-and-distance used.
- **MISS:** a rotor established on only 6 of 18 core scenarios (bar 70%); those sizes ~2–2.5× too large; blade
  parity "even" 71% (bar 80%); the rival did better.
- **Held:** the reflector gave "no rotor" at all 15 distances; shuffled data gave none.

*Opus · 15 Oct 2026*
