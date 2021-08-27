from django.db import models


# Create your models here.
class Stock(models.Model):
    """
    [주식 종목 테이블]
    주식 종목이 들어있는 테이블이다. 
    웹 어플리케이션의 시작시 api를 통해서 데이터를 로드한다.
    일 단위로 데이터를 갱신한다.
    """
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
    """
    주가 테이블
    하루 단위의 주가 정보가 들어있는 테이블이다.
    웹 어플리케이션의 시작시 api를 통해서 데이터를 로드한다.
    일 단위로 데이터를 갱신한다.
    """
    # 심볼 코드
    code = models.CharField(max_length=45)
    # 일자
    date = models.DateField()
    # 시가
    open = models.IntegerField(default=0)
    # 고가
    high = models.IntegerField(default=0)
    # 저가
    low = models.IntegerField(default=0)
    # 종가
    close = models.IntegerField(default=0)
    # 거래량
    volume = models.IntegerField(default=0)
    # 거래대금
    trad_value = models.BigIntegerField(default=0)
    # 등락률
    fluc_rate = models.CharField(max_length=15, default='0.0')
    
    class Meta:
        db_table = "stock_price"
        indexes = [
            models.Index(fields=['code', 'date']),
            models.Index(fields=['code']),
            models.Index(fields=['date'])
        ]
