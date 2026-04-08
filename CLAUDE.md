# CLAUDE.md

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

- `/home/hoornet/projects/home-mind` — The server this component talks to
- `/home/hoornet/projects/home-mind-cloud` — Cloud hosting (closed, irrelevant to this component)
- `/home/hoornet/projects/home-mind-proxy` — LLM proxy (closed, transparent to this component)
