# Parse database configuration from $DATABASE_URL
import dj_database_url
from os import environ

from .base import *

ALLOWED_HOSTS = ['awselbdemo-455991089.us-east-2.elb.amazonaws.com']

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = environ['STATIC_ROOT']
