from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status, viewsets 
from rest_framework.response import Response
from accounts.models import CustomUser
from likes.models import Like
from reposts.models import Repost
from bookmarks.models import Bookmark
from .models import Post
from .serializers import PostSerializer
from comments.serializers import CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request):
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

    # This will return all the posts for the currently logged in user
    @action(detail=False)
    def my_posts(self, request):
        posts = Post.objects.filter(user__username=request.user.username).all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # This will return all the posts of a given user
    @action(detail=False, url_path="(?P<username>[^/.]+)/all_posts")
    def all_posts(self, request, username=None):
        user = get_object_or_404(CustomUser, username=username)
        posts = Post.objects.filter(user=user).all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def like_post(self, request, pk=None):
        post = self.get_object()
        user = request.user

        existing_like = post.likes.filter(user=user).first()

        if existing_like:
            existing_like.delete()
        else:
            like = Like(post=post, user=user)
            like.save()
    
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def repost_post(self, request, pk=None):
        post = self.get_object()
        user = request.user

        # Create a new Repost instance
        repost = Repost(original_post=post, user=user)
        repost.save()
        
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def bookmark_post(self, request, pk=None):
        post = self.get_object()
        user = request.user

        existing_bookmark = post.bookmarks.filter(user=user).first()

        if existing_bookmark:
            existing_bookmark.delete()
        else:
            bookmark = Bookmark(post=post, user=user)
            bookmark.save()
        
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def add_comment(self, request, pk=None):
        post = self.get_object()

        comment_data = {
                "post": post.id,
                "content": request.data.get("content", ""),
        }


        serializer = CommentSerializer(data=comment_data, context={'request': request})

        if serializer.is_valid():
            comment = serializer.save()
            post.comments.add(comment)
            
            post_serializer = PostSerializer(post)
            return Response(post_serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


