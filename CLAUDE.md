# CLAUDE.md

> **This is the maintained HA integration for the OSS `home-mind` server.**
> It is *not* legacy — it was mislabelled as such for a while (2026-04 → 2026-08)
> because the Nives add-on stopped needing it. Nives ships its **own** integration
> from `nives/nives/rootfs/opt/nives/`; that copy and this one are independent and
> must not be synced. Edit this repo for anything that reaches OSS home-mind users.
>
> Priority: **Nives is where new development happens**; home-mind and this
> integration stay maintained, and changes that belong in both are ported across
> deliberately — never copied on autopilot.
>
> Note: the copy vendored at `home-mind/src/ha-integration/` is an old snapshot
> (v0.9.3, no API-token support). This repo (v0.10.0+) is the current one.

---

This file provides guidance to Claude Code when working with code in this repository.

## What This Is

**home-mind-hacs** is the Home Assistant custom component for Home Mind. It registers as an HA conversation agent, forwarding voice/text input to the home-mind-server API and returning responses to HA Assist.

Distributed via [HACS](https://hacs.xyz/) (Home Assistant Community Store).

## License

AGPL-3.0 — this is an open-source project. Do not introduce any code, imports, or dependencies from the closed-source repos (`home-mind-cloud`, `home-mind-proxy`, `home-mind-app`).

## Architecture

```
HA Assist (Voice/Text) → home_mind conversation agent → home-mind-server API (/api/chat)
```

The component is a thin HTTP client. All intelligence lives in the server.

## Key Files

```
custom_components/home_mind/
  __init__.py          — Integration setup, config entry loading
  config_flow.py       — Setup wizard (API URL, token, user ID)
  conversation.py      — ConversationAgent implementation (chat + streaming)
  const.py             — Constants (domain, defaults, endpoints)
  manifest.json        — HA integration metadata, HACS config
  strings.json         — UI strings for config flow
  translations/en.json — English translations
```

## Config Flow

Two-step validation in `validate_input()`:

1. **Reachability**: `GET /api/health` (unauthenticated) — checks server is up
2. **Token validation** (if token provided): `GET /api/memory/{userId}` with `Authorization: Bearer <token>` — checks for 401/403

This two-step approach is necessary because `/api/health` bypasses auth middleware. Without step 2, any random string would be accepted as a valid token.

### Options Flow

After setup, users can configure `custom_prompt` via the integration options (OptionsFlow). This overrides the server's default system prompt personality.

## Conversation Agent

`HomeMindConversationAgent` in `conversation.py`:
- Detects voice vs text via `user_input.agent_id is not None`
- Sends `isVoice=true` to server for voice interactions (server uses shorter prompt)
- Uses `intent.IntentResponse` (not `conversation.IntentResponse`)
- Conversation IDs: `ulid.ulid_now()` (not UUID)
- 120-second timeout for API calls (LLM tool-using responses can take 60+ seconds)
- Supports both `/api/chat` (full response) and `/api/chat/stream` (SSE)

## Development

No build step — Python source is the distribution. Test by copying to HA's `custom_components/` directory or installing via HACS.

HACS installation uses the GitHub repo URL: `https://github.com/hoornet/home-mind-hacs`

## Versioning

Version is in `manifest.json`. Releases are tagged on GitHub (e.g., `v0.10.0`). HACS picks up new versions from GitHub releases.

## Related Projects

- `homemind-projects/home-mind` — the server this component talks to
- `homemind-projects/nives` — the add-on; ships its own integration, independent of this one
- `homemind-projects/nives-cloud` — subscription/billing (closed, irrelevant here)
- `homemind-projects/Legacy/home-mind-proxy` — retired LLM proxy (no live deployment)
