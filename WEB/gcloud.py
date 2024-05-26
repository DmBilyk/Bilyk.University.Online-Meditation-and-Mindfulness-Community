from urllib.parse import urljoin

from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting


class GoogleCloudMediaFileStorage(GoogleCloudStorage):
    bucket_name = setting('GS_BUCKET_NAME')

    def url(self, name):
        media_url = settings.MEDIA_URL
        if not media_url.endswith('/'):
            media_url += '/'

        return urljoin(media_url, name)