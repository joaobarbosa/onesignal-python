import re

import httpretty

from onesignalclient.user_client import OneSignalUserClient


class TestAppModeInit:
    def test_init_client(self, sample_auth_key):
        client = OneSignalUserClient(auth_key=sample_auth_key)
        assert client.mode == OneSignalUserClient.MODE_USER

    def test_get_headers(self, sample_user_client):
        headers = sample_user_client.get_headers()
        assert 'Content-Type' in headers
        assert 'Authorization' in headers
        assert sample_user_client.auth_key in headers['Authorization']

    @httpretty.activate
    def test_get_apps(self, sample_user_client):
        httpretty.register_uri(
            httpretty.GET,
            re.compile("https://onesignal.com/api/v1/(\w+)"),
            body='[{"id": "92911750-242d-4260-9e00-9d9034f139ce"}]',
            content_type="application/json"
        )

        apps = sample_user_client.get_apps()
        assert len(apps) == 1
