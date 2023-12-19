from rest_framework import serializers
from .models import Comment
from accounts.serializers import CustomUserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']
