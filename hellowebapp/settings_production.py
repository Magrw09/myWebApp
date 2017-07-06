from hellowebappsettings import *

import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWAREDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
