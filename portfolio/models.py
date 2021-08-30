from django.db import models
from django.conf import settings
from stock.models import Stock


# Create your models here.
class Portfolio(models.Model):
    """
    포트폴리오 목록 테이블
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    is_deleted = models.BooleanField(default=False)
    # 시스템 설명 (전략형 포트폴리오 생성시 'ai_portfolio'같이 추가해둠. 혼란 방지용.)
    system_log = models.CharField(max_length=255, default='')
    # dates
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "portfolio"


class PortfolioStrategyReport(models.Model):
    """
    Ai 포트폴리오 생성 결과 부가정보 테이블
    """
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE
    )
    # 입력한 투자 금액 (레포트하는 내역이었으므로 그냥 문자열로 저장함)
    money = models.CharField(max_length=255, default='1000000')
    # 입력한 투자 기간 (레포트하는 내역이었으므로 그냥 문자열로 저장함)
    term = models.CharField(max_length=255, default='1')
    # 입력한 '감당 가능한 리스크' (레포트하는 내역이었으므로 그냥 문자열로 저장함)
    risk = models.CharField(max_length=255, default='30')
    # 포트폴리오 성과에 대한 기록. 포트폴리오 기대 수익률, 포트폴리오 예상 변동률, 샤프 비율, 예상 잔금 (원)
    report = models.TextField(default='')

    class Meta:
        db_table = "portfolio_strategy_report"


class PortfolioStock(models.Model):
    """
    포트폴리오의 종목에 관한 테이블
    """
    # 포트폴리오 코드
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE
    )
    # 종목코드
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
    )
    # 수량
    num = models.IntegerField(default=0)
    # 투자 금액
    money = models.IntegerField(default=0)
    # 투자 비중 (소수점 6자리까지만 저장함)
    weight = models.DecimalField(max_digits=10, decimal_places=6, default=0.0)
    # dates
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "portfolio_stock"
