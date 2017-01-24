import pytest
import json
from onesignalclient.notification import Notification


class TestNotification:
    def test_notification_instantiation(self, sample_app_id):
        n = Notification(sample_app_id, Notification.DEVICES_MODE)
        assert n.app_id == sample_app_id
        assert n.mode == Notification.DEVICES_MODE

        n = Notification(sample_app_id)
        assert n.mode == Notification.SEGMENTS_MODE

    def test_notification_with_unknown_mode(self, sample_app_id):
        with pytest.raises(ValueError):
            Notification(sample_app_id, 'unknown')

    def test_set_player_ids(self, sample_device_notification):
        sample_device_notification.include_player_ids = []
        assert sample_device_notification.include_player_ids == []

    def test_set_player_ids_with_wrong_type(self, sample_device_notification):
        with pytest.raises(TypeError):
            sample_device_notification.include_player_ids = 0
        sample_device_notification.include_player_ids = []

    def test_set_player_ids_with_wrong_mode(self, sample_segment_notification):
        with pytest.raises(TypeError):
            sample_segment_notification.include_player_ids = []

    def test_set_data(self, sample_device_notification):
        sample_dict = {'json': 'serializable'}
        sample_device_notification.data = sample_dict
        assert sample_device_notification.data == sample_dict

    def test_set_data_not_serializable(self, sample_device_notification):
        with pytest.raises(TypeError):
            sample_device_notification.data = False

    def test_set_data_string(self, sample_device_notification):
        sample_dict = {'json': 'serializable'}
        sample_device_notification.data = json.dumps(sample_dict)
        assert sample_device_notification.data == sample_dict

    def test_set_data_invalid_string(self, sample_device_notification):
        with pytest.raises(ValueError):
            sample_device_notification.data = 'invalid json string'
