from .base import *

import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

# # python manage.py check --deploy
# # eventually these should all be true
# SECURE_CONTENT_TYPE_NOSNIFF = False
# SECURE_BROWSER_XSS_FILTER = False

# # Change these to true when ssl works
# SECURE_SSL_REDIRECT = False 
# SESSION_COOKIE_SECURE = False

# X_FRAME_OPTIONS = False
