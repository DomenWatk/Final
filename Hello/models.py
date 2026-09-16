from django.db import models
from django.contrib.auth.models import User


class Bankstatement(models.Model):
    description=models.CharField()
    amount=models.DecimalField(max_digits=10,decimal_places=3)

class Stocksheld(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Stockname=models.CharField()
    Amountheld=models.DecimalField(max_digits=10,decimal_places=6)
    Averagecost=models.DecimalField(max_digits=10,decimal_places=6)