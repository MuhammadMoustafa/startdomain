# startdomain

A django app to create apps aligned with [Django API Domains](https://phalt.github.io/django-api-domains/)

## Usage

1- Install the library

    poetry add startdomain
    or:
    pip install startdomain

2- add the app to your settings.py

    INSTALLED_APPS = [
        ...
        'startdomain',
        ...
    ]

3- run the following command

    python manage.py startdomain <some_app>

## Options and Flags

- **settings.py options:**
  - SNIPPTET_FOLDER: Override the default template folder
- **command line flags:**
  - -f: remove the app if exists
