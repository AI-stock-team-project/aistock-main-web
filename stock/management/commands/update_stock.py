from django.core.management.base import BaseCommand
import urllib.request
from urllib.error import HTTPError
import json


class Command(BaseCommand):
    help = 'update stock data'

    # def add_arguments(self, parser):
    # parser.add_argument('num', nargs=1, type=int)

    def handle(self, *args, **options):
        # board_config = BoardConfigFactory()
        # BoardConfigFactory()
        url = 'http://data-api:5000/api/update_stock_list'

        try:
            req = urllib.request.Request(url, method='POST')
            with urllib.request.urlopen(req) as response:
                # encoding
                # encoding = response.info().get_content_charset('utf-8')
                # get data
                data = response.read()
                # print(data)

                # 결과를 json으로 파싱
                # resp_data = json.loads(data.decode(encoding))
                resp_data = json.loads(data.decode('utf-8'))

                # noinspection PyUnusedLocal
                ret = ''
                # 결과값에 key 가 있을 때, 재통신
                key = resp_data['key']
                if key:
                    with urllib.request.urlopen(f"{url}?key={key}") as response2:
                        ret = response2.read().decode('utf-8')
                else:
                    ret = json.dumps(resp_data)
                self.stdout.write(ret)
                self.stdout.write(self.style.SUCCESS('Successfully create stock data'))
        except HTTPError as err:
            if err.code == 400:
                self.stdout.write("400 Error")
            else:
                raise

        self.stdout.write(self.style.SUCCESS('exited update_stock'))
