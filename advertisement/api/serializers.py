from typing_extensions import Required
from rest_framework import serializers 
from advertisement.models import BaseAdvertisement,FoodAdvertisement , ServiceAdvertisement , AnimalAdvertisement, ClothAdvertisement , Comment,Saved

class Advertisement(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    Image = serializers.ImageField(required = False)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True )
    class Meta:

        model = BaseAdvertisement
        fields = ('id' , 'Title' , 'Description' , 'Image' , 'province' , 'City','Address' , 'owner' , 'comments')
      

class ServiceAd(serializers.ModelSerializer):
    class Meta:
        model = ServiceAdvertisement
        fields = Advertisement.Meta.fields + ('service_type' , 'expiration_date' )
        
      
class FoodAd(serializers.ModelSerializer):
    class Meta:
        model = FoodAdvertisement
        fields = Advertisement.Meta.fields + ('Food_type' , 'expiration_date' )
      

class animalAd(serializers.ModelSerializer):
    class Meta:
        model = AnimalAdvertisement
        fields = Advertisement.Meta.fields + ('animal_breed' , 'animal_age' , 'Health' , 'handingover_reason' )
      

class clothesAd(serializers.ModelSerializer):
    class Meta:
        model = ClothAdvertisement
        fields =  fields = Advertisement.Meta.fields + ('cloth_type' , 'expiration_date' , 'cloth_status'
         , 'cloth_size' , 'for_men' , 'for_women' , 'for_kids' , 'unlimited' )
      

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

   
    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post' ]


class SavedSerializer(serializers.ModelSerializer):


    class Meta:
        model = Saved
        fields = "__all__"


