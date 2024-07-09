from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN, CONF_NAME, CONF_HOST, CONF_ENDPOINT

import logging

_LOGGER = logging.getLogger(__name__)
_LOGGER.error("Inicia el config_flow")

class ToldoHTTPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Mi Dispositivo HTTP."""

    VERSION = 1

    _instance = None

    def __init__(self):
        if ToldoHTTPConfigFlow._instance is None:
            ToldoHTTPConfigFlow._instance = self

    @classmethod
    def async_get_options_flow(cls, config_entry):
        if cls._instance is not None:
            return cls._instance._async_get_options_flow(config_entry)
        else:
            return ToldoHTTPOptionsFlowHandler(config_entry=config_entry)

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_NAME])
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_NAME, description={"suggested_value": "Toldo "}): int   #,
            #vol.Required(CONF_HOST): str,
            #vol.Required(CONF_ENDPOINT): str
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
                data={CONF_NAME: self.devices}
            )
        return await self.async_step_user()

    async def async_step_import(self, user_input=None):
        """Handle import from YAML."""
        return await self.async_step_user(user_input)

    async def async_step_options(self, user_input=None):
        """Manage the options for the custom component."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        devices = self.devices if self.devices else []
        options_schema = vol.Schema({
            vol.Required(CONF_NAME, default=devices): list
        })

        return self.async_show_form(
            step_id="options",
            data_schema=options_schema
        )
        
class ToldoHTTPOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry: config_entries.ConfigEntry):
        self.config_entry = config_entry
        self.current_host = config_entry.options.get(CONF_HOST, "192.168.1.")
        self.current_endpoint = config_entry.options.get(CONF_ENDPOINT, "gpio/refresh")

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        OPTIONS_SCHEMA = vol.Schema(
            {
                vol.Required(CONF_HOST, description={"suggested_value": self.current_ip}): str,
                vol.Required(CONF_ENDPOINT, description={"suggested_value": self.current_port}): str,
            }
        )

        return self.async_show_form(
            step_id="init", data_schema=OPTIONS_SCHEMA
        )
      