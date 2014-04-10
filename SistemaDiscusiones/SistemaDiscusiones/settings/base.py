from unipath import Path
BASE_DIR = Path(__file__).ancestor(3) #tomamos la ruta del archivo de donde estamos y subimos 3 niveles 

SECRET_KEY = '!t4e(@wiynrmt#5lm4k9j819u%ingfp=*bvx8v0&uoaqp5eiq_'

DJANGO_APPS = ( #aplicaciones de django
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', #busca los archivos estaticos dentro del directorio declarado en STATIC_URL 
                                  #recopilas los static files de todas las aplicaciones en una unica ubicacion
)

THIRD_PARTY_APPS = ( #Aplicaciones de terceros
    'south',
    'social.apps.django_app.default',  
) 

LOCAL_APPS = ( #Aplicaciones que creamos nosotros
    'apps.home',
    'apps.users',
) 

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SistemaDiscusiones.urls'

WSGI_APPLICATION = 'SistemaDiscusiones.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')] #donde van a estar alojados los html del proyecto

AUTH_USER_MODEL = 'users.User' #con esto le decimos a django que modelo de usuarios personalizado vamos a utilizar

AUTHENTICATION_BACKENDS = ( #los tipos de autentificacion que vamos a utilizar
        'social.backends.facebook.FacebookAppOAuth2',
        'social.backends.facebook.FacebookOAuth2',
        'social.backends.twitter.TwitterOAuth2',
        'django.contrib.auth.backends.ModelBackend',
    )