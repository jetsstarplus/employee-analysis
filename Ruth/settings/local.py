from .base import *
import os

# SECRET_KEY = os.environ.get('SECRET')

DATABASES ={
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ruth',
        'USER': "postgres",
        'PASSWORD': "Otieno",
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.mysql',
#         'NAME':'ruth',
#         'USER':'root',
#         'PASSWORD':'',
#         'HOST':'localhost',
#         'PORT':''
#     }
# }



ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"
# MEDIA_URL="/media/"

# Simplified static file serving.

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY  = False

