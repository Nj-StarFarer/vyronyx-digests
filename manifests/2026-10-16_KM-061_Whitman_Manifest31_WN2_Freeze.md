# Manifest 2026-10-16 (KM-061 Whitman #31): WN2 freeze — a heat pump Whitman has never seen

Prepared by Opus, 16 Oct 2026. Private repository `Nj-StarFarer/SkyNet`, commit `cb4250a`.

- **Why:** WN failed because Whitman was too timid (#30). The fixes must be proved on fresh data. This is a different machine (NIST's 2006 split heat pump), like moving Whitman to a new vessel that has only its own healthy running to learn from.
- **Data:** 135 tests with 7 fault types: charge too low or too high, blocked outdoor coil, low indoor airflow, liquid line restriction, a leaking compressor valve, and air in the system.
  - Two censuses read only the labels and the test plan (conditions and fault levels), never a reading.
- **Method (frozen):**
  - each test is compared with this machine's own fault-free test at the same NIST condition;
  - frozen physics patterns name the fault;
  - near-twin patterns give a shortlist, not a guess.
  - The simple one-gauge rule gets the same normal, the same noise and its own bar.
- **Gates** (healthy tests count for both sides):
  - G1: beats the simple rule, including when "air in the system" is left out;
  - G2: at least 20 hard faults named, at least 60% right;
  - G3: beats the best constant answer;
  - G4: at most 1 false alarm on 8 healthy tests;
  - G5: every test answered.
- **Audits:** two independent checks before freezing found 5 blockers and many smaller issues, all fixed.
- **Build hash:** `0b23a90c49480b0357db8bb70150079463f942c1d7d896ba2eb596fdb324fef1`.
- **Forecast:** about 35% that all gates pass. G1 is the hardest.
- **Limit, stated up front:** one lab machine, few healthy tests, and a cautious noise that may make Whitman shy again.

*Opus · 16 Oct 2026*
