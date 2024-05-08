from django.contrib.messages import constants as messages
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j930@b(14*t_6-is2(-lc44)%@_(q=15vucwb+!o6x1spr-_ry'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django.contrib.sites',

    'import_export', # Import Export

    'dashboards',
    'apps',

    # Crispy Forms
    "crispy_forms",
    "crispy_tailwind",

    # All Auth
    'allauth',
    'allauth.account',
    'myaccount',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'lotteryTracker.urls'

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'lotteryTracker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR,"static")]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    # To login by username in Django admin
    'django.contrib.auth.backends.ModelBackend',

    # To login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    
]

#  Messages customize
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

IMPORT_EXPORT_USE_TRANSACTIONS = True

AUTH_USER_MODEL = "myaccount.User"

#  All Auth Configurations
LOGIN_REDIRECT_URL = "/accounts/profile/"
LOGIN_URL = "account_login"
ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

SOCIALACCOUNT_QUERY_EMAIL = False
ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_LOGIN_ON_GET = False


SITE_ID = 1
ACCOUNT_AUTHENTICATION_METHOD = "username_email"

# SMTP Configure
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.elasticemail.com"
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "sagartikarye@gmail.com"
EMAIL_HOST_PASSWORD = "EAAC928772B2BC3BD7744AAFDC0E3398FA96"
DEFAULT_FROM_EMAIL = "sagartikarye@gmail.com"

ACCOUNT_FORMS = {
    "login": "lotteryTracker.forms.UserLoginForm",
    "signup": "lotteryTracker.forms.UserRegistrationForm",
    "change_password": "lotteryTracker.forms.PasswordChangeForm",
    "reset_password": "lotteryTracker.forms.PasswordResetForm",
    "reset_password_from_key": "lotteryTracker.forms.PasswordResetKeyForm",
}
