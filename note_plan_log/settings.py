"""
Django settings for Plan_and_Log project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR      =  os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 1 dir up!
TEMPLATE_DIR  =  os.path.abspath(os.path.join(BASE_DIR, 'templates'))
SOURCE_DIR    =  os.path.abspath(os.path.join(BASE_DIR, 'sources'))
STATIC_DIR    =  os.path.abspath(os.path.join(BASE_DIR, 'static'))

# Add path to system
if not os.path.exists(BASE_DIR):     sys.path.append(BASE_DIR)
if not os.path.exists(STATIC_DIR):   sys.path.append(STATIC_DIR)
if not os.path.exists(TEMPLATE_DIR): sys.path.append(TEMPLATE_DIR)
if not os.path.exists(SOURCE_DIR):   sys.path.append(SOURCE_DIR)

# Import local modules
import init

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL  =  '/static/'
STATICFILES_DIRS = [ STATIC_DIR, ]

# HTML template pages
TEMPLATE_DIRS = ( TEMPLATE_DIR, )
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^+(#=5v#r_iwr$kmd9=ocq8m&*=jawvmjpinb8h(@&7kn=+7iu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'note_plan_log',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'note_plan_log.urls'

WSGI_APPLICATION = 'note_plan_log.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE':    'django.db.backends.mysql',
        'NAME':      init.mysql_db_naam,
        'USER':      init.mysql_username,
        'PASSWORD':  init.mysql_password,
        'HOST':      init.mysql_db_host,   # Or an IP Address that your DB is hosted on
        'PORT':      init.mysql_db_port,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
