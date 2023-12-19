from django.urls import path
from .api import bookmark_post

urlpatterns = [
        path("add/<uuid:post_id>/", bookmark_post, name="bookmark_post_api"),
]
