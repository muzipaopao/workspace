# 与WSGI兼容的Web服务器为你的项目提供服务的入口点
"""
WSGI config for study project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'study.settings')

application = get_wsgi_application()
