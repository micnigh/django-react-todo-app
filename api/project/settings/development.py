from .base import *

import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6z-8xb*waf*!rfj99vi&n&a4n*1vp$qyf8b1wy)05f&*4t!)z4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
