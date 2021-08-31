#!/usr/bin/env bash

set -euo pipefail

pip freeze

postgres_ready() {
    python manage.py shell << END
import sys
import psycopg2
from django.db import connections
try:
  connections['default'].cursor()
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
      >&2 echo "==> Waiting for Postgres..."
      sleep 1
    done

case "$1" in
  "dev_web_start")
    echo "==> Running migrations..."
    python manage.py collectstatic --noinput
    python manage.py makemigrations
    python manage.py migrate

    echo "==> Loading initial data..."
    python manage.py loaddata "una_hora/users/fixtures/initial.json"

    echo "==> Running web dev server..."
    python manage.py runserver 0.0.0.0:8000
    ;;

  *)
    exec "$@"
    ;;
esac
