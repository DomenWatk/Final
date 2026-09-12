from django.db import models

class Stockheld(models.Model):
    StockName = models.CharField(max_length=20)
    AmountHeld =models.DecimalField(max_digits=8,decimal_places=2)
