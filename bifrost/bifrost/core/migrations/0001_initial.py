# Generated by Django 4.2.7 on 2023-12-03 17:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.api')),
            ],
        ),
    ]
