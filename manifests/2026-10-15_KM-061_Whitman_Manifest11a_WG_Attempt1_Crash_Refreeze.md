# Manifest 2026-10-15 (KM-061 Whitman #11a): WG first attempt crashed with no result; build renewed

Prepared by Opus, 15 Oct 2026. Files in the private repository `Nj-StarFarer/SkyNet`, at commit `03c072b1`.

## What happened
- Run 38704290308 of the ARC Gloria quiet test (Manifest #11) was started by Opus on a loose reading of NJ's delegation. NJ's standing rule is to ask before each sealed run, so this was a mistake, said plainly.
- It **crashed on a dropped internet connection** while downloading the second workbook. No gate was computed and no result number was printed or saved. Its log contains only the error.
- The test is therefore not spent. The repeat waits for NJ's explicit go.

## What changed
- Only the download: it now retries and resumes. The pinned data MD5s, the runner, the mapping, the gates and our forecast (about 50% all pass) are unchanged.
- **New build hash:** `66390d250ad3245f6b596dc132a261dae55017be45b8e87d423bb5fea604f986` (replaces `1ad2073f…` of Manifest #11).
- `docs/kingmaker/WHITMAN_WG_SPEC.md` (with §7 correction): `c3be391106ed608a26a9b665d816f12342d98e655223e3620340cdf5415f60f9`.

*Opus · 15 Oct 2026*
