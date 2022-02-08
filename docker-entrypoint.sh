#!/usr/bin/env bash

set -euo pipefail

postgres_ready() {
    pipenv run python manage.py shell << END
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
    pipenv run python manage.py makemigrations
    pipenv run python manage.py migrate

    echo "==> Loading initial data..."
    pipenv run python manage.py loaddata "una_hora/users/fixtures/initial.json"

    echo "==> Running web dev server..."
    pipenv run python manage.py runserver 0.0.0.0:8000
    ;;

  "dev_tailwind_start")
    echo "==> Installing frontend dependencies..."
    pipenv run python manage.py tailwind install

    echo "==> Running frontend..."
    pipenv run python manage.py tailwind start
    ;;

  "pre_commit")
    echo "==> Running pre-commit..."
    pipenv run pre-commit run --all-files
    ;;

  *)
    exec "$@"
    ;;
esac
