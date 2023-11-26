#!/bin/bash

echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

DJANGO_SUPERUSER_USERNAME="admin"
DJANGO_SUPERUSER_PASSWORD="admin"
DJANGO_SUPERUSER_EMAIL="admin@rune.bolt"
python manage.py createsuperuser --username "admin" --email "admin@rune.bolt" --no-input

exec "$@"