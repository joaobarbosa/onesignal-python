"""Notification class."""
import json


class Notification():
    """Notification class."""
    SEGMENTS_MODE = 'segments'
    DEVICES_MODE = 'devices'
    FILTERS_MODE = 'filters'
    NOTIFICATION_MODES = [SEGMENTS_MODE, DEVICES_MODE, FILTERS_MODE]

    # Mode Settings
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
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

    def __init__(self, app_id, mode=SEGMENTS_MODE):
        if mode not in self.NOTIFICATION_MODES:
            raise ValueError('Unknown operation mode.')

        self.app_id = app_id
        self.mode = mode

        # Device defaults
        self._include_player_ids = []

        # Common defaults
        self._data = ''
