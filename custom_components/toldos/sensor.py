from homeassistant.helpers.entity import Entity
from .device import MiDispositivoHTTP
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the sensor platform."""
    device = MiDispositivoHTTP(entry.data["host"], entry.data["endpoint"])
    async_add_entities([MiDispositivoHTTPSensor(entry, device)])

class MiDispositivoHTTPSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, entry, device):
        """Initialize the sensor."""
        self._entry = entry
        self._device = device
        self._name = "Mi Dispositivo HTTP Sensor"
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch new state data for the sensor."""
        data = self._device.fetch_data()
        # Assuming we want the first value of the first column as the state
        self._state = data.iloc[0, 0]