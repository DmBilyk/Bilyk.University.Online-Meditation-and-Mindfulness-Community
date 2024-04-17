from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting
from urllib.parse import urljoin


class GoogleCloudMediaFileStorage(GoogleCloudStorage):
    bucket_name = setting('GS_BUCKET_NAME')

    def url(self, name):
        # Ensure there's always a trailing slash in the MEDIA_URL
        media_url = settings.MEDIA_URL
        if not media_url.endswith('/'):
            media_url += '/'

        return urljoin(media_url, name)
