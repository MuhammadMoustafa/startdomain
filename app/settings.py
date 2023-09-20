from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7zub%(g44=m(emembmu^vwhm#a%0*@ctfk@n$c3%zi9wiz@5++'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS = [
    'startdomain',
]

MIDDLEWARE = [
]

WSGI_APPLICATION = 'app.wsgi.application'