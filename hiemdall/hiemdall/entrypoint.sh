#!/bin/bash

echo "#########################"
echo "Apply database migrations"
echo "#########################"

python manage.py flush --no-input
python manage.py makemigrations result
python manage.py migrate

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@hiemdall.bolt
python manage.py createsuperuser --no-input

echo "#########################"
echo "Pre-runs completed"
echo "#########################"
exec "$@"