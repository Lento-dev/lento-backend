# Generated by Django 3.2 on 2022-06-04 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0011_remove_account_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='access_phone',
            field=models.BooleanField(default=False),
        ),
    ]
