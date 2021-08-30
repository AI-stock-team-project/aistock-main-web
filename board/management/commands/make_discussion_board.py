from django.core.management.base import BaseCommand
import factory
from board import models, factories
from django.db.models import F


class BoardConfigFactory(factory.django.DjangoModelFactory):
    """
    BoardConfig 를 넣기 위함
    """
    class Meta:
        model = models.BoardConfig
        django_get_or_create = ('route',)
    # fields
    name = '토론방'
    display_name = '토론방'
    route = 'discussion'
    id = 1


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BoardPost
    # fields
    author = factory.SubFactory(factories.UserFactory)
    board = factory.SubFactory(BoardConfigFactory)
    title = '오늘의 주가를 알아볼까요.'
    contents = '...'
    hit = factory.Faker('pyint', min_value=0, max_value=200)

    def __init__(self, title):
        self.title = title


class Command(BaseCommand):
    help = 'create board config [discussion]'

    # def add_arguments(self, parser):
    # parser.add_argument('num', nargs=1, type=int)

    def handle(self, *args, **options):
        # board_config = BoardConfigFactory()
        BoardConfigFactory()

        # 게시글 임의 
        PostFactory(title='네이버, 카카오')
        PostFactory(title='오늘의 주가를 알아볼까요.')
        PostFactory(title='상한가, 하한가')
        PostFactory(title='네이버 다음주는 상승하나')
        PostFactory(title='강력 홀딩')
        PostFactory(title='폭등 마감')
        PostFactory(title='승부처')
        PostFactory(title='주가예측 전망')
        PostFactory(title='제발')
        PostFactory(title='공매도가')
        PostFactory(title='어....?')
        PostFactory(title='오늘장 수고')
        PostFactory(title='약세장')
        PostFactory(title='예측과 분석의 차이')
        PostFactory(title='네이버, 차량용인포테인먼트(IVI) 플랫폼 그린카3000대에')
        PostFactory(title='차랑용 인포테인먼트(IVI) & 자율주행 기술 ')


        models.BoardPost.objects.filter(depth=0).update(
            g_no=F('id')
        )

        self.stdout.write(self.style.SUCCESS('Successfully create discussion'))
