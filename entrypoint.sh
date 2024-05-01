#!/bin/sh

echo 'Running migrations...'
poetry run python manage.py migrate

echo 'Collecting static files...'
poetry run python manage.py collectstatic --no-input

poetry run daphne -b 0.0.0.0 -p 8000 aktivistisch_web.asgi:application
