from rest_framework import generics, pagination
from .serializers import OnlineMeetingDetailSerializer, MeetingsListSerializer
from .models import OnlineMeeting
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limit'


class MeetingsListView(generics.ListAPIView, generics.CreateAPIView):
    filter_backends = [OrderingFilter, SearchFilter]
    queryset = OnlineMeeting.objects.all()
    serializer_class = MeetingsListSerializer
    search_fields = ['date', 'end_time', 'id', 'meeting_url', 'owner_first_name', 'owner_last_name',
                     'participant_first_name', 'participant_last_name', 'start_time']
    ordering_fields = '__all__'
    pagination_class = CustomPagination

class OnlineMeetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OnlineMeetingDetailSerializer
    queryset = OnlineMeeting.objects.all()