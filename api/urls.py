from django.urls import path
from .views import *
urlpatterns = [
    path('orders/',OrderList.as_view(),name='all-orders'),
    path('orders/create',CreateOrder.as_view(),name='add-order'),
]
