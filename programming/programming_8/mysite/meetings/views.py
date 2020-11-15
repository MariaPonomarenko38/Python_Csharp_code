from rest_framework import generics
from .serializers import OnlineMeetingDetailSerializer, MeetingsListSerializer
from .models import OnlineMeeting
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class OnlineMeetingCreateView(generics.CreateAPIView):
    serializer_class = OnlineMeetingDetailSerializer
    queryset = OnlineMeeting.objects.all()


class MeetingsListView(generics.ListAPIView):
    filter_backends = [OrderingFilter, SearchFilter]
    queryset = OnlineMeeting.objects.all()
    serializer_class = MeetingsListSerializer
    search_fields = ['date', 'end_time', 'id', 'meeting_url', 'owner_first_name', 'owner_last_name',
                     'participant_first_name', 'participant_last_name', 'start_time']
    ordering_fields = '__all__'


class OnlineMeetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OnlineMeetingDetailSerializer
    queryset = OnlineMeeting.objects.all()