from django.core.management.base import BaseCommand
from datetime import datetime

from advertisement.models import BaseAdvertisement, ClothAdvertisement, FoodAdvertisement, ServiceAdvertisement


class Command(BaseCommand):
    help = 'Removes expired ads'

    def handle(self, *args, **options):
        qs = BaseAdvertisement.objects.filter(ad_expire_date__lte=datetime.now())
        for i in qs:
            i.delete()
        clothes_qs = ClothAdvertisement.objects.filter(expiration_date__lte=datetime.now())
        for i in clothes_qs:
            i.delete()
        food_qs = FoodAdvertisement.objects.filter(expiration_date__lte=datetime.now())
        for i in food_qs:
            i.delete()
        service_qs = ServiceAdvertisement.objects.filter(expiration_date__lte=datetime.now())
        for i in service_qs:
            i.delete()
        self.stdout.write(f'Removed {len(qs) + len(clothes_qs) + len(food_qs) + len(service_qs)} objects')
