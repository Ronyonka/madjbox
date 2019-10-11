from .base import *
from decouple import config, Csv
import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': ''
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())