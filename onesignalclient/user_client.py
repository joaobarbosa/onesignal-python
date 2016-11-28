"""OneSignal User Client class."""
from .base_client import OneSignalBaseClient


class OneSignalUserClient(OneSignalBaseClient):
    """OneSignal Client."""
    def __init__(self, auth_key):
        """
        Initializes the OneSignal Client.

        :param auth_key: User REST API key.
        Found under OneSignal Dashboard > App Settings > Keys & IDs
        :type auth_key: string
        """
        self.auth_key = auth_key
        self.mode = self.MODE_USER

    def get_headers(self):
        """
        Build default headers for requests.
        :return: Returns dict which contains the headers
        """
        return self._get_headers()

    def get_apps(self):
        return self.get(self._url('apps'))

    def get_app(self, id):
        endpoint = 'apps/%s' % (id)
        return self.get(self._url(endpoint))
