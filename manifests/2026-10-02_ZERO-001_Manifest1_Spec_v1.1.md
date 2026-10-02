# Manifest 2026-10-02: Angel Eyes ZERO, task ZERO-001, frozen specification v1.1 (manifest #1)

Prepared on 2 Oct 2026 (clock tool read 22:31 IST). The commit time of THIS file in this repository is the authoritative publication time.

This manifest holds names and SHA-256 fingerprints only. No Space-Track data, no operator-log (IDS) data and no answer-key content is stored here. The specification text and the scripts sit in the private repository.

## What is being registered
The frozen specification of ZERO-001, part of VyroNyx's KingMaker Protocol (Angel Eyes ZERO). The question: does ZERO, a detector that reads only public orbit data (TLEs), find logged satellite engine burns of at least 0.01 m/s better than a standard baseline (B1), with at most half the baseline's false alarms, honest confidence numbers and a result that an independent checker recomputes? The specification fixes the data, the answer-key boxes, the windows and seeds, the baseline and its threshold, the detector's recipe, the pass rules, the named stops and the forecasts, before ZERO exists. The operator logs for 2024 and 2025 are locked and have not been read by anyone.

NJ froze the specification on Fri 2 Oct 2026 at 21:41 IST.

## Fingerprints of the committed files (SHA-256)
Private repository Nj-StarFarer/SkyNet, commit 8bd9b5ba75b036368708b65564851c9f32fc2b0b (GitHub commit time 2 Oct 2026, 16:34:22 UTC = 22:04:22 IST). Every file was read back from GitHub after the commit and its fingerprint matches the copy on NJ's computer.

| File (in the private repo) | Bytes | SHA-256 |
|---|---|---|
| angel_eyes/zero/zero001_v1.1_manifest1/ZERO-001_Specification_v1.1_FROZEN.md | 44363 | a5a759873bd64dce2da0fa8b1e12d7f76e6188e243896c042b90227c7290225f |
| angel_eyes/zero/zero001_v1.1_manifest1/MANIFEST_1_hashes.txt | 5994 | 2bbc933de2e8dd1c170dc195e75b85cfcbfa434c6bec1580207e5366100f2920 |
| angel_eyes/zero/zero001_v1.1_manifest1/ZERO001_IDS_split.py | 3580 | d99019372e0af0fbef8398cf002f816676b31548adf7d9e97e28bfaab54cf6ba |
| angel_eyes/zero/zero001_v1.1_manifest1/ZERO001_debris_pool_v3.py | 2706 | 556483c7dd40423776b59674ede4aa96a9cd1257ea32f890dd7bd31e343e5ce8 |
| angel_eyes/zero/zero001_v1.1_manifest1/diag_family2.py | 1853 | 56e27080da8fc0fdf72238149209cab1fc84337f0787e1a1f0738517c709a9bc |
| angel_eyes/zero/zero001_v1.1_manifest1/l3b.py | 4986 | 8ba7dd4b289931d7b1bf72e5dd5167c8fff295676f16d175a97d7138ee2ee140 |
| angel_eyes/zero/zero001_v1.1_manifest1/run_l3_pass.py | 2255 | 60606deeaaa55707be07a9af6fa7cde0d4dee9c4ecbaac25ab1b4421b9a73b2c |
| angel_eyes/zero/zero001_v1.1_manifest1/zero001_bulk.py | 9393 | 728474e914d2942df7ce9d969a83371613c3afdaea4a8dc83875455af045b70d |
| angel_eyes/zero/zero001_v1.1_manifest1/zero001_bulk2.py | 8499 | 764a5b625516aea11ea9b112f132f4bc59203f5385dfedb42fb8fe6de213e5f7 |
| angel_eyes/zero/zero001_v1.1_manifest1/zero001_l4.py | 27110 | 98f9157ee5cd7eccf7052da7e5c55c12cbc809f4f2b985f979c14fef10dfe8a1 |
| angel_eyes/zero/zero001_v1.1_manifest1/zero001_l4_v1_before_N.py | 23470 | beefadcce2d3f93812a9355f97ee8cacbdbea065beb01e45ba066271b91d2981 |
| angel_eyes/zero/zero001_v1.1_manifest1/zero001_parse.py | 20936 | f72523b46c04ad7bbb09a76da929336bfa08f69c740fe2a57c360fef082eb3f6 |

`MANIFEST_1_hashes.txt` lists the fingerprint of every item below, so the one line above covers them all.

