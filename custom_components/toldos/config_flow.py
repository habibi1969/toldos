import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_IP_ADDRESS

from .const import DOMAIN

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(NAME, description={"suggested_value": "Toldo"}): str,
        vol.Required(CONF_IP_ADDRESS, description={"suggested_value": "IP toldo"}): str,
        vol.Required("port", description={"value": "80"}): int,
    }
)

@config_entries.HANDLERS.register(DOMAIN)
class MiIntegracionConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow para Toldos."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_IP_ADDRESS])
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title=user_input[CONF_IP_ADDRESS], data=user_input)
        
        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA
        )
