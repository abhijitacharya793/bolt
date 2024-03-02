#!/bin/bash

echo "#########################"
echo "Apply database migrations"
echo "#########################"

python manage.py flush --no-input
python manage.py makemigrations tool
python manage.py makemigrations risk
python manage.py migrate

#python manage.py dumpdata risk.risk > risk.json
python manage.py loaddata data/tag.json
python manage.py loaddata data/fuzzing.json
python manage.py loaddata data/risk.json
python manage.py loaddata data/vulnerability.json
python manage.py loaddata data/template.json

export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin
export DJANGO_SUPERUSER_EMAIL=admin@yggdrasil.bolt
python manage.py createsuperuser --no-input

echo "#########################"
echo "Pre-runs completed"
echo "#########################"
exec "$@"