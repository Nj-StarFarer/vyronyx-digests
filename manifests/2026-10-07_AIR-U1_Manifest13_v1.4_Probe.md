# Manifest 2026-10-07 (#13): Angel Eyes AIR-U1 v1.4 — runner probe PASS (before the CAL v1.4 run)

Prepared on 7 Oct 2026, about 11:31 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, numbers and SHA-256 fingerprints only. It stores no data, no code and no secret.

## The probe
- **The run:** probe run `37577947076` in `VyroNyx/angel-eyes-air-u1`, from `main` at commit `225ddf7`. It was started by NJ's typed phrase at 05:45:59 UTC on 7 Oct 2026, and re-run once ("Re-run failed jobs") as designed.
- **It touched no AIR-U1 data.**
- **Verdict: PASS.** All four conditions of Spec v1.4 Change 3 hold:
  1. **Every automatic check passes:** 19 PASS, 0 FAIL.
  2. **The one LOOK item, read by Opus, passes:** a second upload under the same artifact name was refused, as it must be.
  3. **The key check on `main` matches.** The scorer key reaches the job, and its public key equals the committed `scorer_public.pem` (`d4e6d9ec…0a40`, manifest #9). The job printed only present/absent and match/no match.
  4. **Free disk is 100% of what the v1.3 probe recorded** (the rule is at least 90%). Both show 14 GB available on `/` before the production step. The v1.3 probe log was read before this probe ran.
- **Capacity after the production clean-up and swap step:** 2 CPUs, 7,938 MB of memory, 9,215 MB of swap, 38 GB free.

## Fingerprint (SHA-256)
| File (in `VyroNyx/angel-eyes-air-u1`, commit `346de24`) | SHA-256 |
|---|---|
| air_u1/probe/v1.4/PROBE_RESULT.md | `3189c71295cbd8d10016a4b746ca87d17a901f336890f7f6cdd5013060a67baf` |

The build, checker, CAL plan sums and rehearsal hashes are unchanged since manifest #12.

## Next
The CAL v1.4 run (28 frozen days of 2025, baselines only), started only by NJ's typed phrase.

## Pending
No OpenTimestamps proof exists yet for this or any earlier manifest. One will be added in a later commit if it can be made, and this file will not be edited.
