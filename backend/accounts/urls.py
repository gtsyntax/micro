from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .api import (
    profile,
    register,
    follow_user,
    user_details,
    unfollow_user,
    get_all_users,
    following,
    followers,
)

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('users/', get_all_users, name='get-all-users'),
    path('<str:username>/follow/', follow_user, name='follow-user'),
    path('<str:username>/unfollow/', unfollow_user, name='unfollow-user'),
    path('users/<str:username>/', user_details, name='user-details'),
    path('users/<str:username>/following/', following, name='following'),
    path('users/<str:username>/followers/', followers, name='followers'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
