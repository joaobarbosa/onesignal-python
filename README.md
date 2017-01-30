# onesignal-python
Python client for OneSignal push notification service

[![Build Status](https://travis-ci.org/joaobarbosa/onesignal-python.png?branch=master)](https://travis-ci.org/joaobarbosa/onesignal-python)

## Installing

- ```pip install onesignal-python```
- ```pip install git+https://github.com/joaobarbosa/onesignal-python.git```

## Usage

Example, sending push to specific devices (currently, only way supported).

```python
from requests.exceptions import HTTPError
from onesignalclient.app_client import OneSignalAppClient
from onesignalclient.notification import Notification

player_id = 'sample00-play-er00-id00-000000000000'
os_app_id = 'sample00-app0-id00-0000-000000000000'
os_apikey = 'your-rest-api-key-goes-here'

# Init the client
client = OneSignalAppClient(app_id=os_app_id, app_api_key=os_apikey)

# Creates a new notification
notification = Notification(app_id, Notification.DEVICES_MODE)
notification.include_player_ids = [player_id]  # Must be a list!

try:
    # Sends it!
    result = client.create_notification(notification)
except HTTPError as e:
    result = e.response.json()

print(result)
# Success: {'id': '1d63fa3a-2205-314f-a734-a1de7e27cc2a', 'recipients': 1}
# Error:   {'errors': ['Invalid app_id format']} - or any other message
```

## Requirements

- Python 3.3+
- ```requirements.txt``` or ```requirements-test.txt```

## Running tests

Using **make**:

```make run_tests```

Using **pytest**:

```py.test --pep8 --cov=. --cov-report=term-missing --cov-config=.coveragerc -r a -v -s```

## Todo

### API Methods

List of API methods to be covered by our client.

**[U]** - requires User Auth | **[A]** - requires App API Key

- [A] Create notification
    - Segments mode settings & params
    - ~~Devices mode settings & params~~
        - Improve tests as new params are added
    - Filters mode settings & params
    - Common Parameters
        - App
            - ~~```app_id```~~
            - ```app_ids```
        - Content
            - ~~```contents```~~
                - Behaviour when using ```template_id```
            - ~~```headings```~~
            - ~~```subtitle```~~
            - ```template_id```
            - ```content_available```
            - ```mutable_content```
        - Attachments
            - ~~```data```~~
            - ```url```
            - ```ios_attachments```
            - ```big_picture```
            - ```adm_big_picture```
            - ```chrome_big_picture```
        - Appearance
            - ```android_background_layout```
            - ~~```small_icon```~~
            - ~~```large_icon```~~
            - ```chrome_web_icon```
            - ```firefox_icon```
            - ```adm_small_icon```
            - ```adm_large_icon```
            - ```chrome_icon```
            - ```ios_sound```
            - ```android_sound```
            - ```adm_sound```
            - ```wp_sound```
            - ```wp_wns_sound```
            - ```android_led_color```
            - ```android_accent_color```
            - ```android_visibility```
            - ~~```ios_badgeType```~~
            - ~~```ios_badgeCount```~~
            - ```collapse_id```
        - Delivery
            - ```send_after```
            - ```delayed_option```
            - ```delivery_time_of_day```
            - ```ttl```
            - ```priority```
        - _Others coming soon_
    - Export data for request
- ~~[A] Cancel notification~~
- ~~[U] View apps~~
- ~~[U] View an app~~
- [U] Create an app
- [U] Update an app
- [A] View devices
- View device
- [U] Add a device
- Edit device
- [U] New session
- New purchase
- Increment session length
- [A] CSV export
    - ~~Regular export~~
    - ~~Extra fields~~
    - Make it available in the user client
- [U] View notification
- [A] View notifications
- Track open
