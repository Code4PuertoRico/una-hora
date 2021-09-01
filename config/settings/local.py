import os
import socket

from .base import *  # noqa
from .base import INTERNAL_IPS

# GENERAL
DEBUG = True

SECURE_SSL_REDIRECT = False

SECURE_HSTS_SECONDS = 0

SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# django-debug-toolbar
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405

# Show django-debug-toolbar when using Docker
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]
