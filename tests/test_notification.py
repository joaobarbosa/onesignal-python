import pytest
import json
from onesignalclient.notification import Notification


class TestNotification:
    def test_notification_instantiation(self, app_id):
        n = Notification(app_id)
        assert n.mode == Notification.SEGMENTS_MODE

    def test_notification_with_unknown_mode(self, app_id):
        with pytest.raises(ValueError):
            Notification(app_id, 'unknown')

    def test_notification_segments_mode(self, app_id):
        n = Notification(app_id)
        assert n.mode == Notification.SEGMENTS_MODE
        with pytest.raises(TypeError):
            n.include_player_ids = ['player_id']

    def test_notification_include_segments_size(self, app_id):
        n = Notification(app_id)
        assert n.mode == Notification.SEGMENTS_MODE
        with pytest.raises(TypeError):
            n.include_segments = Notification.SEGMENTS.append('Invalid Segment')
    
    def test_notification_include_segments_type(self, app_id):
        n = Notification(app_id)
        assert n.mode == Notification.SEGMENTS_MODE
        with pytest.raises(TypeError):
            n.include_segments = {"segment": "All"}
    
    def test_notification_include_segments_item_type(self, app_id):
        n = Notification(app_id)
        assert n.mode == Notification.SEGMENTS_MODE
        with pytest.raises(TypeError):
            n.include_segments = [1]

    def test_validate_content_dict(self, sample_notification,
                                   notification_content):
        assert sample_notification._validate_content_dict(notification_content)

    def test_validate_content_dict_invalid_string(self, sample_notification,
                                                  notification_content):
        with pytest.raises(ValueError):
            sample_notification._validate_content_dict('invalid json string')

    def test_validate_content_dict_invalid_type(self, sample_notification,
                                                notification_content):
        with pytest.raises(TypeError):
            sample_notification._validate_content_dict(987)

    def test_validate_content_dict__without_default_language(
            self, sample_notification, notification_content):
        with pytest.raises(KeyError):
            sample_notification._validate_content_dict({'pt': 'Minha msg'})

    def test_set_data(self, sample_notification, sample_dict):
        sample_notification.data = sample_dict
        assert sample_notification.data == sample_dict

    def test_set_data_not_serializable(self, sample_notification):
        with pytest.raises(TypeError):
            sample_notification.data = False

    def test_set_data_string(self, sample_notification, sample_dict):
        sample_notification.data = json.dumps(sample_dict)
        assert sample_notification.data == sample_dict

    def test_set_data_invalid_string(self, sample_notification):
        with pytest.raises(ValueError):
            sample_notification.data = 'invalid json string'

    def test_set_contents(self, sample_notification, notification_content):
        sample_notification.contents = notification_content
        assert sample_notification.contents == notification_content

    def test_set_contents_invalid_string(self, sample_notification):
        with pytest.raises(ValueError):
            sample_notification.contents = 'invalid json string'

    def test_set_contents_invalid_type(self, sample_notification):
        with pytest.raises(TypeError):
            sample_notification.contents = 987

    def test_set_contents_without_default_language(self, sample_notification):
        with pytest.raises(KeyError):
            sample_notification.contents = {'pt': 'Minha mensagem'}

    def test_set_headings(self, sample_notification, notification_content):
        sample_notification.headings = notification_content
        assert sample_notification.headings == notification_content

    def test_set_headings_invalid_string(self, sample_notification):
        with pytest.raises(ValueError):
            sample_notification.headings = 'invalid json string'

    def test_set_headings_invalid_type(self, sample_notification):
        with pytest.raises(TypeError):
            sample_notification.headings = 987

    def test_set_headings_without_default_language(self, sample_notification):
        with pytest.raises(KeyError):
            sample_notification.headings = {'pt': 'Meu título'}
            sample_notification.contents = {'pt': 'Minha mensagem'}

    def test_set_subtitle(self, sample_notification, notification_content):
        sample_notification.subtitle = notification_content
        assert sample_notification.subtitle == notification_content

    def test_set_subtitle_invalid_string(self, sample_notification):
        with pytest.raises(ValueError):
            sample_notification.subtitle = 'invalid json string'

    def test_set_subtitle_invalid_type(self, sample_notification):
        with pytest.raises(TypeError):
            sample_notification.subtitle = 987

    def test_set_subtitle_without_default_language(self, sample_notification):
        with pytest.raises(KeyError):
            sample_notification.subtitle = {'pt': 'Meu subtítulo'}

    def test_set_ios_badge_type(self, sample_notification):
        notification = sample_notification  # PEP8 workaround
        notification.ios_badge_type = Notification.IOS_BADGE_TYPE_SETTO
        assert notification.ios_badge_type == Notification.IOS_BADGE_TYPE_SETTO

    def test_set_invalid_ios_badge_type(self, sample_notification):
        with pytest.raises(TypeError):
            sample_notification.ios_badge_type = 'invalid_type'

    def test_set_ios_badge_count(self, sample_notification):
        sample_notification.ios_badge_count = 10
        assert sample_notification.ios_badge_count == 10

    def test_set_invalid_ios_badge_count(self, sample_notification):
        with pytest.raises(ValueError):
            sample_notification.ios_badge_count = 'invalid_count'

    def test_set_small_icon(self, sample_notification, small_icon):
        sample_notification.small_icon = small_icon
        assert sample_notification.small_icon == small_icon

    def test_set_large_icon(self, sample_notification, large_icon):
        sample_notification.large_icon = large_icon
        assert sample_notification.large_icon == large_icon
