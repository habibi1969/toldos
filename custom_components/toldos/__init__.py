from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN, PLATFORMS, CONF_NAME, CONF_HOST, CONF_ENDPOINT

import logging

_LOGGER = logging.getLogger(__name__)
_LOGGER.error("Inicia el __init__")

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Mi Dispositivo HTTP component."""
    _LOGGER.error("async_setup")
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Mi Dispositivo HTTP from a config entry."""
    _LOGGER.error("async_setup_entry")
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Set up platforms (e.g., sensor)
    for platform in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, platform)
        )

    entry.async_on_unload(entry.add_update_listener(async_update_entry))

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    _LOGGER.error("async_unload_entry")
    for platform in PLATFORMS:
        await hass.config_entries.async_forward_entry_unload(entry, platform)
    hass.data[DOMAIN].pop(entry.entry_id)

    return True

async def async_update_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Update the config entry when options are changed."""
    _LOGGER.error("async_update_entry")
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
       