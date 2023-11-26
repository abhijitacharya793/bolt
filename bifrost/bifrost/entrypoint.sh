#!/bin/bash

echo "Apply database migrations"
python manage.py flush --no-input
python manage.py makemigrations api
python manage.py makemigrations core
python manage.py makemigrations frontend
python manage.py migrate

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@rune.bolt
python manage.py createsuperuser --no-input

exec "$@"