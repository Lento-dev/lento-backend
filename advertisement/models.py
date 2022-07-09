from datetime import timedelta
from django.utils import timezone
from django.db import models
from polymorphic.models import PolymorphicModel


# Create your models here.
def upload_location(instance, filename, **kwargs):
    file_path = 'advertisement/image/{filename}'.format(
        title=str(instance.username), filename=filename
    )
    return file_path


def get_ad_expire_date():
    return timezone.now() + timedelta(days=7)


class BaseAdvertisement(PolymorphicModel):
    Title = models.CharField(max_length=100, blank=True, null=True)
    Description = models.CharField(max_length=1000, blank=True, null=True)
    Image = models.ImageField(upload_location, blank=True, null=True)
    Image1 = models.ImageField(upload_location, blank=True, null=True)
    Image2 = models.ImageField(upload_location, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    Country = models.CharField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=100, blank=True, null=True)
    Address = models.CharField(max_length=500, blank=True, null=True)
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    owner = models.ForeignKey('user_account.Account', related_name='advertisement_owner', on_delete=models.CASCADE)
    ad_expire_date = models.DateTimeField(default=get_ad_expire_date, null=True, blank=True)
    mostaarname = models.CharField(max_length=100, blank=True, null=True)


class ClothAdvertisement(BaseAdvertisement):
    expiration_date = models.DateField(max_length=8, null=True, blank=True)
    cloth_status = models.CharField(max_length=30, blank=True)
    for_men = models.BooleanField(default=False)
    for_women = models.BooleanField(default=False)
    for_kids = models.BooleanField(default=False)
    unlimited = models.BooleanField(default=False)
    cloth_types = [('scarf/shawl', 'scarf/shawl'), ('pants', 'pants'), ('T-shirt', 'T-shirt'), ('hat', 'hat'),
                   ('under wear', 'under wear'), ('jackets/coats', 'jackets/coats'), ]
    cloth_sizes = [('free size', 'free size'), ('Large', 'Large'), ('medium', 'medium'), ('small', 'small'),
                   ('extra large', 'extra large'), ('extra small', 'extra small'), ]
    cloth_size = models.CharField(max_length=20, choices=cloth_sizes, blank=True)
    cloth_type = models.CharField(max_length=20, choices=cloth_types, blank=True)


class FoodAdvertisement(BaseAdvertisement):
    Food_type = models.CharField(max_length=1000, blank=True)
    expiration_date = models.DateField(null=True, blank=True)


class AnimalAdvertisement(BaseAdvertisement):
    animal_breed = models.CharField(max_length=50, blank=True)
    animal_age = models.CharField(max_length=10, blank=True)
    Health = models.CharField(max_length=100, blank=True)
    handingover_reason = models.CharField(max_length=500, blank=True)


class ServiceAdvertisement(BaseAdvertisement):
    service_types = [('dentistry', 'dentistry'), ('medical', 'medical'), ('piping', 'piping'), ('masonry', 'masonry'),
                     ('gardening', 'gardening'), ('vetinery', 'vetinery'), ('teaching', 'teaching'),
                     ('Psychology', 'Psychology')]
    service_type = models.CharField(max_length=20, choices=service_types, blank=True)
    expiration_date = models.DateField(max_length=8, null=True, blank=True)



class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('user_account.Account', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('advertisement.BaseAdvertisement', related_name='comments', on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    class Meta:
        ordering = ['created']

class Saved(models.Model):

    user = models.ForeignKey('user_account.Account', related_name='user', on_delete=models.CASCADE, blank=True)
    post = models.ForeignKey('advertisement.BaseAdvertisement', related_name='post', on_delete=models.CASCADE, blank=True)
    saved = models.BooleanField(default=True, blank=True, null=True)
    
    def str(self):
        return self.post
    
class SavedModel(models.Model):

    user_n = models.ForeignKey('user_account.Account', related_name='save_user', on_delete=models.CASCADE, blank=True)
    post_n = models.ForeignKey('advertisement.BaseAdvertisement', related_name='save_post', on_delete=models.CASCADE, blank=True)
   
    def str(self):
        return self.post

