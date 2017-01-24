"""OneSignal Base Client class."""
import requests
import json


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

    def _get_headers(self, custom_headers={}):
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
        headers.update(custom_headers)
        return headers

    def get(self, url):
        """
        Perform a GET request.
        :return: Returns json response
        :rtype: dict or list
        :raises requests.exceptions.HTTPError: if status code is not 2xx
        """
        request = requests.get(url, headers=self._get_headers())
        request.raise_for_status()
        return request.json()

    def post(self, url, payload={}, headers={}):
        json_paylaod = json.dumps(payload)
        final_headers = self._get_headers(custom_headers=headers)
        request = requests.post(url, data=json_paylaod, headers=final_headers)
        request.raise_for_status()
        return request.json()
