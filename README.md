# Home Mind

A Home Assistant conversation agent powered by Claude AI with persistent memory.

## Features

- **Natural Language Control**: Control your smart home with conversational commands
- **Persistent Memory**: Remembers your preferences, device nicknames, and patterns
- **Semantic Search**: Uses cognitive memory with Hebbian learning for intelligent recall
- **Multi-turn Conversations**: Supports follow-up questions and context
- **Live Data**: Queries real-time sensor data and device states

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Click the three dots in the top right corner
3. Select "Custom repositories"
4. Add `https://github.com/hoornet/home-mind-hacs` as an Integration
5. Click "Add"
6. Search for "Home Mind" and install it
7. Restart Home Assistant

### Manual Installation

1. Download the latest release from the [releases page](https://github.com/hoornet/home-mind-hacs/releases)
2. Extract and copy `custom_components/home_mind` to your Home Assistant `config/custom_components/` directory
3. Restart Home Assistant

## Configuration

1. Go to **Settings** > **Devices & Services** > **Add Integration**
2. Search for "Home Mind"
3. Enter the URL of your Home Mind API server (e.g., `http://192.168.1.100:3100`)
4. Complete the setup

## Requirements

This integration requires a running [Home Mind API server](https://github.com/hoornet/home-mind). The API server handles:

- Claude AI integration
- Memory storage (Shodh Memory)
- Home Assistant tool execution

## Usage

Once configured, Home Mind appears as a conversation agent in Home Assistant Assist. You can:

- Use it via the Assist dialog in the HA interface
- Set it as the default agent for voice assistants
- Access it through Wyoming-protocol voice satellites

### Example Commands

- "What's the temperature in the living room?"
- "Turn on the bedroom lights"
- "What lights are on?"
- "Set my preferred temperature to 22 degrees" (saves to memory)
- "Make it warmer" (uses context from previous conversation)

## Links

- [Main Repository](https://github.com/hoornet/home-mind) - API server and full documentation
- [Issues](https://github.com/hoornet/home-mind/issues) - Report bugs or request features

## License

AGPL-3.0
