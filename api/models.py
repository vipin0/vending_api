from django.db import models
import uuid

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    
    # money related data
    penny = models.IntegerField(default=0)
    nickel = models.IntegerField(default=0)
    dime = models.IntegerField(default=0)
    quarter = models.IntegerField(default=0)
    total = models.IntegerField(blank=True,default=0)
    balance = models.IntegerField(blank=True,default=0)
    
    # order related
    coke = models.IntegerField(default=0)
    pepsi = models.IntegerField(default=0)
    soda = models.IntegerField(default=0)
