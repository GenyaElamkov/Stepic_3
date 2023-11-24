import io
import os
import sys
from zipfile import ZipFile

import pytest

from Module_9.lesson_9_6_step_17_annotation import matrix_to_dict



# берем первый файл из всех файлов в директории, если они имеют расширение zip
file = [f for f in os.listdir() if f.endswith('.zip')][0]

# здесь составляем список файлов попарно (в архиве файлы лежат тоже попарно вопрос/ответ)
with ZipFile(file, 'r') as zf:
    l = list()
    for i in range(0, len(zf.filelist) - 1, 2):
        l.append((zf.filelist[i].filename, zf.filelist[i + 1].filename))

    # читаем файлы и записываем их также попарно в список для выполнения
test_fixtures = list()
for test_file, clue in l:
    with ZipFile(file, 'r') as zf:
        test_fixtures.append((zf.read(test_file).decode('utf8'),
                              zf.read(clue).decode('utf8')))


@pytest.mark.parametrize('test_input,expected', test_fixtures)
def test_exec(test_input, expected):
    # тут подменяем стандартный выход консоли временным, чтобы нормально спарсить ответ
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    # выполняем код из списка, по сути читаем файл с вопросом и выполняем его.
    exec('from solution import *\n' + test_input, globals())
    # дергаем ответ из стандартного вывода
    result = sys.stdout.getvalue().strip()
    # возвращаем стандартный вывод на место
    sys.stdout = old_stdout
    # проверяем результаты
    assert result == expected
