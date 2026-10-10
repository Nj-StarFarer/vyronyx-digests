# Manifest 2026-10-10 (KM-055 #4): Catcher in the Sky, the seal (step 2 done)

Prepared on 10 Oct 2026 by Opus. Published on NJ's instruction ("Publish it", 10 Oct 2026, 14:44 IST).

The commit time of THIS file is the time the sealed test set is fixed. **No catcher, rival, practice scenario or practice generator exists yet.** This manifest holds names, numbers and salted SHA-256 fingerprints only.

## 1. What was sealed
The sealed-side session made the sealed sets under the frozen spec v1.2, Amendment 1 and Amendment 2 (manifests KM-055 #1–#3). It works in a separate private repository that the catcher builder never sees, at commit `42329c0`.

| Item | Question A (micro camera drones) | Question B (fast, erratic FPV-type drones) |
|---|---|---|
| Scenarios | 450 (9 kinds × 50) | 450 (9 kinds × 50) |
| Normal / should-abort | 405 / 45 | 405 / 45 |
| Should-abort types (each) | 8, 8, 8, 7, 7, 7 | 8, 8, 8, 7, 7, 7 |
| Every file check passed | 450 / 450 | 450 / 450 |
| Secret-kind hardness checks (Part R) | 50 / 50 | 50 / 50 |
| Normal hand-offs passing the frozen validator | 133,650 (0 refused) | 133,652 (0 refused) |
| Unwinnable (reference planner) | 0 of 405 normal | 0 of 405 normal |
| TOO_MANY_UNWINNABLE | no | no |
| Remakes | 6 path remakes (4 reversal, 2 airspeed) | 11 trigger-rule remakes; 13 path remakes (11 progress, 2 K8 segment) |

**No target in either set reacts to the catcher** (Amendment 1, Part R). This is enforced by a code test.

## 2. Salted SHA-256 fingerprints
The salts and the master seed are kept private and are revealed after the catcher and rival hashes are published (spec §10 step 4).

| Item | Salted SHA-256 |
|---|---|
| Sealed-side code tree (15 files) | `9658caf1b3c3b327a113cae3917a150fea9112e27f71b6f9be8080be9d375d0f` |
| Set A | `a8c25f204179827f3dd2b04983f1e68b72f53cb7d46a3a58300dfe5a153c943e` |
| Labels A | `fe685cb83babf4bd57f7ffc55fb62999ee7840fb6b6f6c28aedc9ebe5243a8ee` |
| Planner results A | `f578fe569b0033b2b01af1a2055300d1442d79cd06bafd91270ca05f635bd504` |
| Unwinnable flags A | `55346be9e262a21a02f4625e06becf051ccd803e6ad794fc4308ea686d633a27` |
| Set B | `c2bcbe692ea6e807ca6adf38231ad9fbf0c280c7343432f549e1a4561aa03e9f` |
| Labels B | `c4864b409d75776e2bc1f931c5d72784e735aff63c7dcad809d1ac230bea017f` |
| Planner results B | `627728277adacf3830ec1d98292833070c6bde6a8dacff4061c810170063d99b` |
| Unwinnable flags B | `d1a877043489dc227ce10082cfddd9be393e01f0b943cfccb85ded620b413300` |

## 3. How it can be checked later
- The sealed files are regenerated from the private seed, and every file hash is checked. The sealed-side session ran this once and every hash matched.
- At the reveal, anyone with the salts can recompute the fingerprints above.

## 4. Honest notes
- An unwinnable count of 0 is what a reference planner that knows each target's whole path should find. It does not mean the test is easy for a catcher that does not know the path.
- **This is level 1 of a ladder.** Harder sealed tests will follow, each fixed and published before it runs. They will turn up target speed, sensor noise, crowding, wind and tip-off quality, then add the trouble-finder. The results show exactly where the catcher breaks.

## 5. Next
Step 3 (spec §10): the catcher builder makes the simulated world, the practice generator, the catcher and the rival, using practice scenarios and the spec texts only.

*Opus · 10 Oct 2026*
