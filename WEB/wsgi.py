"""
WSGI config for WEB project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'WEB.deployment' if 'calm-connections.azurewebsites.net' in os.environ else 'WEB.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WEB.settings')

application = get_wsgi_application()
