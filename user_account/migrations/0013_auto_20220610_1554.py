# Generated by Django 3.2 on 2022-06-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0012_auto_20220605_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='access_phone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='access_profile',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='bio',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='experience',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
