
from rest_framework import serializers
from advertisement.models import BaseAdvertisement, FoodAdvertisement, SavedModel, ServiceAdvertisement, AnimalAdvertisement, \
    ClothAdvertisement ,  Comment, SavedModel
from rest_polymorphic.serializers import PolymorphicSerializer
from user_account.models import Account

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class userserializer(serializers.ModelSerializer): 
    class Meta: 
        model = Account
        fields = ('id' , 'username' , 'email', 'first_name', 'last_name')

class BaseAdvertisementSerializer(serializers.ModelSerializer):
    owner = userserializer(read_only=True)
    Image = Base64ImageField(
        max_length=None, use_url=True, required = False
    )
    Image1 = Base64ImageField(
        max_length=None, use_url=True, required = False
    )
    Image2 = Base64ImageField(
        max_length=None, use_url=True, required = False
    )
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True )
    class Meta:
        model = BaseAdvertisement
        fields = ('id', 'Title', 'Description', 'Image', 'Image1', 'Image2', 'province', 'Country' , 'City', 'Address', 'owner' , 'date_joined' , 'mostaarname' , 'comments' )


class UpdateAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseAdvertisement
        fields = (
            'id', 'Title', 'Description', 'Image', 'Image1', 'Image2','province', 'City', 'Address' , 'Country')


class ServiceAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAdvertisement
        fields = BaseAdvertisementSerializer.Meta.fields + ('service_type', 'expiration_date')


class UpdateServiceAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAdvertisement
        fields = UpdateAdvertisementSerializer.Meta.fields + ('service_type', 'expiration_date')


class FoodAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodAdvertisement
        fields = BaseAdvertisementSerializer.Meta.fields + ('Food_type', 'expiration_date')


class UpdateFoodAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodAdvertisement
        fields = UpdateAdvertisementSerializer.Meta.fields + ('Food_type', 'expiration_date')


class AnimalAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalAdvertisement
        fields = BaseAdvertisementSerializer.Meta.fields + (
            'animal_breed', 'animal_age', 'Health', 'handingover_reason')


class UpdateAnimalAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalAdvertisement
        fields = UpdateAdvertisementSerializer.Meta.fields + (
            'animal_breed', 'animal_age', 'Health', 'handingover_reason')


class ClothesAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothAdvertisement
        fields = BaseAdvertisementSerializer.Meta.fields + ('cloth_type', 'expiration_date', 'cloth_status'
                                                            , 'cloth_size', 'for_men', 'for_women', 'for_kids',
                                                            'unlimited')


class UpdateClothesAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothAdvertisement
        fields = UpdateAdvertisementSerializer.Meta.fields + ('cloth_type', 'expiration_date', 'cloth_status',
                                                              'cloth_size', 'for_men', 'for_women', 'for_kids',
                                                              'unlimited')


class BaseAdvertisementPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        BaseAdvertisement: BaseAdvertisementSerializer,
        ServiceAdvertisement: ServiceAdvertisementSerializer,
        FoodAdvertisement: FoodAdvertisementSerializer,
        AnimalAdvertisement: AnimalAdvertisementSerializer,
        ClothAdvertisement: ClothesAdvertisementSerializer
    }


class UpdateBaseAdvertisementPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        BaseAdvertisement: UpdateAdvertisementSerializer,
        ServiceAdvertisement: UpdateServiceAdvertisementSerializer,
        FoodAdvertisement: UpdateFoodAdvertisementSerializer,
        AnimalAdvertisement: UpdateAnimalAdvertisementSerializer,
        ClothAdvertisement: UpdateClothesAdvertisementSerializer
    }


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

   
    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post' ]



class SavedmodelSerializer(serializers.ModelSerializer):


    class Meta:
        model = SavedModel
        fields = "__all__"


class SaveAdvertisementDatas(serializers.ModelSerializer):
    post_n = BaseAdvertisementSerializer(read_only=True)
    class Meta:
        model = SavedModel
        fields = "__all__"
