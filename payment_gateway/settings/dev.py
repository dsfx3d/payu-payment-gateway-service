import os
from dotenv import load_dotenv
from payment_gateway.settings.base import * # pylint: disable=unused-wildcard-import

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = ['whitenoise.runserver_nostatic'] + INSTALLED_APPS

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.getenv('DB_NAME', 'payment_gateway_local_dev'),
    'USER': os.getenv('DB_USER', 'root'),
    'PASSWORD': os.getenv('DB_PASSWORD', 'root'),
    'HOST': os.getenv('API_DB_HOST', '127.0.0.1'),   # Or an IP Address that your DB is hosted on
    'PORT': os.getenv('DB_PORT', '3306'),
  }
}

# rest_framework_api_key
API_KEY_CUSTOM_HEADER = os.getenv('API_KEY_CUSTOM_HEADER')
