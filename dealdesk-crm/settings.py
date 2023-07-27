"""
Django settings for dealdesk-crm project.

Generated by 'django-admin startproject' using Django 3.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Define the path to the templates directory
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Check if the 'env.py' file exists
if os.path.exists('env.py'):
    import env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# Set DEBUG mode based on the 'DEVELOPMENT' environment variable
development = os.environ.get('DEVELOPMENT', False)
DEBUG = True

# List of allowed hosts for the Django application
if development:
    ALLOWED_HOSTS = [(
        'localhost', 
        '8000-pjdevex-dealdeskcrm-vjkodp24crr.ws-eu102.gitpod.io'
        )]
else:
    ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME')]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.humanize',  # Humanization utilities for better readability
    'allauth',  # User authentication with social account support
    'allauth.account',  # User authentication with email support
    'cloudinary_storage',  # Third-party "cloudinary_storage" app
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'cloudinary',
    'client',
    'lead_master',
    'task_manager',
    'team',
    'dashboard',
    'landing',
]

# Assign the site ID to 1 as per Django convention in the settings file.
SITE_ID = 1

# Account settings for authentication and redirection
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dealdesk-crm.urls'

# Allowed template packs for crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# Default template pack for crispy forms
CRISPY_TEMPLATE_PACK = "bootstrap5"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
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

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'dealdesk-crm.wsgi.application'

# Database
if development:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    import dj_database_url

    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Base URL for serving media files
MEDIA_URL = '/media/'
# Storage engine for media files
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Static files (CSS, JavaScript, Images)
# Base URL for serving static files
STATIC_URL = '/static/'
# Storage engine for static files
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
# Additional directories to find static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# Location for collected static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom account adapter to disable account signup
ACCOUNT_ADAPTER = 'dealdesk-crm.adapter.CustomAccountAdapter'
