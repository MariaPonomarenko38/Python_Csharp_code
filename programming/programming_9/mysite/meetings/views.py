from rest_framework import generics, pagination
from rest_framework.pagination import PageNumberPagination

from .serializers import OnlineMeetingDetailSerializer, MeetingsListSerializer
from .models import OnlineMeeting

from rest_framework.filters import OrderingFilter, SearchFilter


class PageNumberAsLimitOffset(PageNumberPagination):
    page_query_param = "offset"
    page_size_query_param = "limit"
    page_size = 5
    max_page_size = 100


class MeetingsListView(generics.ListAPIView, generics.CreateAPIView):
    filter_backends = [OrderingFilter, SearchFilter]
    queryset = OnlineMeeting.objects.all()
    serializer_class = MeetingsListSerializer
    search_fields = ['date', 'end_time', 'id', 'meeting_url', 'owner_first_name', 'owner_last_name',
                     'participant_first_name', 'participant_last_name', 'start_time']
    ordering_fields = '__all__'
    pagination_class = PageNumberAsLimitOffset


class OnlineMeetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OnlineMeetingDetailSerializer
    queryset = OnlineMeeting.objects.all()