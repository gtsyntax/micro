from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status 
from posts.models import Post
from .models import Bookmark
from .serializers import BookmarkSerializer

@api_view(['POST'])
def bookmark_post(request, post_id):
    user = request.user
    post = get_object_or_404(Post, pk=post_id)

    # Check if the user already bookmarked the post
    if not Bookmark.objects.filter(user=user, post=post).exists():
        Bookmark.objects.create(user=user, post=post)
        return Response({"message": "Post bookmarked successfully"}, status=status.HTTP_201_CREATED)
    return Response({"message": "You already bookmarked this post."}, status=status.HTTP_400_BAD_REQUEST)
