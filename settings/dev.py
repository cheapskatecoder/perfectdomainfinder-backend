from .base import *

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'perfectdomainfinderbackend',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
}



