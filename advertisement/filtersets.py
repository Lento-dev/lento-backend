from django_filters import rest_framework as filters
from advertisement.models import BaseAdvertisement


class AdvertisementFilterSet(filters.FilterSet):
    clothadvertisement__expiration_date__gte = filters.DateFilter(method='filter_by_expiration_date')
    clothadvertisement__expiration_date__lte = filters.DateFilter(method='filter_by_expiration_date')
    foodadvertisement__expiration_date__gte = filters.DateFilter(method='filter_by_expiration_date')
    foodadvertisement__expiration_date__lte = filters.DateFilter(method='filter_by_expiration_date')
    serviceadvertisement__expiration_date__gte = filters.DateFilter(method='filter_by_expiration_date')
    serviceadvertisement__expiration_date__lte = filters.DateFilter(method='filter_by_expiration_date')
    ad_type = filters.CharFilter(method='filter_by_ad_type')

    class Meta:
        model = BaseAdvertisement
        fields = ['ad_type', 'province', 'City']
        cloth_fields = ['expiration_date__gte', 'expiration_date__lte', 'cloth_status', 'for_men', 'for_women',
                        'for_kids', 'unlimited', 'cloth_size', 'cloth_type']
        food_fields = ['Food_type', 'expiration_date__gte', 'expiration_date__lte']
        animal_fields = ['animal_breed', 'animal_age', 'Health', 'handingover_reason']
        service_fields = ['service_type', 'expiration_date__gte', 'expiration_date__lte']
        fields.extend([f'clothadvertisement__{i}' for i in cloth_fields])
        fields.extend([f'foodadvertisement__{i}' for i in food_fields])
        fields.extend([f'animaladvertisement__{i}' for i in animal_fields])
        fields.extend([f'serviceadvertisement__{i}' for i in service_fields])

    def get_subclasses_as_choice(self, c):
        choices = {subclass.__name__.lower(): subclass
                   for subclass in c.__subclasses__()}
        return choices

    def filter_by_ad_type(self, queryset, name, value):
        ad_choices = self.get_subclasses_as_choice(BaseAdvertisement)
        selected_ad = [v for k, v in ad_choices.items() if k == value.lower()]
        return queryset.instance_of(*selected_ad)

    def filter_by_expiration_date(self, queryset, name, value):
        return queryset.filter(**{f'{name}': value})
