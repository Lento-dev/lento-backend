# Generated by Django 3.2 on 2022-06-06 18:03

import advertisement.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0013_alter_baseadvertisement_ad_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseadvertisement',
            name='ad_expire_date',
            field=models.DateTimeField(blank=True, default=advertisement.models.get_ad_expire_date, null=True),
        ),
    ]
