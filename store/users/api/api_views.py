from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import *
from django.contrib.auth.models import User


class UserAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = ['id', 'date_joined']
    queryset = User.objects.all()
