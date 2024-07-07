from homeassistant.helpers.entity import Entity
from .device import ToldoHTTPDevice
from .const import DOMAIN, CONF_NAME, CONF_HOST, CONF_ENDPOINT

import logging

_LOGGER = logging.getLogger(__name__)
_LOGGER.error("Inicia el sensor")

async def async_setup_entry(hass, entry, async_add_entities):

    """Set up the sensor platform."""
    devices = entry.data[CONF_NAME]
    hass._data_key = data_key
    entities = []
    for device in devices:
        http_device = ToldoHTTPDevice(device[CONF_HOST], device[CONF_ENDPOINT])
        entities.append(ToldoHTTPSensor(device[CONF_NAME], http_device))
    
    async_add_entities(entities)

class ToldoHTTPSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, name, device):
        """Initialize the sensor."""
        self._name = f"{name} Sensor"
        self._device = device
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    async def async_update(self):
        """Fetch new state data for the sensor."""
        data = self._device.fetch_data()
        # Assuming we want the first value of the first column as the state
        self._state = data.iloc[0, 0]
        # Store the whole data as attributes for display
        self._attributes = data.to_dict(orient="list")
