import re
import pytest
import responses
from requests.exceptions import HTTPError
from requests.status_codes import codes
from onesignalclient.user_client import OneSignalUserClient

base_url = 'https://onesignal.com/api/v1'


class TestUserClient:
    default_uri = re.compile('%s/(\w+)' % (base_url))
    requests_mock = {
        'test_get_apps': {
            'uri': '%s/apps' % (base_url),
            'body': '[{"id": "92911750-242d-4260-9e00-9d9034f139ce"}]',
        },
        'test_get_apps_bad_request': {
            'uri': '%s/apps' % (base_url),
            'status': codes.bad_request
        },
        'test_get_app': {
            'uri': re.compile('%s/apps/(\w|\-)+' % (base_url)),
            'body': '{"id": "92911750-242d-4260-9e00-9d9034f139ce"}',
        },
        'test_get_app_not_found': {
            'uri': re.compile('%s/apps/(\w|\-)+' % (base_url)),
            'status': codes.not_found
        },
        'test_csv_export': {
            'method': responses.POST,
            'uri': re.compile(
                '%s/players/csv_export\?app_id=(\w|\-)+' % (base_url)),
            'body': '{"csv_file_url": "https://onesignal.com/csv_exports/b2f7f'
                    '966-d8cc-11e4-bed1-df8f05be55ba/users_184948440ec0e334728'
                    'e87228011ff41_2015-11-10.csv.gz"}',
        }
    }

    def setup_method(self, method):
        responses.start()
        request_data = self.requests_mock.get(method.__name__, {})

        responses.add(
            method=request_data.get('method', responses.GET),
            url=request_data.get('uri', self.default_uri),
            body=request_data.get('body', '{}'),
            status=request_data.get('status', codes.ok),
            content_type=request_data.get('content_type', 'application/json')
        )

    def teardown_method(self, method):
        responses.reset()
        responses.stop()

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

    def test_csv_export(self, sample_user_client, sample_app_id):
        csv_link = sample_user_client.csv_export(sample_app_id)
        assert csv_link.get('csv_file_url', False)
