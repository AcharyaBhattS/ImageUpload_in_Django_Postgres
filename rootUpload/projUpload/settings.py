
from pathlib import Path
import os
import sys
# from django.contrib.messages import constants as messages


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'secret_key.txt')) as myFile:
    SECRET_KEY = myFile.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
# ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'appUpload',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projUpload.urls'


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



WSGI_APPLICATION = 'projUpload.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'dbforcrud.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ImgUploadDB',
        'USER': 'sbcrud',
        'PASSWORD': 'sbcrud@123',
        # 'HOST': '127.0.0.1',
        # 'PORT': '5432',
    }
}




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files


# For Deployment_______________________________________________

# STATIC_URL = '/static/'
# STATIC_DIR = os.path.join(BASE_DIR, 'appUpload/static/')
# STATIC_ROOT = STATIC_DIR


# MEDIA_URL = '/media/'
# MEDIA_DIR = os.path.join(BASE_DIR, 'media/')
# MEDIA_ROOT = MEDIA_DIR


# if(DEBUG==True):
#     STATIC_URL = '/static/'
#     STATIC_ROOT = os.path.join(BASE_DIR, 'appUpload/static/')

#     MEDIA_URL = '/media/'
#     MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')

# else:
#     STATIC_URL = '/static/'
#     STATIC_ROOT=os.path.join(BASE_DIR, 'appUpload/static/')

#     MEDIA_URL='/media/'
#     MEDIA_ROOT=os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR, 'appUpload/static/')

# MEDIA_URL='/media/'
# MEDIA_ROOT=os.path.join(BASE_DIR, 'media/')

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'appUpload/media/')


