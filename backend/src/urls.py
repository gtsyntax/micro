from django.contrib import admin
from django.urls import path, include
from posts.api import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/posts', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/chats/', include('chats.urls')),
    path('api/home-timeline/', include('timeline.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/bookmarks/', include('bookmarks.urls')),
    path('api/likes/', include('likes.urls')),
    path('api/reposts/', include('reposts.urls')),
] + router.urls
