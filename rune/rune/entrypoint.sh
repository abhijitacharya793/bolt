#!/bin/bash

if [[ "$IMAGE_NAME" == "rune_api" ]]
then
  echo "#########################"
  echo "Apply database migrations"
  echo "#########################"
  rm media/burpExport/burp_export*
  rm media/burpExport/dvwa_xss*

  python manage.py flush --no-input
  python manage.py makemigrations burpexport
  python manage.py migrate

  export DJANGO_SUPERUSER_USERNAME=admin
  export DJANGO_SUPERUSER_PASSWORD=admin
  export DJANGO_SUPERUSER_EMAIL=admin@rune.bolt
  python manage.py createsuperuser --no-input

  echo "#########################"
  echo "Pre-runs completed"
  echo "#########################"
fi
exec "$@"