from rest_framework import serializers
from .models import Order
from api.meeting.serializers import MeetingsListSerializer


class OrderSerializer(serializers.ModelSerializer):
    meeting = MeetingsListSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'meeting', 'ordered_date', )


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
