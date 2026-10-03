# Manifest 2026-10-03: Angel Eyes ZERO, task ZERO-001, v1.2 build-gate inputs (manifest #1c)

Prepared on 3 Oct 2026 by Sonnet, after NJ froze specification v1.2 (06:46 IST; manifest #1b). The commit time of THIS file in this repository is the authoritative publication time.

This file is the publication that section 8.9 (item X3) of the frozen v1.2 specification requires BEFORE the build gate is run. After this commit, nothing in ZERO's code or in the training cache changes until the gate has run, and the gate is run once. Names and SHA-256 fingerprints only. No Space-Track data, no operator-log content and no answer-key content is stored here.

## The two code changes (X1 and X2) and the test results
The change from the v1.1 build is one unified diff of three files (206 lines). The v1.1 build files had these fingerprints:

| v1.1 build file | SHA-256 |
|---|---|
| zero001_core.py | fab3cceee33a71fcbb92c4e433987ac734d7c61c589eb948c0614bff9b6ff143 |
| zero001_train.py | 2aba4e0659261024eb00d568719feb2c43b33665094973ae6179fdf2c42cfadf |
| zero001_windows.py | ae7625d2b7fcc2c0ba9010fac76f07a53259d0012c22dfe2eb384ef88c0b5aae |

The v1.2 build files (the ones the gate will use):

| v1.2 build file | SHA-256 |
|---|---|
| zero001_core.py | ea5504f340514fac3d3a81c4019a3cd39f245567a6c007f985ff4acc2a037aa7 |
| zero001_train.py | 854bd074dc4c88bcd2bae57c55cde4f40edaa7c252831adaf590deca5ece3f16 |
| zero001_windows.py (unchanged) | ae7625d2b7fcc2c0ba9010fac76f07a53259d0012c22dfe2eb384ef88c0b5aae |
| ZERO001_v12_X1_X2.diff (v1.1 to v1.2, the logged diff) | 93eb050ea8f6b2c98e233410f66581ebdf5ab0cf31b85e29d358e4b1d3eb77c8 |

Unchanged frozen tools it also uses (same fingerprints as manifest #1): zero001_parse.py f72523b46c04ad7bbb09a76da929336bfa08f69c740fe2a57c360fef082eb3f6; zero001_l4.py 98f9157ee5cd7eccf7052da7e5c55c12cbc809f4f2b985f979c14fef10dfe8a1; zero001_bulk.py 728474e914d2942df7ce9d969a83371613c3afdaea4a8dc83875455af045b70d; zero001_bulk2.py 764a5b625516aea11ea9b112f132f4bc59203f5385dfedb42fb8fe6de213e5f7.

All self-tests of the three build files pass on the run machine (core 45 checks, trainer 20, window builder all), including the new tests for X1 (printed-step counts, the one-step floor, no z5 above 1,000) and X2 (largest-score label step, ties, steps before the event, empty interval).

## The training cache (rebuilt with the v1.2 code)
411 files, one per object (9 answer-key satellites, 2 development-only satellites and the 400 pool objects; an object with no usable data is stored as an empty marker), built from development and calibration orbit data only. No blind-year orbit data and no operator-log line from 2024 or later has been read. `train_cache_hashes_v12.txt` lists the SHA-256 of each cache file (411 lines); the SHA-256 of that list is:

6de314fde5236400cc0c0c52c67bf9e596be60663c52b77a18aa480ac7071963

## Run machine
Python 3.10.12, numpy 2.2.6, sgp4 2.27, scipy 1.15.3, scikit-learn 1.7.2.

## What happens next
The build gate (section 8.9) is run once: the logistic regression, the isotonic map and k_Z are fitted on development and calibration data, then ZERO's BURN flags on development and calibration operator negatives are counted against the limit of 18. The result will be reported either way. A second failure closes ZERO-001.
