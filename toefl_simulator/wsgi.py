"""
WSGI config for toefl_simulator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application

import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toefl_simulator.settings")

application = get_wsgi_application()
