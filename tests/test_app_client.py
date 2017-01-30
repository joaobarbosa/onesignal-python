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

    def test_create_notification(self, app_client, device_notification):
        result = app_client.create_notification(device_notification)
        assert result.get('id', False)
        assert result.get('recipients', False)

    def test_cancel_notification(self, app_client, notification_id):
        result = app_client.cancel_notification(notification_id)
        assert result.get('success', False)

    def test_failed_cancel_notification(self, app_client, notification_id):
        with pytest.raises(HTTPError):
            app_client.cancel_notification(notification_id)

    def test_csv_export(self, app_client):
        csv_link = app_client.csv_export()
        assert csv_link.get('csv_file_url', False)

    def test_csv_export_with_extra_fields(self, app_client):
        csv_link = app_client.csv_export(
            extra_fields=['location', 'country', 'rooted'])
        assert csv_link.get('csv_file_url', False)

    def test_csv_export_not_found(self, app_client):
        with pytest.raises(HTTPError):
            app_client.csv_export()
