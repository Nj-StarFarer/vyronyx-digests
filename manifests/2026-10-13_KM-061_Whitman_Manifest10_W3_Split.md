# Manifest 2026-10-13 (KM-061 #10): Whitman W3, sealed/open split of CARE to Compare (published before any dataset is opened)

- **Prepared:** 13 Oct 2026 by Opus.
- **Data:** CARE to Compare (Fraunhofer IEE, Zenodo record 15846963, CC BY-SA 4.0). It holds real recorded faults from 36 wind turbines.
- **What was looked at:** only a structure census, which reads no sensor value and no fault time or description.
- **How the split was made:** by whole turbine, using a hash order fixed before the census was read. So no open turbine's year of data can contain a sealed fault.

## Fingerprints (private repository `Nj-StarFarer/SkyNet`, commit `7c5de66`)

| Item | SHA-256 |
|---|---|
| `docs/kingmaker/WHITMAN_W3_SPLIT.md` (rule and result) | `b32cb9c7be926e66bcfb19d9a9ef229b44768aa011754e51da2347a2521582a9` |
| `whitman_w3/SPLIT.json` (the sealed and open turbines and events) | `fed02fd9eca1eab541a19bb7a83155fa729886d6d02d8cf48ea9781366c679e0` |
| `whitman_w3/split.py` | `fe1fc63feec1b58808ee0d602de9c21a628f49fec3601f6d5c2a904e3268fa3e` |
| `whitman_w3/census_38424449451/CENSUS.json` | `170f90e49f7d483ffcd5d77f4a970a3ca5163f45b7b953761f24ba5123da683d` |
| `CARE_To_Compare.zip` (MD5 `2547b58c21ac8c242d13232860cf500c`, same as Zenodo) | `ca61379e98956d891041ad45c885109bd8a14199fde0688d0184a11c2d4194f1` |

## The split

| | Turbines | Real fault events | Normal datasets |
|---|---|---|---|
| **SEALED** (one test run only) | 18 | 25 | 25 |
| **OPEN** (development) | 18 | 20 | 25 |

## What follows

1. Whitman's wind-turbine kind is developed on the open side only.
2. The W3 test spec and build are then frozen and published. The rivals and the scorer are fixed there:
   - the dataset authors' own autoencoder (EnergyFaultDetector, MIT);
   - an isolation forest;
   - the alarm panel;
   - the CARE score.
3. Only then are the sealed datasets opened, in one run.

*Opus · VyroNyx Private Limited · 13 Oct 2026*
