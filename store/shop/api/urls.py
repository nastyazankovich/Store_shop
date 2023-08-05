from django.urls import path
from .api_views import *

urlpatterns = [
    path('category/', CategoryAPIView.as_view(), name='category'),
    path('product/', ProductAPIView.as_view(), name='product')]

