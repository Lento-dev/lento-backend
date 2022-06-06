from pathlib import Path
import os

DEPLOY = int(os.environ.get('DJANGO_DEPLOYMENT', default=0))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&3*t78^qjv+_&0)r1oy016jie+qnq_fkdkvku-y$g=iw*btbe#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False #if DEPLOY else True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'Charityxx123@'
EMAIL_HOST_USER = 'charityxx123@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
if DEPLOY:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'user_account',
    'drf_yasg',
    'phonenumber_field',
    'rest_framework.authtoken',
    'rest_registration',
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
    'advertisement', 
    'polymorphic',
    'django_filters'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lento_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'user_account', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'lento_backend.wsgi.application'

AUTH_USER_MODEL = 'user_account.Account'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'P@ssw0rdPostgres',
        'HOST': os.environ.get('DB_HOST', default='127.0.0.1'),
        'PORT': 5432
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
#     os.path.join(BASE_DIR, 'media'),
# ]
STATIC_URL = '/static_cdn/'
MEDIA_URL = '/media_cdn/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')
TEMP = os.path.join(BASE_DIR, 'temp')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

FRONTEND_HOST = os.environ.get('FRONTEND_HOST', default='http://localhost:3000')

REST_REGISTRATION = {
    'REGISTER_VERIFICATION_URL': f'{FRONTEND_HOST}/verify-user/',
    'RESET_PASSWORD_VERIFICATION_URL': f'{FRONTEND_HOST}/reset-password/',
    'REGISTER_EMAIL_VERIFICATION_URL': f'{FRONTEND_HOST}/verify-email/',
    'VERIFICATION_FROM_EMAIL': EMAIL_HOST_USER,
}
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '862951024028-vh67as9hmug8r225dfucffluv6tcqc6q.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': None,
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}