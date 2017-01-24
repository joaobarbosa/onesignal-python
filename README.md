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

- [A] Create notification
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
- ~~[A] CSV export~~
- [A] CSV export with extra fields
- [U] View notification
- [A] View notifications
- Track open
