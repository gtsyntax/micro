from django.urls import path
from .api import (
    get_all_posts, 
    create_post,
    get_single_post,
    get_user_post,
)

urlpatterns = [
    path('', get_all_posts, name='get-all-posts'),
    path('<uuid:post_id>/', get_single_post, name='get-single-post'),
    path('create/', create_post, name='create-post'),
    path('users/<str:username>/', get_user_post, name="get-user-post")
]