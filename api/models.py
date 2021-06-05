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
    billed_amount = models.IntegerField(blank=True,default=0)
    # order related
    coke = models.IntegerField(default=0)
    pepsi = models.IntegerField(default=0)
    soda = models.IntegerField(default=0)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.total = self.penny + self.nickel * 5 + self.dime *10 +self.quarter * 25
        self.billed_amount = 25*self.coke + 32 * self.pepsi + 47 * self.soda
        self.balance = self.total - self.billed_amount

    class Meta:
        ordering = ['-timestamp']