from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status 
from posts.models import Post
from .models import Comment
from .serializers import CommentSerializer

@api_view(['POST'])
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user

    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        comment = serializer.save(post=post, user=user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
