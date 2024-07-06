from homeassistant.helpers.entity import Entity
from .device import ToldoHTTP
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the sensor platform."""
    http_device = ToldoHTTP(entry.data["host"], entry.data["endpoint"])
    async_add_entities([ToldoHTTPSensor(entry, http_device)])

class ToldoHTTPSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, entry, device):
        """Initialize the sensor."""
        self._entry = entry
        self._device = device
        self._name = f"{entry.data['name']} Sensor"
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
