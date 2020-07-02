from rest_witchcraft.viewsets import ModelViewSet

from message.models import Message
from message.serializers import MessageSerializer


class MessageView(ModelViewSet):
    queryset = Message.undelivered
    serializer_class = MessageSerializer
