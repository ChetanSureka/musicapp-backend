from django.urls import path
from .views import PostView, RoomView


urlpatterns = [
    path('room', RoomView.as_view(), name="room"),
    path('post', PostView.as_view(), name="post"),
]