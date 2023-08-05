from rest_framework import generics
from .serializers import *
from ..models import Order


class OrderAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PaidOrderAPIView(generics.ListAPIView):
    queryset = Order.objects.filter(paid=True)
    serializer_class = OrderSerializer

