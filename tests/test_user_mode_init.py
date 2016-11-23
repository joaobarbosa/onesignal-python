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
