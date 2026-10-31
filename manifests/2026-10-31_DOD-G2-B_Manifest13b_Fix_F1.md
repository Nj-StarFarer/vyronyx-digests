# Manifest 2026-10-31 (13b): DOD-G2-B fix F1 (gaps in the data)

The commit time of THIS file is the authoritative publication time.

- **What happened:** the first scoring run on Clocaenog made no rows. The frozen reader rejected every tree because the site's files mark gaps as NaN.
- **The fix:** code only. Windows with gaps are skipped, and CAL's law and the rules are unchanged. Rivox and Kershope rows stay bit-identical.
- **Disclosure:** the fix was made after seeing Clocaenog's file layout, and before any result existed.

| File | SHA-256 |
|---|---|
| sealed/DOD-G2-B/build_sha256.json | 8080918abab9d0fb3d10bd889e6762941460cdec2f916872061221d3df6b73a3 |
| sealed/DOD-G2-B/DOD-G2-B_Spec.md | 6fec33c44d6d6c34d769a40c43397183e7d4ef0f50a09ce60cf820b9973f88de |

Commit: 52ecd495cec3cd44801b86ba2baf00399e22e8f5.
