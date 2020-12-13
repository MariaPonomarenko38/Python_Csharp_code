from rest_framework import generics, permissions, status
from .serializers import OnlineMeetingDetailSerializer
from .models import Meeting
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import OrderingFilter, SearchFilter
from .permissions import ReadOnlyOrAdmin
from rest_framework.pagination import PageNumberPagination
import constants
from rest_framework.response import Response


class PageNumberAsLimitOffset(PageNumberPagination):
    page_query_param = "offset"
    page_size_query_param = "limit"
    page_size = constants.page_size_value
    max_page_size = constants.max_page_size_value


class MeetingsView(generics.ListAPIView, generics.CreateAPIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated(), ReadOnlyOrAdmin()]
        elif self.request.method == 'POST':
            return (permissions.IsAuthenticated(), IsAdminUser(), )
    filter_backends = [OrderingFilter, SearchFilter]
    serializer_class = OnlineMeetingDetailSerializer
    search_fields = ['date', 'end_time', 'id', 'meeting_url', 'owner_first_name', 'owner_last_name', 'start_time']
    ordering_fields = '__all__'
    permission_classes = (ReadOnlyOrAdmin,)
    pagination_class = PageNumberAsLimitOffset
    queryset = Meeting.objects.all()


class OnlineMeetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return (permissions.IsAuthenticated(), IsAdminUser(), )
    serializer_class = OnlineMeetingDetailSerializer
    queryset = Meeting.objects.all()


