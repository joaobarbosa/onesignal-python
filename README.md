# onesignal-python
Python client for OneSignal push notification service

[![Build Status](https://travis-ci.org/joaobarbosa/onesignal-python.png?branch=master)](https://travis-ci.org/joaobarbosa/onesignal-python)

## Installing

- ```pip install onesignal-python```
- ```pip install git+https://github.com/joaobarbosa/onesignal-python.git```

## Usage

*Coming soon...*

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

- [A] Create notification to segments
    - Segments mode settings & params
    - ~~Devices mode settings & params~~
    - Filters mode settings & params
    - Common Parameters
        - App
            - ~~```app_id```~~
            - ```app_ids```
        - Content
            - ```contents``` - _started_
                - Improve validation
                - Behaviour when using ```template_id```
            - ```headings```
            - ```subtitle```
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
        - _Others coming soon_
    - Export data for request
- [A] Cancel notification
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
    - Extra fields
- [U] View notification
- [A] View notifications
- Track open
