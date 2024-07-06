"""The toldos component."""
import logging
import aiohttp
from homeassistant.config_entries import SOURCE_IMPORT
#from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
#from homeassistant.const import CONF_IP_ADDRESS

_LOGGER = logging.getLogger(__name__)

from .const import DOMAIN, CONF_IP_ADDRESS, CONF_PORT

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

    hass.data[DOMAIN]["ip_address"] = entry.data[CONF_IP_ADDRESS]
    ip_address = entry.data[CONF_IP_ADDRESS]

    # Obtener las opciones del config entry
    scan_interval = entry.options.get("scan_interval", 10)
    hass.data[DOMAIN]["scan_interval"] = scan_interval

    # Registrar el dispositivo
    device_registry = await hass.helpers.device_registry.async_get_registry()
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        connections={(DOMAIN, entry.data["ip_address"])},
        identifiers={(DOMAIN, entry.entry_id)},
        manufacturer="Habibi",
        name="Toldo",
        model="Modelo 1",
        sw_version="1.0"
    )

    """hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "sensor"))"""
    return True

async def async_unload_entry(hass: HomeAssistant, entry):
    """Unload a config entry."""
    _LOGGER.info("Descargando Toldos")
    """return await hass.config_entries.async_forward_entry_unload(entry, "sensor")"""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    
