# Generated by Django 4.2.7 on 2023-12-04 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='install_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tool',
            name='install_script',
            field=models.TextField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
