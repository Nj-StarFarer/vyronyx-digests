# Manifest 2026-10-10 (AIR-D1 #3): the v1 LEAKAGE stop, and Amendment 2 in force

Prepared on 10 Oct 2026 by Fable. Published under NJ's delegated decision ("Take decision", 10 Oct 2026, 18:26 IST).

The commit time of THIS file is the time Amendment 2 comes into force. This manifest holds names, numbers and SHA-256 fingerprints only. **No sealed score exists**, and no sealed or buffer file has been opened by any build or seal session.

## 1. The stop, reported first
The near-duplicate check v1 (full-frame dHash, spec v0.4 §4) ran on a separate GitHub-hosted runner on NJ's typed phrase and **fired LEAKAGE**: more than 5% of the 177 sealed video clips matched a practice clip within 10 bits. Under the frozen rules that stopped the test before any model saw a sealed file. The stop stands in this record.

## 2. The diagnosis, on practice files only
32.6% of IR and 52.3% of visible **practice** clips match a **different-class** practice clip under v1's rule. A duplicated recording cannot change class, so v1 measured shared sky and camera background. A second candidate (object-crop dHash) was also rejected, with its failure numbers on record.

## 3. Amendment 2
Repository `Nj-StarFarer/SkyNet`, commit `88c094b`:

| File | SHA-256 | Bytes |
|---|---|---|
| `angel_eyes/air_d1/AIR_D1_AMENDMENT_2.md` | `80461ebdb597c3032d1d663c0c134b756212911a5fb3f42d8cc7d7d8d71e0800` | 3,454 |

The v2 instrument compares the labelled object's **track** (centre path over time) between sealed and practice clips: offset ≤ 30 frames, overlap ≥ 30 frames, median centre distance ≤ 4.0 px, motion ≥ 10.0 px on both sides. It reads label files only. Frozen rule text: `NEARDUP_V2_RULE.md`, SHA-256 `44463323f686006939da79bf398bc8ce6eb6c6677dace3cef565cf10068b7647`, private repo commit `0b24ab5`.

**Validation, practice only:** 60/60 planted duplicates caught (re-encode, trim, trim + re-annotation jitter); cross-class false matches 32.6% / 52.3% → 0.00% / 0.00%; same-class 1.19% / 1.30% (consecutive-number same-flight pairs, already covered by Amendment 1's buffer).

## 4. Pre-commitment
**If v2 also flags more than 5% of sealed video clips, LEAKAGE stands, there is no further amendment, and the test moves to a new dataset.** Frozen before v2 has seen any sealed file.

## 5. Honest limits
- The sealed tail is later recordings of the **same campaign**; that limit stays in every claim whatever v2 finds.
- v2 was designed after v1 fired. Its protections: tuned on practice only, published before any score, and able to fail by the pre-commitment above.

## 6. Next
1. v2 runs on the separate runner, on NJ's typed phrase.
2. If it passes: the final sealed list is fixed, the pre-run manifest is published, and one sealed run follows on NJ's typed phrase.
3. If it fires: the stop is final and the next manifest names the new dataset plan.

*Fable · 10 Oct 2026*
