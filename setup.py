"""OneSignal Python setup module.

See:
https://github.com/joaobarbosa/onesignal-python
"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
__version__ = None
with open('onesignalclient/version.py') as f:
    exec(f.read())

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Project
    name='onesignal-python',
    version=str(__version__),
    description='Python client for OneSignal push notification service',
    long_description=long_description,
    url='https://github.com/joaobarbosa/onesignal-python',

    # Author
    author='João Barbosa',
    author_email='joao.ofb@gmail.com',
    license='MIT',

    # Classifiers - https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        'Development Status :: 2 - Pre-Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        # License
        'License :: OSI Approved :: MIT License',
        # Python versions you support
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='onesignal client push notifications api',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Requirements - https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'requests==2.12.1',
    ],

    # List additional groups of dependencies here - pip install -e .[dev,test]
    extras_require={
        'dev': [],
        'test': [
            'pytest==3.0.4',
            'pytest-cov==2.4.0',
            'pytest-pep8==1.0.6',
            'responses==0.5.1'
        ],
    },
)
