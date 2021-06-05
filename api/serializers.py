from django.db.models import fields
from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['id','penny','nickel','dime','quarter','total','coke','pepsi','soda','balance','timestamp']
