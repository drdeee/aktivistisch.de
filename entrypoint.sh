#!/bin/sh

echo 'Running migrations...'
poetry run python manage.py migrate

echo 'Collecting static files...'
poetry run python manage.py collectstatic --no-input

poetry run python manage.py runserver 0.0.0.0:8000
