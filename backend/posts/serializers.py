from rest_framework import serializers
from .models import Post
from accounts.serializers import CustomUserSerializer
from comments.serializers import CommentSerializer
from bookmarks.serializers import BookmarkSerializer
from likes.serializers import LikeSerializer
from reposts.serializers import RepostSerializer

class PostSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    bookmarks = BookmarkSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    reposts = RepostSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'likes', 'comments', 'reposts', 'bookmarks']
