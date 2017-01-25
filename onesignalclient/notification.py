"""Notification class."""
import json


class Notification():
    """Notification class."""
    SEGMENTS_MODE = 'segments'
    DEVICES_MODE = 'devices'
    FILTERS_MODE = 'filters'
    DEFAULT_LANGUAGE = 'en'
    NOTIFICATION_MODES = [SEGMENTS_MODE, DEVICES_MODE, FILTERS_MODE]
    IOS_BADGE_TYPE_NONE = 'None'
    IOS_BADGE_TYPE_SETTO = 'SetTo'
    IOS_BADGE_TYPE_INCREASE = 'Increase'
    IOS_BADGES_TYPES = [
        IOS_BADGE_TYPE_NONE, IOS_BADGE_TYPE_SETTO, IOS_BADGE_TYPE_INCREASE]

    # Mode Settings
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if value not in self.NOTIFICATION_MODES:
            raise ValueError('Unknown operation mode.')

        self._mode = value

    # Device mode properties
    @property
    def include_player_ids(self):
        return self._include_player_ids

    @include_player_ids.setter
    def include_player_ids(self, value):
        if self.mode != self.DEVICES_MODE:
            raise TypeError('Mode should be set to device.')

        if not isinstance(value, list):
            raise TypeError('Value must be a list.')

        self._include_player_ids = value

    # Common Parameters - App
    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, value):
        self._app_id = value

    # Common Parameters - Content & Language
    @property
    def contents(self):
        return json.loads(self._contents)

    @contents.setter
    def contents(self, value):
        if isinstance(value, str):
            value = json.loads(value)

        if not isinstance(value, dict):
            raise TypeError('Value must be a dict.')

        if not value.get(self.DEFAULT_LANGUAGE, False):
            raise KeyError('Default language (%s) must be included.' % (
                self.DEFAULT_LANGUAGE))

        self._contents = json.dumps(value)

    @property
    def headings(self):
        return json.loads(self._headings)

    @headings.setter
    def headings(self, value):
        if isinstance(value, str):
            value = json.loads(value)

        if not isinstance(value, dict):
            raise TypeError('Value must be a dict.')

        if not value.get(self.DEFAULT_LANGUAGE, False):
            raise KeyError('Default language (%s) must be included.' % (
                self.DEFAULT_LANGUAGE))

        self._headings = json.dumps(value)

    # Common Parameters - Attachments
    @property
    def data(self):
        return json.loads(self._data)

    @data.setter
    def data(self, value):
        if isinstance(value, str):
            value = json.loads(value)

        if not isinstance(value, dict):
            raise TypeError('Value must be a dict.')

        self._data = json.dumps(value)

    # Common Parameters - Appearance
    @property
    def ios_badge_type(self):
        return self._ios_badge_type

    @ios_badge_type.setter
    def ios_badge_type(self, value):
        if value not in self.IOS_BADGES_TYPES:
            raise TypeError('Unknown badge type.')

        self._ios_badge_type = value

    @property
    def ios_badge_count(self):
        return self._ios_badge_count

    @ios_badge_count.setter
    def ios_badge_count(self, value):
        self._ios_badge_count = int(value)

    def __init__(self, app_id, mode=SEGMENTS_MODE):
        self.app_id = app_id
        self.mode = mode

        # Device defaults
        self._include_player_ids = []

        # Common defaults
        self.headings = {'en': 'Default title.'}
        self.contents = {'en': 'Default message.'}
        self._data = ''
        self.ios_badge_type = self.IOS_BADGE_TYPE_NONE
        self.ios_badge_count = 1
