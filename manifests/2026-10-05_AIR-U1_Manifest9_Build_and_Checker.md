# Manifest 2026-10-05 (#9): Angel Eyes AIR-U1 build, independent checker and scorer public key (before any AIR-U1 data is processed)

Prepared on 5 Oct 2026 at about 17:40 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, versions and SHA-256 fingerprints only. It stores no data, code or results.

## What is being registered
The software that will run AIR-U1 under **Specification v1.3** (manifests #5 to #8). It is registered before it has ever touched AIR-U1 data:
- **The build:** the pipeline, the run guard, the tests and the GitHub Actions workflows.
- **The independent checker:** `evaluate.py`. It recomputes every number of the scorer's result from the detector outputs and the answer keys.
  - It was written in a separate session from the spec and a written interface only.
  - That session never saw the scorer's code.
- **The scorer public key:** RSA, 4096 bits.
  - The answer keys are encrypted to it before detection.
  - Only the private key, which NJ alone holds, can open them, and only inside the scorer job.
- **The airport list:** at the pin already published in the freeze (manifest #5).

**What has been seen:**
- No AIR-U1 DEV, CAL or SEAL data has been processed.
- The only real data read so far is the census counts in manifest #4.
- Every test of this software used invented (synthetic) data.

## Build gate: passed on 5 Oct 2026
- **Seven Opus reviews (v1.3 to v1.3g).**
  - Two of them added an independent reviewer who tried to break the build.
  - Every blocker and should-fix item was closed.
- **The build's own tests:** 16 of 16 suites pass in a hash-pinned environment.
- **The checker's own tests:** 97 pass.
- **The build's scorer against the independent checker:** run on 14 invented scenarios, they agree on every one. The scenarios cover all four labels, the placebo test, dropped 7500 tracks and the cases with no events.
  - That comparison found three differences in how values were written.
  - All three were fixed and written into the interface before this manifest.

## Fingerprints (SHA-256) of the files in the private repo Nj-StarFarer/SkyNet
| File | Bytes | SHA-256 |
|---|---|---|
| air_u1/build/AIR_U1_BUILD_SHA256SUMS.txt (lists all 76 build files) | 6527 | dd53cc1d6c305ed19eccd02e88b12a137bba3b5025ded9454a3d761e9867dece |
| air_u1/build/requirements.txt (hash-pinned packages) | 5035 | a1d8f07c7c378f669f6c211f18d1f35ca5c65bcb57da642a96841f246e1570f6 |
| air_u1/checker/evaluate.py | 55107 | 4b859336d707cebbd5249793f0b1b7168350f27667019bb8fbcb616442906609 |
| air_u1/checker/SHA256SUMS.txt (checker, its tests, its notes) | 244 | e99c2602dae4e18550f49073435edb0bc7f45db68264914501436be0d1773b6c |
| air_u1/keys/scorer_public.pem | 800 | d4e6d9ec1bb565c919c39b305a43802228a97320e73ac4c5d045ac27dd750a40 |
| air_u1/spec/airports.csv (the pin of manifest #5) | 12734638 | ff5143921ef72d767402c299a5d868f79166c5c589267aca13dce957c41bd2a2 |
| .github/workflows/air-u1-dev.yml | 13078 | 503007f0090efd2541f1011b4dce41598b9888f70363b440823b785bb2bf6d04 |
| .github/workflows/air-u1-headroom.yml | 24586 | c7b6640bb7d22336b5de29374f74fc6367a6a784b94f479a81cb4328432fb86c |
| .github/workflows/air-u1-sealed.yml | 34776 | bdfcfdad92512dc1b3650288349e4a5c202f4ea42677f7aeb34f2170d6531e01 |
| .github/workflows/air-u1-probe.yml | 14294 | e6e940516d794217cb92c68dd354899b4fd041e7ac8afbabacf155ef89136ee3 |

- **Private-repo commit:** 64f9ff866369afc644040079c3cf6d2fbc5056f9 (5 Oct 2026, 17:34:06 IST).
- **Fingerprint check:** every fingerprint was recomputed from a fresh copy of the repository after the commit, and all of them match. The build's own sums file also verifies all 76 files.
- **Earlier files:** the spec files of manifests #5 to #8 and the day permutations were re-hashed at the same time. All are unchanged.

## How the runs are guarded (unchanged from the spec, now in code)
- **Each run needs NJ's typed phrase.** The workflows start only by hand, never on a push.
- **Version pins:**
  - Every workflow pins its GitHub actions by commit. Opus checked the pins against the official release tags on 5 Oct.
  - Every Python package is pinned by hash.
- **The plan sums come later.** The CAL plan sums need the DEV manifest; the SEAL plan sums need the CAL result. Each is committed before its own run.
- **The independent checker gates every result.** A CAL or SEAL result is committed only if the checker agrees with it, and only if the checker's hash is listed in that run's plan sums.

## Approval trail
- Opus: build gate Part 1 passed (5 Oct, 16:15 IST); Part 2, the checker, passed (17:45 IST).
- NJ made the RSA key pair on his own computer (17:24 IST). Only the public half left it.
- NJ approved this commit and manifest: "yes." (17:26 IST).
- These are statements in private chat, and they remain claims until this manifest exists.
- No AIR-U1 run has started. Runs wait for November's Actions quota.

## How to verify
1. Ask VyroNyx for the files, compute their SHA-256, and compare them with the table.
2. Check that this file's commit is dated before any AIR-U1 DEV, headroom or sealed run in the GitHub Actions history.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
