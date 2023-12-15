from django.urls import path
from .api import (
        home_timeline_view
)

urlpatterns = [
    path('', home_timeline_view, name='home-timeline-view'),
]
