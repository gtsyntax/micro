from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from posts.models import Post
from posts.serializers import PostSerializer
from .models import Repost

@api_view(['POST'])
def repost_post(request, post_id):
    user = request.user
    original_post = get_object_or_404(Post, pk=post_id)

    # Check if the user already reposted the post
    if not Repost.objects.filter(user=user, original_post=original_post).exists():
        Repost.objects.create(user=user, original_post=original_post)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"message": "You already reposted this post."}, status=status.HTTP_400_BAD_REQUEST)
