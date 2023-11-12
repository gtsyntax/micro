from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_post(request, username):
    posts = Post.objects.filter(user__username=username).all().order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':

        # Parse and validate post data from the request
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():

            # If the data is valid, create a new post
            post = serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # If data is invalid, return an error response with validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Return a 405 Method Not Allowed response for other HTTP methods
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)