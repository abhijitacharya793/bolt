#!/bin/bash

echo "#########################"
echo "Apply database migrations"
echo "#########################"

python manage.py flush --no-input
python manage.py makemigrations enricher
python manage.py migrate

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@valhalla.bolt
python manage.py createsuperuser --no-input

echo "#########################"
echo "Pre-runs completed"
echo "#########################"
exec "$@"