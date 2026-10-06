# Manifest 2026-10-06 (#11): Angel Eyes AIR-U1 — the v1.3 CAL ending, and Specification v1.4 FROZEN

Prepared on 6 Oct 2026; the clock tool read 17:52:58 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, numbers and SHA-256 fingerprints only. It stores no data, no code and no secret.

## 1. How the v1.3 CAL run ended
- The CAL headroom run (`37434825702`, manifest #10) ended with the terminal stop **CHECKER_MISMATCH**: the independent checker refused the scorer's output. **No CAL number was released, committed or seen.** The stop record is preserved in the test repository.
- **Root cause, found without opening any answer key:** 1,383 of about 2.26 million CAL tracks have fewer than two points with a finite barometric altitude, so they carry no baseline score (NaN). The spec never said what an undefined baseline score means. The scorer ranked such tracks as "never"; the checker, built from the spec alone, required every score to be finite. Shown by replaying the real label-free outputs with synthetic answer keys sealed by a throwaway key pair; with the gap closed in a throwaway copy, scorer and checker agreed on 7 of 7 replays.
- Under the frozen rules (v1.2 Change 4, v1.3 Change 2), this ending is not a MISS, and a retry needs a new spec version with a new CAL period. That is v1.4.

## 2. Specification v1.4 is FROZEN
- NJ froze it: "And yes Freeze v1.4" (6 Oct 2026, 17:49 IST).
- Before the freeze, independent reviews rejected drafts 1 to 4 (the review history is recorded in the spec itself); draft 5 was reviewed **READY TO FREEZE**.
- **What v1.4 changes** (full text in the spec file):
  1. Undefined baseline scores: a track with `n_baro < 2` carries NaN for B0 and B1, counts in T, n and K, and is never ranked. Both programs implement the same rule; the checker gains exit 4 for a breach (NON_FINITE). Angel Eyes is untouched.
  2. A new CAL period: 28 fixed days of 2025 (CAL permutation ordinals 29–59, skipping 30, 45 and 54, which have no qualifying release). The v1.3 CAL days are retired. The list is frozen; it is never re-derived.
  3. The test moves to the private repository `VyroNyx/angel-eyes-air-u1` (GitHub repository ID 1407170694), seeded byte-for-byte from the previous repository (commit `0fe93b0`). GitHub Free gives a private repository no environment secrets, deployment-branch rules or required reviewers, so the spec assumes any branch can read the scorer key, adds a probe key check (a DER public-key match on `main`), and adds a repository-identity check before any key is read.
  4. BUDGET is retired. Costs are planned with frozen constants (c_S = 10.0 min/day, s_S = 3.9 MB/day), a start condition on the organisation's remaining minutes and storage, a 60-day latest-start deadline after the CAL result (missing it counts as a MISS, with three named park exceptions), and the stop TOO_COSTLY.
  5. The SEAL days are a frozen list: A = 180 days of 2026 have a qualifying release (SEAL ordinal 9, 2026-05-06, is skipped for good). **N_max = 102** (set by the 500 MB artifact-storage limit), so N = min(102, max(28, ceil(60 × 28 / k))) and TOO_FEW fires if k ≤ 8.
  6. The DEV results carry over byte-for-byte; the build may differ from the manifest #10 build only by an enumerated list of changes, held by an independent build gate.
  7. A label-free dress rehearsal (9 frozen scenarios, seeds 1–3) runs before every keyed run. A disagreement before the sealed run is the terminal stop REHEARSAL_MISMATCH, and it counts as a MISS.
  8. No second CAL draw: every possible CAL ending is named, with its consequence.
- **Key disclosure (stated plainly):** on 6 Oct 2026 the scorer private key was exposed to a private chat transcript by its holder, and the holder chose to keep the key pair. The spec records this and why the test still stands: everything that decides the result — code hashes, day lists, bars, the latest start date, and (in SEAL) the committed alert-list hashes — is fixed and published before any answer key is opened. No key material appears in any repository or note.

## 3. The CAL v1.4 days (public, from release metadata only)
2025-02-15, 2025-05-27, 2025-01-30, 2025-10-04, 2025-11-14, 2025-03-09, 2025-11-16, 2025-01-12, 2025-07-06, 2025-05-03, 2025-12-06, 2025-07-08, 2025-07-02, 2025-02-16, 2025-09-28, 2025-03-26, 2025-08-15, 2025-11-04, 2025-04-05, 2025-03-27, 2025-12-27, 2025-08-14, 2025-07-18, 2025-01-16, 2025-07-28, 2025-01-02, 2025-11-17, 2025-05-08.
These follow mechanically from the frozen permutation (manifest #5) and from which dates have a release, so publishing them reveals no label.

## 4. Fingerprints (SHA-256)
| File (in `VyroNyx/angel-eyes-air-u1`, commit `87b7991`) | SHA-256 |
|---|---|
| air_u1/spec/AIR_U1_SPEC_v1.4_AMENDMENT.md (FROZEN) | `21a8d3b877f552f8f4b7d83cce6eafa4272519b917a3042646dc40a45b2585d4` |
| air_u1/spec/v1.4/cal_v14_days.json | `92a0a68a17a55e81b84e10141395d0c1ccdc89b6afb17a1f444a04f018ee9d09` |
| air_u1/spec/v1.4/tags_2025.txt | `f71fffc921a87e6f2130a549716f95afa148d96d93c8e0fb4b478bcc38e4a0e4` |
| air_u1/spec/v1.4/cal_releases_ord0_59.txt | `c38421ef2eee9f38b9d3598729d763e8b0a856c143bc5dbfc81dd14c85e3df59` |
| air_u1/spec/v1.4/seal_a180.json | `a66aaf10d704eb871b5c0786f9eff81557f9e134c9a48afe04c39f8e4c183b9e` |
| air_u1/spec/v1.4/releases_2026_list.json | `5ff53f351c766c21f2412744f685a97a3e75df8aa613219f57b3517b68e80336` |
| air_u1/reading/AIR_U1_READING_PLAN.md (carried over unchanged) | `acc3bf4026a43afe77c7f7e5e496c835e9696cd1fab405fdcd0e1649bf023371` |
| Build sums (unchanged since manifest #10; the v1.4 build will publish new sums before CAL) | `5da8f245ef4ecbcb2c4c41c01c85f4205846d557c01cfced032a3c5371aba5e5` |
| Spec chain: v1 / v1.1 / v1.2 / v1.3 (unchanged) | `f07212d2…`, `e977d5d3…`, `d58292a3…`, `15e81c65…` (full values in manifests #5–#8) |

- The carry-over commit is `0fe93b0` (6 Oct 2026, 17:12 IST), byte-for-byte from the previous repository's head `55b8cca`.

## 5. What happens next (in order)
1. The v1.4 build (an enumerated change list only), then an independent build gate and a manifest with the new build hashes.
2. The pre-CAL dress rehearsal on the v1.3 label-free outputs.
3. The runner probe, then the CAL v1.4 run, started only by NJ's typed phrase.
4. If CAL commits a clean result: the sealed-run plan files, a pre-run manifest, and the sealed run within 60 days.

## How to verify
1. Ask VyroNyx for any file listed. Compute its SHA-256 and compare it with the table.
2. Check that this file's commit is dated before any v1.4 workflow run in the test repository's Actions history.

## Pending
No OpenTimestamps proof exists yet for this or any earlier manifest. One will be added in a later commit if it can be made, and this file will not be edited.
