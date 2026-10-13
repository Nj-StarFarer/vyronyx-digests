# Manifest 2026-10-13 (KM-061 #4): Whitman Rung 1, PRE-RUN correction. New build hash after a workflow fix

- **Prepared and published:** 13 Oct 2026 by Opus, on NJ's instruction "Do everything yourself".
- **Contents:** names, numbers and SHA-256 fingerprints only. No data, no code, no secret.

## What happened

- The first start of the sealed run (GitHub Actions run `38343445569`) **stopped before any download**.
  - Its pretest job passed: the frozen files, the open pack and the sandbox proof checked out, and every self-test ran with no network.
  - The next step, the one-run guard, then failed. It ran `git fetch` without credentials on a private repository.
- **No sealed data was fetched, cut, planted or seen.** No seed was drawn and nothing was committed.
- Under spec v1.0 §8, a stop before outputs is fixed and run again.

## The fix

- Only `.github/workflows/whitman-r1-sealed.yml` changed. The guard now reads the history that the checkout already holds.
- Its SHA-256 changes from `23e9bb17…25a6` to `5c5924d55eb672fc1585dd93377068773793ed0166eb02aaefe19bb49722e19a`.
- **Every other frozen file is byte-identical to Manifest #3:** the spec, amendment A2, the detector code and models, the reader, the planting script and the second scorer.

**New build hash = SHA-256 of `r1/FREEZE_SHA256SUMS.txt`, at repository `VyroNyx/whitman` commit `aac59b23b27a208014514da67f69335e246da4f1`:**

`bffd61b23d5ac04b4606cf779cdb79d32f8cf18857f8697a10fc700dad87f47c`

It replaces `2699e43f…620d8e` from Manifest #3 and is the hash typed into the run.

*Opus · VyroNyx Private Limited · 13 Oct 2026*
