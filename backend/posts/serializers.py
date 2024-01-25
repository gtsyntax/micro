from rest_framework import serializers
from .models import Post
from accounts.serializers import CustomUserSerializer
from comments.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'likes', 'comments', 'reposts', 'bookmarks']
