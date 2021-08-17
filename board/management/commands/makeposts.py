from django.core.management.base import BaseCommand, CommandError
from board.factories import PostFactory


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('num', nargs=1, type=int)

    def handle(self, *args, **options):
        try:
            cnt = int(options['num'][0])
        except ValueError:
            raise CommandError('Not integer!')
        
        if cnt <= 0:
            raise CommandError('greater than or equal to 1.')

        for i in range(cnt):
            post = PostFactory()

        self.stdout.write(self.style.SUCCESS('Successfully "%s"' % cnt))