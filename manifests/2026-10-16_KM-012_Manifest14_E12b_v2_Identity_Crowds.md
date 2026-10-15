# Manifest 2026-10-16 (KM-012 #14): E12b v2, identity in crowds (simulation). PASS under the frozen v2 bars; MISS under E12's old bars

Prepared by Opus, under NJ's standing delegation. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `bda4a30a`.

| File | SHA-256 | Bytes |
|---|---|---|
| `docs/kingmaker/E12B_SPEC.md` (frozen v2 spec and the result) | `5180de7fcd4df899e3d7dfa5d9a50baf1cd26005e5c5fe45192c0e6780aa2acf` | 11461 |
| `angel_eyes/identity/sealed_e12b_v2/seeds.json` (drawn after freeze `be9df6ea`; hash committed first in `a741c235`) | `288162e36bfa1c78c25ec4e78dd3ab86905c311a10dec767822db6b71752f1f6` | 2534 |
| `angel_eyes/identity/sealed_e12b_v2/result.json` | `da49905f0c25c3453de6e4c9b3efc679a0dcd64e788f8ddc6495348599fe73f3` | 8184 |
| `angel_eyes/identity/calibration_e12b_v2.json` (frozen) | `c062b326a2dfbf81093b37a8c2bd8e5b7681764eb564a96a51b3e8f6273937fc` | — |

- **Test:** simulated crowds of 10, 100 and 1,000 flying objects (synthetic — bookkeeping of identity, not a sensor).
  Does Angel Eyes' identity braid, when it says it is sure, beat a standard tracker — with honest odds?
- **PASS (v2 bars):** sure claims wrong 3.2% of the time vs the tracker's 16–33%; sure on 32–63% of claims (above the
  floor); odds calibrated over all claims (error 0.010–0.017); utility beats every rival (lower bounds +0.16 to +0.35);
  ledger verifies; 269 ms per frame at 1,000 objects.
- **MISS (E12's old bars), reported side by side:** calibration averaged per scene at 10 objects was 0.102 (bar 0.10).
- **Bar changes before the freeze, stated:** plain accuracy replaced by NJ's new I1 mark (15 Oct 18:12 IST);
  calibration measured over all claims rather than averaged per scene (in a 10-object scene every claim rides on the
  same few swaps). These two changes separate PASS from MISS.

*Opus · 16 Oct 2026*
