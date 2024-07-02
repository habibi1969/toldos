import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_IP_ADDRESS

from .const import DOMAIN, CONF_KWH_PER_100KM, CONF_PRECIO_LUZ

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_IP_ADDRESS, description={"suggested_value": "IP trydan"}): str,
    }
)
