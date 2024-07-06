import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_IP_ADDRESS

from .const import DOMAIN, NAME, PORT

DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_IP_ADDRESS, description={"suggested_value": "192.168.1."}): str,
    }
)

@config_entries.HANDLERS.register(DOMAIN)
class ToldoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow para Toldos."""
    
    VERSION = 1
    
    _instance = None

    def __init__(self):
        if ToldoConfigFlow._instance is None:
            ToldoConfigFlow._instance = self
            
    @classmethod
    def async_get_options_flow(cls, config_entry):
        if cls._instance is not None:
            return cls._instance._async_get_options_flow(config_entry)
        else:
            return ToldoOptionsFlowHandler(config_entry=config_entry)

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_IP_ADDRESS])
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title=user_input[CONF_IP_ADDRESS], data=user_input)
        
        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA
        )
        
    async def async_step_import(self, user_input):
        """Import entry from configuration.yaml."""
        return await self.async_step_user(user_input)

    def _async_get_options_flow(self, config_entry):
        return ToldoOptionsFlowHandler(config_entry=config_entry)

class ToldoOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry: config_entries.ConfigEntry):
        self.config_entry = config_entry
        self.current_ip = config_entry.options.get(CONF_IP_ADDRESS, "192.168.1.")
        self.current_port = config_entry.options.get(PORT, 80)
        self.current_name = f"{config_entry.options.get(NAME)} ({self.current_ip})"

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title=f"Toldo 1{self.current_name}<", data=user_input)

        OPTIONS_SCHEMA = vol.Schema(
            {
                vol.Required(CONF_IP_ADDRESS, description={"suggested_value": self.current_ip}): str,
                vol.Required(PORT, description={"suggested_value": self.current_port}): vol.Coerce(int),
            }
        )

        return self.async_show_form(
            step_id="init", data_schema=OPTIONS_SCHEMA
        )
