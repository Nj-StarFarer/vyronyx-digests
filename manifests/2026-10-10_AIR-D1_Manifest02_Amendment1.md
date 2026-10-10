# Manifest 2026-10-10 (AIR-D1 #2): Angel Eyes drone detection, Amendment 1 in force

Prepared on 10 Oct 2026 by Opus. Published on NJ's instruction ("Yes", 10 Oct 2026, 15:23 IST).

The commit time of THIS file is the time Amendment 1 comes into force. This manifest holds names, numbers and SHA-256 fingerprints only. The repository the hashes refer to is private.

## 1. What is frozen
Repository `Nj-StarFarer/SkyNet`, commit `37751d9`:

| File | SHA-256 | Bytes |
|---|---|---|
| `angel_eyes/air_d1/AIR_D1_AMENDMENT_1.md` | `2fa2e7279a6243342c5d0a85ac88dbe3c4d7eec70cec72bb1868ddb049551c56` | 3,642 |
| `angel_eyes/air_d1/AIR_D1_SPEC_v0.4.md` (unchanged since #1) | `975bb51cedddbbd1fc0c0dc6da6330a474f036b25d07e1589cd245013aba7045` | 24,023 |

## 2. What Amendment 1 does
- **A1, the gap:** clip numbers are shared across drone types, so some practice clips sat right next to sealed clips of another type.
  - **Fix:** any recorded practice clip within 10 numbers of a sealed clip of the same sensor and class moves to the unused buffer.
  - This moves 37 clips. **The sealed set is unchanged**: 204 clips, with the same list fingerprint.
- **A2:** the near-duplicate check runs on a separate machine that outputs only clip IDs and counts. The build workspace downloads practice files only, through an allowlist.
- **A3:** a clarification of how internet clips are counted.
- **A4:** the distance mix is reported. Sealed IR drone clips are 37% "distant", against 19% in practice.

## 3. The split, from metadata only
No video, audio or label file has been opened. The expected counts all match spec v0.4 §4:

| Group | Count |
|---|---|
| IR micro-drone, sealed | 38 |
| IR look-alike, sealed | 63 |
| Visible micro-drone, sealed | 29 |
| Visible look-alike, sealed | 36 |
| Sound clips (all) | 90 |

| Role | Clips |
|---|---|
| Sealed | 204 |
| Buffer | 168 |
| Practice | 317 |
| Practice-only | 51 |

The sealed ID list fingerprint is `3bcf0232bbdf38d03c7c7c6176c36a41fca1c8fb7ce18db453c78b680458643c`. It is **provisional**, because the near-duplicate check can still move sealed clips into the buffer.

## 4. Next
1. The 703 practice files are downloaded through the allowlist, each checked against its git ID.
2. The near-duplicate check runs on the separate machine, on NJ's typed phrase, and the final sealed list is published.
3. Then come the build, the build gate, a fresh checker and one sealed run.

*Opus · 10 Oct 2026*
