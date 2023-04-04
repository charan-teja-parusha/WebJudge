"""
WSGI config for my_capstone_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

import sys
sys.path.append('/WebJudge/my_capstone_project/env')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_capstone_project.settings')

application = get_wsgi_application()
