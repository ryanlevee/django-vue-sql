DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jokes_old',
        'USER': 'postgres',
        # 'PASSWORD': 'password has been removed',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_URL = '/static/'

# SENDGRID = 'keys have been removed'
# AWS = 'keys have been removed'
