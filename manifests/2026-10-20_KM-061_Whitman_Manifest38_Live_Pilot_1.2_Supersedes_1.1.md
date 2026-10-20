# Manifest 2026-10-20 (KM-061 Whitman #38): Whitman Live pilot build 1.2 supersedes 1.1, before any vessel

Prepared by Opus, 20 Oct 2026.

## Why 1.1 is replaced

An independent fact-check of the pilot proposal found a flaw in build 1.1 (Manifest #37): complete days were judged 6 hours after their last hour. Every alert raised by the daily rule (the same thing on 2 of the last 3 days) therefore went out about 6 hours after its data, which breaks the frozen 2-hour "alert speed" mark. In the 1.1 rehearsal, both warnings came from the daily rule. The hourly window rule raised none: where it matched the fault, the window had fewer than the 6 steady hours it needs.

## What changed in 1.2

- A day is judged **1 hour** after its last hour arrives.
- The alert text is plainer. The crew answers by replying to the alert; VyroNyx seals the reply word for word, and the independent checker confirms it.

Nothing else changed: the engine, the window rule and the scorer (`live_score.py`, same SHA-256 as in #37) are the same. The live pass marks are unchanged; the criteria file only adds one sentence saying that a warning from either rule raises an alert. No vessel has been chosen, so this is allowed: a change starts a new build, never a running pilot.

| Item | SHA-256 |
|---|---|
| `whitman-pilot-1.2-live/SHA256SUMS` (the build's one fingerprint; commit `5f8ae03`, tag `whitman-pilot-1.2-live`) | `02ea5c63b36f105d8c76cef62c084ba250ecee5b4b885fb4afbb351dc13f45cd` |
| `whitman-pilot-1.2-live.tar.gz` | `031154c02c4c825a25d149d440152b612b044b89347e28c255bce658d63af8cf` |
| `whitman_live/live.py` | `c961a68f444a9d0d0ba9a0b050cca9f509c714c91308009b178476f092fca1c7` |
| `whitman_live/live_score.py` (unchanged) | `4ea7213a6be4fe34f5ff654b3ec79aceb85c10046d67535a9312d9ca5262d51a` |
| `docs/kingmaker/WHITMAN_LIVE_PILOT_CRITERIA.md` | `9d41e08f163498d192b810f1f66182ef8c0f89ac6c5f928811c76a7304b81a1b` |

*Opus · VyroNyx Private Limited · 20 Oct 2026*
