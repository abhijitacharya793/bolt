#!/bin/bash

if [[ "$IMAGE_NAME" == "asgard_api" ]]
then
  echo "#########################"
  echo "Apply database migrations"
  echo "#########################"
  python manage.py flush --no-input
  # python manage.py makemigrations burpexport
  python manage.py migrate

  export DJANGO_SUPERUSER_USERNAME=admin
  export DJANGO_SUPERUSER_PASSWORD=admin
  export DJANGO_SUPERUSER_EMAIL=admin@asgard.bolt
  python manage.py createsuperuser --no-input

  echo "#########################"
  echo "Pre-runs completed"
  echo "#########################"
else
  celery -A asgard beat -l INFO --detach
fi
exec "$@"