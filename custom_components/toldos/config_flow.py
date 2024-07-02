import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_IP_ADDRESS

from .const import DOMAIN

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_IP_ADDRESS, description={"suggested_value": "IP toldo"}): str,
    }
)
