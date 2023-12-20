from django.urls import path
from .api import repost_post

urlpatterns = [
        path("<uuid:post_id>/create/", repost_post, name="repost_post_api"), 
]
