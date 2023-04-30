#####################################################
# Модуль 4.1 потоковый ввод stdin и вывод stdout    #
#####################################################

import sys

from datetime import datetime

def reverse_order():
    """
    Выводит все введенные строки, предварительно расположив в каждой
    строке все символы в обратном порядке.
    """

    # for line in sys.stdin:
    #     print(line.strip('\n')[::-1])

    txt = [line[::-1].strip() for line in sys.stdin.readlines()]
    print(*txt, sep='\n')


# reverse_order()

def data_scope():
    """
    Выводит единственное число — количество дней между максимальной
    и минимальной датами введенной последовательности.
    """
    pattern = '%Y-%m-%d'
    dts = list(map(str.strip, sys.stdin))
    dt_max = datetime.strptime(max(dts), pattern)
    dt_min = datetime.strptime(min(dts), pattern)

    print((dt_max - dt_min).days)

    # date = [datetime.fromisoformat(i.strip()) for i in sys.stdin]

data_scope()