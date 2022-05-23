import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': os.getenv("DB_NAME"),

          'USER': os.getenv("DB_USER"),

          'PASSWORD': os.getenv("DB_PASSWORD"),

          'HOST': os.getenv("DB_HOST"),

          'PORT': os.getenv("DB_PORT"),
    }
}

AUTH_USER_MODEL = 'shop.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = ''
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_HOST_PASSWORD = ''

