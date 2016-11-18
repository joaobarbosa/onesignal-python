# onesignal-python
Python client for OneSignal push notification service

[![Build Status](https://travis-ci.org/joaobarbosa/onesignal-python.png?branch=master)](https://travis-ci.org/joaobarbosa/onesignal-python)

## Requirements

- Python 3.3+
- ```requirements.txt``` or ```requirements-test.txt```

## Running tests

Using **make**:

```make run_tests```

Using **pytest**:

```py.test --pep8 --cov=. --cov-report=term-missing --cov-config=.coveragerc -r a -v -s```
