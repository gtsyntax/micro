from django.urls import path
from .api import bookmark_post, get_user_bookmarks

urlpatterns = [
        path("", get_user_bookmarks, name="user_bookmarks_api"),
        path("<uuid:post_id>/add/", bookmark_post, name="bookmark_post_api"),
]
