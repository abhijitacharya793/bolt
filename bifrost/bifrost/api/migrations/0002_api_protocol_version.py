# Generated by Django 4.2.7 on 2023-12-25 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='protocol_version',
            field=models.CharField(default='HTTP/1.1', max_length=10),
        ),
    ]
