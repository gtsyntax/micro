from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField(method_name='following_count')
    followers = serializers.SerializerMethodField(method_name='followers_count')
    posts = serializers.SerializerMethodField(method_name='posts_count')
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'first_name', 
                  'last_name', 'following', 'followers', 'posts', 'bio', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def following_count(self, user:CustomUser):
        return user.following.all().count()
    
    def followers_count(self, user:CustomUser):
        return user.followers.all().count()
    
    def posts_count(self, user:CustomUser):
        return user.posts_by_user.all().count()


    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        return user