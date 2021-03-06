from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = True

ADMINS = (
    ('Hugh Brown', 'hughdbrown@yahoo.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

import django
DJANGO_ROOT = django.__path__[0]
PROJECT_ROOT = os.path.dirname(__file__)

MEDIA_URL = '/static/'
MEDIA_ROOT = os.path.realpath(os.path.join(PROJECT_ROOT, "static/"))

ADMIN_MEDIA_PREFIX = '/media/'
ADMIN_MEDIA_ROOT = os.path.realpath(os.path.join(DJANGO_ROOT, "contrib/admin/media"))

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%cbirgd_)mowwx7$m@1br(p@-_002869#t!r!4y=7!i*^el#t-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'lather.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.flatpages',
    'mobileadmin',
    
    'lather.meowr',
    'lather.search',

    # Blech. I just added these modules directly under lather/
    # HDB 2009-07-09
    'lather.compressor',
    'lather.typogrify',
    'lather.tagging',
    'lather.syncr',
    'lather.djumblr',
)

try:
    from local_settings import *
except ImportError:
    print "Missing %s" % os.path.join(PROJECT_ROOT, "local_settings.py")

if DEBUG:
    paths = [PROJECT_ROOT, MEDIA_ROOT, ADMIN_MEDIA_ROOT] + list(TEMPLATE_DIRS)
    for p in paths:
        p = os.path.normpath(p)
        if not os.path.exists(p):
            print "Missing path: %s" % p
