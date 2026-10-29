# Manifest 2026-10-29 (7): DOD-G1 v1 outcome, FAIL at rung R0

The commit time of THIS file is the authoritative publication time.

- **CAL's formulas** were committed before any sealed field existed (commit 74c32d587406dcb6238ae10a3f8ba99e14133974).
- **Rung R0:** CAL's R0 travel-time law scored a median 20.2% error on the held-out R0 fields, against a mark of 10%. **FAIL.**
- **The sealed fields were never made.**
- **Cause:** the R0 search had 9 rows and CAL overfitted them. See results/DIAGNOSIS.md.

| File | SHA-256 |
|---|---|
| sealed/DOD-G1/formulas/formulas.json | bdfdbcd1ec49729470d4f28813bc5703628036e55a7b3803700068dc71ab2116 |
| sealed/DOD-G1/results/score_report.json | d5fe9385841bad31414bc44a95b6443ca047152a2a28f5f8fc9109fd21b7aee5 |

Results commit: 0229c977659f1217fb6af10693b784ae8356eabb (commit date Thu, 29 Oct 2026 17:00:30 +0530).
