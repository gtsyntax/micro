from rest_framework import serializers
from .models import Repost
from accounts.serializers import CustomUserSerializer

class RepostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Repost
        fields = ['id', 'original_post', 'user', 'created_at']
