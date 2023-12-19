from django.urls import path
from .api import (
    get_all_comments, 
    create_comment,
)

urlpatterns = [
        path('', get_all_comments, name='get-all-comments'),
        path('<uuid:post_id>/create/', create_comment, name='create-comment'),
]
