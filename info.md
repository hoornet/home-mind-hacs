## Home Mind

A Home Assistant conversation agent with a memory that survives between conversations. Tell it once that 100 ppm is normal for your NOx sensor, or that the WLED strip is "the main kitchen light", and it still knows next week.

### Features

- Natural language control of your smart home
- Persistent memory that learns your preferences, routines and device nicknames
- Semantic recall with cognitive memory — not keyword matching
- Ask it to forget something, and it confirms before deleting
- Multi-turn conversations and real-time sensor queries

### Requirements

A running [Home Mind server](https://github.com/hoornet/home-mind) — it handles the AI provider (Anthropic, OpenAI, or a local model via Ollama), the memory store, and Home Assistant tool execution. This integration is a thin client.

### Quick start

1. Install and run the Home Mind server
2. Install this integration via HACS
3. Add the integration in Home Assistant settings
4. Enter your server URL (and API token, if you've set one)
5. Set it as your conversation agent under Voice assistants

### Not running the add-on, are you?

If you use the [Nives](https://github.com/hoornet/nives) add-on, it already bundles its own integration — installing this one too will conflict. This is for people running the Home Mind server themselves.
