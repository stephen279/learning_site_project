import os

AWS_ACCESS_KEY_ID = os.environ.get('AKIAJEW3XBL5RXLUV7VQ')
AWS_SECRET_ACCESS_KEY = os.environ.get('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')
AWS_STORAGE_BUCKET_NAME = 'mylearningsitebucket'


#MEDIA_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#MEDIA_URL = 'https://s3.console.aws.amazon.com/s3/buckets/mylearningsitebucket/?region=us-east-2'
#STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
#ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
#STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

MEDIA_URL = 'http://s3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME + '/'