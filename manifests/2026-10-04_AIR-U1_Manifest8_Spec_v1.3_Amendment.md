# Manifest 2026-10-04 (#8): Angel Eyes AIR-U1 Specification v1.3, an open amendment (before any AIR-U1 data is processed)

Prepared on 4 Oct 2026 at about 21:40 IST. The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names, versions and SHA-256 fingerprints only. It stores no data, code or results.

## What is being registered
**AIR-U1 Specification v1.3** = Spec v1 (manifest #5) + the v1.1 amendment (manifest #6) + the v1.2 amendment (manifest #7) + one new amendment file. The earlier files are unchanged.

Why: an independent review of the v1.2 build, run on **synthetic data only**, found gaps that the written rules still left open. v1.3 closes them:
- **A started run always ends with a result or a recorded stop.**
  - A sealed run starts with its first attempt marker. Each job commits its marker before downloading any sealed file.
  - From then on, the run ends either with a result committed by the scorer job, or with a terminal stop. A terminal stop counts as a MISS.
  - If no result is committed within 168 hours, the run ends with SEAL_INCOMPLETE. This covers a cancelled run, a run never re-run, and a scorer that is never approved.
  - No key is opened outside the scorer job until the ending is recorded.
- **Exact arithmetic.** Every recall is kept as hits / n, and every constant is an exact decimal. This means computer rounding can never flip a label or make the scorer and the independent checker disagree.
- **Named stops:** MERGE_INPUT, NO_TRACE_FILES, DOWNLOAD_FAILED and DOWNLOAD_TIMEOUT may be re-run once. CAL_INCOMPLETE is terminal and is not a MISS.
- **The bars and the sealed day list** must equal the committed CAL result.
- **The BUDGET projection** now counts the measured CAL minutes and a fixed 30 minutes for the coordinating jobs. The limit stays at 1,300 minutes.
- **One forecast added:** a SEAL_INCOMPLETE ending, 4%.

**What has been seen:**
- No AIR-U1 DEV, CAL or SEAL data has been processed.
- The only real data read so far is the census counts in manifest #4.
- CAL (2025) and SEAL (Jan–Jun 2026) data have never been downloaded.

## Fingerprint (SHA-256) of the file in the private repo Nj-StarFarer/SkyNet
| File | Bytes | SHA-256 |
|---|---|---|
| air_u1/spec/AIR_U1_SPEC_v1.3_AMENDMENT.md | 10005 | 15e81c65492b558c418eeff886491c210608543f004f4ce0f12fcb0badb9abbc |

- **Private-repo commit:** d4458db01c3da5504a73d50a11f3108ad19e6d18 (4 Oct 2026, 21:38:22 IST).
- **Fingerprint check:** the fingerprint was recomputed from the file as stored on GitHub after the commit. It matches.
- **Earlier files:** the files of manifests #5, #6 and #7 were re-hashed on GitHub at the same time. All three are unchanged.

## What does not change
- the bars;
- the seeds;
- the baselines and their budget K;
- the sizing rules N and TOO_FEW;
- the BUDGET limit;
- the split sealed run;
- the answer-key handling;
- the day permutations.

**The forecasts of v1, v1.1 and v1.2 are not edited.**

## Approval trail
- Opus wrote v1.3 after reviewing the v1.2 build (4 Oct, 20:30 IST).
- NJ: "After that brainstorming on other topics and then commit v1.3" (20:35 IST). NJ: "I trust your judgement. Opus now." (21:32 IST).
- Before the commit, an independent review found 2 blockers, 9 should-fix items and 5 notes. All were applied.
- These are statements in private chat, and they remain claims until this manifest exists.
- No AIR-U1 run has started. Runs wait for November's Actions quota.

## How to verify
1. Ask VyroNyx for the amendment file, compute its SHA-256, and compare it with the table.
2. Check that this file's commit is dated before any AIR-U1 DEV, headroom or sealed run in the GitHub Actions history.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
