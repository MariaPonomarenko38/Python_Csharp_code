from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Meeting


def valid_name(dob):
    if dob.isalpha() is False:
        raise serializers.ValidationError("Name and surname must contain only letters")
    return dob


class MeetingsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = '__all__'


class OnlineMeetingDetailSerializer(serializers.ModelSerializer):
    owner_first_name = serializers.CharField(validators=[valid_name])
    owner_last_name = serializers.CharField(validators=[valid_name])

    def validate(self, data):
        if data['start_time'] > data['end_time']:
            raise serializers.ValidationError("finish must occur after start")
        return data

    class Meta:
        model = Meeting
        fields = '__all__'

