"""OneSignal Base Client class."""
import requests


class OneSignalBaseClient():
    """OneSignal Base Client."""
    MODE_APP = 'app'
    MODE_USER = 'user'

    def _url(self, endpoint):
        """
        Build the full OneSignal API URL.
        :return: Returns the complete url string
        :rtype: str
        """
        return 'https://onesignal.com/api/v1/%s' % endpoint

    def _get_headers(self):
        """
        Build default headers for requests. Fallback to "app" mode
        :return: Returns dict which contains the headers
        :rtype: dict
        """
        auth = "Basic %s" % self.auth_key if self.mode == self.MODE_USER \
            else self.app_api_key

        headers = {
            "Content-Type": "application/json",
            "Authorization": auth
        }
        return headers

    def get(self, url):
        """
        Perform a GET request.
        :return: Returns json response
        :rtype: dict or list
        :raises requests.exceptions.HTTPError: if status code is not 2xx
        """
        request = requests.get(url)
        request.raise_for_status()
        return request.json()

    def post(self):
        raise NotImplementedError()
