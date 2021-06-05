from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    penny = serializers.IntegerField(min_value=0)
    nickel = serializers.IntegerField(min_value=0)
    dime = serializers.IntegerField(min_value=0)
    quarter = serializers.IntegerField(min_value=0)
    coke = serializers.IntegerField(min_value=0)
    pepsi = serializers.IntegerField(min_value=0)
    soda = serializers.IntegerField(min_value=0)
    class Meta:
        model = Transaction
        fields = ['id',
                  'penny',
                  'nickel',
                  'dime',
                  'quarter',
                  'coke',
                  'pepsi',
                  'soda',
                  'total',
                  'billed_amount',
                  'balance',
                  'timestamp']
