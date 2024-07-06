import requests
import pandas as pd
import io

class ToldoHTTP:
    """Representation of the HTTP device."""

    def __init__(self, host, endpoint):
        """Initialize the device."""
        self._host = host
        self._endpoint = endpoint

    def fetch_data(self):
        """Fetch data from the device."""
        url = f"http://{self._host}/{self._endpoint}"
        response = requests.get(url)
        response.raise_for_status()
        
        # Assuming the response content is in CSV format
        csv_data = response.content.decode("utf-8")
        data = pd.read_csv(io.StringIO(csv_data))
        
        return data
        