import pytest
from requests.exceptions import HTTPError
from onesignalclient.user_client import OneSignalUserClient
from .base_test import BaseTest


class TestUserClient(BaseTest):
    def test_init_client(self, auth_key):
        client = OneSignalUserClient(auth_key=auth_key)
        assert client.mode == OneSignalUserClient.MODE_USER

    def test_get_headers(self, user_client):
        headers = user_client.get_headers()
        assert 'Content-Type' in headers
        assert 'Authorization' in headers
        assert user_client.auth_key in headers['Authorization']

    def test_view_apps(self, user_client):
        apps = user_client.view_apps()
        assert len(apps) == 1

    def test_view_apps_bad_request(self, user_client):
        with pytest.raises(HTTPError):
            user_client.view_apps()

    def test_view_app(self, user_client, app_id):
        app = user_client.view_app(app_id)
        assert app.get('id', False)

    def test_view_app_not_found(self, user_client, app_id):
        with pytest.raises(HTTPError):
            user_client.view_app(app_id)

    def test_view_device(self, user_client, player_id_1, app_id):
        device = user_client.view_device(player_id_1, app_id)
        assert device.get('identifier', False)

    def test_view_device_not_found(self, user_client, player_id_1, app_id):
        with pytest.raises(HTTPError):
            user_client.view_device(player_id_1, app_id)
