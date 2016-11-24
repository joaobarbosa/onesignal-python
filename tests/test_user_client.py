import re
import pytest
import httpretty
from requests.exceptions import HTTPError
from onesignalclient.user_client import OneSignalUserClient


class TestUserClient:
    default_uri = re.compile('https://onesignal.com/api/v1/(\w+)')
    requests_mock = {
        'test_get_apps': {
            'uri': 'https://onesignal.com/api/v1/apps',
            'body': '[{"id": "92911750-242d-4260-9e00-9d9034f139ce"}]',
        },
        'test_get_apps_bad_request': {
            'uri': 'https://onesignal.com/api/v1/apps',
            'status': 400
        }
    }

    def setup_method(self, method):
        httpretty.enable()
        request_data = self.requests_mock.get(method.__name__, {})

        httpretty.register_uri(
            request_data.get('method', httpretty.GET),
            request_data.get('uri', self.default_uri),
            status=request_data.get('status', 200),
            body=request_data.get('body', '{}'),
            content_type=request_data.get('content_type', 'application/json')
        )

    def teardown_method(self, method):
        httpretty.disable()

    def test_init_client(self, sample_auth_key):
        client = OneSignalUserClient(auth_key=sample_auth_key)
        assert client.mode == OneSignalUserClient.MODE_USER

    def test_get_headers(self, sample_user_client):
        headers = sample_user_client.get_headers()
        assert 'Content-Type' in headers
        assert 'Authorization' in headers
        assert sample_user_client.auth_key in headers['Authorization']

    def test_get_apps(self, sample_user_client):
        apps = sample_user_client.get_apps()
        assert len(apps) == 1

    def test_get_apps_bad_request(self, sample_user_client):
        with pytest.raises(HTTPError):
            sample_user_client.get_apps()
