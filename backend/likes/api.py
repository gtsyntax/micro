from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from posts.models import Post
from posts.serializers import PostSerializer
from .models import Like

@api_view(['POST'])
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user

    # Check if the user already liked the post
    if not Like.objects.filter(user=user, post=post).exists():
        Like.objects.create(user=user, post=post)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"message": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
