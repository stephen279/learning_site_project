from learning_site.settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['mylearningsite.herokuapp.com','127.0.0.1']
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
