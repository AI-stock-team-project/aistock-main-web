from django.db import models
# from django.db.models import indexes


# Create your models here.
class StrategyStockList(models.Model):
    """
    생성된 전략별 종목 리스트 테이블
    """
    # 전략 구분 코드
    strategy_code = models.CharField(max_length=45, default='')
    # 주식 코드
    ticker = models.CharField(max_length=45)
    # 순위
    rank = models.IntegerField(default=9999)
    # 수행된 일자
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'strategy_stock_list'
        indexes = [
            models.Index(fields=['strategy_code']),
            models.Index(fields=['strategy_code', 'rank'])
        ]


class StrategyMaster(models.Model):
    """
    주식 전략 종류에 대한 테이블.
    모멘텀 1개월, 모멘텀 3개월, 듀얼 모멘텀, 상승일 빈도, 급상승 총 5개의 항목이 
    미리 입력되어있다.
    """
    # 스톡 전략 명칭
    title = models.CharField(max_length=255, null=True, default='')
    # 전략 구분 코드 (리스트에서 이용되는 코드)
    code = models.CharField(max_length=45, default='')
    # 설명
    description = models.TextField(default='')

    class Meta:
        db_table = 'strategy_master'
        indexes = [
            models.Index(fields=['code'])
        ]
