"""
Django settings for MyCommunity project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l+xsg*)0d8jsv7xm1%=-j_2p=z^a#xwy*@s@=@l=&3mu^r%3ue'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'authentication',
    'activities',
    'feeds',
    'home',
    'search',
    'articles',
    'questions',
    'messenger',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'MyCommunity.urls'

WSGI_APPLICATION = 'MyCommunity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mycommunity',
        'USER': 'root',
        'PASSWORD': 'me5.',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATIC_URL = '/staticfiles/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'staticfiles'),

ALLOWED_SIGNUP_DOMAINS = ['*']

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/feeds/'

FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0o644

EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Admin@sporthilites.com'
SERVER_EMAIL = 'Admin@sporthilites.com'
EMAIL_HOST = 'smtp-pulse.com'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'markemma2012@gmail.com'
EMAIL_HOST_PASSWORD = 'HJc3bCokgm26X'
EMAIL_BACKEND = 'django.home.mail.backends.smtp.EmailBackend'