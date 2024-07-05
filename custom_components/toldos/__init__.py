"""The toldos component."""
import logging
import aiohttp
from homeassistant.config_entries import SOURCE_IMPORT
"""from homeassistant.config_entries import ConfigEntry"""
from homeassistant.core import HomeAssistant, ServiceCall
"""from homeassistant.const import CONF_NAME"""

_LOGGER = logging.getLogger(__name__)

from .const import DOMAIN, CONF_NAME

PLATFORMS = ["sensor"]
"""["sensor", "switch", "number"]"""

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the integration using YAML."""
    _LOGGER.info("Configurando Toldos")
    
    hass.data.setdefault(DOMAIN, {})
    if DOMAIN not in config:
        return True

    for entry_config in config[DOMAIN]:
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN, context={"source": SOURCE_IMPORT}, data=entry_config
            )
        )
    return True

async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up the integration using UI."""
    _LOGGER.info("Configurando Toldos desde una entrada de configuración")
    
    for platform in PLATFORMS:
        await hass.config_entries.async_forward_entry_setup(entry, platform)

    hass.data[DOMAIN][CONF_NAME] = entry.data[CONF_NAME]
    CONF_NAME = entry.data[CONF_NAME]
    
    """hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "sensor"))"""
    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    """Unload a config entry."""
    _LOGGER.info("Descargando Toldos")
    """return await hass.config_entries.async_forward_entry_unload(entry, "sensor")"""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
