# Django settings for whwn project.

import os
import socket
from fnmatch import fnmatch

class IPList(list):
    def __contains__(self, key):
        for elt in self:
            if fnmatch(key, elt):
                return True
        return False

INTERNAL_IPS = IPList(['127.0.0.1', '192.168.1.*', '192.168.123.*',
    '192.168.111.*'])

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Project path
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

# URLS to serve static and media while in DEBUG. Change in production.
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

AUTH_USER_MODEL = 'whwn.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'wehaveweneed',                      # Or path to database file if using sqlite3.
        'USER': 'whwn',
        'PASSWORD': 'whwn',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation.
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# We use Django internationalization
USE_I18N = True

# Format dates according to current locale
USE_L10N = True

# Time-aware datetimes
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_PATH, "public/media")
STATIC_ROOT = os.path.join(PROJECT_PATH, "public")

# Django-compressor settings #

# Use compressed assets
# COMPRESS_ENABLED = True

# COMPRESS_ROOT = os.path.join(PROJECT_PATH, 'static/')
# COMPRESS_OUTPUT_DIR = 'compiled/'
# 
# COMPRESS_CSS_FILTERS = [
#     'compressor.filters.css_default.CssAbsoluteFilter',
#     'compressor.filters.cssmin.CSSMinFilter',
# ]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
#   'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "static/compiled"),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates/'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

SECRET_KEY = '=e0#!)b-bc3!srkno@(7gt+hc!)nz%r*l37pwns1%el#7w3wj%'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_nose',
    'south',
    'whwn',
    'tastypie',
    # 'compressor',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "whwn.util.context_processors.debug_context",
)

APPEND_SLASH = False
TASTYPIE_ALLOW_MISSING_SLASH = True
