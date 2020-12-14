from rest_framework import generics, status
from .serializers import OrderSerializer, OrderDetailSerializer
from rest_framework.response import Response
from .models import Order
from .permissions import IsOwnerOrAdmin
from api.meeting.models import Meeting


class OrderView(generics.CreateAPIView, generics.ListAPIView):
    permission_classes = (IsOwnerOrAdmin,)
    serializer_class = OrderSerializer

    def post(self, request, format=None):
        pk = request.data['meeting']
        if Meeting.objects.filter(id=pk[0]).exists():
            meet = Meeting.objects.get(id=pk[0])
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user_list = Order.objects.filter(user=request.user)
        for order in user_list:
            for meeti in order.meeting.all():
                if meeti.id == pk[0]:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        if meet.max_count == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        meet.max_count -= 1
        meet.save()

        conv = Order()
        conv.user = request.user
        conv.save()
        conv.meeting.add(meet)

        return Response(status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = (IsOwnerOrAdmin,)
