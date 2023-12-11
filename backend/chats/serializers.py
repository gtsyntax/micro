from rest_framework import serializers
from .models import Chat, ChatMessage
from accounts.serializers import CustomUserSerializer


class ChatSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'participants', 'created_at', 'updated_at']

class ChatMessageSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer(read_only=True)
    recipient = CustomUserSerializer(read_only=True)

    class Meta:
        model = ChatMessage
        fields = ['id','sender', 'recipient', 'content', 'created_at', 'updated_at']

class ChatDetailSerializer(serializers.ModelSerializer):
    participants = CustomUserSerializer(many=True, read_only=True)
    messages = ChatMessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['id', 'participants', 'created_at', 'updated_at', 'messages']
