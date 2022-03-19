""" Send static files to s3 """

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    """ Class for staticstorage """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ Class for mediastorage """
    location = settings.MEDIAFILES_LOCATION
