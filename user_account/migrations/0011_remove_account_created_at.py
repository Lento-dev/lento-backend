# Generated by Django 3.2 on 2022-05-02 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0010_account_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='created_at',
        ),
    ]
