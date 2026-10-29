# Manifest 2026-10-29 (10): DOD-G2 "real gusts through a real forest", data split (pre-registration)

The commit time of THIS file is the authoritative publication time.

- **Data:** "The motion of trees in the wind: a collection of multiple data sets" (Jackson et al. 2021), Zenodo record 4915883, CC BY 4.0. Each site has several trees whose sway was recorded at the same moments as a 3D sonic anemometer, at 10 Hz.
- **The split, fixed before any analysis of Kershope:**
  - **Development (open to Claude and SkyNet):** Rivox.zip. 3 Sitka spruce (T1, T2, T4) plus sonic, 10 recording days, 1988.
  - **Sealed (not unzipped until the DOD-G2 spec is frozen and published):** Kershope.zip, a different forest. Pairs of Sitka spruce recorded on the same days plus sonic, 1989–1990.

| File | Bytes | SHA-256 |
|---|---|---|
| Rivox.zip | 17068498 | 329cf28e9c381ebcfadb365308430c7482871c95c40a842369324b0c02761b1c |
| Kershope.zip | 32382569 | 942b1bae1f32ac7a37f6ce7435ac93b780e2916b42cb1b298b08a7edaea157dc (added before unzipping) |

- **State at publication:** the Rivox CSV headers and row counts have been read. No analysis has been run. Kershope's only exposure so far is its zip file list, read in the browser to check that it contains simultaneous trees, plus one 6-row header sample. No series was analysed.