## Fingerprints of the data and derived files (hash only; the files are not stored anywhere public)
These were re-computed on NJ's computer on 2 Oct 2026 and match Appendix A of the frozen specification. Their paths are under the Downloads folder of that computer.

| File | SHA-256 |
|---|---|
| ZERO001_IDS_raw/cs2man.txt | a2d83bdcf5661525a696dd636a670e31f3e55f5d38649e29e55f492d3a1e064b |
| ZERO001_IDS_raw/h2aman.txt | f4ede7f09cdf04c507f1e7f2c287b4e2652c3fc82f833024c8d66a1b43f47850 |
| ZERO001_IDS_raw/h2cman.txt | 084ad5720077cedf018dfce08621dd5bb3dfab7b8a32e3ada55875abc79b8ac1 |
| ZERO001_IDS_raw/h2dman.txt | 610ebe269f6e53d33f3a2bdc38a3f844fe39d7cf25639a806e5d3ab95c308797 |
| ZERO001_IDS_raw/ja2man.txt | 63f5d6cfc300d942fb1906fa10f03022a08c8702ef087631c9dbd33bf7fe0d38 |
| ZERO001_IDS_raw/ja3man.txt | 1216a388c6972b9c9dfc8f8eb3b1e1503af4522b19d68346e14f09a5eb5f4fb8 |
| ZERO001_IDS_raw/s3aman.txt | 2e227a3eee368b1c8ce134a01f8246472e491527a76c9408b2635c1270e565c9 |
| ZERO001_IDS_raw/s3bman.txt | 4e55becbc22bcfa3e37f2b1dfb12dafc9b598afa93824763b656869faae8c9d0 |
| ZERO001_IDS_raw/s6aman.txt | 9edd03cb3542e6be0754e6480a5b670fd3060ebd7e2b9cb8f368673ca253ecc3 |
| ZERO001_IDS_raw/srlman.txt | 2b87977470ad3f32284ede1361b8c14dbbc888dfa249744fd499623f6d332ceb |
| ZERO001_IDS_raw/swoman.txt | 6ff7b618efe20e63c43e9cbe16eecd67635472e38a6a34bc040094e14b75793c |
| ZERO001_IDS_raw/man.readme | 56f009242d8d5a3482dfb403580563e3ba1aa6885ed406a37e043cf7daca003d |
| ZERO001_IDS_split.py | d99019372e0af0fbef8398cf002f816676b31548adf7d9e97e28bfaab54cf6ba |
| ZERO001_IDS_split/SPLIT_MANIFEST.txt | 75747142c83990a3fed6f2b15c396dd25c3c16ca3900aa9cd362d47c610e3eb4 |
| ZERO001_25544_ISS_gp_history_2020-12-01_2023-12-31.tle | 0bb36012d71785cdecc73f8fc7dffceacf8d84b21e8d9aec70d806a06b44cce2 |
| ZERO001_36508_CRYOSAT2_gp_history_2020-12-01_2023-12-31.tle | c7290cae14565c6cf1c548934d126f6b0af823dea532fe516bbfed3b46e7d6bd |
| ZERO001_39086_SARAL_gp_history_2020-12-01_2023-12-31.tle | a508e05306f80ce21a0f8e6a1e9f9540b685c75cc908b20e59a5d3865adc6559 |
| ZERO001_41240_JASON3_gp_history_2020-12-01_2023-12-31.tle | 2d18388f64e94caa3bee95dff8eaaf35c11f90134c02a45ca1bed0a5c443eafb |
| ZERO001_41335_SENTINEL3A_gp_history_2020-12-01_2023-12-31.tle | 02c415701317b9863a86846a1d67c5fdbe3c91156dc9682c9f3ad0b31b445a5b |
| ZERO001_43437_SENTINEL3B_gp_history_2020-12-01_2023-12-31.tle | 9fd2713aa7925ef04d9cbf2dd436a3cf09a2942e51fd32afb3adf8c8c0bee01c |
| ZERO001_46469_HY2C_gp_history_2020-12-01_2023-12-31.tle | e97f6ec86726266c6dbe6d0f51780e0cab08cc1c098355d5fd195e544ae8d258 |
| ZERO001_46984_SENTINEL6A_gp_history_2020-12-01_2023-12-31.tle | 8d6d74cdcc2cdcef581a0933a3c0287f76de0b2035e715ce4db77bc94dc6f0a9 |
| ZERO001_48621_HY2D_gp_history_2020-12-01_2023-12-31.tle | 70665ba766f6f9194f0acc5f9daea29a0b177b540c421887426937576da1585d |
| ZERO001_54754_SWOT_gp_history_2020-12-01_2023-12-31.tle | 493f3bb2d7c37203c3af9810e4b1f52afdb90bfc2dbbdca7a434f2c81eb913fb |
| SATCAT export from Space-Track (file name withheld) | 60beac9d1e181a95499a5af4b37dfe215b19645ff4c0f34dca3d051eb4b715cd |
| ZERO001_GFZ/Kp_ap_Ap_SN_F107_since_1932.txt | cfd3c7dcf021f1d4125f8ecc71a8c5edcb13efe228d111fead95b628e3ba5b4e |
| ZERO001_bulk_extract/pool_final_400.csv | 0458b78dbf09f2bc761425079e6336ba26f037e5db5dad07972992468987e02b |
| ZERO001_bulk_extract/pool_candidates_1200.csv | 26e47aa7789454c73827cd36dc6a1b6e55e9af6b2121539b19781f60d8d513a7 |
| ZERO001_bulk_extract/exclude_ids.txt | a391a7fa6db3aeace02796a52ee44468bd8456a47593c79ada6d8a1f2fbdc118 |
| ZERO001_bulk_extract/bulk2018_extract.txt | fc56bdce32493791a74defa570cc0d0f9fad3b0b25f0697c2dfe83dd3f26b04b |
| ZERO001_bulk_extract/bulk2019_extract.txt | fe720477964b0d9c11cc8f21d091da4dad06d58c7615dcb0efc8fd24c978ba4a |
| ZERO001_bulk_extract/bulk2020_extract.txt | 4240881a1e22ac50bb6cb8d6de552e9029627fce214704cebd49f48b4b55ccca |
| ZERO001_bulk_extract/l4_window_manifest.csv | 4deb1db5ec7a08e0c5187f036bb75afe76a3c0272f9fec2a4f350009ca6b4ca9 |
| ZERO001_bulk_extract/l4_run_v2_output.txt | 1f7479c772d76e7e900653829ebaa8a149170cebaaa86c99083304c719e46c33 |
| ZERO001_bulk_extract/l4_sats.pkl | fc592dba94b6ee8f9243e5ac92e38fe71deda146cf94cb0cbcda8f6089cf8aa9 |
| ZERO001_bulk_extract/l4_debris.pkl | 4e18a5ee1e2241c0ba51213447d6f079e28a11c0b83171f2f587ac8dd52aff8e |
| tle2018.txt.zip | 17020755cf936c6054703aee071869c5949e384215b36634b1de9c04b89950c8 |
| tle2019.txt.zip | 4ab35c498803caf6bae7d48910ef9c200caa0e8610fc589e4310dc01146a7dd5 |
| tle2020.txt.zip | 582ee6b9c9305e3d8443aa748439be728535cb19e67bcda55bbd8674c981941e |
| zero001_burn_list_candidate_v0.json | b89d48ccc4eb4e3d67068d2f2f0236b7ac8400418804f50efcf614ada9b9cedc |

