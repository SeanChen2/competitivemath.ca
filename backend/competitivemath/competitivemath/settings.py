"""
Django settings for competitivemath project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

from . import cm_secrets

# import django
# django.setup()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = cm_secrets.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'djoser',
    
    'user',
]

AUTH_USER_MODEL = 'user.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'competitivemath.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        # Build folder from frontend
        
        # Uncomment
        # 'DIRS': [os.path.join(BASE_DIR, 'build')],
        
        'DIRS':[],

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

WSGI_APPLICATION = 'competitivemath.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE':'django.db.backends.sqlite3',
    #     'NAME':os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    
    'default': {
        
        
        # Set database to Postgresql
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'competitivemath.ca',
        'USER': cm_secrets.PG_USER,
        'PASSWORD': cm_secrets.PG_PASSWORD,
        'HOST': "Kevin",
        'PORT': cm_secrets.PG_PORT
    }
}

# Djoser stuff
EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = cm_secrets.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = cm_secrets.EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = True


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Should prob uncomment this at one point
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}

# Djoser settings: https://djoser.readthedocs.io/en/latest/settings.html
DJOSER = {
    
    # Specifies users login using their email
    'LOGIN_FIELD':'username',
    
    # User create password (additional confirm password field called 're_password')
    'USER_CREATE_PASSWORD_RETYPE': True,
    
    # Confirmation to email when they attempt to change username or password
    'USERNAME_CHANGED_EMAIL_CONFIRMATION':True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
    'SEND_CONFIRMATION_EMAIL':True,
    
    'SET_USERNAME_RETYPE':True,
    
    # Confirmation before reset password
    'SET_PASSWORD_RETYPE':True,
    
    # Url to frontend password reset page
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirmation/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirmation/{uid}/{token}',

    # When user wants to activate their account, they click link of this format
    'ACTIVATION_URL':'activate/{uid}/{token}',
    
    # Sends activation email for new user account
    'SEND_ACTIVATION_EMAIL':True,
    
    # Serializers
    'SERIALIZERS': {
        # 'user_create': 'authentication.serializers.UserCreateSerializer',
        # 'user': 'authentication.serializers.UserCreateSerializer',
        # 'user_delete': 'djoser.serializers.UserDeleteSerializer',
        'user_create': 'authentication.serializers.UserCreateSerializer',
        'user': 'authentication.serializers.UserCreateSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Your React app's address
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
