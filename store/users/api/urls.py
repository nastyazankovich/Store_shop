from django.urls import path
from .api_views import *

urlpatterns = [
    path('user/', UserAPIView.as_view(), name='user'),
]
