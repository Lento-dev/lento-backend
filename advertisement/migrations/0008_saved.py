# Generated by Django 3.2 on 2022-05-10 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisement', '0007_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved', models.BooleanField(blank=True, default=True, null=True)),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='advertisement.baseadvertisement')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
