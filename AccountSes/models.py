from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit','Deposit'),
        ('withdrawal','withdrawal')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transct_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField(auto_now_add=True)



