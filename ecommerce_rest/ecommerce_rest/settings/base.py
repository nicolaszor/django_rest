from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jbh-5&59*l*#)(%xf)6$6yvj2gc575wtu2j@)7t^@-zq7q!)v9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.users',
    'apps.products',
    'apps.base',
    'apps.mercancias'
    ]

THIRD_APPS = [
    'rest_framework',
    'rest_framework.authtoken',#una vez agregado tenemos que migrar
    'simple_history',
    'rest_framework_simplejwt',
    'drf_yasg',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    ]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': "none"
}
#esto sirve para que el listado de mercancias productos usuarios aparesca en pestañas desplegables

#TOKEN_EXPIRED_AFTER_SECONDS = 900 #NOS INDICA EN CUANTO TIEMPO EXPIRA EL TOKEN, NO LO UTILIZAMOS MAS POR JWT

#para que la class Autenticacion sea gloval (para todas las vistas añadimos lo siguiente)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'apps.users.autentication_mixin.Authentication',LO DEJAMOS DE UTILIZAR POR JWT
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',#esto se utiliza para que se autentiquen todas las vistas
    )
}






MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',#colocar lo mas arribla posible
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware', #reconose cual es el usurio que realizo cada cambio en la bd
]

ROOT_URLCONF = 'ecommerce_rest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce_rest.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.User' # la app va a funcionar con un model llamado usuario

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000"   
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000"
]

SIMPLE_JWT = {
    "BLACK_LIST_AFTER_ROTATION": True,
    "ROTATE_REFRESH_TOKENS": True,
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes = 5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days = 1),
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'


