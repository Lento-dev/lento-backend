# Generated by Django 3.2 on 2022-04-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0004_clothadvertisement_for_kids'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothadvertisement',
            name='cloth_size',
            field=models.CharField(blank=True, choices=[('free size', 'free size'), ('Large', 'Large'), ('medium', 'medium'), ('small', 'small'), ('extra large', 'extra large'), ('extra small', 'extra small')], max_length=20),
        ),
        migrations.AddField(
            model_name='clothadvertisement',
            name='cloth_type',
            field=models.CharField(blank=True, choices=[('scarf/shawl', 'scarf/shawl'), ('pants', 'pants'), ('T-shirt', 'T-shirt'), ('hat', 'hat'), ('under wear', 'under wear'), ('jackets/coats', 'jackets/coats')], max_length=20),
        ),
    ]
