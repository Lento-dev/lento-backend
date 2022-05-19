from rest_framework import serializers
from advertisement.models import BaseAdvertisement, FoodAdvertisement, ServiceAdvertisement, AnimalAdvertisement, \
    ClothAdvertisement ,  Comment,Saved
from rest_polymorphic.serializers import PolymorphicSerializer


class BaseAdvertisementSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    Image = serializers.FileField(required = False)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True )
    class Meta:
        model = BaseAdvertisement
        fields = ('id', 'Title', 'Description', 'Image', 'province', 'City', 'Address', 'owner' , 'comments')


class ServiceAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAdvertisement
        fields = BaseAdvertisementSerializer.Meta.fields + ('service_type', 'expiration_date')


class FoodAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodAdvertisement
        fields = BaseAdvertisementSerializer.Meta.fields + ('Food_type', 'expiration_date')


class AnimalAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalAdvertisement
        fields = BaseAdvertisementSerializer.Meta.fields + (
            'animal_breed', 'animal_age', 'Health', 'handingover_reason')


class ClothesAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothAdvertisement
        fields = BaseAdvertisementSerializer.Meta.fields + ('cloth_type', 'expiration_date', 'cloth_status'
                                                            , 'cloth_size', 'for_men', 'for_women', 'for_kids',
                                                            'unlimited')


class BaseAdvertisementPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        BaseAdvertisement: BaseAdvertisementSerializer,
        ServiceAdvertisement: ServiceAdvertisementSerializer,
        FoodAdvertisement: FoodAdvertisementSerializer,
        AnimalAdvertisement: AnimalAdvertisementSerializer,
        ClothAdvertisement: ClothesAdvertisementSerializer
    }
      

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

   
    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post' ]


class SavedSerializer(serializers.ModelSerializer):


    class Meta:
        model = Saved
        fields = "__all__"


