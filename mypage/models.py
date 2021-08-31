from django.db import models
from django.conf import settings
from stock.models import Stock


# Create your models here.
class UserStockPinned(models.Model):
    """
    관심 종목 테이블
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
    )
    # 활성 여부
    is_active = models.BooleanField(default=True)
    # dates
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "user_stock_pinned"
