from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_account.api.serializers import UserProfileSerializer
from user_account.models import Account


class UserProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    queryset = Account.objects.all()

    def get_object(self):
        return Account.objects.get(id=self.request.user.id)
