from rest_framework import generics
from api.models import Transaction
from .serializers import TransactionSerializer


class OrderList(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class CreateOrder(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer