from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN, CONF_DEVICES, CONF_NAME, CONF_HOST, CONF_ENDPOINT

class MiDispositivoHTTPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Mi Dispositivo HTTP."""

    VERSION = 1

    def __init__(self):
        self.devices = []

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            self.devices.append(user_input)
            return self.async_show_form(
                step_id="add_another_device",
                data_schema=vol.Schema({}),
                description_placeholders={
                    "message": "Device added. Would you like to add another?"
                }
            )

        data_schema = vol.Schema({
            vol.Required(CONF_NAME): str,
            vol.Required(CONF_HOST): str,
            vol.Required(CONF_ENDPOINT): str
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            description_placeholders={
                "message": "Please add your first device."
            }
        )

    async def async_step_add_another_device(self, user_input=None):
        """Prompt to add another device."""
        if user_input is not None:
            return self.async_create_entry(
                title="Devices Configuration",
                data={CONF_DEVICES: self.devices}
            )

        return await self.async_step_user()

    async def async_step_import(self, user_input=None):
        """Handle import from YAML."""
        return await self.async_step_user(user_input)
