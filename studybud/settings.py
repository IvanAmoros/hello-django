"""
Django settings for studybud project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v9&*8t61_iv*7-oz88_$7zdsip8(ufxe*ck6gx9ssh+9&wwebu'

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

	'base.apps.BaseConfig',

	 'social_django',
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

ROOT_URLCONF = 'studybud.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			BASE_DIR / 'templates'
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

WSGI_APPLICATION = 'studybud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
	BASE_DIR / 'static'
]

# STATIC_ROOT =

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#  THIRD PARTY APY AUTH

AUTHENTICATION_BACKENDS = (
	# 'social_core.backends.oauth.OAuthAuth',
	'base.backends.Slug42OAuth2',
	'social_core.backends.google.GoogleOAuth2',
	'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['https://www.googleapis.com/auth/gmail.readonly']


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '783186248272-rvseh11bthjboenm7k83n1qr0t2atldp.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'


# 42
SOCIAL_AUTH_OAUTH2_42_KEY = 'u-s4t2ud-c243f702176ac2fd6d528047d4501505d39c54201dfe1535380c2e3cfedc60f1'
SOCIAL_AUTH_OAUTH2_42_SECRET = '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'

SOCIAL_AUTH_OAUTH2_42_SCOPE = ['public']

# SOCIAL_AUTH_42_KEY = 'u-s4t2ud-c243f702176ac2fd6d528047d4501505d39c54201dfe1535380c2e3cfedc60f1'
# SOCIAL_AUTH_42_SECRET = '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'

# SOCIAL_AUTH_42_SCOPE = ['public']

# SOCIAL_AUTH_42_EXTRA_DATA = ['picture', 'cursus_users']

# Redirect URI is typically generated automatically based on your Django project's URL configuration
# SOCIAL_AUTH_42_REDIRECT_URI = 'http://localhost:8000/social-auth/complete/42/'
# https://api.intra.42.fr/oauth/authorize?client_id=None&redirect_uri=http://localhost:8000/social-auth/complete/oauth2-42/&state=S1H4strQLkGmEsqhcdFSpDoK8SJimUkb&response_type=code
# https://api.intra.42.fr/oauth/authorize?client_id=None&redirect_uri=http://localhost:8000/social-auth/complete/oauth2-42/&state=tod5RpLCIT3DpaN6OeRWD5R5Vu6bAy5M&response_type=code
# https://api.intra.42.fr/oauth/authorize?client_id=None&redirect_uri=http://localhost:8000/social-auth/complete/oauth2-42/&state=uVKqFtVqJqPpocSrUd8qqAvbyucevTDS&response_type=code
# http://localhost:8000/social-auth/complete/oauth2-42/?code=529a6d5d0bcc3eb3a8d7785c425e3305c93f1601d56b82972f076d6c90f4f31e&state=pELcOAa238cTT3UgpbAeYOCqUAVfiKFu