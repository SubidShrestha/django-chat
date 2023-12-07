from user.serializers import UserSerializer
from .models import Conversation, Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('conversation_id',)

class ConversationListSerializer(serializers.ModelSerializer):
    initiator = UserSerializer(many=False,allow_null=False,read_only=True)
    receiver = UserSerializer(many=False,allow_null=False,read_only=True)
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver', 'last_message']

    def get_last_message(self, instance):
        message = instance.message_set.first()
        return MessageSerializer(instance=message)


class ConversationSerializer(serializers.ModelSerializer):
    initiator = UserSerializer(many=False,allow_null=False,read_only=True)
    receiver = UserSerializer(many=False,allow_null=False,read_only=True)
    message_set = MessageSerializer(many=True,read_only=True)

    class Meta:
        model = Conversation
        fields = ['id','initiator', 'receiver', 'message_set']
