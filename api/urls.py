from django.urls import path
from .views import *
urlpatterns = [
    # path('money/add/',add_money,name='add_money'),
    path('orders/',orders,name='all-orders'),
    path('orders/create/',order,name='add-order')
    

]
