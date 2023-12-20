from rest_framework import serializers
from .models import Comment
from accounts.serializers import CustomUserSerializer

class CommentSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        return Comment.objects.create(user=self.context['request'].user, **validated_data)

