# Generated by Django 4.2.7 on 2023-12-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burpexport', '0004_burpexport_completion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burpexport',
            name='burpExport',
            field=models.FileField(upload_to='burpExport/'),
        ),
    ]
