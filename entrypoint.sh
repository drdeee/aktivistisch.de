#!/bin/sh

echo 'Running migrations...'
poetry run python manage.py migrate

echo 'Collecting static files...'
poetry run python manage.py collectstatic --no-input

exec "$@"
