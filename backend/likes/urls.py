from django.urls import path
from .api import like_post

urlpatterns = [
        path("<uuid:post_id>/add/", like_post, name="like_post_api"), 
]
