from onesignalclient.app_client import OneSignalAppClient


class TestAppModeInit:
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
