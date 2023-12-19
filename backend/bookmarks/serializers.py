from rest_framework import serializers
from accounts.serializers import CustomUserSerializer
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'post', 'created_at']
