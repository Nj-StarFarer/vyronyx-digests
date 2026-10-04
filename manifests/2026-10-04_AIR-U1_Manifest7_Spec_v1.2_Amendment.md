# Manifest 2026-10-04 (#7): Angel Eyes AIR-U1 Specification v1.2, an open amendment (before any AIR-U1 data is processed)

Prepared on 4 Oct 2026 at about 17:15 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, versions and SHA-256 fingerprints only. It stores no data, code or results.

## What is being registered
**AIR-U1 Specification v1.2** = Spec v1 (manifest #5) + the v1.1 amendment (manifest #6) + one new amendment file. Both earlier files are unchanged.

Why: the AIR-U1 pipeline was built and tested on **synthetic data only**. That build and two independent reviews found one bar that could not be met, one statistical flaw, and some gaps in the text. v1.2 fixes them:
- **The B0 accuracy check** moves from 1e-9 to 1e-7. Ordinary computer rounding alone gave differences of up to 8.0e-9 on synthetic tracks. The daily check of B0 against Stone Soup on real tracks (1e-6) is unchanged.
- **The placebo check** changes only when there are fewer than 20 events: it then needs 2 chance hits instead of 1. From 20 events up, v1 is unchanged.
- **No escape from a bad result:** any stop after the first sealed file is downloaded counts as a MISS for the parking rule.
- **Every named stop** is classified as "may be re-run once" or "final". Six integrity stops are added.
- **Workflow enforcement** is added: re-run limits, once-only guards, and checks before the scorer opens the key. No rule changes.
- **Readings fixed now:** where v1 was silent or unclear, the literal reading is kept and written down before any data.
- **One forecast added:** NOT_REPRODUCIBLE from the build check, 3%.

**What has been seen:** no AIR-U1 DEV, CAL or SEAL data has been processed. The only real data read so far is the census counts in manifest #4. CAL (2025) and SEAL (Jan–Jun 2026) data have never been downloaded.

## Fingerprint (SHA-256) of the file in the private repo Nj-StarFarer/SkyNet
| File | Bytes | SHA-256 |
|---|---|---|
| air_u1/spec/AIR_U1_SPEC_v1.2_AMENDMENT.md | 10563 | d58292a36170728f5610f2a9747a3efb209025467eb2a91f43010ffd18ccd7d6 |

- Private-repo commit: 956855460b4efb9ae0969b8b86731d7ab143270f (4 Oct 2026, 17:09:31 IST).
- The fingerprint was recomputed from the file as stored on GitHub after the commit. It matches.
- The files of manifests #5 and #6 are unchanged.

## What does not change
- the P-U1 bar;
- the baselines and their budget K;
- the sizing rules N and TOO_FEW;
- BUDGET (1,300 minutes);
- the split sealed run;
- the answer-key handling;
- the seeds;
- the day permutations.

**The forecasts of v1 and v1.1 are not edited.**

## Approval trail
- Opus wrote v1.2 under NJ's delegation ("Opus now. Take decisions Chief.", 4 Oct, 16:47 IST).
- A first commit attempt on that delegation was blocked as not explicit, and nothing was committed.
- Opus explained what the commit was. NJ answered **"Commit it."** at 16:53 IST.
- Before the commit, an independent review found 2 blockers, 4 should-fix items and 4 notes. All were applied.
- These are statements in private chat, and they remain claims until this manifest exists. No AIR-U1 run has started. Runs wait for November's Actions quota.

## How to verify
1. Ask VyroNyx for the amendment file, compute its SHA-256, and compare it with the table.
2. Check that this file's commit is dated before any AIR-U1 DEV, headroom or sealed run in the GitHub Actions history.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
