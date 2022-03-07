from rest_framework import serializers
from .models import Post, Rooms

class RoomSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')


class PostSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'created_at', 'author')
    
