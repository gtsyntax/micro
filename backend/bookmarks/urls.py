from django.urls import path
from .api import bookmark_post

urlpatterns = [
        path("<uuid:post_id>/add/", bookmark_post, name="bookmark_post_api"),
]
