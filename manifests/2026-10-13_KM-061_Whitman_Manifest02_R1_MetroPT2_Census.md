# Manifest 2026-10-13 (KM-061 #2): Whitman Rung 1, MetroPT2 pre-build census, and the open pack

- **Prepared:** 13 Oct 2026 by Opus.
- **Published on NJ's instruction:** "Do everything yourself" (13 Oct 2026, 06:13 IST). This covers the publication step listed as pending in the overnight log.
- **Contents:** names, numbers and SHA-256 fingerprints only. No data, no code, no secret. The repository the hashes refer to is private.
- **What this is:** step 1 of spec v1.0 §9. It pins the MetroPT2 file before any builder reads it. No sensor value from MetroPT2's sealed part (on or after 2022-05-25 00:00:00) was read; only its timestamps were counted.

## 1. The run

GitHub Actions run `38284874817` in the private repository `VyroNyx/whitman`. NJ approved it: "Yes, run it".

- Its spec is `r1/spec/WHITMAN_R1_DC2_OPENPACK.md`, SHA-256 `9d28f59120554bb4db0c4b919090e1fad78ca9d82e2d22e03ac1ac9bec5dda4c`.
- The output was committed by run `38287073599`, after an independent leak check, at commit `b8144bbbbe5c5c3715f392455ad330d12d012450`.

| File | SHA-256 |
|---|---|
| `r1/datacheck/results/dc2_38284874817/mp2_census.json` | `4214c220102711e652cd389fd5b3d31d2bebe5088a9f5464850b1ffd54cf5cc6` |
| `r1/datacheck/results/dc2_38284874817/summary.md` | `7d33e81a6dc7f0c477f1d1b784d33c53cddfb30f446342e713207df2d23cfc1a` |
| `r1/datacheck/openpack.py` (the packer) | `d828ae4a421a3812f25f45426c4b9d24c4947e54d6f6957c04710a4ed5998de6` |
| `r1/datacheck/leakcheck_openpack.py` (independent leak checker) | `ef4a00c37a27f863eae72d0691fdc15f0311fb40a44e605d93108d9b750da3f9` |
| `r1/open/OPEN_PACK_MANIFEST.json` | `fee1ef8c2852d46a4f9082ca4f4a8ae5f1d4484d85745dfb77ca967ff5ba0539` |
| `r1/open/OPEN_PACK_SHA256SUMS.txt` (every open file the build may use) | `a2975dff9324f1127e59cb2f75cec3c396bed6a954a1775ad6b364dedabfc5db` |

## 2. MetroPT2.csv (Zenodo 7766691), as pinned

| Item | Value |
|---|---|
| SHA-256 | `b62a95876d0d3f8d9250e62e218641125c56b01238bda42c6157fade319133f4` |
| MD5 (equals the Zenodo record) | `056e04fd1874eaef4697d6b6657502c3` |
| Size | 1,209,663,443 bytes |
| Columns | `timestamp`, TP2, TP3, H1, DV_pressure, Reservoirs, Oil_temperature, Flowmeter, Motor_current, COMP, DV_eletric, Towers, MPG, LPS, Pressure_switch, Oil_level, Caudal_impulses, gpsLat, gpsLong, gpsSpeed, gpsQuality |
| Rows | 7,116,940. By month: Apr 215,881; May 2,442,988; Jun 2,351,499; Jul 2,106,572 |
| First / last timestamp | 2022-04-28 12:33:29.120 / 2022-07-28 12:24:34.839 |
| Time step | median 0.991 s; 99% of steps within 0.99–0.994 s; no zero or backward steps |
| Gaps | 103 over 60 s; 69 over 10 min; 49 over 1 h; none over 1 day |
| Usability (spec §2b) | **usable**: the timestamp parses, the first row is before 2022-05-01 and the last row is after 2022-07-16 11:00 |
| Sealed span | 2022-05-25 00:00:00 to the last row: 64.52 days. **G3 limit for MP2 = 2 false alarms.** |
| Analogue channels (spec §4a, from the open part) | TP2, TP3, H1, DV_pressure, Reservoirs, Oil_temperature, Flowmeter, Motor_current, gpsLat, gpsLong, gpsSpeed |

## 3. The open pack (what the build may use)

`r1/open/` holds only the open parts:
- M3 before 2020-05-01 (644,032 rows);
- MP2 before 2022-05-25, as 10-second medians (205,738 buckets);
- the 17 open SKAB files plus `anomaly-free.csv`;
- the 11 open MEF files of spec §2d.

An independent checker, which does not import the packer, confirmed four things before the commit:
- L1: every M3 timestamp is before 2020-05-01.
- L2: every MP2 bucket is before 2022-05-25.
- L3: the SKAB list is exactly the open list (SHA-256 `cbaf8cd0…ecef0`).
- L4: the MEF list is exactly the open list, and no sealed name appears.

## 4. Where the build stands (for the record, not a result)

- The detector exists in the private repository and passes its 12 self-tests. It has **not** been frozen.
- Its development numbers on the open data did not yet clear its own pre-freeze check (build spec §5).
- The next manifest is the build freeze: the build hash, the reader hash and the seed rule.

*Opus · VyroNyx Private Limited · 13 Oct 2026*
