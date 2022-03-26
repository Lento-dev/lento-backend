# Generated by Django 3.2 on 2022-03-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0004_account_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='bio',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='city',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='education',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(blank=True, default='male', max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='job',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='province',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
