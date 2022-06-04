from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from chat.models import Chat, Contact
from chat.views import get_user_contact
from .serializers import ChatSerializer , ContactSerializer

User = get_user_model()


# class contactCreateView(createAPIview): 
#     serializer_class = ContactSerializer

class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated )

    def get_queryset(self):
        queryset = Chat.objects.all()
        username = self.request.query_params.get('email', None)
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.all()
        return queryset


class ChatDetailView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = ()

class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = ()


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = ()


class ChatDeleteView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = ()