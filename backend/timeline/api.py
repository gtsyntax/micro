from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from posts.serializers import PostSerializer
from posts.models import Post

@api_view(['GET'])
def home_timeline_view(request):
    user = request.user
    following_users = user.following.all()
    posts = Post.objects.filter(user__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
