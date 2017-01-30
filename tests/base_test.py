"""Base test class."""
import re
import responses
from requests.status_codes import codes


base_url = 'https://onesignal.com/api/v1'


class BaseTest():
    default_uri = re.compile('%s/(\w+)' % (base_url))
    requests_mock = {
        'test_get_apps': {
            'uri': '%s/apps' % (base_url),
            'body': '[{"id": "92911750-242d-4260-9e00-9d9034f139ce"}]'
        },
        'test_get_apps_bad_request': {
            'uri': '%s/apps' % (base_url),
            'status': codes.bad_request
        },
        'test_get_app': {
            'uri': re.compile('%s/apps/(\w|\-)+' % (base_url)),
            'body': '{"id": "92911750-242d-4260-9e00-9d9034f139ce"}'
        },
        'test_get_app_not_found': {
            'uri': re.compile('%s/apps/(\w|\-)+' % (base_url)),
            'status': codes.not_found
        },
        'test_create_notification': {
            'method': responses.POST,
            'uri': '%s/notifications' % (base_url),
            'body': '{"id": "458dcec4-cf53-11e3-000c940e62c", "recipients": 3}'
        },
        'test_cancel_notification': {
            'method': responses.DELETE,
            'uri': re.compile(
                '%s/notifications/(\w|\-)+\?app_id=(\w|\-)+' % (base_url)),
            'body': '{"success": "true"}'
        },
        'test_failed_cancel_notification': {
            'method': responses.DELETE,
            'status': codes.bad_request,
            'uri': re.compile(
                '%s/notifications/(\w|\-)+\?app_id=(\w|\-)+' % (base_url)),
            'body': '{"errors": ["..."]}'
        },
        'test_csv_export': {
            'method': responses.POST,
            'uri': re.compile(
                '%s/players/csv_export\?app_id=(\w|\-)+' % (base_url)),
            'body': '{"csv_file_url": "https://onesignal.com/csv_exports/b2f7f'
                    '966-d8cc-11e4-bed1-df8f05be55ba/users_184948440ec0e334728'
                    'e87228011ff41_2015-11-10.csv.gz"}'
        },
        'test_csv_export_not_found': {
            'method': responses.POST,
            'status': codes.not_found,
            'uri': re.compile(
                '%s/players/csv_export\?app_id=(\w|\-)+' % (base_url))
        },
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
