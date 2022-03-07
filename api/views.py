from django.shortcuts import render
from api.models import Post, Rooms
from api.serailizers import RoomSerailizer, PostSerailizer
from rest_framework import generics

class RoomView(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerailizer


class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerailizer