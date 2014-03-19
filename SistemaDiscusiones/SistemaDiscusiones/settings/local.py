from .base import * #importamos todas las configuraciones de base.py

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': Path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE' 	: 'django.db.backends.postgresql_psycopg2',
        'NAME' 		: 'Discusiones',
        'USER' 		: 'cursodjango'
        'PASSWORD' 	: 'pass'
        'HOST' 		: 'localhost',
        'PORT' 		: '5432' #default port of postgres
    }
}

STATIC_URL = '/static/'
