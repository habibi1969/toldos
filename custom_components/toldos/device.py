from homeassistant.helpers.entity import Entity

class ToldoDevice(Entity):
    """Representation de un Toldo Device."""

    def __init__(self, entry):
        """Initialize the device."""
        self._entry = entry
        self._name = "Toldo"
        self._state = None

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def state(self):
        """Return the state of the device."""
        return self._state

    async def async_update(self):
        """Fetch new state data for the device."""
        self._state = False  # Actualiza el estado con la lógica necesaria
