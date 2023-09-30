from rest_framework import serializers
from Bapp.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','Name','Age']

