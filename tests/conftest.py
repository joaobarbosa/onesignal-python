import pytest

from onesignalclient.app_client import OneSignalAppClient
from onesignalclient.user_client import OneSignalUserClient
from onesignalclient.notification import Notification


@pytest.fixture(scope="module")
def sample_app_id():
    return 'e6d73965-8ee6-410c-5e33-4c0cef331557'


@pytest.fixture(scope="module")
def sample_app_api_key():
    return 'Ojh0MMk22NGTRjz2DjyGQTUyMEOIM4L4OMEtD0IktVMJDjwN'


@pytest.fixture(scope="module")
def sample_auth_key():
    return 'OMEtD0IktVMJDjwN22NGTRjzOjh0MMkEOIM4L42DjyGQTUyM'


@pytest.fixture(scope="module")
def sample_app_client(sample_app_id, sample_app_api_key):
    return OneSignalAppClient(
        app_id=sample_app_id, app_api_key=sample_app_api_key)


@pytest.fixture(scope="module")
def sample_user_client(sample_auth_key):
    return OneSignalUserClient(auth_key=sample_auth_key)


@pytest.fixture(scope="module")
def sample_device_notification(sample_app_id):
    return Notification(sample_app_id, Notification.DEVICES_MODE)


@pytest.fixture(scope="module")
def sample_segment_notification(sample_app_id):
    return Notification(sample_app_id, Notification.SEGMENTS_MODE)
