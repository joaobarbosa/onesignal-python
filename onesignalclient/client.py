"""OneSignal Client class."""


class OneSignalClient():
    """OneSignal Client."""
    def __init__(self, app_id, app_api_key):
        """
        Initializes the OneSignal Client.

        :param app_id: OneSignal App ID.
        Found under OneSignal Dashboard > App Settings > Keys & IDs
        :type app_id: string
        :param app_auth_key: Application REST API key.
        Found under OneSignal Dashboard > App Settings > Keys & IDs
        :type app_auth_key: string
        """
        self.app_id = app_id
        self.app_api_key = app_api_key

    def get_headers(self):
        """
        Build default headers for requests.
        :return: Returns dict which contains the headers
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic %s" % self.app_api_key
        }
        return headers
