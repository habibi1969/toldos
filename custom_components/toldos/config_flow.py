from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class ToldoHTTPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Toldo HTTP."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Toldo HTTP", data=user_input)

        data_schema = vol.Schema({
            vol.Required("host"): str,
            vol.Required("endpoint"): str
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema
        )

    async def async_step_import(self, user_input=None):
        """Handle import from YAML."""
        return await self.async_step_user(user_input)