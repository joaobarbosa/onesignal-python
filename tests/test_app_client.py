import pytest
from onesignalclient.app_client import OneSignalAppClient
from requests.exceptions import HTTPError
from .base_test import BaseTest


class TestAppClient(BaseTest):
    def test_init_client(self, app_id, app_api_key):
        client = OneSignalAppClient(
            app_id=app_id, app_api_key=app_api_key
        )
        assert client.mode == OneSignalAppClient.MODE_APP

    def test_get_headers(self, app_client):
        headers = app_client.get_headers()
        assert 'Content-Type' in headers
        assert 'Authorization' in headers
        assert app_client.app_api_key in headers['Authorization']

    def test_csv_export(self, app_client):
        csv_link = app_client.csv_export()
        assert csv_link.get('csv_file_url', False)

    def test_csv_export_not_found(self, app_client):
        with pytest.raises(HTTPError):
            app_client.csv_export()
