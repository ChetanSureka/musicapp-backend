from rest_framework import serializers
from .models import Rooms

class RoomSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
    
