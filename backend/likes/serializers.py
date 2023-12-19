from rest_framework import serializers
from .models import Like
from accounts.serializers import CustomUserSerializer

class LikeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']
