"""OneSignal App Client class."""
from .base_client import OneSignalBaseClient


class OneSignalAppClient(OneSignalBaseClient):
    """OneSignal Client."""
    def __init__(self, app_id, app_api_key):
        """
        Initializes the OneSignal Client.

        :param app_id: OneSignal App ID.
        Found under OneSignal Dashboard > App Settings > Keys & IDs
        :type app_id: string
        :param app_api_key: Application REST API key.
        Found under OneSignal Dashboard > App Settings > Keys & IDs
        :type app_api_key: string
        """
        self.app_id = app_id
        self.app_api_key = app_api_key
        self.mode = self.MODE_APP

    def get_headers(self):
        """
        Build default headers for requests.
        :return: Returns dict which contains the headers
        """
        return self._get_headers()

    def csv_export(self):
        """
        Request a CSV export from OneSignal.
        :return: Returns the request result.
        """
        endpoint = 'players/csv_export?app_id=%s' % (self.app_id)
        return self.post(self._url(endpoint))
