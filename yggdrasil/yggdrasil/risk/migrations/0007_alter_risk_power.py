# Generated by Django 4.2.7 on 2023-12-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0006_alter_risk_power'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='power',
            field=models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')]),
        ),
    ]
