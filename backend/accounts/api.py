from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import CustomUserSerializer
from .models import CustomUser, Contact

@api_view(['GET'])
def get_all_users(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def profile(request):
    user = request.user
    serializer = CustomUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def user_details(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        serializer = CustomUserSerializer(user)
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def follow_user(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        Contact.objects.get_or_create(
            user_follower=request.user,
            user_following=user
        )
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"message": "Followed"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def unfollow_user(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        Contact.objects.filter(
            user_follower=request.user,
            user_following=user
        ).delete()
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"message": "Unfollowed"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def following(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        following_list = user.following.all()
        serializer = CustomUserSerializer(following_list, many=True)
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def followers(request, username):
    try:
        user = CustomUser.objects.get(username=username)
        followers_list = user.followers.all()
        serializer = CustomUserSerializer(followers_list, many=True)
    except CustomUser.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data, status=status.HTTP_200_OK)