The last row, the ISS burn list, is not on the computer yet; its value is the one recorded in the specification. It must be found and checked before the run.

## State at publication (22:31 IST)
- The specification is frozen and committed. Nothing else has been built: ZERO, the window builder, the scorer and the checker do not exist yet. They will be fingerprinted in manifest #2, before the run.
- The 2024 and 2025 orbit files have not been downloaded. They will be downloaded only after NJ types the run phrase.
- The sealed operator-log box (2024-25) and the reserve box (2026 onward) have not been opened by anyone. The split files and their line counts are fingerprinted above (`SPLIT_MANIFEST.txt`).
- No ZERO result exists.

## What this manifest proves, and what it does not
- It proves that files with exactly these fingerprints existed no later than the commit time of this file, and therefore before ZERO was built and before any result exists.
- It does NOT by itself prove the earlier private commit time (22:04:22 IST). VyroNyx can show that commit on request.
- It says nothing about what ZERO-001 will find. The forecasts are inside the registered specification.

## How to verify
Ask VyroNyx for a file from the first table. Compute its SHA-256 (for example `shasum -a 256 ZERO-001_Specification_v1.1_FROZEN.md`) and look for the same string above. Then check that this file's commit in this repository is dated before the run.

## Pending
An independent timestamp proof (for example OpenTimestamps) over this manifest has not been added yet. It will be added in a later commit, and this file will not be edited.
