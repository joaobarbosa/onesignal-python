from onesignal_client import OneSignalClient


class TestInitialization:
    def test_init_client(self, sample_app_id, sample_app_api_key):
        client = OneSignalClient(
            app_id=sample_app_id, app_api_key=sample_app_api_key
        )
        assert client

    def test_get_headers(self, sample_client):
        headers = sample_client.get_headers()
        assert 'Content-Type' in headers
        assert 'Authorization' in headers
