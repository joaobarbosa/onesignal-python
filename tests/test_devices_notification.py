import pytest
import json
from onesignalclient.notification import Notification


class TestNotification:
    def test_notification_instantiation(self, app_id):
        n = Notification(app_id, Notification.DEVICES_MODE)
        assert n.app_id == app_id
        assert n.mode == Notification.DEVICES_MODE

        n = Notification(app_id)
        assert n.mode == Notification.SEGMENTS_MODE

    def test_notification_with_unknown_mode(self, app_id):
        with pytest.raises(ValueError):
            Notification(app_id, 'unknown')

    def test_set_player_ids(self, device_notification, player_ids_list):
        device_notification.include_player_ids = player_ids_list
        assert device_notification.include_player_ids == player_ids_list

    def test_set_player_ids_with_wrong_type(self, device_notification):
        with pytest.raises(TypeError):
            device_notification.include_player_ids = 0

    def test_set_player_ids_with_wrong_mode(self, segment_notification):
        with pytest.raises(TypeError):
            segment_notification.include_player_ids = []

    def test_set_data(self, device_notification, dict):
        device_notification.data = dict
        assert device_notification.data == dict

    def test_set_data_not_serializable(self, device_notification):
        with pytest.raises(TypeError):
            device_notification.data = False

    def test_set_data_string(self, device_notification, dict):
        device_notification.data = json.dumps(dict)
        assert device_notification.data == dict

    def test_set_data_invalid_string(self, device_notification):
        with pytest.raises(ValueError):
            device_notification.data = 'invalid json string'

    def test_set_contents(self, device_notification, notification_content):
        device_notification.contents = notification_content
        assert device_notification.contents == notification_content

    def test_set_contents_invalid_string(self, device_notification):
        with pytest.raises(ValueError):
            device_notification.contents = 'invalid json string'

    def test_set_contents_invalid_type(self, device_notification):
        with pytest.raises(TypeError):
            device_notification.contents = 987

    def test_set_contents_without_default_language(self, device_notification):
        with pytest.raises(KeyError):
            device_notification.contents = {'pt': 'Minha mensagem'}

    def test_set_headings(self, device_notification, notification_content):
        device_notification.headings = notification_content
        assert device_notification.headings == notification_content

    def test_set_headings_invalid_string(self, device_notification):
        with pytest.raises(ValueError):
            device_notification.headings = 'invalid json string'

    def test_set_headings_invalid_type(self, device_notification):
        with pytest.raises(TypeError):
            device_notification.headings = 987

    def test_set_headings_without_default_language(self, device_notification):
        with pytest.raises(KeyError):
            device_notification.headings = {'pt': 'Meu título'}

    def test_set_ios_badge_type(self, device_notification):
        notification = device_notification  # PEP8 workaround
        notification.ios_badge_type = Notification.IOS_BADGE_TYPE_SETTO
        assert notification.ios_badge_type == Notification.IOS_BADGE_TYPE_SETTO

    def test_set_invalid_ios_badge_type(self, device_notification):
        with pytest.raises(TypeError):
            device_notification.ios_badge_type = 'invalid_type'

    def test_set_ios_badge_count(self, device_notification):
        device_notification.ios_badge_count = 10
        assert device_notification.ios_badge_count == 10

    def test_set_invalid_ios_badge_count(self, device_notification):
        with pytest.raises(ValueError):
            device_notification.ios_badge_count = 'invalid_count'

    def test_set_small_icon(self, device_notification, small_icon):
        device_notification.small_icon = small_icon
        assert device_notification.small_icon == small_icon

    def test_set_large_icon(self, device_notification, large_icon):
        device_notification.large_icon = large_icon
        assert device_notification.large_icon == large_icon

    def test_get_payload_for_request(self, device_notification, small_icon,
                                     large_icon):
        device_notification.data = {'sample': 'data'}
        device_notification.headings = {'en': 'Sample Heading'}
        device_notification.small_icon = small_icon
        device_notification.large_icon = large_icon
        device_notification.ios_badge_count = 1

        payload = json.loads(device_notification.get_payload_for_request())

        assert payload.get('app_id', False)
        assert payload.get('include_player_ids', False)
        assert payload.get('data', False)
        assert payload.get('contents', False)
        assert payload.get('headings', False)
        assert payload.get('small_icon', False)
        assert payload.get('large_icon', False)
        assert payload.get('ios_badgeType', False)
        assert payload.get('ios_badgeCount', False)
