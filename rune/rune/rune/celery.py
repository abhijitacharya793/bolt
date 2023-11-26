import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rune.settings')

app = Celery("rune")
app.config_from_object("django.conf:settings", namespace="CELERY")


# @app.task
# def add():
#     return


app.autodiscover_tasks()
