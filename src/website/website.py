import requests

class Website:
    def __init__(self, api_address):
        self._api_address = api_address

    @property
    def api_address(self) -> str:
        return self._api_address

    @property
    def summary(self) -> dict:
        return self._get()

    def _get(self):
        response = requests.get(self.api_address)
        response.raise_for_status()
        return response.json()



