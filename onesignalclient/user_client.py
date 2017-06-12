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

    def view_apps(self):
        return self.get(self._url('apps'))

    def view_app(self, app_id):
        endpoint = 'apps/%s' % (app_id)
        return self.get(self._url(endpoint))

    def view_device(self, player_id, app_id):
        endpoint = 'players/%s?%s' % (player_id, app_id)
        return self.get(self._url(endpoint))
