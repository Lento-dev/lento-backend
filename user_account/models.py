import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


def upload_location(instance, filename, **kwargs):
    file_path = 'account/image/{filename}'.format(
        title=str(instance.username), filename=filename
    )
    return file_path


def upload_cover(instance, filename, **kwargs):
    file_path = 'account/cover/{filename}'.format(
        title=str(instance.username), filename=filename
    )
    return file_path


class Account(AbstractUser):
    GENDERS = [('male', 'male'), ('female', 'female')]
    email = models.EmailField(max_length=255, unique=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True, default='a2.jpg')
    cover = models.ImageField(upload_to=upload_cover, blank=True, null=True)
    bio = models.CharField(max_length= 800, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True)
    date_birth = models.DateField(max_length=8, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    job = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=7, null=True, choices=GENDERS, blank=True)
    education = models.CharField(max_length=30, null=True, blank=True)
    experience = models.CharField(max_length=800, null=True, blank=True)
    access_phone = models.BooleanField(default=False)
    access_profile = models.BooleanField(default = True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    @property
    def _image(self):
        if self.image:
            return self.image
        return None


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
