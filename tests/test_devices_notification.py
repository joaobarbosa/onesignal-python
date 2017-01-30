import pytest
import json
from onesignalclient.notification import Notification


class TestDeviceNotification:
    def test_notification_instantiation(self, app_id):
        n = Notification(app_id, Notification.DEVICES_MODE)
        assert n.app_id == app_id
        assert n.mode == Notification.DEVICES_MODE

    def test_set_player_ids(self, device_notification, player_ids_list):
        device_notification.include_player_ids = player_ids_list
        assert device_notification.include_player_ids == player_ids_list

    def test_set_player_ids_with_wrong_type(self, device_notification):
        with pytest.raises(TypeError):
            device_notification.include_player_ids = 0

    def test_set_player_ids_with_wrong_mode(self, segment_notification):
        with pytest.raises(TypeError):
            segment_notification.include_player_ids = []

    def test_get_payload_for_request(self, device_notification, small_icon,
                                     large_icon):
        device_notification.data = {'sample': 'data'}
        device_notification.headings = {'en': 'Sample Heading'}
        device_notification.small_icon = small_icon
        device_notification.large_icon = large_icon
        device_notification.ios_badge_count = 1

        payload = device_notification.get_payload_for_request()

        assert payload.get('app_id', False)
        assert payload.get('include_player_ids', False)
        assert payload.get('data', False)
        assert payload.get('contents', False)
        assert payload.get('headings', False)
        assert payload.get('small_icon', False)
        assert payload.get('large_icon', False)
        assert payload.get('ios_badgeType', False)
        assert payload.get('ios_badgeCount', False)
