import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_IP_ADDRESS

from .const import DOMAIN

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_IP_ADDRESS, description={"suggested_value": "IP toldo"}): str,
    }
)

@config_entries.HANDLERS.register(DOMAIN)
class MiIntegracionConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow para Toldos."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Toldo", data=user_input)

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({
                vol.Required("host"): str,
                vol.Required("port"): int,
            })
        )
