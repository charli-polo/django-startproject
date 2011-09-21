from myproject.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

STATIC_ROOT = '/home/dotcloud/data/static/'
MEDIA_ROOT = '/home/dotcloud/data/media/'
VAR_ROOT = '/home/dotcloud/data/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'dev.db'),
    }
}

ROOT_URLCONF = '%s.conf.dotcloud.urls' % PROJECT_MODULE_NAME


INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)
