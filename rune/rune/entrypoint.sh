#!/bin/bash

if [[ "$IMAGE_NAME" == "celery" ]]
then
  echo "Apply database migrations"
  python manage.py flush --no-input
  python manage.py makemigrations burpexport
  python manage.py migrate

  export DJANGO_SUPERUSER_USERNAME=admin
  export DJANGO_SUPERUSER_PASSWORD=admin
  export DJANGO_SUPERUSER_EMAIL=admin@rune.bolt
  python manage.py createsuperuser --no-input
fi
exec "$@"