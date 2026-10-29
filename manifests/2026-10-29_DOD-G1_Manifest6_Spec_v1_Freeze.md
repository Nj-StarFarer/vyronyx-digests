# Manifest 2026-10-29 (6): Dodona DOD-G1 "gust propagation", Spec v1 (pre-registration)

The commit time of THIS file is the authoritative publication time.

A new line of Dodona, on NJ's direction: learn **how air behaves as it moves** (how gusts travel, how fast, and how quickly they lose their shape), judged by gust structure (arrival, duration, what comes next), not by wind speed.
- **Level 1 is simulation only.** It contains Taylor's and Davenport's known laws. A pass proves the engine and the instrument, not new physics.
- **Pass marks:** set from public headroom data by fixed rules, before any CAL search.

## Fingerprints (SHA-256), private repo VyroNyx/dodona
| File | Bytes | SHA-256 |
|---|---|---|
| sealed/DOD-G1/DOD-G1_Spec_v1.md | 10067 | 66548b63eca8c5f49daa6ac7251ef6470bcbc5e0b187b525e1fab3dcf0e58c6d |
| sealed/DOD-G1/thresholds.json | 544 | 2cb99f8f041248d3ddb85f0b2700cde788b50cca53e9ce10869340eb66d6d0fd |
| sealed/DOD-G1/headroom/headroom_report.json | 4707 | 306e8f9301b35e41561ff3f8edf78884390d355d0a91a98fcc0d47c27e59d114 |
| sealed/DOD-G1/MANIFEST.sha256 (all code files) | 2531 | 37270e4f393d81e72fb508a3c5650c9660612f08dd4a8ba89f5c87ddfa003377 |
| docs/DATA_AUDIT_G1.md | 4396 | ae3f809e23fb8043703f701f2c0af32cdbda437cb04e2643ae08425bbe409043 |

Commit: 12b7dba76a06f0f189b66c4d813f000f90f3bff9 (commit date Thu, 29 Oct 2026 16:48:49 +0530).

## State at publication
- **Formulas:** CAL has not run its frozen search. No formula exists.
- **Sealed fields:** none exists. They will be made from the commit that freezes CAL's formulas.
- **Disclosure:** a 3-iteration plumbing check on public TRAIN rows returned `d_par / c_g` (spec section 8.5).
