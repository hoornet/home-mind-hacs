# Home Mind — Home Assistant integration

The companion integration for the [Home Mind](https://github.com/hoornet/home-mind) server. Install it through HACS, point it at your server, and Home Mind becomes a conversation agent in Home Assistant Assist — with a memory that survives between conversations.

This is the current, maintained integration for the open-source Home Mind server, and the recommended way to install it.

> **Running the [Nives](https://github.com/hoornet/nives) add-on?** Then you don't need this. Nives bundles its own integration and installs it for you — adding this one as well will conflict. This repo is only for people running the Home Mind server themselves.

## Features

- **Natural language control** — talk to your home in plain sentences
- **Persistent memory** — preferences, device nicknames, routines and baselines, remembered across conversations
- **Semantic recall** — cognitive memory with Hebbian learning, so the right context surfaces at the right moment
- **Multi-turn conversations** — follow-up questions keep their context
- **Live data** — real-time sensor readings and device states

## Installation

### HACS (recommended)

1. Open HACS in Home Assistant
2. Click the three dots in the top right corner
3. Select **Custom repositories**
4. Add `https://github.com/hoornet/home-mind-hacs` as an **Integration**
5. Click **Add**
6. Search for **Home Mind** and install it
7. Restart Home Assistant

### Manual

1. Download the latest release from the [releases page](https://github.com/hoornet/home-mind-hacs/releases)
2. Copy `custom_components/home_mind` into your Home Assistant `config/custom_components/` directory
3. Restart Home Assistant

> Install from here rather than copying the older snapshot vendored in the server repo — that copy predates API token support and can't authenticate against a server with `API_TOKEN` set.

## Configuration

1. Go to **Settings → Devices & Services → Add Integration**
2. Search for **Home Mind**
3. Enter the URL of your Home Mind server (e.g. `http://192.168.1.100:3100`)
4. If you've set `API_TOKEN` on the server, enter that too
5. Complete the setup

Then set it as your conversation agent: **Settings → Voice assistants → (your assistant) → Conversation agent → Home Mind**.

You can also give it a personality later under **Settings → Devices & Services → Home Mind → Configure** ("custom prompt"). Whatever you write there replaces its default identity.

## Requirements

A running [Home Mind server](https://github.com/hoornet/home-mind), which handles the AI provider, memory storage (Shodh Memory), and Home Assistant tool execution. This integration is a thin client — all the intelligence lives in the server.

## Usage

Once configured, Home Mind appears as a conversation agent in Assist. Use it from the Assist dialog, set it as the default agent for a voice pipeline, or reach it through Wyoming-protocol voice satellites.

### Example commands

- "What's the temperature in the living room?"
- "Turn on the bedroom lights"
- "Set my preferred temperature to 22 degrees" *(saved to memory)*
- "Make it warmer" *(uses context from the previous turn)*
- "Forget that my preferred temperature is 22" *(it confirms before deleting)*

## Would you rather not run a server?

[**Nives**](https://github.com/hoornet/nives) is the same engine packaged as a single Home Assistant add-on — server and memory in one container, this integration installed for you, no Docker and no terminal. It's where most new development happens, and it has grown things Home Mind doesn't have (creating automations from conversation, an AI Task provider, camera-snapshot vision).

Home Mind stays maintained and open source, and the things that belong in both get ported across. If you like running your own stack, you're in the right place.

## Links

- [Home Mind server](https://github.com/hoornet/home-mind) — the server this talks to, and full documentation
- [Issues](https://github.com/hoornet/home-mind/issues) — bugs and feature requests for either piece
- [Nives](https://github.com/hoornet/nives) — the one-click add-on version

## License

AGPL-3.0
