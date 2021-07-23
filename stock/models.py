from django.db import models

# Create your models here.
class Stock(models.Model):
    code = models.CharField(max_length=45)
    code_std = models.CharField(max_length=45)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table = "stock"

class StockPrice(models.Model):
    code = models.CharField(max_length=45)
    open = models.CharField(max_length=45)
    class Meta:
        db_table = "stock_price"
