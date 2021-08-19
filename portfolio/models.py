from stock.models import Stock
from django.conf import settings
from django.db import models


# Create your models here.
class Portfolio(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "portfolio"


class PortfolioStock(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE
    )
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = "portfolio_stock"
