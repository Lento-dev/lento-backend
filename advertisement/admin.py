from django.contrib import admin
from .models import BaseAdvertisement , FoodAdvertisement, AnimalAdvertisement , ClothAdvertisement , ServiceAdvertisement, Saved

# Register your models here.
admin.site.register(BaseAdvertisement)
admin.site.register(FoodAdvertisement)
admin.site.register(AnimalAdvertisement)
admin.site.register(ClothAdvertisement)
admin.site.register(ServiceAdvertisement)
admin.site.register(Saved)