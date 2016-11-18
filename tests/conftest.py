import pytest

from onesignal_client import OneSignalClient


@pytest.fixture(scope="module")
def sample_app_id():
    return 'e6d73965-8ee6-410c-5e33-4c0cef331557'


@pytest.fixture(scope="module")
def sample_app_api_key():
    return 'Ojh0MMk22NGTRjz2DjyGQTUyMEOIM4L4OMEtD0IktVMJDjwN'


@pytest.fixture(scope="module")
def sample_client(sample_app_id, sample_app_api_key):
    return OneSignalClient(
        app_id=sample_app_id, app_api_key=sample_app_api_key)
