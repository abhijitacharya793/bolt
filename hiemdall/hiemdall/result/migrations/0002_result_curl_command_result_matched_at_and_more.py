# Generated by Django 4.2.7 on 2024-03-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='curl_command',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='matched_at',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='payload_str',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='template_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='uuid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
