from rest_framework import serializers
from .models import Post
from accounts.serializers import CustomUserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at']