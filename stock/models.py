from django.db import models


# Create your models here.
class Stock(models.Model):
    # 코드. 기본값 6자리 숫자
    code = models.CharField(max_length=45, null=True)
    # 코드. 국제증권식별번호 ISIN (영문,숫자 12자리)
    code_isin = models.CharField(max_length=45, null=True)
    # 심볼 코드 or 6자리 숫자
    symbol = models.CharField(max_length=45)
    # 종목명
    name = models.CharField(max_length=255, null=True)
    # 거래소
    market = models.CharField(max_length=255, null=True)
    # 업종
    sector = models.CharField(max_length=255, null=True)
    # 산업
    industry = models.CharField(max_length=255, null=True)
    # 상장일
    listing_date = models.DateField(null=True)
    # 결산월
    settle_month = models.CharField(max_length=255, null=True)
    # 대표자명
    representative = models.CharField(max_length=255, null=True)
    # 웹페이지
    homepage = models.CharField(max_length=255, null=True)
    # 활성 여부 (기본값 true)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "stock"


class StockPrice(models.Model):
    code = models.CharField(max_length=45)
    open = models.CharField(max_length=45)
    close = models.CharField(max_length=45)
    high = models.CharField(max_length=45)
    volume = models.CharField(max_length=45)
    diff = models.CharField(max_length=45)
    date = models.DateField()

    class Meta:
        db_table = "stock_price"
