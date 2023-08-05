from django.urls import path
from .api_views import *

urlpatterns = [
    path('order/', OrderAPIView.as_view(), name='order'),
    path('paid_order/', PaidOrderAPIView.as_view(), name='paid_order')
]
