"""
WSGI config for ResBuilder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/home/django_projects/ResBuilder')
sys.path.append('/home/django_projects/ResBuilder/ResBuilder')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ResBuilder.settings')

application = get_wsgi_application()
