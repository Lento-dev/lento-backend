from rest_framework import serializers
from user_account.models import Account


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'username', 'email', 'image', 'cover', 'first_name', 'last_name', 'bio', 'phone', 'date_birth', 'province',
            'city', 'country', 'job', 'gender', 'education', 'date_joined', 'experience', 'region'
        )
        extra_kwargs = {
            'username': {'read_only': True}, 'email': {'required': False},
        }
