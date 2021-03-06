from myproject.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Charlie', 'charles-antoine.idrac_webdevadmin@m4x.org'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'dev.db'),
    }
}

ROOT_URLCONF = '%s.conf.local.urls' % PROJECT_MODULE_NAME

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)
