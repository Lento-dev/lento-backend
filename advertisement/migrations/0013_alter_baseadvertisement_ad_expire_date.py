# Generated by Django 3.2 on 2022-06-05 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0012_auto_20220605_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseadvertisement',
            name='ad_expire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 12, 16, 17, 40, 984557), null=True),
        ),
    ]
