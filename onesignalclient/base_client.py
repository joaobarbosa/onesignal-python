"""OneSignal Base Client class."""


class OneSignalBaseClient():
    """OneSignal Base Client."""
    MODE_APP = 'app'
    MODE_USER = 'user'

    def _get_headers(self):
        """
        Build default headers for requests. Fallback to "app" mode
        :return: Returns dict which contains the headers
        """
        auth = "Basic %s" % self.auth_key if self.mode == self.MODE_USER \
            else self.app_api_key

        headers = {
            "Content-Type": "application/json",
            "Authorization": auth
        }
        return headers
