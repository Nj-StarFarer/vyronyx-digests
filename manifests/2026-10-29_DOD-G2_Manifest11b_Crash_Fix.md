# Manifest 2026-10-29 (11b): DOD-G2 crash fix before search

The commit time of THIS file is the authoritative publication time.

- **What happened:** the search stopped at its first step (the units table was missing the DOD-G2 inputs). No formula existed, and Kershope.zip was not unzipped.
- **The fix:** code only. The spec is unchanged.

| File | SHA-256 |
|---|---|
| sealed/DOD-G2/MANIFEST.sha256 | e8625dcf53ed701276949062074b5e62f2eac6570874224179e7999d58701df4 |

Commit: 920160da02b0bf6a3fa8c318f6cc677c03300adf.
