# Generated by Django 3.2 on 2022-06-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0014_auto_20220611_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='access_phone',
            field=models.BooleanField(default=False),
        ),
    ]
