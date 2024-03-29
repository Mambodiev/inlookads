import os
import environ
from django.utils.translation import gettext_lazy as _


env = environ.Env()
environ.Env.read_env()
from pathlib import Path
SECRET_KEY =env('SECRET_KEY')
DEBUG = True
# ALLOWED_HOSTS = ['.demodjangoblog.herokuapp.com']
ALLOWED_HOSTS = ['*']
BASE_DIR = Path(__file__).resolve().parent.parent
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "modeltranslation",
    "django.contrib.admin",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_tailwind", 
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    'ckeditor_uploader',
    'ckeditor',
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    'django_filters',
    'widget_tweaks',
    "django.forms",
    'storages',
    'tailwind',
    'theme',
    'django_browser_reload',
    'rosetta',
    
    'allauth.socialaccount.providers.google',
]

INTERNAL_IPS = [
    "127.0.0.1",
]

LOCAL_APPS = [
    "content",
    "users",
    'core',
    'staff',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'config.urls'
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
WSGI_APPLICATION = 'config.wsgi.application'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': env('POSTGRES_DB'),
#             'USER': env('POSTGRES_USER'),
#             'PASSWORD': env('POSTGRES_PASSWORD'),
#             'HOST': env('POSTGRES_HOST'),
#             'PORT': env('POSTGRES_PORT'),
#             'keepalives':1,
#             'keepalives_idle':130,
#             'keepalives_interval':10,
#             'keepalives_count':15
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
# DATABASES['default'].update(db_from_env)
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

gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
)

LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
USE_THOUSAND_SEPARATOR = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
ADMIN_URL = "admin/"
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'images/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

###################################
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'none',
        # 'height': 100,
    },
}

AUTH_USER_MODEL = 'users.User'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

SITE_ID = 1


CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
TAILWIND_APP_NAME = 'theme'
CRISPY_TEMPLATE_PACK = "tailwind"
CRISPY_CLASS_CONVERTERS = {
    'textinput': 'dark:text-white text-gray-700'
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #new
EMAIL_HOST = 'smtp.gmail.com' #new
EMAIL_PORT = 587 #new
EMAIL_HOST_USER =env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS =env('EMAIL_USE_TLS')
NOTIFY_EMAIL = env('NOTIFY_EMAIL')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

# Additional configuration google authentication settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_LOGOUT_ON_GET= True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}





# AWS_S3_ACCESS_KEY_ID=env('AWS_S3_ACCESS_KEY_ID')
# AWS_S3_SECRET_ACCESS_KEY=env('AWS_S3_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_FILE_OVERWRITE=False
# AWS_DEFAULT_ACL=None

# production
# DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# end production

# local
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# end local
TAILWIND_MODE='watch'

