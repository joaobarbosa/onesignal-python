import pytest
from requests.exceptions import HTTPError
from onesignalclient.user_client import OneSignalUserClient
from .base_test import BaseTest


class TestUserClient(BaseTest):
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

    def test_get_app(self, sample_user_client, sample_app_id):
        app = sample_user_client.get_app(sample_app_id)
        assert app.get('id', False)

    def test_get_app_not_found(self, sample_user_client, sample_app_id):
        with pytest.raises(HTTPError):
            sample_user_client.get_app(sample_app_id)
