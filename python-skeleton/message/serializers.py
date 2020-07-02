from datetime import datetime

from rest_framework.fields import JSONField
from rest_witchcraft.serializers import ModelSerializer

from message.models import Message, db


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        session = db
        fields = ['pk', 'event', 'message', 'error_message', 'created_at', 'dispatched_at']

    message = JSONField()

    def create(self, validated_data):
        message = super().create(validated_data)
        message.created_at = datetime.now()
        message.locked = False

        return message
