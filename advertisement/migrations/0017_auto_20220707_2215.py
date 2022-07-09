# Generated by Django 3.2 on 2022-07-07 17:45

import advertisement.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0016_baseadvertisement_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseadvertisement',
            name='Image1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name=advertisement.models.upload_location),
        ),
        migrations.AddField(
            model_name='baseadvertisement',
            name='Image2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name=advertisement.models.upload_location),
        ),
    ]