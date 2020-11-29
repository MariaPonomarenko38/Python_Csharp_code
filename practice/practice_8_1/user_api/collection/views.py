from rest_framework import generics, permissions, status
from .serializers import OnlineMeetingDetailSerializer
from .models import OnlineMeeting, User
from rest_framework.filters import OrderingFilter, SearchFilter
from .permissions import IsOwnerOrReadOnly


class MeetingsListView(generics.ListAPIView, generics.CreateAPIView):
    filter_backends = [OrderingFilter, SearchFilter]
    serializer_class = OnlineMeetingDetailSerializer
    search_fields = ['date', 'end_time', 'id', 'meeting_url', 'owner_first_name', 'owner_last_name',
                     'participant_first_name', 'participant_last_name', 'start_time']
    ordering_fields = '__all__'
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        return OnlineMeeting.objects.filter(user=self.request.user)


class OnlineMeetingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OnlineMeetingDetailSerializer
    queryset = OnlineMeeting.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


