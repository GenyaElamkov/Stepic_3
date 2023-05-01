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


# data_scope()


def three_socks_lemma(socs):
    """
    Определяет победителя в игре, правила которой представлены
    в условии задачи, и вывести его имя.
    """

    dima_even = len(socs) % 2 == 0 and socs[-1] % 2 == 0
    dima_odd = len(socs) % 2 > 0 and socs[-1] % 2 > 0

    name = 'Анри'
    if dima_even or dima_odd:
        name = 'Дима'

    return name


# socs = list(map(int, sys.stdin))
# socs = [1, 3, 5, 10, 3, 2, 12]
# print(three_socks_lemma(socs))


def statistics_lesson(socs):
    """
    Определяет рост самого низкого и самого высокого учеников,
    а также средний рост среди всех учеников.
    """
    socs = list(map(int, socs))
    if not socs:
        return "нет учеников"
    low_man = f"Рост самого низкого ученика: {min(socs)}"
    tall_man = f"Рост самого высокого ученика: {max(socs)}"
    average_man = f"Средний рост: {sum(socs) / len(socs)}"
    # return f"{low_man}\n{tall_man}\n{average_man}"
    # print(f"{low_man}\n{tall_man}\n{average_man}")

    return f"{low_man} {tall_man} {average_man}"


# socs = list(map(int, sys.stdin))
# socs = []

# print(statistics_lesson(socs))


def commentator():
    """
    Выводит единственное число — количество строк в введенном коде,
    которые содержат в себе только комментарии.
    """
    counter = 0
    for line in sys.stdin:
        if line.strip().startswith('#'):
            counter += 1
    print(counter)

    # print(sum(1 for row in stdin if row.lstrip().startswith('#')))


# commentator()

def no_commentator():
    """
    Выводит введенный блок кода, предварительно удалив из него все строки
    которые содержат в себе только комментарии.
    """
    for line in sys.stdin:
        if line.lstrip(' ')[0] != '#':
            print(line.rstrip('\n'))

no_commentator()
