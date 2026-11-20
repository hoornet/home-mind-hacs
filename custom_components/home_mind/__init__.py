"""Home Mind integration for Home Assistant."""
from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING
from urllib.parse import quote

import aiohttp

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import CONF_API_TOKEN, CONF_API_URL, CONF_USER_ID, DEFAULT_USER_ID, DOMAIN

if TYPE_CHECKING:
    from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.CONVERSATION]


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Home Mind component."""
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Home Mind from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(_async_update_listener))

    if (entry.data.get(CONF_API_TOKEN) or "").strip():
        entry.async_create_background_task(
            hass, _async_use_api_token(hass, entry), "home_mind_use_api_token"
        )

    _LOGGER.info("Home Mind integration loaded")
    return True


async def _async_use_api_token(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Send the API token once, as soon as the entry has it.

    Since 0.21.0 the server requires a token it generated from the first
    request that carries it. Sending it at load protects the API from the
    moment the token arrives instead of from the next conversation. The
    add-on may still be starting, so try a few times.
    """
    session = async_get_clientsession(hass)
    api_url = entry.data[CONF_API_URL].rstrip("/")
    user_id = entry.data.get(CONF_USER_ID) or DEFAULT_USER_ID
    headers = {"Authorization": f"Bearer {entry.data[CONF_API_TOKEN].strip()}"}
    for attempt in range(1, 6):
        if attempt > 1:
            await asyncio.sleep(30)
        try:
            async with session.get(
                f"{api_url}/api/memory/{quote(user_id, safe='')}",
                headers=headers,
                timeout=aiohttp.ClientTimeout(total=10),
            ) as response:
                if response.status in (401, 403):
                    _LOGGER.warning(
                        "Home Mind refused the API token (HTTP %s). Remove the "
                        "integration and add it again with the server's token",
                        response.status,
                    )
                return
        except (aiohttp.ClientError, TimeoutError) as err:
            _LOGGER.debug("Home Mind not reachable yet (%s), attempt %d", err, attempt)


async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Reload the config entry when its options or data change."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
