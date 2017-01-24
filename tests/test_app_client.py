import pytest
from onesignalclient.app_client import OneSignalAppClient
from requests.exceptions import HTTPError
from .base_test import BaseTest


class TestAppClient(BaseTest):
    def test_init_client(self, sample_app_id, sample_app_api_key):
        client = OneSignalAppClient(
            app_id=sample_app_id, app_api_key=sample_app_api_key
        )
        assert client.mode == OneSignalAppClient.MODE_APP

    def test_get_headers(self, sample_app_client):
        headers = sample_app_client.get_headers()
        assert 'Content-Type' in headers
        assert 'Authorization' in headers
        assert sample_app_client.app_api_key in headers['Authorization']

    def test_csv_export(self, sample_app_client, sample_app_id):
        csv_link = sample_app_client.csv_export(sample_app_id)
        assert csv_link.get('csv_file_url', False)

    def test_csv_export_not_found(self, sample_app_client, sample_app_id):
        with pytest.raises(HTTPError):
            sample_app_client.csv_export(sample_app_id)
