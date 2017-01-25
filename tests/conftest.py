import pytest

from onesignalclient.app_client import OneSignalAppClient
from onesignalclient.user_client import OneSignalUserClient
from onesignalclient.notification import Notification


@pytest.fixture(scope="session")
def app_id():
    return 'e6d73965-8ee6-410c-5e33-4c0cef331557'


@pytest.fixture(scope="session")
def app_api_key():
    return 'Ojh0MMk22NGTRjz2DjyGQTUyMEOIM4L4OMEtD0IktVMJDjwN'


@pytest.fixture(scope="session")
def auth_key():
    return 'OMEtD0IktVMJDjwN22NGTRjzOjh0MMkEOIM4L42DjyGQTUyM'


@pytest.fixture(scope="session")
def player_id_1():
    return '1dd608f2-c6a1-11e3-851d-000c2940e62c'


@pytest.fixture(scope="session")
def player_id_2():
    return '000c2940-11e3-c6a1-1d85-1dd608f2e62c'


@pytest.fixture(scope="session")
def player_ids_list(player_id_1, player_id_2):
    return [player_id_1, player_id_2]


@pytest.fixture(scope="function")
def app_client(app_id, app_api_key):
    return OneSignalAppClient(
        app_id=app_id, app_api_key=app_api_key)


@pytest.fixture(scope="function")
def user_client(auth_key):
    return OneSignalUserClient(auth_key=auth_key)


@pytest.fixture(scope="function")
def device_notification(app_id, player_ids_list):
    notification = Notification(app_id, Notification.DEVICES_MODE)
    notification.include_player_ids = player_ids_list
    return notification


@pytest.fixture(scope="function")
def segment_notification(app_id):
    return Notification(app_id, Notification.SEGMENTS_MODE)


@pytest.fixture(scope="session")
def dict():
    return {'json': 'serializable'}


@pytest.fixture(scope="session")
def notification_content():
    return {'en': 'Custom message.'}


@pytest.fixture(scope="session")
def small_icon():
    return 'small_icon_example'


@pytest.fixture(scope="session")
def large_icon():
    return 'large_icon_example'
