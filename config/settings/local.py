import os
from .production import INSTALLED_APPS, DEBUG

SECRET_KEY = os.environ.get('DJ_SECRET_KEY')
FORCE_SCRIPT_NAME = None

INSTALLED_APPS += ['django_extensions', ]
DEBUG = True


#This stops WhiteNoise from complaining about a missing STATIC_ROOT
#directory.
WHITENOISE_AUTOREFRESH = True

BASE_API_URL = "https://api-test.mpharma.com/"
