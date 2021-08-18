from django.core.management.base import BaseCommand
import factory
from board import models


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


class Command(BaseCommand):
    help = 'create board config [discussion]'

    # def add_arguments(self, parser):
        # parser.add_argument('num', nargs=1, type=int)

    def handle(self, *args, **options):
        board_config = BoardConfigFactory()

        self.stdout.write(self.style.SUCCESS('Successfully create discussion'))
