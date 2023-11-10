import os
import re

from django.conf import settings


class Test01Dockerfile:

    def test_dockerfile(self):
        try:
            with open(
                f'{os.path.join(settings.BASE_DIR, "Dockerfile")}', 'r'
            ) as f:
                dockerfile = f.read()
        except FileNotFoundError:
            assert False, 'Проверьте, что файл Dockerfile существует'

        assert re.search(r'FROM\s+python:', dockerfile), (
            'Проверьте, что в файл Dockerfile добавлена инструкция'
            ' FROM с указанием образа python'
        )
