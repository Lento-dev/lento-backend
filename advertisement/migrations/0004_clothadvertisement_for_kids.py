# Generated by Django 3.2 on 2022-04-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_alter_foodadvertisement_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothadvertisement',
            name='for_kids',
            field=models.BooleanField(default=False),
        ),
    ]