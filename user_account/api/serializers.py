from rest_framework import serializers
from user_account.models import Account


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'username', 'email', 'image', 'cover', 'first_name', 'last_name', 'bio', 'phone', 'date_birth', 'city',
            'country', 'job', 'gender', 'education', 'date_joined', 'experience',
        )
        extra_kwargs = {
            'username': {'read_only': True}, 'email': {'required': False},
        }


class PublicProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'username', 'email', 'image', 'cover', 'first_name', 'last_name', 'bio', 'phone', 'date_birth',
            'city', 'country', 'job', 'gender', 'education', 'experience'
        )


class PublicProfileSerializerwithoutphonenumber(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id', 'username', 'email', 'image', 'cover', 'first_name', 'last_name', 'bio', 'date_birth',
            'city', 'country', 'job', 'gender', 'education', 'experience'
        )

