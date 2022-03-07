from django.shortcuts import render
from api.models import Rooms
from api.serailizers import RoomSerailizer
from rest_framework import generics

class RoomView(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerailizer